from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.lambda_layer_awscli.AwsCliLayer
class AwsCliLayerDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = ['add_permission', 'apply_removal_policy']
    _classmethod_names: typing.ClassVar[list[str]] = ['from_layer_version_arn', 'from_layer_version_attributes']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.lambda_layer_awscli.AwsCliLayer'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = ['from_layer_version_arn', 'from_layer_version_attributes']
    ...


    from_layer_version_arn: typing.Optional[AwsCliLayerDefFromLayerVersionArnParams] = pydantic.Field(None, description='Imports a layer version by ARN.\nAssumes it is compatible with all Lambda runtimes.')
    from_layer_version_attributes: typing.Optional[AwsCliLayerDefFromLayerVersionAttributesParams] = pydantic.Field(None, description='Imports a Layer that has been defined externally.')
    resource_config: typing.Optional[AwsCliLayerDefConfig] = pydantic.Field(None)


class AwsCliLayerDefConfig(pydantic.BaseModel):
    add_permission: typing.Optional[list[AwsCliLayerDefAddPermissionParams]] = pydantic.Field(None, description='Add permission for this layer version to specific entities.\nUsage within\nthe same account where the layer is defined is always allowed and does not\nrequire calling this method. Note that the principal that creates the\nLambda function using the layer (for example, a CloudFormation changeset\nexecution role) also needs to have the ``lambda:GetLayerVersion``\npermission on the layer version.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)

class AwsCliLayerDefAddPermissionParams(pydantic.BaseModel):
    id: str = pydantic.Field(..., description='-\n')
    account_id: str = pydantic.Field(..., description='The AWS Account id of the account that is authorized to use a Lambda Layer Version. The wild-card ``\'*\'`` can be used to grant access to "any" account (or any account in an organization when ``organizationId`` is specified).\n')
    organization_id: typing.Optional[str] = pydantic.Field(None, description="The ID of the AWS Organization to which the grant is restricted. Can only be specified if ``accountId`` is ``'*'``")
    ...

class AwsCliLayerDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: aws_cdk.RemovalPolicy = pydantic.Field(..., description='-')
    ...

class AwsCliLayerDefFromLayerVersionArnParams(pydantic.BaseModel):
    scope: models.constructs.ConstructDef = pydantic.Field(..., description='-\n')
    id: str = pydantic.Field(..., description='-\n')
    layer_version_arn: str = pydantic.Field(..., description='-')
    ...

class AwsCliLayerDefFromLayerVersionAttributesParams(pydantic.BaseModel):
    scope: models.constructs.ConstructDef = pydantic.Field(..., description='the parent Construct that will use the imported layer.\n')
    id: str = pydantic.Field(..., description='the id of the imported layer in the construct tree.\n')
    layer_version_arn: str = pydantic.Field(..., description='The ARN of the LayerVersion.\n')
    compatible_runtimes: typing.Optional[typing.Sequence[models.aws_lambda.RuntimeDef]] = pydantic.Field(None, description='The list of compatible runtimes with this Layer.')
    ...


import models

class ModuleModel(pydantic.BaseModel):
    AwsCliLayer: typing.Optional[dict[str, AwsCliLayerDef]] = pydantic.Field(None)
    ...
