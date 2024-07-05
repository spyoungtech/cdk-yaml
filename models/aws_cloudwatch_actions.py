from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_cloudwatch_actions.ApplicationScalingAction
class ApplicationScalingActionDef(BaseClass):
    step_scaling_action: typing.Union[models.aws_applicationautoscaling.StepScalingActionDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['step_scaling_action']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.ApplicationScalingAction'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.ApplicationScalingActionDefConfig] = pydantic.Field(None)


class ApplicationScalingActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.ApplicationScalingActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use an ApplicationScaling StepScalingAction as an alarm action.')

class ApplicationScalingActionDefBindParams(pydantic.BaseModel):
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.AutoScalingAction
class AutoScalingActionDef(BaseClass):
    step_scaling_action: typing.Union[models.aws_autoscaling.StepScalingActionDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['step_scaling_action']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.AutoScalingAction'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.AutoScalingActionDefConfig] = pydantic.Field(None)


class AutoScalingActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.AutoScalingActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use an AutoScaling StepScalingAction as an alarm action.')

class AutoScalingActionDefBindParams(pydantic.BaseModel):
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.Ec2Action
class Ec2ActionDef(BaseClass):
    instance_action: typing.Union[aws_cdk.aws_cloudwatch_actions.Ec2InstanceAction, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['instance_action']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.Ec2Action'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.Ec2ActionDefConfig] = pydantic.Field(None)


class Ec2ActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.Ec2ActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use an EC2 action as an alarm action.')

class Ec2ActionDefBindParams(pydantic.BaseModel):
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.LambdaAction
class LambdaActionDef(BaseClass):
    lambda_function: typing.Union[_REQUIRED_INIT_PARAM, typing.Union[models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef], typing.Union[models.aws_lambda.VersionDef], typing.Union[models.aws_lambda.AliasDef]] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['lambda_function']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.LambdaAction'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.LambdaActionDefConfig] = pydantic.Field(None)


class LambdaActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.LambdaActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use a Lambda action as an alarm action.')

class LambdaActionDefBindParams(pydantic.BaseModel):
    scope: models.constructs.ConstructDef = pydantic.Field(..., description='-\n')
    alarm: typing.Union[models.aws_cloudwatch.AlarmBaseDef, models.aws_cloudwatch.AlarmDef, models.aws_cloudwatch.CompositeAlarmDef] = pydantic.Field(..., description='-\n\n:see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html\n')
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.SnsAction
class SnsActionDef(BaseClass):
    topic: typing.Union[_REQUIRED_INIT_PARAM, models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['topic']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.SnsAction'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.SnsActionDefConfig] = pydantic.Field(None)


class SnsActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.SnsActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use an SNS topic as an alarm action.')

class SnsActionDefBindParams(pydantic.BaseModel):
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.SsmAction
class SsmActionDef(BaseClass):
    severity: typing.Union[aws_cdk.aws_cloudwatch_actions.OpsItemSeverity, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    category: typing.Optional[aws_cdk.aws_cloudwatch_actions.OpsItemCategory] = pydantic.Field(None, description='-')
    _init_params: typing.ClassVar[list[str]] = ['severity', 'category']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.SsmAction'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.SsmActionDefConfig] = pydantic.Field(None)


class SsmActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.SsmActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use an SSM OpsItem action as an alarm action.')

class SsmActionDefBindParams(pydantic.BaseModel):
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.SsmIncidentAction
class SsmIncidentActionDef(BaseClass):
    response_plan_name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['response_plan_name']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cloudwatch_actions.SsmIncidentAction'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_cloudwatch_actions.SsmIncidentActionDefConfig] = pydantic.Field(None)


class SsmIncidentActionDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[models.aws_cloudwatch_actions.SsmIncidentActionDefBindParams]] = pydantic.Field(None, description='Returns an alarm action configuration to use an SSM Incident as an alarm action based on an Incident Manager Response Plan.')

class SsmIncidentActionDefBindParams(pydantic.BaseModel):
    ...


#  autogenerated from aws_cdk.aws_cloudwatch_actions.Ec2InstanceAction
# skipping emum

#  autogenerated from aws_cdk.aws_cloudwatch_actions.OpsItemCategory
# skipping emum

#  autogenerated from aws_cdk.aws_cloudwatch_actions.OpsItemSeverity
# skipping emum

class ModuleModel(pydantic.BaseModel):
    ApplicationScalingAction: typing.Optional[dict[str, models.aws_cloudwatch_actions.ApplicationScalingActionDef]] = pydantic.Field(None)
    AutoScalingAction: typing.Optional[dict[str, models.aws_cloudwatch_actions.AutoScalingActionDef]] = pydantic.Field(None)
    Ec2Action: typing.Optional[dict[str, models.aws_cloudwatch_actions.Ec2ActionDef]] = pydantic.Field(None)
    LambdaAction: typing.Optional[dict[str, models.aws_cloudwatch_actions.LambdaActionDef]] = pydantic.Field(None)
    SnsAction: typing.Optional[dict[str, models.aws_cloudwatch_actions.SnsActionDef]] = pydantic.Field(None)
    SsmAction: typing.Optional[dict[str, models.aws_cloudwatch_actions.SsmActionDef]] = pydantic.Field(None)
    SsmIncidentAction: typing.Optional[dict[str, models.aws_cloudwatch_actions.SsmIncidentActionDef]] = pydantic.Field(None)
    ...

import models
