from __future__ import annotations

import abc
import collections.abc
import datetime
import enum
import importlib
import inspect
import logging
import types
import typing
from collections import deque

import aws_cdk
import constructs
import pydantic
import cdk_yaml.generated  # noqa
from cdk_yaml.generated import _generated


class ReplaceKey(pydantic.BaseModel):
    with_key: typing.Optional[str] = None
    prefix_with_key: typing.Optional[str] = None


class Duration(pydantic.BaseModel):
    parse_from_string: typing.Optional[str] = None
    minutes: typing.Optional[int] = None
    millis: typing.Optional[int] = None
    hours: typing.Optional[int] = None
    days: typing.Optional[int] = None


PostgresEngineVersion = enum.Enum(
    'PostgresEngineVersion',
    {name: name for name in dir(aws_cdk.aws_rds.PostgresEngineVersion) if name.startswith('VER_')},
)
MysqlEngineVersion = enum.Enum(
    'MysqlEngineVersion', {name: name for name in dir(aws_cdk.aws_rds.MysqlEngineVersion) if name.startswith('VER_')}
)
MariaDbEngineVersion = enum.Enum(
    'MariaDbEngineVersion',
    {name: name for name in dir(aws_cdk.aws_rds.MariaDbEngineVersion) if name.startswith('VER_')},
)



class PostgresEngine(pydantic.BaseModel):
    version: PostgresEngineVersion


class MysqlEngine(pydantic.BaseModel):
    version: MysqlEngineVersion


class MariaDbEngine(pydantic.BaseModel):
    version: MariaDbEngineVersion


class Engine(pydantic.BaseModel):
    postgres: typing.Optional[PostgresEngine] = None
    mysql: typing.Optional[MysqlEngine] = None
    maria_db: typing.Optional[MariaDbEngine] = None


class TypeNotImplemented(pydantic.BaseModel):
    unsupported_field: typing.Any = None

Architecture = enum.Enum(
    'Architecture', {'X86_64': 'X86_64', 'ARM64': 'ARM64'}
)

class CpuArchitecture(pydantic.BaseModel):
    architecture:  Architecture


OSFamily = enum.Enum('OSFamily',
                                  {name: name for name in dir(aws_cdk.aws_ecs.OperatingSystemFamily) if not name.startswith('_') and name.replace('_', '').isupper()})

class OperatingSystemFamily(pydantic.BaseModel):
    family: OSFamily

class CertificateValidation(pydantic.BaseModel):
    notimplemented: None

AllowedMethods = enum.Enum(
    'AllowedMethods',
    {name: name for name in dir(aws_cdk.aws_cloudfront.AllowedMethods) if not name.startswith('_') and name.replace('_', '').isupper()}
)

ResponseHeaderPolicy = enum.Enum(
    'ResponseHeaderPolicy',
    {name: name for name in dir(aws_cdk.aws_cloudfront.ResponseHeadersPolicy) if
     not name.startswith('_') and name.replace('_', '').isupper()}
)

class ConstructBase(pydantic.BaseModel):
    nothinghere: bool

_special_cases = {
    constructs.Construct: ConstructBase,
    aws_cdk.aws_iam.IPrincipal: TypeNotImplemented,
    aws_cdk.Duration: Duration,
    aws_cdk.aws_s3.ReplaceKey: ReplaceKey,
    aws_cdk.aws_rds.IEngine: Engine,
    aws_cdk.aws_rds.IInstanceEngine: Engine,
    aws_cdk.aws_ec2.IGatewayVpcEndpointService: TypeNotImplemented,
    aws_cdk.aws_ecs.CpuArchitecture: CpuArchitecture,
    aws_cdk.aws_ecs.OperatingSystemFamily: OperatingSystemFamily,
    aws_cdk.aws_certificatemanager.CertificateValidation: TypeNotImplemented,
    aws_cdk.aws_autoscaling.HealthCheck: TypeNotImplemented,
    aws_cdk.Size: TypeNotImplemented,
    aws_cdk.aws_servicediscovery.INamespace: TypeNotImplemented,
    aws_cdk.aws_autoscaling.BlockDeviceVolume: TypeNotImplemented,
    aws_cdk.aws_ecs.PlacementConstraint: TypeNotImplemented,
    aws_cdk.aws_cloudfront.CacheCookieBehavior: TypeNotImplemented,
    aws_cdk.aws_cloudfront.OriginRequestHeaderBehavior: TypeNotImplemented,
    aws_cdk.aws_cloudfront.CacheQueryStringBehavior: TypeNotImplemented,
    aws_cdk.aws_cloudfront.GeoRestriction: TypeNotImplemented,
    aws_cdk.aws_signer.Platform: TypeNotImplemented,
    aws_cdk.aws_cloudfront.CachedMethods: TypeNotImplemented,
    aws_cdk.aws_cloudfront.AllowedMethods: AllowedMethods,
    aws_cdk.aws_lambda.IDestination: TypeNotImplemented,
    aws_cdk.aws_cloudfront.OriginRequestCookieBehavior: TypeNotImplemented,
    aws_cdk.aws_lambda.IEventSource: TypeNotImplemented,
    aws_cdk.aws_lambda.Architecture: TypeNotImplemented,
    aws_cdk.aws_cloudfront.OriginRequestQueryStringBehavior: TypeNotImplemented,
    aws_cdk.aws_cloudfront.CacheHeaderBehavior: TypeNotImplemented,
    aws_cdk.aws_lambda.FileSystem: TypeNotImplemented,
    aws_cdk.aws_cloudfront.ResponseHeadersPolicy: ResponseHeaderPolicy,
    aws_cdk.aws_lambda.Function: TypeNotImplemented,
    aws_cdk.aws_cloudfront.FunctionEventType: TypeNotImplemented,
    aws_cdk.aws_cloudfront.Function: TypeNotImplemented,
    aws_cdk.aws_cloudfront.LambdaEdgeEventType: TypeNotImplemented,
    aws_cdk.aws_cloudfront.IOrigin: TypeNotImplemented,

}
from collections.abc import Iterable
import types
from typing import Any, Dict

def _is_iterable(obj: typing.Any) -> bool:
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def flatten_object(nested: Any, sep: str="_", prefix="") -> Dict[str, Any]:
    """Flattens nested dictionaries and iterables

    The key to a leaf (something is not list-like or a dictionary)
    is the accessors to that leaf from the root separated by sep
    prefixed with prefix.

    If flattening results in a duplicate key raises a ValueError.

    For example:
      flatten_object([{'a': {'b': 'c'}}, [1]],
                     prefix='nest_') == {'nest_0_a_b': 'c', 'nest_1_0': 1}
    """
    ans = {}

    def flatten(x, name=()):
        if isinstance(x, dict):
            for k,v in x.items():
                flatten(v, name + (str(k),))
        elif isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for i, v in enumerate(x):
                flatten(v, name + (str(i),))
        else:
            key = sep.join(name)
            if key in ans:
                raise ValueError(f"Duplicate key {key}")
            ans[prefix + sep.join(name)] = x

    flatten(nested)
    return ans

def flatten_annotation(annotation: typing.Any) -> typing.Generator[typing.Any, None, None]:
    """
    flatten an annotation to yield its constructive parts.

    For example, flatting the following annotation:
        Union[Sequence[aws_cdk.aws_foo.Bar], aws_cdk.aws_baz.Bacon]
    Will traverse generics and successively yield the constituent concrete types like so:
        aws_cdk.aws_foo.Bar, aws_cdk.aws_baz.Bacon

    If a provided annotation is already a concrete type, it is yielded back unaltered
    """
    args = typing.get_args(annotation)
    if args:
        for arg in args:
            yield from flatten_annotation(arg)
    else:
        yield annotation


class ConstructTree:
    def __init__(self, root):
        self.root = root
        self.seen: set[ConstructNode] = set()
        self.current_node = root

    def traverse(self) -> set['ConstructNode']:
        """
        Build the tree, iterating through all children
        :return:
        """
        to_do: deque[ConstructNode] = deque([self.current_node])
        while to_do:

            node = to_do.pop()
            if node in self.seen:
                continue
            self.seen.add(node)
            for child in node.children:
                to_do.appendleft(child)
            if node.is_implementation_protocol:
                if node.has_concrete:
                    implementation = node.get_implementation()
                    to_do.appendleft(implementation)
                # else:
                #     if node in

        self.build_relationships()
        return self.seen

    def build_relationships(self) -> None:
        for node in self.seen:
            for child in node.children:
                child.parents.add(node)

    def dependency_order(self) -> list[ConstructNode]:
        # XXX: doesn't really work.
        # but probably is not needed anymore
        nodes = list(self.seen)
        # start with nodes that have no dependencies
        ordered = [node for node in nodes if not node.children]
        for node in ordered:
            nodes.remove(node)
        while nodes:
            to_add = []
            for node in nodes:
                if all(child in ordered for child in node.children if child.name != node.name):
                    to_add.append(node)
            if not to_add and nodes:
                # we still have nodes with unresolved dependencies
                # but there are no more nodes to add that have all met dependencies -- possible circular/self reference
                # we're stuck here unless we implement handling for circular/self references.
                breakpoint()
                raise NotImplementedError(f'Circular/self reference detected. This is not currently supported.')
            ordered.extend(to_add)
            for node in to_add:
                nodes.remove(node)
        to_remove = []
        for node in ordered:
            if node.is_implementation_protocol and node.has_concrete:
                assert node.get_implementation() in ordered
                to_remove.append(node)
        for node in to_remove:
            ordered.remove(node)
        return ordered


class ConstructNode:
    def __init__(self, construct, allowed_names: typing.Union[typing.Literal['__all__'], typing.List[str]] = '__all__'):
        self.construct = construct
        self._allowed_names: typing.Union[typing.Literal['__all__'], typing.List[str]] = allowed_names
        self._children: set[ConstructNode] = set()
        self._implementations: set[ConstructNode] = set()
        self.parents: set[ConstructNode] = set()  # for now this is just informational, I don't think this is required

    def __repr__(self) -> str:
        return f'ConstructNode({self.construct!r})'

    def __hash__(self) -> int:
        return hash(self.construct)

    def __eq__(self, other: typing.Any) -> bool:
        return hash(other) == hash(self)

    @property
    def is_implementation_protocol(self) -> bool:
        return self.name.startswith('I') and self.name[1].isupper()

    @property
    def has_concrete(self) -> bool:
        if self._implementations:
            return True
        else:
            concrete = self._get_concrete()
            if concrete is not None:
                return True
            else:
                return False

    def get_implementation(self) -> typing.Optional['ConstructNode']:
        if self._implementations:
            assert len(self._implementations) == 1
            return list(self._implementations)[0]
        else:
            concrete = self._get_concrete()
            return concrete

    def _get_concrete(self) -> typing.Optional['ConstructNode']:
        if not self.is_implementation_protocol:
            raise ValueError('Cannot get concrete from non-implementation classes')

        concrete_name = self.name.replace('I', '', 1)
        concrete = getattr(self.module, concrete_name, None)
        if concrete is not None:
            concrete_node = ConstructNode(concrete)
            logging.debug(f'({self}) Resolved implementation to {concrete_node}')
            self._implementations.add(concrete_node)
            return concrete_node
        else:
            logging.debug(f'({self}) failed to resolve concrete construct')
            return None

    @property
    def model_module(self):
        return f'cdk_yaml.generated{("." + self.mod_namespace) if self.mod_namespace else ""}'

    @property
    def model_qualname(self):
        return f'{self.model_module}.{self.name}'

    @property
    def modname(self) -> str:
        return self.construct.__module__

    @property
    def module(self) -> types.ModuleType:
        mod = importlib.import_module(self.modname)
        return mod

    @property
    def name(self) -> str:
        return self.construct.__qualname__

    @property
    def qualname(self) -> str:
        return f'{self.modname}.{self.name}'

    @property
    def mod_namespace(self) -> str:
        if 'aws_cdk' not in self.modname:
            raise ValueError('cant get mod namespace for non-cdk modules')
        if self.modname == 'aws_cdk':
            return ''
        if '.' not in self.modname:
            raise ValueError('Error in calculating module namespace. This is most likely a bug.')
        return self.modname.split('.', 1)[1]

    @property
    def children(self) -> set['ConstructNode']:
        """Direct descendents for parameters"""
        if self._children:
            return self._children
        else:
            for child in self._get_children():
                self._children.add(child)
            return self._children

    def _resolve_forward_ref(self, ref: typing.ForwardRef) -> typing.Any:
        if '.' in ref.__forward_arg__:
            parts = ref.__forward_arg__.split('.')[::-1]
            get_from = self.module
            while parts:
                name = parts.pop()
                obj = getattr(get_from, name, None)
                if obj is None:
                    return None
                get_from = obj
            logging.debug(f'({self}) resolved forward ref: {ref!r}) to {obj!r}')
            return obj

        obj = getattr(self.module, ref.__forward_arg__, None)
        if obj is None:
            logging.debug(f'({self}) failed to resolve forward ref: {ref!r})')
            return None
        logging.debug(f'({self}) resolved forward ref: {ref!r}) to {obj!r}')
        return obj

    def _get_children(self) -> typing.Generator['ConstructNode', None, None]:
        sig = inspect.signature(self.construct.__init__)
        for param_name, param in sig.parameters.items():
            if param_name in ('self', 'scope'):
                continue
            for annotation in flatten_annotation(param.annotation):
                if type(annotation) == typing.ForwardRef:
                    resolved_annotation = self._resolve_forward_ref(annotation)
                    if resolved_annotation is None:
                        breakpoint()
                        logging.debug(
                            f'({self}) annotation skipped for unresolved param "{param_name}": {annotation!r} (type: {type(annotation)})'
                        )
                        continue
                    else:
                        annotation = resolved_annotation
                if 'aws_cdk' in getattr(annotation, '__module__', ''):
                    yield ConstructNode(annotation)
                    continue
                if annotation in (str, type(None), int, float, bool, datetime.datetime):
                    continue
                else:
                    logging.debug(
                        f'({self}) annotation skipped for param "{param_name}": {annotation!r} (type: {type(annotation)})'
                    )
                    continue

    @property
    def parameters(self):
        sig = inspect.signature(self.construct.__init__)
        if self._allowed_names == '__all__':
            return sig.parameters
        else:
            assert isinstance(self._allowed_names, list)
            return {n: p for n,p in sig.parameters.items() if n in self._allowed_names}


_annotation_model_map = {}


class ModelTree:
    def __init__(self, construct_tree: ConstructTree):
        self._construct_tree = construct_tree
        self.nodes: list[ConstructNode] = self._construct_tree.dependency_order()
        self.annotation_model_map = _annotation_model_map

    def clean_annotation(self, annotation: typing.Any, node: typing.Optional[ConstructNode] = None) -> typing.Any:
        """
        Replace references to constructs with references to models.

        For example, this annotation:
            Union[Sequence[aws_cdk.aws_foo.Bar], aws_cdk.aws_baz.Bacon]
        Will become this annotation:
            Union[Sequence[cdk_yaml.generated.aws_foo.BarModel], cdk_yaml.generated.aws_baz.BaconModel]
        """
        if type(annotation) == typing.ForwardRef and node is not None:
            resolved = node._resolve_forward_ref(annotation)
            if resolved:
                annotation = resolved
            else:
                logging.debug('Failed to resolve ref while cleaning annotation')
        if type(annotation) == str:
            assert node is not None, "Tried to resolve string type reference, but no node was provided"
            resolved = node._resolve_forward_ref(typing.ForwardRef(annotation))
            if resolved:
                annotation = resolved
            else:
                logging.debug('Failed to resolve ref while cleaning annotation')
        if annotation in _special_cases:
            return _special_cases[annotation]
        if annotation in self.annotation_model_map:
            return self.annotation_model_map[annotation]

        if 'aws_cdk' in getattr(annotation, '__module__', ''):
            _node = ConstructNode(annotation)
            if _node.is_implementation_protocol and _node.has_concrete:
                annotation = _node.get_implementation().construct
                return self.clean_annotation(annotation, node=_node)
        origin = typing.get_origin(annotation)
        args = typing.get_args(annotation)
        if origin is collections.abc.Sequence:
            origin = typing.Sequence
        if args:
            new_args = []
            for arg in args:
                arg = self.clean_annotation(arg, node=node)
                new_args.append(arg)
            new_args = tuple(new_args)
            return origin[new_args]
        else:
            if annotation in self.annotation_model_map:
                return self.annotation_model_map[annotation]
            elif 'aws_cdk' in getattr(annotation, '__module__', ''):
                return typing.ForwardRef(ConstructNode(annotation).model_qualname)
            else:
                return annotation

    def to_models(self) -> typing.Sequence[typing.Type[pydantic.BaseModel]]:
        models: list[typing.Type[pydantic.BaseModel]] = []
        for node in self.nodes:
            construct = node.construct
            model_params = {}
            param_descriptions = {}
            if construct in _special_cases:
                model = _special_cases[construct]
                models.append(model)
                continue
            if construct in self.annotation_model_map:
                continue
            if not isinstance(construct, type):
                breakpoint()
            if issubclass(construct, enum.Enum):
                self.annotation_model_map[construct] = construct
                if node.mod_namespace in _generated:
                    namespace = _generated[node.mod_namespace]
                else:
                    namespace = types.SimpleNamespace()
                    _generated[node.mod_namespace] = namespace
                setattr(namespace, node.name, construct)
                continue
            if node.is_implementation_protocol and node.has_concrete:
                logging.debug(
                    f'skipping implementation protocol node that has concrete implementation: {node!r} (implementation: {node.get_implementation()!r})'
                )
                continue

            for param_name, param in node.parameters.items():
                if param_name in ('self', 'scope', 'args', 'kwargs'):
                    continue
                logging.debug(f'({construct!r}) cleaning annotation for param "{param_name}"')
                annotation = self.clean_annotation(param.annotation, node)
                default = param.default if param.default != inspect._empty else ...
                if param_name == 'schema':
                    param_name = 'schema_'
                if param_name == 'json':
                    param_name = 'json_'
                if param_name == 'construct':
                    param_name = 'construct_'

                model_params[param_name] = (annotation, default)





            # def _to_construct_or_self(self, param_name, obj: typing.Any, _scope=None):
            #     logging.debug(f'resolving {obj!r}  {self.Config.params[param_name]}')
            #     if hasattr(obj, 'to_construct'):
            #         logging.debug('converting to construct')
            #         return obj.to_construct(_scope=_scope)
            #     elif isinstance(obj, list):
            #         logging.debug('flattening...')
            #         return [self._to_construct_or_self(param_name, item, _scope=_scope) for item in obj]
            #     elif isinstance(obj, dict):
            #         logging.debug('flattening...')
            #         return {k: self._to_construct_or_self(param_name, v) for k, v in obj.items()}
            #     else:
            #         logging.debug(f'skipping {obj!r}')
            #     return obj

            # def _to_construct(self, _scope=None):
            #
            #     config = self.Config
            #     params = config.params
            #     construct_klass = config.cdk_construct
            #     # kwargs = self.dict(exclude_unset=True)
            #     kwargs = dict(self._iter(
            #         to_dict=False,
            #         by_alias=False,
            #         exclude_unset=True,
            #         include=None,
            #         exclude=None,
            #         exclude_defaults=False,
            #         exclude_none=False
            #
            #     ))
            #     id = kwargs.pop('id', None)
            #     if _scope and id in _scope.resources:
            #         return _scope.resources[id]
            #     for param_name, value in kwargs.items():
            #         if hasattr(value, 'dict'):
            #             if list(value.dict(exclude_unset=True)) == ['id']:
            #                 kwargs[param_name] = _scope.resources[value.id]
            #                 continue
            #         kwargs[param_name] = self._to_construct_or_self(param_name, value, _scope=_scope)
            #
            #     if id:
            #         assert _scope is not None
            #         return construct_klass(_scope, id, **kwargs)
            #     else:
            #         return construct_klass(**kwargs)
            #
            #
            # def _validate_values(cls, values):
            #     return values

            Config = type('Config', (), {'params': model_params, 'cdk_construct': construct, 'arbitrary_types_allowed': True})
            # Base = type('Base', (pydantic.BaseModel, abc.ABC), {'Config': Config})
            if node.mod_namespace in _generated:
                namespace = _generated[node.mod_namespace]
            else:
                namespace = types.SimpleNamespace()
                _generated[node.mod_namespace] = namespace
            try:
                model = pydantic.create_model(node.name, **model_params, __module__=node.model_module, __config__=Config)
            except Exception as e:
                print('model creation failure', e, node)
                self.annotation_model_map[construct] = TypeNotImplemented
                setattr(namespace, node.name, TypeNotImplemented)
                continue
            self.annotation_model_map[construct] = model
            setattr(namespace, node.name, model)
            models.append(model)
        return models
