from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel.DataSecurityConfigProperty
class CfnFlywheel_DataSecurityConfigPropertyDef(BaseStruct):
    data_lake_kms_key_id: typing.Optional[str] = pydantic.Field(None, description='ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data in the data lake.\n')
    model_kms_key_id: typing.Optional[str] = pydantic.Field(None, description='ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``\n')
    volume_kms_key_id: typing.Optional[str] = pydantic.Field(None, description='ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.\n')
    vpc_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_VpcConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    data_security_config_property = comprehend.CfnFlywheel.DataSecurityConfigProperty(\n        data_lake_kms_key_id="dataLakeKmsKeyId",\n        model_kms_key_id="modelKmsKeyId",\n        volume_kms_key_id="volumeKmsKeyId",\n        vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(\n            security_group_ids=["securityGroupIds"],\n            subnets=["subnets"]\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['data_lake_kms_key_id', 'model_kms_key_id', 'volume_kms_key_id', 'vpc_config']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel.DataSecurityConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel.DocumentClassificationConfigProperty
class CfnFlywheel_DocumentClassificationConfigPropertyDef(BaseStruct):
    mode: str = pydantic.Field(..., description='Classification mode indicates whether the documents are ``MULTI_CLASS`` or ``MULTI_LABEL`` .\n')
    labels: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='One or more labels to associate with the custom classifier.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    document_classification_config_property = comprehend.CfnFlywheel.DocumentClassificationConfigProperty(\n        mode="mode",\n\n        # the properties below are optional\n        labels=["labels"]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['mode', 'labels']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel.DocumentClassificationConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel.EntityRecognitionConfigProperty
class CfnFlywheel_EntityRecognitionConfigPropertyDef(BaseStruct):
    entity_types: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_EntityTypesListItemPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='Up to 25 entity types that the model is trained to recognize.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    entity_recognition_config_property = comprehend.CfnFlywheel.EntityRecognitionConfigProperty(\n        entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(\n            type="type"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['entity_types']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel.EntityRecognitionConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel.EntityTypesListItemProperty
class CfnFlywheel_EntityTypesListItemPropertyDef(BaseStruct):
    type: str = pydantic.Field(..., description='An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer. Entity types must not contain the following invalid characters: \\n (line break), \\n (escaped line break, \\r (carriage return), \\r (escaped carriage return), \\t (tab), \\t (escaped tab), space, and , (comma).\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    entity_types_list_item_property = comprehend.CfnFlywheel.EntityTypesListItemProperty(\n        type="type"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['type']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel.EntityTypesListItemProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel.TaskConfigProperty
class CfnFlywheel_TaskConfigPropertyDef(BaseStruct):
    language_code: str = pydantic.Field(..., description='Language code for the language that the model supports.\n')
    document_classification_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_DocumentClassificationConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Configuration required for a document classification model.\n')
    entity_recognition_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_EntityRecognitionConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Configuration required for an entity recognition model.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    task_config_property = comprehend.CfnFlywheel.TaskConfigProperty(\n        language_code="languageCode",\n\n        # the properties below are optional\n        document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(\n            mode="mode",\n\n            # the properties below are optional\n            labels=["labels"]\n        ),\n        entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(\n            entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(\n                type="type"\n            )]\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['language_code', 'document_classification_config', 'entity_recognition_config']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel.TaskConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel.VpcConfigProperty
class CfnFlywheel_VpcConfigPropertyDef(BaseStruct):
    security_group_ids: typing.Sequence[str] = pydantic.Field(..., description='The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .\n')
    subnets: typing.Sequence[str] = pydantic.Field(..., description='The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    vpc_config_property = comprehend.CfnFlywheel.VpcConfigProperty(\n        security_group_ids=["securityGroupIds"],\n        subnets=["subnets"]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['security_group_ids', 'subnets']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel.VpcConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheel
class CfnFlywheelDef(BaseCfnResource):
    data_access_role_arn: str = pydantic.Field(..., description='The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.\n')
    data_lake_s3_uri: str = pydantic.Field(..., description='Amazon S3 URI of the data lake location.\n')
    flywheel_name: str = pydantic.Field(..., description='Name for the flywheel.\n')
    active_model_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Number (ARN) of the active model version.\n')
    data_security_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_DataSecurityConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Data security configuration.\n')
    model_type: typing.Optional[str] = pydantic.Field(None, description="Model type of the flywheel's model.\n")
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.\n')
    task_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_TaskConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Configuration about the model associated with a flywheel.')
    _init_params: typing.ClassVar[list[str]] = ['data_access_role_arn', 'data_lake_s3_uri', 'flywheel_name', 'active_model_arn', 'data_security_config', 'model_type', 'tags', 'task_config']
    _method_names: typing.ClassVar[list[str]] = ['DataSecurityConfigProperty', 'DocumentClassificationConfigProperty', 'EntityRecognitionConfigProperty', 'EntityTypesListItemProperty', 'TaskConfigProperty', 'VpcConfigProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheel'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnFlywheelDefConfig] = pydantic.Field(None)


class CfnFlywheelDefConfig(pydantic.BaseModel):
    DataSecurityConfigProperty: typing.Optional[list[CfnFlywheelDefDatasecurityconfigpropertyParams]] = pydantic.Field(None, description='')
    DocumentClassificationConfigProperty: typing.Optional[list[CfnFlywheelDefDocumentclassificationconfigpropertyParams]] = pydantic.Field(None, description='')
    EntityRecognitionConfigProperty: typing.Optional[list[CfnFlywheelDefEntityrecognitionconfigpropertyParams]] = pydantic.Field(None, description='')
    EntityTypesListItemProperty: typing.Optional[list[CfnFlywheelDefEntitytypeslistitempropertyParams]] = pydantic.Field(None, description='')
    TaskConfigProperty: typing.Optional[list[CfnFlywheelDefTaskconfigpropertyParams]] = pydantic.Field(None, description='')
    VpcConfigProperty: typing.Optional[list[CfnFlywheelDefVpcconfigpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnFlywheelDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnFlywheelDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnFlywheelDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnFlywheelDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnFlywheelDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnFlywheelDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnFlywheelDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnFlywheelDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnFlywheelDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnFlywheelDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnFlywheelDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnFlywheelDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnFlywheelDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnFlywheelDefDatasecurityconfigpropertyParams(pydantic.BaseModel):
    data_lake_kms_key_id: typing.Optional[str] = pydantic.Field(None, description='')
    model_kms_key_id: typing.Optional[str] = pydantic.Field(None, description='')
    volume_kms_key_id: typing.Optional[str] = pydantic.Field(None, description='')
    vpc_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_VpcConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='')
    ...

class CfnFlywheelDefDocumentclassificationconfigpropertyParams(pydantic.BaseModel):
    mode: str = pydantic.Field(..., description='')
    labels: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    ...

class CfnFlywheelDefEntityrecognitionconfigpropertyParams(pydantic.BaseModel):
    entity_types: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_EntityTypesListItemPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='')
    ...

class CfnFlywheelDefEntitytypeslistitempropertyParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='')
    ...

class CfnFlywheelDefTaskconfigpropertyParams(pydantic.BaseModel):
    language_code: str = pydantic.Field(..., description='')
    document_classification_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_DocumentClassificationConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='')
    entity_recognition_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_EntityRecognitionConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='')
    ...

class CfnFlywheelDefVpcconfigpropertyParams(pydantic.BaseModel):
    security_group_ids: typing.Sequence[str] = pydantic.Field(..., description='')
    subnets: typing.Sequence[str] = pydantic.Field(..., description='')
    ...

class CfnFlywheelDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnFlywheelDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnFlywheelDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnFlywheelDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnFlywheelDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnFlywheelDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnFlywheelDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnFlywheelDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnFlywheelDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnFlywheelDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnFlywheelDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='- tree inspector to collect and process attributes.')
    ...

class CfnFlywheelDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnFlywheelDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnFlywheelDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_comprehend.CfnFlywheelProps
class CfnFlywheelPropsDef(BaseCfnProperty):
    data_access_role_arn: str = pydantic.Field(..., description='The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.\n')
    data_lake_s3_uri: str = pydantic.Field(..., description='Amazon S3 URI of the data lake location.\n')
    flywheel_name: str = pydantic.Field(..., description='Name for the flywheel.\n')
    active_model_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Number (ARN) of the active model version.\n')
    data_security_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_DataSecurityConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Data security configuration.\n')
    model_type: typing.Optional[str] = pydantic.Field(None, description="Model type of the flywheel's model.\n")
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.\n')
    task_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_comprehend.CfnFlywheel_TaskConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Configuration about the model associated with a flywheel.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_comprehend as comprehend\n\n    cfn_flywheel_props = comprehend.CfnFlywheelProps(\n        data_access_role_arn="dataAccessRoleArn",\n        data_lake_s3_uri="dataLakeS3Uri",\n        flywheel_name="flywheelName",\n\n        # the properties below are optional\n        active_model_arn="activeModelArn",\n        data_security_config=comprehend.CfnFlywheel.DataSecurityConfigProperty(\n            data_lake_kms_key_id="dataLakeKmsKeyId",\n            model_kms_key_id="modelKmsKeyId",\n            volume_kms_key_id="volumeKmsKeyId",\n            vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(\n                security_group_ids=["securityGroupIds"],\n                subnets=["subnets"]\n            )\n        ),\n        model_type="modelType",\n        tags=[CfnTag(\n            key="key",\n            value="value"\n        )],\n        task_config=comprehend.CfnFlywheel.TaskConfigProperty(\n            language_code="languageCode",\n\n            # the properties below are optional\n            document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(\n                mode="mode",\n\n                # the properties below are optional\n                labels=["labels"]\n            ),\n            entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(\n                entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(\n                    type="type"\n                )]\n            )\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['data_access_role_arn', 'data_lake_s3_uri', 'flywheel_name', 'active_model_arn', 'data_security_config', 'model_type', 'tags', 'task_config']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_comprehend.CfnFlywheelProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnFlywheel_DataSecurityConfigProperty: typing.Optional[dict[str, CfnFlywheel_DataSecurityConfigPropertyDef]] = pydantic.Field(None)
    CfnFlywheel_DocumentClassificationConfigProperty: typing.Optional[dict[str, CfnFlywheel_DocumentClassificationConfigPropertyDef]] = pydantic.Field(None)
    CfnFlywheel_EntityRecognitionConfigProperty: typing.Optional[dict[str, CfnFlywheel_EntityRecognitionConfigPropertyDef]] = pydantic.Field(None)
    CfnFlywheel_EntityTypesListItemProperty: typing.Optional[dict[str, CfnFlywheel_EntityTypesListItemPropertyDef]] = pydantic.Field(None)
    CfnFlywheel_TaskConfigProperty: typing.Optional[dict[str, CfnFlywheel_TaskConfigPropertyDef]] = pydantic.Field(None)
    CfnFlywheel_VpcConfigProperty: typing.Optional[dict[str, CfnFlywheel_VpcConfigPropertyDef]] = pydantic.Field(None)
    CfnFlywheel: typing.Optional[dict[str, CfnFlywheelDef]] = pydantic.Field(None)
    CfnFlywheelProps: typing.Optional[dict[str, CfnFlywheelPropsDef]] = pydantic.Field(None)
    ...