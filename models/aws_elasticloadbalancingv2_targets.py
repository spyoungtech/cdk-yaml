from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_elasticloadbalancingv2_targets.AlbArnTarget
class AlbArnTargetDef(BaseClass):
    alb_arn: str = pydantic.Field(..., description='The ARN of the application load balancer to load balance to.\n')
    port: typing.Union[int, float] = pydantic.Field(..., description='The port on which the target is listening.')
    _init_params: typing.ClassVar[list[str]] = ['alb_arn', 'port']
    _method_names: typing.ClassVar[list[str]] = ['attach_to_network_target_group']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_elasticloadbalancingv2_targets.AlbArnTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[AlbArnTargetDefConfig] = pydantic.Field(None)


class AlbArnTargetDefConfig(pydantic.BaseModel):
    attach_to_network_target_group: typing.Optional[list[AlbArnTargetDefAttachToNetworkTargetGroupParams]] = pydantic.Field(None, description="Register this alb target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")

class AlbArnTargetDefAttachToNetworkTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.NetworkTargetGroupDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_elasticloadbalancingv2_targets.AlbTarget
class AlbTargetDef(BaseClass):
    alb: models.aws_elasticloadbalancingv2.ApplicationLoadBalancerDef = pydantic.Field(..., description='The application load balancer to load balance to.')
    port: typing.Union[int, float] = pydantic.Field(..., description='The port on which the target is listening.')
    _init_params: typing.ClassVar[list[str]] = ['alb', 'port']
    _method_names: typing.ClassVar[list[str]] = ['attach_to_network_target_group']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_elasticloadbalancingv2_targets.AlbTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[AlbTargetDefConfig] = pydantic.Field(None)


class AlbTargetDefConfig(pydantic.BaseModel):
    attach_to_network_target_group: typing.Optional[list[AlbTargetDefAttachToNetworkTargetGroupParams]] = pydantic.Field(None, description="Register this alb target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")

class AlbTargetDefAttachToNetworkTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.NetworkTargetGroupDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_elasticloadbalancingv2_targets.InstanceIdTarget
class InstanceIdTargetDef(BaseClass):
    instance_id: str = pydantic.Field(..., description='Instance ID of the instance to register to.\n')
    port: typing.Union[int, float, None] = pydantic.Field(None, description='Override the default port for the target group.')
    _init_params: typing.ClassVar[list[str]] = ['instance_id', 'port']
    _method_names: typing.ClassVar[list[str]] = ['attach_to_application_target_group', 'attach_to_network_target_group']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_elasticloadbalancingv2_targets.InstanceIdTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[InstanceIdTargetDefConfig] = pydantic.Field(None)


class InstanceIdTargetDefConfig(pydantic.BaseModel):
    attach_to_application_target_group: typing.Optional[list[InstanceIdTargetDefAttachToApplicationTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")
    attach_to_network_target_group: typing.Optional[list[InstanceIdTargetDefAttachToNetworkTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")

class InstanceIdTargetDefAttachToApplicationTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.ApplicationTargetGroupDef] = pydantic.Field(..., description='-')
    ...

class InstanceIdTargetDefAttachToNetworkTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.NetworkTargetGroupDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_elasticloadbalancingv2_targets.InstanceTarget
class InstanceTargetDef(BaseClass):
    instance: models.aws_ec2.InstanceDef = pydantic.Field(..., description='Instance to register to.\n')
    port: typing.Union[int, float, None] = pydantic.Field(None, description='Override the default port for the target group.')
    _init_params: typing.ClassVar[list[str]] = ['instance', 'port']
    _method_names: typing.ClassVar[list[str]] = ['attach_to_application_target_group', 'attach_to_network_target_group']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_elasticloadbalancingv2_targets.InstanceTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[InstanceTargetDefConfig] = pydantic.Field(None)


class InstanceTargetDefConfig(pydantic.BaseModel):
    attach_to_application_target_group: typing.Optional[list[InstanceTargetDefAttachToApplicationTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")
    attach_to_network_target_group: typing.Optional[list[InstanceTargetDefAttachToNetworkTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")

class InstanceTargetDefAttachToApplicationTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.ApplicationTargetGroupDef] = pydantic.Field(..., description='-')
    ...

class InstanceTargetDefAttachToNetworkTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.NetworkTargetGroupDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_elasticloadbalancingv2_targets.IpTarget
class IpTargetDef(BaseClass):
    ip_address: str = pydantic.Field(..., description='The IP Address to load balance to.\n')
    port: typing.Union[int, float, None] = pydantic.Field(None, description="Override the group's default port.\n")
    availability_zone: typing.Optional[str] = pydantic.Field(None, description='Availability zone to send traffic from.')
    _init_params: typing.ClassVar[list[str]] = ['ip_address', 'port', 'availability_zone']
    _method_names: typing.ClassVar[list[str]] = ['attach_to_application_target_group', 'attach_to_network_target_group']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_elasticloadbalancingv2_targets.IpTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[IpTargetDefConfig] = pydantic.Field(None)


class IpTargetDefConfig(pydantic.BaseModel):
    attach_to_application_target_group: typing.Optional[list[IpTargetDefAttachToApplicationTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")
    attach_to_network_target_group: typing.Optional[list[IpTargetDefAttachToNetworkTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")

class IpTargetDefAttachToApplicationTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.ApplicationTargetGroupDef] = pydantic.Field(..., description='-')
    ...

class IpTargetDefAttachToNetworkTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.NetworkTargetGroupDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_elasticloadbalancingv2_targets.LambdaTarget
class LambdaTargetDef(BaseClass):
    fn: typing.Union[models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef] = pydantic.Field(..., description='-')
    _init_params: typing.ClassVar[list[str]] = ['fn']
    _method_names: typing.ClassVar[list[str]] = ['attach_to_application_target_group', 'attach_to_network_target_group']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_elasticloadbalancingv2_targets.LambdaTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[LambdaTargetDefConfig] = pydantic.Field(None)


class LambdaTargetDefConfig(pydantic.BaseModel):
    attach_to_application_target_group: typing.Optional[list[LambdaTargetDefAttachToApplicationTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")
    attach_to_network_target_group: typing.Optional[list[LambdaTargetDefAttachToNetworkTargetGroupParams]] = pydantic.Field(None, description="Register this instance target with a load balancer.\nDon't call this, it is called automatically when you add the target to a\nload balancer.")

class LambdaTargetDefAttachToApplicationTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.ApplicationTargetGroupDef] = pydantic.Field(..., description='-')
    ...

class LambdaTargetDefAttachToNetworkTargetGroupParams(pydantic.BaseModel):
    target_group: typing.Union[models.aws_elasticloadbalancingv2.NetworkTargetGroupDef] = pydantic.Field(..., description='-')
    ...


import models

class ModuleModel(pydantic.BaseModel):
    AlbArnTarget: typing.Optional[dict[str, AlbArnTargetDef]] = pydantic.Field(None)
    AlbTarget: typing.Optional[dict[str, AlbTargetDef]] = pydantic.Field(None)
    InstanceIdTarget: typing.Optional[dict[str, InstanceIdTargetDef]] = pydantic.Field(None)
    InstanceTarget: typing.Optional[dict[str, InstanceTargetDef]] = pydantic.Field(None)
    IpTarget: typing.Optional[dict[str, IpTargetDef]] = pydantic.Field(None)
    LambdaTarget: typing.Optional[dict[str, LambdaTargetDef]] = pydantic.Field(None)
    ...
