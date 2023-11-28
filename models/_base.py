import aws_cdk
import typing
from typing import Optional

import pydantic

UnsupportedResource: typing.TypeAlias = typing.Any

class _REQUIRED_INIT_PARAM(pydantic.BaseModel):
    """Sentinel value"""
    ...

REQUIRED_INIT_PARAM = _REQUIRED_INIT_PARAM()

class AnyResource(pydantic.BaseModel):
    from_resource_id: str

class GenericApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: aws_cdk.RemovalPolicy = pydantic.Field(...)


class PortRangeConfiguration(pydantic.BaseModel):
    start_port: int
    end_port: int

class ICMPTypeCodeConfiguration(pydantic.BaseModel):
    type: int | float
    code: int | float


class PortConfiguration(pydantic.BaseModel):
    tcp: Optional[int] = None
    udp: Optional[int] = None
    tcp_range: Optional[PortRangeConfiguration] = None
    udp_range: Optional[PortRangeConfiguration] = None
    icmp_type: Optional[int] = None
    icmp_type_and_code: Optional[ICMPTypeCodeConfiguration] = None
    icmp_ping: bool = False
    all_traffic: bool = False
    all_tcp: bool = False
    all_icmp: bool = False
    esp: bool = False
    ah: bool = False


class PortConnectionConfiguration(pydantic.BaseModel):
    resource_id: str
    port: PortConfiguration
    description: Optional[str] = None



class PeerConnectionConfiguration(pydantic.BaseModel):
    resource_id: str
    description: Optional[str] = None


class AnyConnectionConfiguration(pydantic.BaseModel):
    description: Optional[str] = None


class ConnectionsConfiguration(pydantic.BaseModel):
    add_security_group: Optional[list[PeerConnectionConfiguration]] = None
    allow_default_port_from: Optional[list[PeerConnectionConfiguration]] = None
    allow_default_port_from_any_ipv4: Optional[list[AnyConnectionConfiguration]] = None
    allow_default_port_internally: Optional[list[AnyConnectionConfiguration]] = None
    allow_default_port_to: Optional[list[PeerConnectionConfiguration]] = None
    allow_from: Optional[list[PortConnectionConfiguration]] = None
    allow_from_any_ipv4: Optional[list[AnyConnectionConfiguration]] = None
    allow_internally: Optional[list[AnyConnectionConfiguration]] = None
    allow_to: Optional[list[PortConnectionConfiguration]] = None
    allow_to_any_ipv4: Optional[list[AnyConnectionConfiguration]] = None
    allow_to_default_port: Optional[list[PeerConnectionConfiguration]] = None

class ConnectableMixin(pydantic.BaseModel):
    connections: Optional[ConnectionsConfiguration] = None

class APIBaseDef(pydantic.BaseModel):
    def shallow_dict(self, by_alias: bool = True, exclude_unset: bool = True, exclude_defaults: bool = False):
        """
        Like ``.dict`` but not recursive
        """
        d = dict(self._iter(
            to_dict=False,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            include=None,
            exclude=None,
            exclude_defaults=exclude_defaults,
            exclude_none=False
        ))
        return d


    def to_cdk_obj(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        raise NotImplementedError


class BaseConstruct(APIBaseDef):
    _construct_obj: typing.Any = pydantic.PrivateAttr(None)

    from_resource_id: Optional[str] = pydantic.Field(None)

    def to_cdk_obj(self, *args, **kwargs) -> typing.Any:
        return self.create_construct(*args, **kwargs)


    @classmethod
    @property
    def cdk_class(cls):
        assert hasattr(cls, '_cdk_class_fqn')
        return eval(cls._cdk_class_fqn)

    def create_construct(self, id: str, scope: aws_cdk.Stack):
        assert hasattr(self, '_init_params')
        assert hasattr(self, '_cdk_class_fqn')
        assert hasattr(self, '_alternate_constructor_method_names')
        kwargs = self.shallow_dict()
        create_kwargs = {}
        construct_klass = self.cdk_class
        alternate_constructor_params = []
        init_params = []

        method_calls = []

        for key, value in kwargs.items():
            if key in self._init_params and value is not REQUIRED_INIT_PARAM:
                init_params.append(key)
            if key in self._alternate_constructor_method_names:
                alternate_constructor_params.append(key)

            if key in self._method_names:
                method_calls.append(key)

        if 'from_resource_id' in kwargs and (alternate_constructor_params or init_params):
            raise ValueError("Invalid arguments. Import from resource ID was specified, but init params or alternate constructors were also provided.")


        if init_params and alternate_constructor_params:
            raise ValueError("Alternate constructors must be sole configuration element if present")

        if 'from_resource_id' in kwargs:
            ...
            construct = ...

        elif init_params:
            ...
            construct = ...

        elif alternate_constructor_params:
            assert len(alternate_constructor_params) == 1, 'Only one alternate constructor may be used, but multiple were specified'
            constructor_name = alternate_constructor_params[0]
            constructor_method = getattr(construct_klass, constructor_name)
            construct = ...

        else:
            # assume that the resource can be created with no arguments...
            ...
            construct = ...

        for method_name in method_calls:
            meth = getattr(construct, method_name)
            params = kwargs[method_name]
            meth_kwargs = {}




    def _configure_resource(self):
        ...

    def _from_init_params(self, id: str, scope: aws_cdk.Stack, **params):
        kwargs = {}
        for key, value in params.items():
            if isinstance(value, APIBaseDef):
                value = value.to_cdk_obj()
            elif ...:
                ...
            kwargs[key] = value
        cls = self.cdk_class(id, scope, **kwargs)
        return cls


    def _from_alternate_constructor(self, id: str, scope: aws_cdk.Stack, constructor_name: str, constructor_params: typing.Any) -> typing.Any:
        ...


    @classmethod
    def _get_class(cls):
        assert hasattr(cls, '_cdk_class_fqn')
        return eval(cls._cdk_class_fqn)


class BaseClass(APIBaseDef):
    ...


class BaseStruct(APIBaseDef):
    ...

class BaseCfnResource(APIBaseDef):
    ...

class BaseCfnProperty(APIBaseDef):
    ...

class BaseMethodParams(APIBaseDef):
    ...