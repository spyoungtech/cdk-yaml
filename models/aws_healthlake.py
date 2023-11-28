from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastore.CreatedAtProperty
class CfnFHIRDatastore_CreatedAtPropertyDef(BaseStruct):
    nanos: typing.Union[_REQUIRED_INIT_PARAM, int, float] = pydantic.Field(REQUIRED_INIT_PARAM, description='Nanoseconds.\n')
    seconds: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Seconds since epoch.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_healthlake as healthlake\n\n    created_at_property = healthlake.CfnFHIRDatastore.CreatedAtProperty(\n        nanos=123,\n        seconds="seconds"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['nanos', 'seconds']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastore.CreatedAtProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty
class CfnFHIRDatastore_IdentityProviderConfigurationPropertyDef(BaseStruct):
    authorization_strategy: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The authorization strategy that you selected when you created the data store.\n')
    fine_grained_authorization_enabled: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='If you enabled fine-grained authorization when you created the data store.\n')
    idp_lambda_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Name (ARN) of the Lambda function that you want to use to decode the access token created by the authorization server.\n')
    metadata: typing.Optional[str] = pydantic.Field(None, description='The JSON metadata elements that you want to use in your identity provider configuration. Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see `Metadata <https://docs.aws.amazon.com/https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata>`_ in SMART\'s App Launch specification. ``authorization_endpoint`` : The URL to the OAuth2 authorization endpoint. ``grant_types_supported`` : An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are ``authorization_code`` and ``client_credentials`` . ``token_endpoint`` : The URL to the OAuth2 token endpoint. ``capabilities`` : An array of strings of the SMART capabilities that the authorization server supports. ``code_challenge_methods_supported`` : An array of strings of supported PKCE code challenge methods. You must include the ``S256`` method in the array of PKCE code challenge methods.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_healthlake as healthlake\n\n    identity_provider_configuration_property = healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(\n        authorization_strategy="authorizationStrategy",\n\n        # the properties below are optional\n        fine_grained_authorization_enabled=False,\n        idp_lambda_arn="idpLambdaArn",\n        metadata="metadata"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['authorization_strategy', 'fine_grained_authorization_enabled', 'idp_lambda_arn', 'metadata']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty
class CfnFHIRDatastore_KmsEncryptionConfigPropertyDef(BaseStruct):
    cmk_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .\n')
    kms_key_id: typing.Optional[str] = pydantic.Field(None, description='The KMS encryption key id/alias used to encrypt the data store contents at rest.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_healthlake as healthlake\n\n    kms_encryption_config_property = healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(\n        cmk_type="cmkType",\n\n        # the properties below are optional\n        kms_key_id="kmsKeyId"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['cmk_type', 'kms_key_id']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastore.PreloadDataConfigProperty
class CfnFHIRDatastore_PreloadDataConfigPropertyDef(BaseStruct):
    preload_data_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The type of preloaded data. Only Synthea preloaded data is supported.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_healthlake as healthlake\n\n    preload_data_config_property = healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(\n        preload_data_type="preloadDataType"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['preload_data_type']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastore.PreloadDataConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastore.SseConfigurationProperty
class CfnFHIRDatastore_SseConfigurationPropertyDef(BaseStruct):
    kms_encryption_config: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_KmsEncryptionConfigPropertyDef, dict[str, typing.Any]] = pydantic.Field(REQUIRED_INIT_PARAM, description='The server-side encryption key configuration for a customer provided encryption key (CMK).\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_healthlake as healthlake\n\n    sse_configuration_property = healthlake.CfnFHIRDatastore.SseConfigurationProperty(\n        kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(\n            cmk_type="cmkType",\n\n            # the properties below are optional\n            kms_key_id="kmsKeyId"\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['kms_encryption_config']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastore.SseConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastore
class CfnFHIRDatastoreDef(BaseCfnResource):
    datastore_type_version: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The FHIR version of the data store. The only supported version is R4.\n')
    datastore_name: typing.Optional[str] = pydantic.Field(None, description='The user generated name for the data store.\n')
    identity_provider_configuration: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_IdentityProviderConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The identity provider configuration that you gave when the data store was created.\n')
    preload_data_config: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_PreloadDataConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.\n')
    sse_configuration: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_SseConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .')
    _init_params: typing.ClassVar[list[str]] = ['datastore_type_version', 'datastore_name', 'identity_provider_configuration', 'preload_data_config', 'sse_configuration', 'tags']
    _method_names: typing.ClassVar[list[str]] = ['CreatedAtProperty', 'IdentityProviderConfigurationProperty', 'KmsEncryptionConfigProperty', 'PreloadDataConfigProperty', 'SseConfigurationProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastore'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_healthlake.CfnFHIRDatastoreDefConfig] = pydantic.Field(None)


class CfnFHIRDatastoreDefConfig(pydantic.BaseModel):
    CreatedAtProperty: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefCreatedatpropertyParams]] = pydantic.Field(None, description='')
    IdentityProviderConfigurationProperty: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefIdentityproviderconfigurationpropertyParams]] = pydantic.Field(None, description='')
    KmsEncryptionConfigProperty: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefKmsencryptionconfigpropertyParams]] = pydantic.Field(None, description='')
    PreloadDataConfigProperty: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefPreloaddataconfigpropertyParams]] = pydantic.Field(None, description='')
    SseConfigurationProperty: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefSseconfigurationpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[models.aws_healthlake.CfnFHIRDatastoreDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    attr_created_at_config: typing.Optional[models._interface_methods.CoreIResolvableDefConfig] = pydantic.Field(None)
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnFHIRDatastoreDefCreatedatpropertyParams(pydantic.BaseModel):
    nanos: typing.Union[int, float] = pydantic.Field(..., description='')
    seconds: str = pydantic.Field(..., description='')
    ...

class CfnFHIRDatastoreDefIdentityproviderconfigurationpropertyParams(pydantic.BaseModel):
    authorization_strategy: str = pydantic.Field(..., description='')
    fine_grained_authorization_enabled: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='')
    idp_lambda_arn: typing.Optional[str] = pydantic.Field(None, description='')
    metadata: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnFHIRDatastoreDefKmsencryptionconfigpropertyParams(pydantic.BaseModel):
    cmk_type: str = pydantic.Field(..., description='')
    kms_key_id: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnFHIRDatastoreDefPreloaddataconfigpropertyParams(pydantic.BaseModel):
    preload_data_type: str = pydantic.Field(..., description='')
    ...

class CfnFHIRDatastoreDefSseconfigurationpropertyParams(pydantic.BaseModel):
    kms_encryption_config: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_KmsEncryptionConfigPropertyDef, dict[str, typing.Any]] = pydantic.Field(..., description='')
    ...

class CfnFHIRDatastoreDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnFHIRDatastoreDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnFHIRDatastoreDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnFHIRDatastoreDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnFHIRDatastoreDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnFHIRDatastoreDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnFHIRDatastoreDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnFHIRDatastoreDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnFHIRDatastoreDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnFHIRDatastoreDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnFHIRDatastoreDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnFHIRDatastoreDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnFHIRDatastoreDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnFHIRDatastoreDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_healthlake.CfnFHIRDatastoreProps
class CfnFHIRDatastorePropsDef(BaseCfnProperty):
    datastore_type_version: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The FHIR version of the data store. The only supported version is R4.\n')
    datastore_name: typing.Optional[str] = pydantic.Field(None, description='The user generated name for the data store.\n')
    identity_provider_configuration: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_IdentityProviderConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The identity provider configuration that you gave when the data store was created.\n')
    preload_data_config: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_PreloadDataConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.\n')
    sse_configuration: typing.Union[models.UnsupportedResource, models.aws_healthlake.CfnFHIRDatastore_SseConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_healthlake as healthlake\n\n    cfn_fHIRDatastore_props = healthlake.CfnFHIRDatastoreProps(\n        datastore_type_version="datastoreTypeVersion",\n\n        # the properties below are optional\n        datastore_name="datastoreName",\n        identity_provider_configuration=healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(\n            authorization_strategy="authorizationStrategy",\n\n            # the properties below are optional\n            fine_grained_authorization_enabled=False,\n            idp_lambda_arn="idpLambdaArn",\n            metadata="metadata"\n        ),\n        preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(\n            preload_data_type="preloadDataType"\n        ),\n        sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(\n            kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(\n                cmk_type="cmkType",\n\n                # the properties below are optional\n                kms_key_id="kmsKeyId"\n            )\n        ),\n        tags=[CfnTag(\n            key="key",\n            value="value"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['datastore_type_version', 'datastore_name', 'identity_provider_configuration', 'preload_data_config', 'sse_configuration', 'tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_healthlake.CfnFHIRDatastoreProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




class ModuleModel(pydantic.BaseModel):
    CfnFHIRDatastore_CreatedAtProperty: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastore_CreatedAtPropertyDef]] = pydantic.Field(None)
    CfnFHIRDatastore_IdentityProviderConfigurationProperty: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastore_IdentityProviderConfigurationPropertyDef]] = pydantic.Field(None)
    CfnFHIRDatastore_KmsEncryptionConfigProperty: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastore_KmsEncryptionConfigPropertyDef]] = pydantic.Field(None)
    CfnFHIRDatastore_PreloadDataConfigProperty: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastore_PreloadDataConfigPropertyDef]] = pydantic.Field(None)
    CfnFHIRDatastore_SseConfigurationProperty: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastore_SseConfigurationPropertyDef]] = pydantic.Field(None)
    CfnFHIRDatastore: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastoreDef]] = pydantic.Field(None)
    CfnFHIRDatastoreProps: typing.Optional[dict[str, models.aws_healthlake.CfnFHIRDatastorePropsDef]] = pydantic.Field(None)
    ...

import models
