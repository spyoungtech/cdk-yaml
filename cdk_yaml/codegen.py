from __future__ import annotations

import datetime
import enum
import importlib
import inspect
import logging
import types
import typing
from collections import deque

import aws_cdk
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


_special_cases = {
    aws_cdk.aws_iam.IPrincipal: TypeNotImplemented,
    aws_cdk.Duration: Duration,
    aws_cdk.aws_s3.ReplaceKey: ReplaceKey,
    aws_cdk.aws_rds.IEngine: Engine,
    aws_cdk.aws_rds.IInstanceEngine: Engine,
    aws_cdk.aws_ec2.IGatewayVpcEndpointService: TypeNotImplemented,
}


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


#
# _known_node_implementations = {
#     aws_cdk.aws_rds.IEngine: [aws_cdk.aws_rds.Engine]
# }


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
        nodes = list(self.seen)
        # start with nodes that have no dependencies
        ordered = [node for node in nodes if not node.children]
        for node in ordered:
            nodes.remove(node)
        while nodes:
            to_add = []
            for node in nodes:
                if all(child in ordered for child in node.children):
                    to_add.append(node)
            if not to_add and nodes:
                # we still have nodes with unresolved dependencies
                # but there are no more nodes to add that have all met dependencies -- possible circular/self reference
                # we're stuck here unless we implement handling for circular/self references.
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
    def __init__(self, construct):
        self.construct = construct
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
        return self.construct.__name__

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
            raise ValueError('something is wrong')
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
        return sig.parameters


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
            if not node:
                raise ValueError('heckkkk')
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
            if construct in _special_cases:
                model = _special_cases[construct]
                models.append(model)
                continue
            if construct in self.annotation_model_map:
                continue
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
                if param_name in ('self', 'scope'):
                    continue
                logging.debug(f'({construct!r}) cleaning annotation for param "{param_name}"')
                annotation = self.clean_annotation(param.annotation, node)
                default = param.default if param.default != inspect._empty else ...
                model_params[param_name] = (annotation, default)

            Config = type('Config', (), {'params': model_params, 'cdk_construct': construct})
            model = pydantic.create_model(node.name, **model_params, __module__=node.model_module, __config__=Config)
            self.annotation_model_map[construct] = model
            if node.mod_namespace in _generated:
                namespace = _generated[node.mod_namespace]
            else:
                namespace = types.SimpleNamespace()
                _generated[node.mod_namespace] = namespace
            setattr(namespace, node.name, model)
            models.append(model)
        return models
