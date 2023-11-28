from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.alexa_ask.CfnSkill.AuthenticationConfigurationProperty
class CfnSkill_AuthenticationConfigurationPropertyDef(BaseStruct):
    client_id: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Client ID from Login with Amazon (LWA).\n')
    client_secret: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Client secret from Login with Amazon (LWA).\n')
    refresh_token: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Refresh token from Login with Amazon (LWA). This token is secret.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import alexa_ask\n\n    authentication_configuration_property = alexa_ask.CfnSkill.AuthenticationConfigurationProperty(\n        client_id="clientId",\n        client_secret="clientSecret",\n        refresh_token="refreshToken"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['client_id', 'client_secret', 'refresh_token']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.alexa_ask.CfnSkill.AuthenticationConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.alexa_ask.CfnSkill.OverridesProperty
class CfnSkill_OverridesPropertyDef(BaseStruct):
    manifest: typing.Any = pydantic.Field(None, description='Overrides to apply to the skill manifest inside of the skill package. The skill manifest contains metadata about the skill. For more information, see .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import alexa_ask\n\n    # manifest: Any\n\n    overrides_property = alexa_ask.CfnSkill.OverridesProperty(\n        manifest=manifest\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['manifest']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.alexa_ask.CfnSkill.OverridesProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.alexa_ask.CfnSkill.SkillPackageProperty
class CfnSkill_SkillPackagePropertyDef(BaseStruct):
    s3_bucket: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the Amazon S3 bucket where the .zip file that contains the skill package is stored.\n')
    s3_key: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The location and name of the skill package .zip file.\n')
    overrides: typing.Union[models.UnsupportedResource, models.alexa_ask.CfnSkill_OverridesPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Overrides to the skill package to apply when creating or updating the skill. Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.\n')
    s3_bucket_role: typing.Optional[str] = pydantic.Field(None, description='ARN of the IAM role that grants the Alexa service ( ``alexa-appkit.amazon.com`` ) permission to access the bucket and retrieve the skill package. This property is optional. If you do not provide it, the bucket must be publicly accessible or configured with a policy that allows this access. Otherwise, AWS CloudFormation cannot create the skill.\n')
    s3_object_version: typing.Optional[str] = pydantic.Field(None, description='If you have S3 versioning enabled, the version ID of the skill package.zip file.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import alexa_ask\n\n    # manifest: Any\n\n    skill_package_property = alexa_ask.CfnSkill.SkillPackageProperty(\n        s3_bucket="s3Bucket",\n        s3_key="s3Key",\n\n        # the properties below are optional\n        overrides=alexa_ask.CfnSkill.OverridesProperty(\n            manifest=manifest\n        ),\n        s3_bucket_role="s3BucketRole",\n        s3_object_version="s3ObjectVersion"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['s3_bucket', 's3_key', 'overrides', 's3_bucket_role', 's3_object_version']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.alexa_ask.CfnSkill.SkillPackageProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.alexa_ask.CfnSkill
class CfnSkillDef(BaseCfnResource):
    authentication_configuration: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, models.alexa_ask.CfnSkill_AuthenticationConfigurationPropertyDef, dict[str, typing.Any]] = pydantic.Field(REQUIRED_INIT_PARAM, description='Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the are supported. The client ID, client secret, and refresh token are required.\n')
    skill_package: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, models.alexa_ask.CfnSkill_SkillPackagePropertyDef, dict[str, typing.Any]] = pydantic.Field(REQUIRED_INIT_PARAM, description='Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the .\n')
    vendor_id: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in . The provided LWA credentials must be linked to the developer account associated with this vendor ID.')
    _init_params: typing.ClassVar[list[str]] = ['authentication_configuration', 'skill_package', 'vendor_id']
    _method_names: typing.ClassVar[list[str]] = ['AuthenticationConfigurationProperty', 'OverridesProperty', 'SkillPackageProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.alexa_ask.CfnSkill'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnSkillDefConfig] = pydantic.Field(None)


class CfnSkillDefConfig(pydantic.BaseModel):
    AuthenticationConfigurationProperty: typing.Optional[list[CfnSkillDefAuthenticationconfigurationpropertyParams]] = pydantic.Field(None, description='')
    OverridesProperty: typing.Optional[list[CfnSkillDefOverridespropertyParams]] = pydantic.Field(None, description='')
    SkillPackageProperty: typing.Optional[list[CfnSkillDefSkillpackagepropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnSkillDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnSkillDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnSkillDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnSkillDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnSkillDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnSkillDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnSkillDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnSkillDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnSkillDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnSkillDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnSkillDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnSkillDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnSkillDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')

class CfnSkillDefAuthenticationconfigurationpropertyParams(pydantic.BaseModel):
    client_id: str = pydantic.Field(..., description='')
    client_secret: str = pydantic.Field(..., description='')
    refresh_token: str = pydantic.Field(..., description='')
    ...

class CfnSkillDefOverridespropertyParams(pydantic.BaseModel):
    manifest: typing.Any = pydantic.Field(None, description='')
    ...

class CfnSkillDefSkillpackagepropertyParams(pydantic.BaseModel):
    s3_bucket: str = pydantic.Field(..., description='')
    s3_key: str = pydantic.Field(..., description='')
    overrides: typing.Union[models.UnsupportedResource, models.alexa_ask.CfnSkill_OverridesPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='')
    s3_bucket_role: typing.Optional[str] = pydantic.Field(None, description='')
    s3_object_version: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnSkillDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnSkillDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnSkillDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnSkillDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnSkillDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnSkillDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnSkillDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnSkillDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnSkillDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnSkillDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnSkillDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnSkillDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnSkillDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnSkillDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.alexa_ask.CfnSkillProps
class CfnSkillPropsDef(BaseCfnProperty):
    authentication_configuration: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, models.alexa_ask.CfnSkill_AuthenticationConfigurationPropertyDef, dict[str, typing.Any]] = pydantic.Field(REQUIRED_INIT_PARAM, description='Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the are supported. The client ID, client secret, and refresh token are required.\n')
    skill_package: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, models.alexa_ask.CfnSkill_SkillPackagePropertyDef, dict[str, typing.Any]] = pydantic.Field(REQUIRED_INIT_PARAM, description='Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the .\n')
    vendor_id: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in . The provided LWA credentials must be linked to the developer account associated with this vendor ID.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import alexa_ask\n\n    # manifest: Any\n\n    cfn_skill_props = alexa_ask.CfnSkillProps(\n        authentication_configuration=alexa_ask.CfnSkill.AuthenticationConfigurationProperty(\n            client_id="clientId",\n            client_secret="clientSecret",\n            refresh_token="refreshToken"\n        ),\n        skill_package=alexa_ask.CfnSkill.SkillPackageProperty(\n            s3_bucket="s3Bucket",\n            s3_key="s3Key",\n\n            # the properties below are optional\n            overrides=alexa_ask.CfnSkill.OverridesProperty(\n                manifest=manifest\n            ),\n            s3_bucket_role="s3BucketRole",\n            s3_object_version="s3ObjectVersion"\n        ),\n        vendor_id="vendorId"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['authentication_configuration', 'skill_package', 'vendor_id']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.alexa_ask.CfnSkillProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnSkill_AuthenticationConfigurationProperty: typing.Optional[dict[str, CfnSkill_AuthenticationConfigurationPropertyDef]] = pydantic.Field(None)
    CfnSkill_OverridesProperty: typing.Optional[dict[str, CfnSkill_OverridesPropertyDef]] = pydantic.Field(None)
    CfnSkill_SkillPackageProperty: typing.Optional[dict[str, CfnSkill_SkillPackagePropertyDef]] = pydantic.Field(None)
    CfnSkill: typing.Optional[dict[str, CfnSkillDef]] = pydantic.Field(None)
    CfnSkillProps: typing.Optional[dict[str, CfnSkillPropsDef]] = pydantic.Field(None)
    ...
