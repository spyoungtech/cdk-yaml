from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_simspaceweaver.CfnSimulation.S3LocationProperty
class CfnSimulation_S3LocationPropertyDef(BaseStruct):
    bucket_name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of an Amazon S3 bucket. For more information about buckets, see `Creating, configuring, and working with Amazon S3 buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html>`_ in the *Amazon Simple Storage Service User Guide* .\n')
    object_key: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The key name of an object in Amazon S3 . For more information about Amazon S3 objects and object keys, see `Uploading, downloading, and working with objects in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html>`_ in the *Amazon Simple Storage Service User Guide* .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_simspaceweaver as simspaceweaver\n\n    s3_location_property = simspaceweaver.CfnSimulation.S3LocationProperty(\n        bucket_name="bucketName",\n        object_key="objectKey"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['bucket_name', 'object_key']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_simspaceweaver.CfnSimulation.S3LocationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_simspaceweaver.CfnSimulation
class CfnSimulationDef(BaseCfnResource):
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the simulation.\n')
    role_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role that the simulation assumes to perform actions. For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* . For more information about IAM roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *AWS Identity and Access Management User Guide* .\n')
    maximum_duration: typing.Optional[str] = pydantic.Field(None, description='The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is ``14D`` , or its equivalent in the other units. The default value is ``14D`` . A value equivalent to ``0`` makes the simulation immediately transition to ``STOPPING`` as soon as it reaches ``STARTED`` .\n')
    schema_s3_location: typing.Union[models.UnsupportedResource, models.aws_simspaceweaver.CfnSimulation_S3LocationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="The location of the simulation schema in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SchemaS3Location`` to start your simulation from a schema. If you provide a ``SchemaS3Location`` then you can't provide a ``SnapshotS3Location`` .\n")
    snapshot_s3_location: typing.Union[models.UnsupportedResource, models.aws_simspaceweaver.CfnSimulation_S3LocationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="The location of the snapshot in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SnapshotS3Location`` to start your simulation from a snapshot. If you provide a ``SnapshotS3Location`` then you can't provide a ``SchemaS3Location`` .")
    _init_params: typing.ClassVar[list[str]] = ['name', 'role_arn', 'maximum_duration', 'schema_s3_location', 'snapshot_s3_location']
    _method_names: typing.ClassVar[list[str]] = ['S3LocationProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_simspaceweaver.CfnSimulation'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnSimulationDefConfig] = pydantic.Field(None)


class CfnSimulationDefConfig(pydantic.BaseModel):
    S3LocationProperty: typing.Optional[list[CfnSimulationDefS3LocationpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnSimulationDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnSimulationDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnSimulationDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnSimulationDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnSimulationDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnSimulationDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnSimulationDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnSimulationDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnSimulationDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnSimulationDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnSimulationDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnSimulationDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnSimulationDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')

class CfnSimulationDefS3LocationpropertyParams(pydantic.BaseModel):
    bucket_name: str = pydantic.Field(..., description='')
    object_key: str = pydantic.Field(..., description='')
    ...

class CfnSimulationDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnSimulationDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnSimulationDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnSimulationDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnSimulationDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnSimulationDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnSimulationDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnSimulationDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnSimulationDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnSimulationDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnSimulationDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnSimulationDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnSimulationDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnSimulationDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_simspaceweaver.CfnSimulationProps
class CfnSimulationPropsDef(BaseCfnProperty):
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the simulation.\n')
    role_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role that the simulation assumes to perform actions. For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* . For more information about IAM roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *AWS Identity and Access Management User Guide* .\n')
    maximum_duration: typing.Optional[str] = pydantic.Field(None, description='The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is ``14D`` , or its equivalent in the other units. The default value is ``14D`` . A value equivalent to ``0`` makes the simulation immediately transition to ``STOPPING`` as soon as it reaches ``STARTED`` .\n')
    schema_s3_location: typing.Union[models.UnsupportedResource, models.aws_simspaceweaver.CfnSimulation_S3LocationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="The location of the simulation schema in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SchemaS3Location`` to start your simulation from a schema. If you provide a ``SchemaS3Location`` then you can't provide a ``SnapshotS3Location`` .\n")
    snapshot_s3_location: typing.Union[models.UnsupportedResource, models.aws_simspaceweaver.CfnSimulation_S3LocationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The location of the snapshot in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SnapshotS3Location`` to start your simulation from a snapshot. If you provide a ``SnapshotS3Location`` then you can\'t provide a ``SchemaS3Location`` .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_simspaceweaver as simspaceweaver\n\n    cfn_simulation_props = simspaceweaver.CfnSimulationProps(\n        name="name",\n        role_arn="roleArn",\n\n        # the properties below are optional\n        maximum_duration="maximumDuration",\n        schema_s3_location=simspaceweaver.CfnSimulation.S3LocationProperty(\n            bucket_name="bucketName",\n            object_key="objectKey"\n        ),\n        snapshot_s3_location=simspaceweaver.CfnSimulation.S3LocationProperty(\n            bucket_name="bucketName",\n            object_key="objectKey"\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['name', 'role_arn', 'maximum_duration', 'schema_s3_location', 'snapshot_s3_location']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_simspaceweaver.CfnSimulationProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnSimulation_S3LocationProperty: typing.Optional[dict[str, CfnSimulation_S3LocationPropertyDef]] = pydantic.Field(None)
    CfnSimulation: typing.Optional[dict[str, CfnSimulationDef]] = pydantic.Field(None)
    CfnSimulationProps: typing.Optional[dict[str, CfnSimulationPropsDef]] = pydantic.Field(None)
    ...
