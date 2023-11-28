from __future__ import annotations

import collections
import os
import typing
import aws_cdk
from typing import Union, Optional, Dict, Mapping, Sequence, Tuple, Any, List
import constructs
import bs4
import pydantic
import pydantic.typing
from bs4 import BeautifulSoup
import inspect
from info import parse_docstring, DocstringInfo
from dataclasses import dataclass
ResourceTypeT: typing.TypeAlias = typing.Literal[
    'Construct',
    'Class',
    'Struct',
    'Interface',
    'CloudFormation Resource',
    'CloudFormation Property Type',
    'Enum',
]


NEWLINE = '\n'

def navsubgroup(tag: bs4.Tag) -> bool:
    if tag.name == 'div':
        classes = tag.get('class', '')
        assert classes is not None
        if 'navGroup' in classes and 'subNavGroup' in classes:
            return True
    return False

def get_doc(obj: Any) -> DocstringInfo:
    obj_doc = inspect.getdoc(obj)
    doc = inspect.cleandoc(obj_doc) if obj_doc else ''
    parsed = parse_docstring(doc)
    return parsed


@dataclass
class APIResource:
    name: str
    doc_url: str
    module_name: str
    resource_type: str
    _obj: Any = None

    def __hash__(self) -> int:
        return hash(self.qualname)

    def __repr__(self) -> str:
        return self.as_python_annotation()

    @property
    def model_class_name(self) -> str:
        return f'{self.name.replace(".", "_")}Def'

    @property
    def model_class_fullname(self) -> str:
        mod = modules[self.module_name]
        return f'models.{mod.namespace}.{self.model_class_name}'

    @property
    def config_class_name(self) -> str | None:
        if not self.nonconstructor_methods and not self.configurable_properties:
            return None
        else:
            if self.resource_type == 'Interface':
                return snake_to_camel(self.module_info.namespace) + self.model_class_name + 'Config'
            else:
                return self.model_class_name + 'Config'

    @property
    def config_class_fullname(self) -> str | None:
        name = self.config_class_name
        if name is None:
            return None
        else:
            mod = modules[self.module_name]
            return f'models.{mod.namespace}.{name}'



    @property
    def qualname(self) -> str:
        return f'{self.module_name}.{self.name}'

    @property
    def python_doc_url(self) -> str:
        python_location = self.doc_url.replace('/docs/aws-cdk-lib', '/python/aws_cdk')
        parts = python_location.split('.')
        component = parts.pop(-2)
        parts[-2] += f'/{component}'
        python_location = '.'.join(parts)
        return python_location

    @property
    def python_qualname(self) -> str:
        return f'{self.module_name.replace("aws-cdk-lib", "aws_cdk")}.{self.name}'

    @property
    def obj(self) -> Any:
        if self._obj:
            return self._obj
        else:
            obj = eval(self.python_qualname)
            self._obj = obj
            return obj
    @property
    def doc(self) -> DocstringInfo:
        return get_doc(self.obj)

    @property
    def module_info(self) -> Module:
        return modules[self.module_name]

    @property
    def init_signature(self) -> Optional[inspect.Signature]:
        obj = self.obj
        if hasattr(obj, '__init__'):
            return inspect.signature(obj.__init__, globals=globals(), locals=self.module_info.globals)
        return None

    @property
    def init_info(self) -> Optional[MethodInfo]:
        if not self.init_signature:
            return None
        return MethodInfo(module_name=self.module_name, resource=self, method_name='__init__', method_object=self.obj.__init__)

    @property
    def init_params(self) -> Optional[dict[str, ParamInfo]]:
        init_sig = self.init_signature
        if init_sig is None:
            return None

        init_docs = get_doc(self.obj.__init__)
        d: dict[str, ParamInfo] = {}
        for param_name, param in init_sig.parameters.items():
            if param_name in ('self', 'args', 'kwargs') or param_name.startswith('_'):
                continue
            for p in init_docs['params']:
                if p['name'] == param_name:
                    docstring = p['doc']
                    break
            else:
                docstring = ''
            methodinfo = self.init_info
            assert methodinfo is not None
            info = ParamInfo(name=param_name, doc=docstring, annotation=param.annotation, default=param.default, kind=param.kind, method=methodinfo)
            d[param_name] = info
        return d


    def inspect_members(self, static: bool = True, public_only: bool = True) -> list[tuple[str, Any]]:
        if static:
            members = inspect.getmembers_static(self.obj)
        else:
            members = inspect.getmembers(self.obj)
        if public_only:
            return [(name, obj) for name, obj in members if not name.startswith('_')]
        else:
            return members


    def implements(self) -> list[Any]:
        if hasattr(self.obj, '__jsii_ifaces__'):
            interfaces = self.obj.__jsii_ifaces__
            assert isinstance(interfaces, list)
            return interfaces
        return []

    @property
    def _basename(self):
        if self.module_name == 'aws_cdk':
            basename = f'models.core.{self.name.replace(".", "_")}'
        elif self.module_name.startswith('constructs'):
            basename = f'models.constructs.{self.name.replace(".", "_")}'
        else:
            basename = f'{self.module_name.replace("aws-cdk-lib", "models")}.{self.name.replace(".", "_")}'
        return basename

    def as_python_annotation(self) -> str:
        basename = self._basename
        if self.resource_type == 'Enum':
            return f'{self.obj.__module__}.{self.obj.__qualname__}'
        elif self.resource_type == 'Interface':
            # XXX: Interface finding is flaky, due to implementation details in AWS CDK for Python.
            if self.obj in (constructs.IConstruct, aws_cdk.IResource, aws_cdk.aws_iam.IGrantable):  # TODO: figure out better way for IGrantable
                return 'models.AnyResource'
            if self.obj in (aws_cdk.IResolvable, constructs.IDependable):
                return 'models.UnsupportedResource'
            ret = _implementations.get(self.obj)
            if not ret:
                ... # TODO: find 'obtainable from' classes
                return 'models.UnsupportedResource'
            # if len(ret) > 20:
            #     print('overloaded', basename)
            #     return 'models.UnsupportedResource'
            return f'typing.Union[{", ".join(str(r) for r in ret if ".experimental." not in r.as_python_annotation())}]'
        if self.resource_type == 'Construct':
            ret = f'{basename}Def'
        elif self.resource_type == 'Class':
            ret = f'{basename}Def'
        elif self.resource_type == 'Struct':
            ret = f'{basename}Def'
        elif self.resource_type == 'CloudFormation Resource':
            ret = f'{basename}Def'
        elif self.resource_type == 'CloudFormation Property Type':
            ret = f'{basename}Def'
        else:
            raise ValueError()

        return ret


    @property
    def methods(self) -> list[MethodInfo]:
        methods = []
        for member_name, value in self.inspect_members():
            if member_name.startswith('as_'):
                continue
            if member_name.startswith('to_'):
                continue
            if member_name.startswith('is_'):
                continue

            if callable(value):
                real_method_object = getattr(self._obj, member_name)
                methods.append(MethodInfo(module_name=self.module_name, resource=self, method_object=real_method_object, method_name=member_name))
            elif type(value) is classmethod:
                real_method_object = getattr(self._obj, member_name)
                methods.append(MethodInfo(module_name=self.module_name, resource=self, method_object=real_method_object, method_name=member_name))
        return methods

    @property
    def alternate_constructors(self) -> list[MethodInfo]:
        # XXX: this is really just a best guess
        ret = []
        for method in self.methods:
            if method.method_name.startswith('from_') or (method.is_classmethod() and (method.signature.return_annotation in reverse_resources or method.clean_return_type in _implementations)):
                ret.append(method)
        return ret

    @property
    def nonconstructor_methods(self) -> list[MethodInfo]:
        ret = []
        alternate_constructors = self.alternate_constructors
        for method in self.methods:
            if method not in alternate_constructors:
                ret.append(method)
        return ret

    @property
    def property_names(self):
        props = []
        for member_name, value in self.inspect_members():
            if type(value) is property:
                props.append(member_name)
        return props

    @property
    def configurable_properties(self) -> dict[str, Any]:
        ret = {}
        for member_name, value in self.inspect_members():
            if member_name in ('node',):
                continue
            if type(value) is property:
                sig = inspect.signature(value.fget)
                rt = sig.return_annotation
                if rt in reverse_resources:
                    return_resource = reverse_resources[rt]
                    if return_resource.nonconstructor_methods:
                        ret[member_name] = return_resource
        return ret

class UnSet:
    ...
@dataclass
class ParamInfo:
    name: str
    doc: str
    annotation: Any
    kind: int
    default: Any
    method: MethodInfo

    def clean_annotation(self, annotation=UnSet) -> Any:
        if annotation is UnSet:
            annotation = self.annotation
            if type(annotation) is str:
                try:
                    glbs = self.method.module_info.globals
                    if self.method.module_name == 'aws-cdk-lib.aws_stepfunctions_tasks':
                        glbs.update(modules['aws-cdk-lib.aws_stepfunctions'].globals)
                    elif self.method.module_name == 'aws-cdk-lib.aws_codebuild':
                        glbs.update({
                            'IGroup': aws_cdk.aws_iam.IGroup,
                            'IRole': aws_cdk.aws_iam.IRole,
                            'IUser': aws_cdk.aws_iam.IUser,
                            'PolicyStatement': aws_cdk.aws_iam.PolicyStatement,
                        })
                    annotation = eval(annotation, glbs)
                except Exception as e:
                    _prev_anno_name = annotation
                    resolved = True
                    if annotation == 'Stack':
                        annotation = aws_cdk.Stack
                    elif annotation == 'ListenerAction':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.ListenerAction
                    elif annotation == 'CfnResource':
                        annotation = aws_cdk.CfnResource
                    elif annotation == 'Reference':
                        annotation = aws_cdk.Reference
                    elif annotation == 'RemovalPolicy':
                        annotation = aws_cdk.RemovalPolicy
                    elif annotation == 'FunctionUrl':
                        annotation = aws_cdk.aws_lambda.FunctionUrl
                    elif annotation == 'NotificationRuleTargetConfig':
                        annotation = aws_cdk.aws_codestarnotifications.NotificationRuleTargetConfig
                    elif annotation == 'NotificationRuleSourceConfig':
                        annotation = aws_cdk.aws_codestarnotifications.NotificationRuleSourceConfig
                    elif annotation == 'INetworkTargetGroup':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.INetworkTargetGroup
                    elif annotation == 'PolicyStatement':
                        annotation = aws_cdk.aws_iam.PolicyStatement
                    elif annotation == 'OriginBindConfig':
                        annotation = aws_cdk.aws_cloudfront.OriginBindConfig
                    elif annotation == 'OidcOptionsProperty':
                        annotation = aws_cdk.aws_ec2.CfnVerifiedAccessTrustProvider.OidcOptionsProperty
                    elif annotation == 'Function':
                        annotation = aws_cdk.aws_lambda.Function
                    elif annotation == 'IApplicationTargetGroup':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.IApplicationTargetGroup
                    elif annotation == 'LoadBalancer':
                        annotation = aws_cdk.aws_elasticloadbalancing.LoadBalancer
                    elif annotation == 'LoadBalancerTargetProps':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.LoadBalancerTargetProps
                    elif annotation == 'PrincipalBase':
                        annotation = aws_cdk.aws_iam.PrincipalBase
                    elif annotation == 'InstanceType' and self.method.module_name == 'aws-cdk-lib.aws_batch':
                        annotation = aws_cdk.aws_ec2.InstanceType
                    else:
                        resolved = False
                        print(self.method.method_name, self.method.module_name)
                        print(f'failed to resolve param string annotation {annotation!r}', e)
                    if resolved and _prev_anno_name not in ('CfnResource', 'Reference', 'RemovalPolicy'):
                        print(f'Resolved annotation {_prev_anno_name!r} to {annotation!r} (method {self.method.method_name!r} in module {self.method.module_name!r})')

        origin = typing.get_origin(annotation)
        args = typing.get_args(annotation)
        if origin is collections.abc.Sequence:
            origin = typing.Sequence
        if origin is collections.abc.Mapping:
            origin = typing.Mapping

        if args:
            new_args = []
            for arg in args:
                new_arg = self.clean_annotation(annotation=arg)
                new_args.append(new_arg)
            new_args = tuple(new_args)
            ret = origin[new_args]
            if 'ForwardRef' in str(ret):
                breakpoint()
            return ret
        else:
            if annotation in reverse_resources:
                resource = reverse_resources[annotation]
                return resource
            elif type(annotation) == typing.ForwardRef:
                guess_namespace = self.method.module_info.globals
                if getattr(annotation, '__globals__', None):
                    guess_globals = annotation.__globals__
                else:
                    guess_globals=globals()
                    guess_globals.update(modules['aws-cdk-lib'].globals)
                try:
                    new = typing.cast(typing.Any, annotation)._evaluate(guess_globals, guess_namespace, set())
                    return self.clean_annotation(new)
                except Exception as e:
                    if annotation.__forward_evaluated__:
                        return self.clean_annotation(annotation.__forward_value__)
                    breakpoint()
            elif inspect.isclass(annotation):
                return annotation
            else:
                return annotation





@dataclass
class MethodInfo:
    module_name: str
    resource: APIResource
    method_name: str
    method_object: Any

    @property
    def docstring(self):
        doc = self.doc
        short = doc['short_description']
        long = doc['long_description']
        return f'{short}\n{long}'.strip()

    @property
    def doc(self) -> DocstringInfo:
        parsed = get_doc(self.method_object)
        return parsed

    @property
    def module_info(self) -> Module:
        return modules[self.module_name]


    @property
    def signature(self) -> inspect.Signature:
        return inspect.signature(self.method_object, globals=globals(), locals=self.module_info.globals)

    def parameters(self, exclude: Optional[list[str]]=None) -> dict[str, ParamInfo]:
        d = {}
        if exclude is None:
            exclude = []
        doc = self.doc
        for param_name, param in self.signature.parameters.items():
            if param_name.startswith('_'):
                continue
            if param_name in exclude:
                continue
            for p in doc['params']:
                if p['name'] == param_name:
                    docstring = p['doc']
                    break
            else:
                docstring = ''
            info = ParamInfo(name=param_name, doc=docstring, kind=param.kind, default=param.default, annotation=param.annotation, method=self)
            d[param_name] = info
        return d

    @staticmethod
    def _isclassmethod(method: Any) -> bool:
        #  https://stackoverflow.com/a/19228282/5747944
        bound_to = getattr(method, '__self__', None)
        if not isinstance(bound_to, type):
            # must be bound to a class
            return False
        name = method.__name__
        for cls in bound_to.__mro__:
            descriptor = vars(cls).get(name)
            if descriptor is not None:
                return isinstance(descriptor, classmethod)
        return False

    def is_classmethod(self) -> bool:
        return self._isclassmethod(self.method_object)

    @property
    def clean_return_type(self) -> Any:
        return self.clean_return_annotation()

    def clean_return_annotation(self, annotation=UnSet) -> Any:
        if annotation is UnSet:
            annotation = self.signature.return_annotation
            if type(annotation) is str:
                try:
                    annotation = eval(annotation, self.module_info.globals)
                except Exception as e:
                    _prev_anno_name = annotation
                    resolved = True
                    if annotation == 'Stack':
                        annotation = aws_cdk.Stack
                    elif annotation == 'ListenerAction':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.ListenerAction
                    elif annotation == 'CfnResource':
                        annotation = aws_cdk.CfnResource
                    elif annotation == 'Reference':
                        annotation = aws_cdk.Reference
                    elif annotation == 'RemovalPolicy':
                        annotation = aws_cdk.RemovalPolicy
                    elif annotation == 'FunctionUrl':
                        annotation = aws_cdk.aws_lambda.FunctionUrl
                    elif annotation == 'NotificationRuleTargetConfig':
                        annotation = aws_cdk.aws_codestarnotifications.NotificationRuleTargetConfig
                    elif annotation == 'NotificationRuleSourceConfig':
                        annotation = aws_cdk.aws_codestarnotifications.NotificationRuleSourceConfig
                    elif annotation == 'INetworkTargetGroup':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.INetworkTargetGroup
                    elif annotation == 'PolicyStatement':
                        annotation = aws_cdk.aws_iam.PolicyStatement
                    elif annotation == 'OriginBindConfig':
                        annotation = aws_cdk.aws_cloudfront.OriginBindConfig
                    elif annotation == 'OidcOptionsProperty':
                        annotation = aws_cdk.aws_ec2.CfnVerifiedAccessTrustProvider.OidcOptionsProperty
                    elif annotation == 'Function':
                        annotation = aws_cdk.aws_lambda.Function
                    elif annotation == 'IApplicationTargetGroup':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.IApplicationTargetGroup
                    elif annotation == 'LoadBalancer':
                        annotation = aws_cdk.aws_elasticloadbalancing.LoadBalancer
                    elif annotation == 'LoadBalancerTargetProps':
                        annotation = aws_cdk.aws_elasticloadbalancingv2.LoadBalancerTargetProps
                    elif annotation == 'PrincipalBase':
                        annotation = aws_cdk.aws_iam.PrincipalBase
                    elif annotation == 'InstanceType' and self.module_name == 'aws-cdk-lib.aws_batch':
                        annotation = aws_cdk.aws_ec2.InstanceType
                    else:
                        resolved = False
                        print(self.module_name)
                        print(f'failed to resolve param return string annotation {annotation!r}', e)
                    if resolved and _prev_anno_name not in ('Reference', 'CfnResource', 'RemovalPolicy'):
                        print(f'Resolved annotation {_prev_anno_name!r} to {annotation!r} (module {self.module_name!r})')


        origin = typing.get_origin(annotation)
        args = typing.get_args(annotation)
        if origin is collections.abc.Sequence:
            origin = typing.Sequence
        if origin is collections.abc.Mapping:
            origin = typing.Mapping

        if args:
            new_args = []
            for arg in args:
                new_arg = self.clean_return_annotation(annotation=arg)
                new_args.append(new_arg)
            new_args = tuple(new_args)
            ret = origin[new_args]
            if 'ForwardRef' in str(ret):
                breakpoint()
            return ret
        else:
            if False and annotation in reverse_resources:
                resource = reverse_resources[annotation]
                return resource
            elif type(annotation) == typing.ForwardRef:
                guess_namespace = self.module_info.globals
                if getattr(annotation, '__globals__', None):
                    guess_globals = annotation.__globals__
                elif self.module_name == 'aws-cdk-lib.aws_stepfunctions_tasks':
                    guess_globals = modules['aws-cdk-lib.aws_stepfunctions'].globals
                else:
                    guess_globals=globals()
                new = typing.cast(Any, annotation)._evaluate(guess_globals, guess_namespace, set())
                return self.clean_return_annotation(new)
            elif inspect.isclass(annotation):
                return annotation
            else:
                return annotation

@dataclass
class Module:
    name: str
    classes: dict[str, APIResource]
    constructs: dict[str, APIResource]
    structs: dict[str, APIResource]
    enums: dict[str, APIResource]
    interfaces: dict[str, APIResource]
    cloudformation_resources: dict[str, APIResource]
    cloudformation_property_types: dict[str, APIResource]
    _obj: Any = None

    @property
    def obj(self) -> Any:
        if self._obj:
            return self._obj
        else:
            obj = eval(self.python_name)
            self._obj = obj
            return obj

    @property
    def python_name(self) -> str:
        return self.name.replace('aws-cdk-lib', 'aws_cdk')

    @property
    def all(self) -> dict[str, APIResource]:
        return self.classes | self.constructs | self.structs | self.enums | self.interfaces | self.cloudformation_resources | self.cloudformation_property_types

    @property
    def globals(self) -> dict[Any, Any]:
        ret = self.obj.__dict__
        assert isinstance(ret, dict)
        return ret

    @property
    def namespace(self) -> str:
        if self.python_name == 'aws_cdk':
            return 'core'
        return self.python_name.replace('aws_cdk.', '')


_MOD_HEADER = '''\
from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM
'''

def render_module(mod: Module) -> str:
    s = _MOD_HEADER
    if mod.namespace == 'core':
        s = s.replace('import constructs', '', 1)
    for name, resource in mod.all.items():
        s += f'\n#  autogenerated from {resource.python_qualname}\n'
        s += render_resource(resource)
        s += '\n'


    s += '\nclass ModuleModel(pydantic.BaseModel):'

    for name, resource in mod.all.items():
        if resource.resource_type in ('Enum', 'Interface'):
            continue
        attrname = f'{resource.name.replace(".", "_")}'
        class_name = f'{attrname}Def'
        fullname = f'models.{mod.namespace}.{class_name}'
        s += f'\n    {attrname}: typing.Optional[dict[str, {fullname}]] = pydantic.Field(None)'
    s += '\n    ...'
    s += '\n'

    s += '\nimport models\n'

    return s


def render_resource(resource: APIResource) -> str:
    if resource.resource_type == 'Enum':
        return '# skipping emum'
    elif resource.resource_type == 'Interface':
        return '#  skipping Interface'
    else:
        return render_pydantic(resource)




def render_pydantic(resource: APIResource) -> str:
    s = ''
    if resource.resource_type == 'Construct':
        base_class = 'BaseConstruct'
        class_name = f'{resource.name.replace(".", "_")}Def'
    elif resource.resource_type == 'Class':
        base_class = 'BaseClass'
        class_name = f'{resource.name.replace(".", "_")}Def'
    elif resource.resource_type == 'Struct':
        base_class = 'BaseStruct'
        class_name = f'{resource.name.replace(".", "_")}Def'
    elif resource.resource_type == 'CloudFormation Resource':
        base_class = 'BaseCfnResource'
        class_name = f'{resource.name.replace(".", "_")}Def'
    elif resource.resource_type == 'CloudFormation Property Type':
        base_class = 'BaseCfnProperty'
        class_name = f'{resource.name.replace(".", "_")}Def'
    else:
        raise ValueError(f"Unexpected resource type {resource.resource_type!r}")

    base_classes = [base_class]

    if aws_cdk.aws_ec2.IConnectable in resource.implements():
        base_classes.append('ConnectableMixin')
    s = _render_class_head(resource=resource, base_classes=base_classes, class_name=class_name)


    s += _render_methods(resource, class_name=class_name)
    s += '\n'

    return s

_pydantic_reserved_words = {'schema', 'json', 'construct', 'validate', 'copy', 'register', 'model_fields', 'model_construct', 'model_copy', 'model_dump', 'model_json_schema', 'model_dump_json', 'model_validate', 'list', 'dict', 'models'}

def _render_class_head(resource: APIResource, class_name: str, base_classes: list[str]) -> str:
    # print('rendering class head', resource)
    if not base_classes:
        raise ValueError("Must provide at least one base class")
    s = f'class {class_name}({", ".join(c for c in base_classes)}):'
    init_param_names = []
    if resource.init_params:
        has_protected_attrs = False
        for param_name, param in resource.init_params.items():
            if param_name in ('id', 'self', 'scope'):
                continue
            if param_name.startswith('_'):
                continue

            init_param_names.append(param_name)
            if param_name.startswith('model_'):
                s += '\n    model_config = pydantic.ConfigDict(protected_namespaces=())'
                has_protected_attrs = True

            s += f'\n    {param_name}'

            if param_name in _pydantic_reserved_words or has_protected_attrs:
                s += '_'
                is_reserved = True
            else:
                is_reserved = False
            if param.annotation is inspect._empty:
                cleaned_annotation = 'typing.Any'
            else:
                cleaned_annotation = param.clean_annotation()
                if isinstance(cleaned_annotation, APIResource):
                    cleaned_annotation = cleaned_annotation.as_python_annotation()
                elif inspect.isclass(cleaned_annotation):
                    if str(cleaned_annotation.__module__) == 'builtins':
                        cleaned_annotation = f'{cleaned_annotation.__qualname__}'
                        cleaned_annotation = cleaned_annotation
                    else:
                        cleaned_annotation = f'{cleaned_annotation.__module__}.{cleaned_annotation.__qualname__}'
                # print(f'resolved annotation ({param.annotation!r} for init param {param_name} to {cleaned_annotation!r}')
            cleaned_annotation = str(cleaned_annotation).replace('NoneType', 'None')
            if cleaned_annotation == 'Protocol':
                breakpoint()
            if param.kind in (2, 4):
                if param.kind == 2:
                    s += f': list[{cleaned_annotation}] = pydantic.Field('
                elif param.kind == 4:
                    s += f': dict[str, {cleaned_annotation}] = pydantic.Field('
                else:
                    raise ValueError()
            else:
                if param.default is inspect._empty:
                    if cleaned_annotation.startswith('typing.Union['):
                        cleaned_annotation = cleaned_annotation.replace('typing.Union[', 'typing.Union[_REQUIRED_INIT_PARAM, ', 1)
                        s += f': {cleaned_annotation} = pydantic.Field('
                    else:
                        s += f': typing.Union[{cleaned_annotation}, _REQUIRED_INIT_PARAM] = pydantic.Field('
                else:
                    s += f': {cleaned_annotation} = pydantic.Field('

            if param.default is inspect._empty:
                s += 'REQUIRED_INIT_PARAM'  # TODO: make init params optional to allow alternate constructors and references
            else:
                s += repr(param.default)  # XXX: hope this works

            if param.kind not in (2, 4):
                s += f', description={param.doc!r}'
            if is_reserved:
                s += f', alias={param_name!r}'
            s += ')'
    s += f'\n    _init_params: typing.ClassVar[list[str]] = {init_param_names!r}'
    methods = []
    classmethods = []
    for method in resource.methods:
        if method.is_classmethod():
            classmethods.append(method.method_name)
        else:
            methods.append(method.method_name)

    altconstructors = []
    for method in resource.alternate_constructors:
        altconstructors.append(method.method_name)

    s += f'\n    _method_names: typing.ClassVar[list[str]] = {methods!r}'
    s += f'\n    _classmethod_names: typing.ClassVar[list[str]] = {classmethods!r}'
    s += f'\n    _cdk_class_fqn: typing.ClassVar[str] = {resource.python_qualname!r}'
    s += f'\n    _alternate_constructor_method_names: typing.ClassVar[list[str]] = {altconstructors!r}'

    s += '\n    ...'
    s += '\n'
    return s

def render_method(method_name: str, body: str, decorators: Optional[list[str]] = None, parameters: Optional[dict[str, str | None]] = None, return_type: Optional[str] = None):
    ...

_module_param_classes = {}
_module_param_classes['_interface_methods'] = []
def _render_methods(resource: APIResource, class_name: str) -> str:
    s = '\n'
    if resource.module_name not in _module_param_classes:
        _module_param_classes[resource.module_name] = []
    assert class_name == resource.model_class_name

    model_config_class_name = resource.config_class_name
    model_config_class_full_name = resource.config_class_fullname
    has_protected_attr = False

    for method in resource.alternate_constructors:
        if not has_protected_attr and method.method_name.startswith('model_'):
            has_protected_attr = True
            s += '\n    model_config = pydantic.ConfigDict(protected_namespaces=())'


        if method.method_name in _pydantic_reserved_words or method.method_name.startswith('model_'):
            method_name = method.method_name + '_'
            is_reserved = True
        else:
            method_name = method.method_name
            is_reserved = False
        meth_param_model_name = f'{class_name}{snake_to_camel(method.method_name)}Params'
        mod = modules[method.module_name]
        fullname = f'models.{mod.namespace}.{meth_param_model_name}'
        _module_param_classes[resource.module_name].append(fullname)
        s += f'\n    {method_name}: typing.Optional[{fullname}] = pydantic.Field(None, description={method.docstring!r}'
        if is_reserved:
            s += f', alias={method.method_name!r}'
        s += ')'



    if resource.nonconstructor_methods or resource.configurable_properties:
        s += f'\n    resource_config: typing.Optional[{model_config_class_full_name}] = pydantic.Field(None)'
        _module_param_classes[resource.module_name].append(resource.model_class_fullname)
        s += '\n\n'

        # TODO: interface simplification?
        s += f'\nclass {model_config_class_name}(pydantic.BaseModel):'
        for method in resource.nonconstructor_methods:

            if not has_protected_attr and method.method_name.startswith('model_'):
                has_protected_attr = True
                s += '\n    model_config = pydantic.ConfigDict(protected_namespaces=())'

            if method.method_name in _pydantic_reserved_words or method.method_name.startswith('model_'):
                method_name = method.method_name + '_'
                is_reserved = True
            else:
                method_name = method.method_name
                is_reserved = False

            if method.parameters(exclude=['self']) or method.clean_return_type in reverse_resources:
                meth_param_model_name = f'{class_name}{snake_to_camel(method.method_name)}Params'
                mod = modules[method.module_name]
                fullname = f'models.{mod.namespace}.{meth_param_model_name}'
                _module_param_classes[resource.module_name].append(fullname)
                if method.method_name == 'apply_removal_policy':
                    s += f'\n    {method_name}: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None'
                else:
                    s += f'\n    {method_name}: typing.Optional[list[{fullname}]] = pydantic.Field(None, description={method.docstring!r}'
            else:
                s += f'\n    {method_name}: typing.Optional[bool] = pydantic.Field(None, description={method.docstring!r}'
            if is_reserved:
                s += f', alias={method.method_name!r}'
            s += ')'
        for property_name, return_resource in resource.configurable_properties.items():
            if return_resource.resource_type == 'Interface' and return_resource.nonconstructor_methods:
                prop_config_name = f'models._interface_methods.{return_resource.config_class_name}'
            else:
                prop_config_name = return_resource.config_class_fullname
            if prop_config_name is not None:
                s += f'\n    {property_name}_config: typing.Optional[{prop_config_name}] = pydantic.Field(None)'

    for method in resource.methods:
        if not method.parameters(exclude=['self']) and not method.clean_return_type in reverse_resources:
            continue
        s += '\n\n'
        param_protected_attr = False
        meth_param_model_name = f'{class_name}{snake_to_camel(method.method_name)}Params'
        s += f'class {meth_param_model_name}(pydantic.BaseModel):'
        for param_name, param in method.parameters(exclude=['self']).items():
            if param_name in ('id', 'self', 'scope'):
                # print(f'WARNING: sus param {param_name!r} in resource config for method {method.method_name!r} ({resource.model_class_fullname})')
                ...


            if not param_protected_attr and param_name.startswith('model_'):
                param_protected_attr = True
                s += '\n    model_config = pydantic.ConfigDict(protected_namespaces=())'

            s += f'\n    {param_name}'
            if param_name in _pydantic_reserved_words or param_name.startswith('model_'):
                s += '_'
                is_reserved = True
            else:
                is_reserved = False
            if param.annotation is inspect._empty:
                cleaned_annotation = 'typing.Any'
            else:
                cleaned_annotation = param.clean_annotation()
                if isinstance(cleaned_annotation, APIResource):
                    cleaned_annotation = cleaned_annotation.as_python_annotation()
                elif inspect.isclass(cleaned_annotation):
                    if str(cleaned_annotation.__module__) == 'builtins':
                        cleaned_annotation = f'{cleaned_annotation.__qualname__}'
                        cleaned_annotation = cleaned_annotation
                    else:
                        cleaned_annotation = f'{cleaned_annotation.__module__}.{cleaned_annotation.__qualname__}'
                # print(f'resolved annotation ({param.annotation!r} for init param {param_name} to {cleaned_annotation!r}')
            cleaned_annotation = str(cleaned_annotation).replace('NoneType', 'None')
            if cleaned_annotation == 'Protocol':
                breakpoint()
            if param.kind in (2, 4):
                if param.kind == 2:
                    s += f': list[{cleaned_annotation}] = pydantic.Field('
                elif param.kind == 4:
                    s += f': dict[str, {cleaned_annotation}] = pydantic.Field('
                else:
                    raise ValueError()
            else:
                s += f': {cleaned_annotation} = pydantic.Field('

            if param.default is inspect._empty:
                s += '...'
            else:
                s += repr(param.default)  # XXX: hope this works

            if param.kind not in (2, 4):
                s += f', description={param.doc!r}'
            if is_reserved:
                s += f', alias={param_name!r}'
            s += ')'
        if method not in resource.nonconstructor_methods:
            s += '\n    ...'
            continue
        rtype = method.clean_return_type
        if rtype in reverse_resources:
            rtype_resource = reverse_resources[rtype]
            if rtype_resource.resource_type == 'Interface':
                if rtype_resource.nonconstructor_methods:

                    rtype_config_type_name = f'models._interface_methods.{rtype_resource.config_class_name}'
                else:
                    rtype_config_type_name = None
            else:
                rtype_config_type_name = rtype_resource.config_class_fullname

            if rtype_config_type_name is not None:
                # TODO: handle cyclical references in return type
                return_config_name = 'return_config' # TODO: name this better?
                s += f'\n    {return_config_name}: typing.Optional[list[{rtype_config_type_name}]] = pydantic.Field(None)'

        s += '\n    ...'
    return s


# _iface_method_config_class_names = {}

def render_iface_methods(resource: APIResource) -> str:
    assert resource.resource_type == 'Interface'
    class_name = f'{snake_to_camel(resource.module_info.namespace)}{resource.model_class_name}'
    config_class_name = resource.config_class_name
    s = ''
    if not resource.nonconstructor_methods:
        # _iface_method_config_class_names[resource.obj] = None
        return f'\n#  {resource.qualname} skipped\n'
    s += f'\n\nclass {config_class_name}(pydantic.BaseModel):'
    _module_param_classes['_interface_methods'].append(f'models._interface_methods.{config_class_name}')
    i = 0
    n = 0
    for method in resource.nonconstructor_methods:
        if method.method_name in _pydantic_reserved_words:
            method_name = method.method_name + '_'
            is_reserved = True
        else:
            method_name = method.method_name
            is_reserved = False

        if method.parameters(exclude=['self']) or (method.clean_return_type in reverse_resources and reverse_resources[method.clean_return_type].config_class_name):
            i += 1
            meth_param_model_name = f'{class_name}{snake_to_camel(method.method_name)}Params'
            mod = modules[method.module_name]
            fullname = f'models._interface_methods.{meth_param_model_name}'
            _module_param_classes['_interface_methods'].append(fullname)
            s += f'\n    {method_name}: typing.Optional[list[{fullname}]] = pydantic.Field(None, description={method.docstring!r}'
        else:
            s += f'\n    {method_name}: typing.Optional[bool] = pydantic.Field(None, description={method.docstring!r}'
        if is_reserved:
            s += f', alias={method.method_name!r}'
        s += ')'

    s += '\n'
    for method in resource.nonconstructor_methods:
        if not method.parameters(exclude=['self']) and (not method.clean_return_type in reverse_resources or reverse_resources[method.clean_return_type].config_class_name is None):
            continue
        n += 1
        meth_param_model_name = f'{class_name}{snake_to_camel(method.method_name)}Params'
        s += f'\n\nclass {meth_param_model_name}(pydantic.BaseModel):'
        for param_name, param in method.parameters(exclude=['self']).items():
            if param_name in ('id', 'self', 'scope'):
                # print(f'WARNING: interface method {method.method_name!r} param {param_name!r} is suspect ({resource.config_class_name})')
                ...
            s += f'\n    {param_name}'
            if param_name in _pydantic_reserved_words:
                s += '_'
                is_reserved = True
            else:
                is_reserved = False
            if param.annotation is inspect._empty:
                cleaned_annotation = 'typing.Any'
            else:
                cleaned_annotation = param.clean_annotation()
                if isinstance(cleaned_annotation, APIResource):
                    cleaned_annotation = cleaned_annotation.as_python_annotation()
                elif inspect.isclass(cleaned_annotation):
                    if str(cleaned_annotation.__module__) == 'builtins':
                        cleaned_annotation = f'{cleaned_annotation.__qualname__}'
                        cleaned_annotation = cleaned_annotation
                    else:
                        cleaned_annotation = f'{cleaned_annotation.__module__}.{cleaned_annotation.__qualname__}'
                # print(f'resolved annotation ({param.annotation!r} for init param {param_name} to {cleaned_annotation!r}')
            cleaned_annotation = str(cleaned_annotation).replace('NoneType', 'None')
            if cleaned_annotation == 'Protocol':
                breakpoint()
            if param.kind in (2, 4):
                if param.kind == 2:
                    s += f': list[{cleaned_annotation}] = pydantic.Field('
                elif param.kind == 4:
                    s += f': dict[str, {cleaned_annotation}] = pydantic.Field('
                else:
                    raise ValueError()
            else:
                s += f': {cleaned_annotation} = pydantic.Field('

            if param.default is inspect._empty:
                s += '...'
            else:
                s += repr(param.default)  # XXX: hope this works

            if param.kind not in (2, 4):
                s += f', description={param.doc!r}'
            if is_reserved:
                s += f', alias={param_name!r}'
            s += ')'
        rtype = method.clean_return_type
        if rtype in reverse_resources:
            rtype_resource = reverse_resources[rtype]
            if rtype_resource.resource_type == 'Interface' and rtype_resource.nonconstructor_methods:
                rtype_config_type_name = f'models._interface_methods.{rtype_resource.config_class_name}'
            else:
                rtype_config_type_name = rtype_resource.config_class_fullname

            if rtype_config_type_name is not None:
                return_config_name = 'return_config'  # TODO: name this better?
                s += f'\n    {return_config_name}: typing.Optional[list[{rtype_config_type_name}]] = pydantic.Field(None)'
    assert i == n
    return s
def snake_to_camel(s: str) -> str:
    return ''.join(p.title() for p in s.split('_'))


def _get_all_modules() -> dict[str, Module]:
    with open('t.html', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')

    nav_container = soup.find(id='docsNav')

    modules: dict[str, Module] = {}

    assert isinstance(nav_container, bs4.Tag)
    navgroups = nav_container.find('div', class_='navGroups')
    assert isinstance(navgroups, bs4.Tag)
    for group in navgroups.find_all('div', class_='navGroup'):
        assert isinstance(group, bs4.Tag)
        heading = group.find('h3')
        if not heading:
            continue
        title: str = heading.text.strip()
        if 'API Reference' in title:
            continue
        if title.startswith('@'):
            continue
        # if title.startswith('constructs'):
        #     continue
        if 'aws_codeartifact' in title:
            continue
        if title.endswith('¹'):
            title = title[:-1]
        module_qualname = title

        classes: dict[str, APIResource] = {}
        constructs: dict[str, APIResource] = {}
        structs: dict[str, APIResource] = {}
        enums: dict[str, APIResource] = {}
        interfaces: dict[str, APIResource] = {}
        cloudformation_resources: dict[str, APIResource] = {}
        cloudformation_property_types: dict[str, APIResource] = {}

        submapping = {
            'Constructs': (constructs, 'Construct'),
            'Classes': (classes, 'Class'),
            'Structs': (structs, 'Struct'),
            'Interfaces': (interfaces, 'Interface'),
            'CloudFormation Resources': (cloudformation_resources, 'CloudFormation Resource'),
            'CloudFormation Property Types': (cloudformation_property_types, 'CloudFormation Property Type'),
            'Enums': (enums, 'Enum')
        }

        subnav_sections = group.find_all(navsubgroup)
        for section in subnav_sections:
            subtitle = section.find('h4')
            if not subtitle:
                continue
            subtitle = subtitle.text.strip()
            print('\t', subtitle)
            if subtitle not in submapping:
                raise ValueError(f"Unknown submapping {subtitle}")

            data: dict[str, APIResource]
            rtype: str

            data, rtype = submapping[subtitle]

            for item in section.find_all('li'):
                print('\t\t', item.text)
                link = item.find('a')
                if not link:
                    print('No link on LI', item)
                    continue
                href: str = link.get('href')
                if not href:
                    print('no href')
                assert href.startswith('/')
                url = 'https://docs.aws.amazon.com' + href
                name = href.split('/')[-1].removesuffix('.html').replace(module_qualname, '', 1).removeprefix('.')
                if '.experimental.' in module_qualname:
                    continue
                resource = APIResource(doc_url=url, module_name=module_qualname, name=name, resource_type=rtype)
                data[name] = resource
        module = Module(
            name=module_qualname,
            classes=classes,
            constructs=constructs,
            structs=structs,
            enums=enums,
            interfaces=interfaces,
            cloudformation_resources=cloudformation_resources,
            cloudformation_property_types=cloudformation_property_types,
        )
        modules[module_qualname] = module
    return modules

modules = _get_all_modules()

all_resources: dict[str, APIResource] = {}
for modname, module in modules.items():
    mod_resources = dict(**module.all)
    for rname, resource in mod_resources.items():
        all_resources[resource.python_qualname] = resource

reverse_resources: dict[Any, APIResource] = {}
for _, resource in all_resources.items():
    obj = resource.obj
    reverse_resources[obj] = resource

_interfaces = []
for _, r in all_resources.items():
    if r.resource_type == 'Interface':
        _interfaces.append(r.obj)
_implementations = {i: [] for i in _interfaces}

for _, r in all_resources.items():
    for iface in r.implements():
        if iface not in _implementations:
            _implementations[iface] = [r]
        else:
            _implementations[iface].append(r)


# special cases
_implementations[aws_cdk.aws_rds.IInstanceEngine] = [all_resources['aws_cdk.aws_rds.DatabaseInstanceEngine']]
_implementations[aws_cdk.aws_rds.IClusterEngine] = [all_resources['aws_cdk.aws_rds.DatabaseClusterEngine']]


for iface, _impls in _implementations.items():
    if not _impls:
        print(f'NO IMPL FOR {iface!r}')




def write_modules(mods: list[Module], outdir: str) -> None:
    interace_method_module = os.path.join(outdir, '_interface_methods.py')
    s = ''
    for mod in mods:
        for ifaceresource in mod.interfaces.values():
            s += render_iface_methods(ifaceresource)
    with open(interace_method_module, 'w', encoding='utf-8') as f:
        f.write('from __future__ import annotations\n')
        f.write('import pydantic\nimport aws_cdk\nimport typing\nimport datetime\n\n')
        f.write(s)
        f.write('\n\nimport models')

    for mod in mods:
        mod_code = render_module(mod)
        outfile = os.path.join(outdir, mod.namespace) + '.py'
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(mod_code)
    utilfile = os.path.join(outdir, '_utils.py')
    with open(utilfile, 'w', encoding='utf-8') as f:
        f.write('import models, datetime')
        f.write('\nfor m in (')
        for mod in mods:
            for n, r in mod.all.items():
                if r.resource_type in ('Enum', 'Interface'):
                    continue
                fullname = r.as_python_annotation()
                if '.experimental.' not in fullname:
                    f.write(f'{fullname},')
            paramclasses = _module_param_classes.get(mod.name, '')
            for classname in paramclasses:
                if '.experimental.' in classname:
                    continue
                f.write(f'{classname},')
        for c in _module_param_classes['_interface_methods']:
            f.write(f'{c}, ')
        f.write('):')
        f.write('\n    try:')
        f.write(f'\n        m.update_forward_refs()')
        f.write('\n    except Exception as e:')
        f.write('\n        print("f", m, e)')
        f.write('\n')
    initfile = os.path.join(outdir, '_init.py')
    with open(initfile, 'w') as f:
        f.write('import typing\nimport pydantic\nfrom ._base import BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, BaseConstruct, UnsupportedResource, AnyResource, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM\nfrom .core import *\n')
        for mod in mods:
            if '.experimental' in mod.namespace:
                continue
            f.write(f'from . import {mod.namespace}\n')
        f.write('from . import _interface_methods\nfrom . import _utils\nfrom . import core\n')
        f.write('for mod in [\n')
        for mod in mods:
            if '.experimental' in mod.namespace:
                continue
            f.write(f'    {mod.namespace},\n')
        f.write(']:\n')
        f.write("    for name in dir(mod):\n")
        f.write("        obj = getattr(mod, name)\n")
        f.write("        if hasattr(obj, 'update_forward_refs'):\n")
        f.write("            try:\n")
        f.write("                obj.update_forward_refs()\n")
        f.write("            except Exception as e:\n")
        f.write("                print('f', mod, name, e)\n")

        for mod in mods:
            if mod.namespace == 'core':
                continue
            if '.experimental' in mod.namespace:
                continue
            f.write(f'{mod.namespace}.ModuleModel.update_forward_refs()\n')

        f.write('class MegaModel(pydantic.BaseModel):\n')
        for mod in mods:
            if '.experimental' in mod.namespace:
                continue
            if mod.namespace == 'core':
                continue
            f.write(f"    {mod.namespace}_: typing.Optional[{mod.namespace}.ModuleModel] = pydantic.Field(None, alias={mod.namespace!r})\n")



if __name__ == '__main__':
    write_modules(list(modules.values()), outdir='models')

