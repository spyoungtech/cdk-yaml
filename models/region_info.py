from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.region_info.Default
class DefaultDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = ['service_principal']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.region_info.Default'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.region_info.DefaultDefConfig] = pydantic.Field(None)


class DefaultDefConfig(pydantic.BaseModel):
    service_principal: typing.Optional[list[models.region_info.DefaultDefServicePrincipalParams]] = pydantic.Field(None, description='Computes a "standard" AWS Service principal for a given service, region and suffix.\nThis is useful for example when\nyou need to compute a service principal name, but you do not have a synthesize-time region literal available (so\nall you have is ``{ "Ref": "AWS::Region" }``). This way you get the same defaulting behavior that is normally used\nfor built-in data.')

class DefaultDefServicePrincipalParams(pydantic.BaseModel):
    service_fqn: str = pydantic.Field(..., description='the name of the service (s3, s3.amazonaws.com, ...).\n')
    region: str = pydantic.Field(..., description='the region in which the service principal is needed.\n')
    url_suffix: str = pydantic.Field(..., description='deprecated and ignored.')
    ...


#  autogenerated from aws_cdk.region_info.Fact
class FactDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = ['defined_facts', 'find', 'register', 'require_fact', 'unregister']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.region_info.Fact'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.region_info.FactDefConfig] = pydantic.Field(None)


class FactDefConfig(pydantic.BaseModel):
    defined_facts: typing.Optional[bool] = pydantic.Field(None, description='Return all pairs of (region, factName) that are defined.')
    find: typing.Optional[list[models.region_info.FactDefFindParams]] = pydantic.Field(None, description='Retrieves a fact from this Fact database.')
    register_: typing.Optional[list[models.region_info.FactDefRegisterParams]] = pydantic.Field(None, description='Registers a new fact in this Fact database.', alias='register')
    require_fact: typing.Optional[list[models.region_info.FactDefRequireFactParams]] = pydantic.Field(None, description='Retrieve a fact from the Fact database.\n(retrieval will fail if the specified region or\nfact name does not exist.)')
    unregister: typing.Optional[list[models.region_info.FactDefUnregisterParams]] = pydantic.Field(None, description='Removes a fact from the database.')

class FactDefFindParams(pydantic.BaseModel):
    region: str = pydantic.Field(..., description='the name of the region (e.g: ``us-east-1``).\n')
    name: str = pydantic.Field(..., description='the name of the fact being looked up (see the ``FactName`` class for details).\n')
    ...

class FactDefRegisterParams(pydantic.BaseModel):
    fact: models.UnsupportedResource = pydantic.Field(..., description='the new fact to be registered.\n')
    allow_replacing: typing.Optional[bool] = pydantic.Field(None, description='whether new facts can replace existing facts or not.')
    ...

class FactDefRequireFactParams(pydantic.BaseModel):
    region: str = pydantic.Field(..., description='the name of the region (e.g: ``us-east-1``).\n')
    name: str = pydantic.Field(..., description='the name of the fact being looked up (see the ``FactName`` class for details).')
    ...

class FactDefUnregisterParams(pydantic.BaseModel):
    region: str = pydantic.Field(..., description='the region for which the fact is to be removed.\n')
    name: str = pydantic.Field(..., description='the name of the fact to remove.\n')
    value: typing.Optional[str] = pydantic.Field(None, description='the value that should be removed (removal will fail if the value is specified, but does not match the current stored value).')
    ...


#  autogenerated from aws_cdk.region_info.FactName
class FactNameDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = ['adot_lambda_layer', 'app_config_lambda_layer_version', 'cloudwatch_lambda_insights_version', 'params_and_secrets_lambda_layer', 'service_principal']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.region_info.FactName'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.region_info.FactNameDefConfig] = pydantic.Field(None)


class FactNameDefConfig(pydantic.BaseModel):
    adot_lambda_layer: typing.Optional[list[models.region_info.FactNameDefAdotLambdaLayerParams]] = pydantic.Field(None, description='The ARN of Amazon Distro for OpenTelemetry (ADOT) Lambda layer for a given lambda type, version and architecture.')
    app_config_lambda_layer_version: typing.Optional[list[models.region_info.FactNameDefAppConfigLambdaLayerVersionParams]] = pydantic.Field(None, description='The ARN of AppConfig Lambda Layer for a given version (e.g. 2.0.181).')
    cloudwatch_lambda_insights_version: typing.Optional[list[models.region_info.FactNameDefCloudwatchLambdaInsightsVersionParams]] = pydantic.Field(None, description='The ARN of CloudWatch Lambda Insights for a version (e.g. 1.0.98.0).')
    params_and_secrets_lambda_layer: typing.Optional[list[models.region_info.FactNameDefParamsAndSecretsLambdaLayerParams]] = pydantic.Field(None, description='The ARN of Parameters and Secrets Lambda layer for a given lambda architecture.')
    service_principal: typing.Optional[list[models.region_info.FactNameDefServicePrincipalParams]] = pydantic.Field(None, description='The name of the regional service principal for a given service.')

class FactNameDefAdotLambdaLayerParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the type of the ADOT lambda layer.\n')
    version: str = pydantic.Field(..., description='the layer version.\n')
    architecture: str = pydantic.Field(..., description="the Lambda Function architecture (e.g. 'x86_64' or 'arm64').")
    ...

class FactNameDefAppConfigLambdaLayerVersionParams(pydantic.BaseModel):
    version: str = pydantic.Field(..., description='The layer version.\n')
    arch: typing.Optional[str] = pydantic.Field(None, description='The architecture (optional), defaults to x86_64.')
    ...

class FactNameDefCloudwatchLambdaInsightsVersionParams(pydantic.BaseModel):
    version: str = pydantic.Field(..., description='-\n')
    arch: typing.Optional[str] = pydantic.Field(None, description='-')
    ...

class FactNameDefParamsAndSecretsLambdaLayerParams(pydantic.BaseModel):
    version: str = pydantic.Field(..., description='the layer version.\n')
    architecture: str = pydantic.Field(..., description="the Lambda Function architecture (e.g. 'x86_64' or 'arm64').")
    ...

class FactNameDefServicePrincipalParams(pydantic.BaseModel):
    service: str = pydantic.Field(..., description='the service name, either simple (e.g: ``s3``, ``codedeploy``) or qualified (e.g: ``s3.amazonaws.com``). The ``.amazonaws.com`` and ``.amazonaws.com.cn`` domains are stripped from service names, so they are canonicalized in that respect.')
    ...


#  autogenerated from aws_cdk.region_info.RegionInfo
class RegionInfoDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = ['adot_lambda_layer_arn', 'app_config_lambda_arn', 'cloudwatch_lambda_insights_arn', 'params_and_secrets_lambda_layer_arn', 'service_principal']
    _classmethod_names: typing.ClassVar[list[str]] = ['get', 'limited_region_map', 'region_map']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.region_info.RegionInfo'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.region_info.RegionInfoDefConfig] = pydantic.Field(None)


class RegionInfoDefConfig(pydantic.BaseModel):
    adot_lambda_layer_arn: typing.Optional[list[models.region_info.RegionInfoDefAdotLambdaLayerArnParams]] = pydantic.Field(None, description='The ARN of the ADOT Lambda layer, for the given layer type, version and architecture.')
    app_config_lambda_arn: typing.Optional[list[models.region_info.RegionInfoDefAppConfigLambdaArnParams]] = pydantic.Field(None, description='The ARN of the AppConfig Lambda Layer, for the given version.')
    cloudwatch_lambda_insights_arn: typing.Optional[list[models.region_info.RegionInfoDefCloudwatchLambdaInsightsArnParams]] = pydantic.Field(None, description='The ARN of the CloudWatch Lambda Insights extension, for the given version.')
    get: typing.Optional[list[models.region_info.RegionInfoDefGetParams]] = pydantic.Field(None, description='Obtain region info for a given region name.')
    limited_region_map: typing.Optional[list[models.region_info.RegionInfoDefLimitedRegionMapParams]] = pydantic.Field(None, description='Retrieves a collection of all fact values for all regions, limited to some partitions.')
    params_and_secrets_lambda_layer_arn: typing.Optional[list[models.region_info.RegionInfoDefParamsAndSecretsLambdaLayerArnParams]] = pydantic.Field(None, description='The ARN of the Parameters and Secrets Lambda layer for the given lambda architecture.')
    region_map: typing.Optional[list[models.region_info.RegionInfoDefRegionMapParams]] = pydantic.Field(None, description='Retrieves a collection of all fact values for all regions that fact is defined in.')
    service_principal: typing.Optional[list[models.region_info.RegionInfoDefServicePrincipalParams]] = pydantic.Field(None, description='The name of the service principal for a given service in this region.')

class RegionInfoDefAdotLambdaLayerArnParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the type of the ADOT lambda layer.\n')
    version: str = pydantic.Field(..., description='the layer version.\n')
    architecture: str = pydantic.Field(..., description="the Lambda Function architecture (e.g. 'x86_64' or 'arm64').")
    ...

class RegionInfoDefAppConfigLambdaArnParams(pydantic.BaseModel):
    layer_version: str = pydantic.Field(..., description='The layer version (e.g. 2.0.181).\n')
    architecture: typing.Optional[str] = pydantic.Field(None, description="The Lambda Function architecture (e.g. 'x86_64' or 'arm64'), defaults to x86_64.")
    ...

class RegionInfoDefCloudwatchLambdaInsightsArnParams(pydantic.BaseModel):
    insights_version: str = pydantic.Field(..., description='the version (e.g. 1.0.98.0).\n')
    architecture: typing.Optional[str] = pydantic.Field(None, description="the Lambda Function architecture (e.g. 'x86_64' or 'arm64').")
    ...

class RegionInfoDefGetParams(pydantic.BaseModel):
    name: str = pydantic.Field(..., description='the name of the region (e.g: us-east-1).')
    return_config: typing.Optional[list[models.region_info.RegionInfoDefConfig]] = pydantic.Field(None)
    ...

class RegionInfoDefLimitedRegionMapParams(pydantic.BaseModel):
    fact_name: str = pydantic.Field(..., description='the name of the fact to retrieve values for. For a list of common fact names, see the FactName class\n')
    partitions: typing.Sequence[str] = pydantic.Field(..., description="list of partitions to retrieve facts for. Defaults to ``['aws', 'aws-cn']``.\n")
    ...

class RegionInfoDefParamsAndSecretsLambdaLayerArnParams(pydantic.BaseModel):
    version: str = pydantic.Field(..., description='the layer version.\n')
    architecture: str = pydantic.Field(..., description="the Lambda Function architecture (e.g. 'x86_64' or 'arm64').")
    ...

class RegionInfoDefRegionMapParams(pydantic.BaseModel):
    fact_name: str = pydantic.Field(..., description='the name of the fact to retrieve values for. For a list of common fact names, see the FactName class\n')
    ...

class RegionInfoDefServicePrincipalParams(pydantic.BaseModel):
    service: str = pydantic.Field(..., description='the service name (e.g: s3.amazonaws.com).')
    ...


#  autogenerated from aws_cdk.region_info.IFact
#  skipping Interface

class ModuleModel(pydantic.BaseModel):
    Default: typing.Optional[dict[str, models.region_info.DefaultDef]] = pydantic.Field(None)
    Fact: typing.Optional[dict[str, models.region_info.FactDef]] = pydantic.Field(None)
    FactName: typing.Optional[dict[str, models.region_info.FactNameDef]] = pydantic.Field(None)
    RegionInfo: typing.Optional[dict[str, models.region_info.RegionInfoDef]] = pydantic.Field(None)
    ...

import models
