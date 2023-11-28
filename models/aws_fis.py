from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.CloudWatchLogsConfigurationProperty
class CfnExperimentTemplate_CloudWatchLogsConfigurationPropertyDef(BaseStruct):
    log_group_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the destination Amazon CloudWatch Logs log group.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    cloud_watch_logs_configuration_property = fis.CfnExperimentTemplate.CloudWatchLogsConfigurationProperty(\n        log_group_arn="logGroupArn"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['log_group_arn']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.CloudWatchLogsConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateActionProperty
class CfnExperimentTemplate_ExperimentTemplateActionPropertyDef(BaseStruct):
    action_id: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The ID of the action.\n')
    description: typing.Optional[str] = pydantic.Field(None, description='A description for the action.\n')
    parameters: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='The parameters for the action, if applicable.\n')
    start_after: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The name of the action that must be completed before the current action starts.\n')
    targets: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='One or more targets for the action.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    experiment_template_action_property = fis.CfnExperimentTemplate.ExperimentTemplateActionProperty(\n        action_id="actionId",\n\n        # the properties below are optional\n        description="description",\n        parameters={\n            "parameters_key": "parameters"\n        },\n        start_after=["startAfter"],\n        targets={\n            "targets_key": "targets"\n        }\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['action_id', 'description', 'parameters', 'start_after', 'targets']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateActionProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateLogConfigurationProperty
class CfnExperimentTemplate_ExperimentTemplateLogConfigurationPropertyDef(BaseStruct):
    log_schema_version: typing.Union[_REQUIRED_INIT_PARAM, int, float] = pydantic.Field(REQUIRED_INIT_PARAM, description='The schema version.\n')
    cloud_watch_logs_configuration: typing.Any = pydantic.Field(None, description='The configuration for experiment logging to CloudWatch Logs .\n')
    s3_configuration: typing.Any = pydantic.Field(None, description='The configuration for experiment logging to Amazon S3 .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    # cloud_watch_logs_configuration: Any\n    # s3_configuration: Any\n\n    experiment_template_log_configuration_property = fis.CfnExperimentTemplate.ExperimentTemplateLogConfigurationProperty(\n        log_schema_version=123,\n\n        # the properties below are optional\n        cloud_watch_logs_configuration=cloud_watch_logs_configuration,\n        s3_configuration=s3_configuration\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['log_schema_version', 'cloud_watch_logs_configuration', 's3_configuration']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateLogConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateStopConditionProperty
class CfnExperimentTemplate_ExperimentTemplateStopConditionPropertyDef(BaseStruct):
    source: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The source for the stop condition.\n')
    value: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    experiment_template_stop_condition_property = fis.CfnExperimentTemplate.ExperimentTemplateStopConditionProperty(\n        source="source",\n\n        # the properties below are optional\n        value="value"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['source', 'value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateStopConditionProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty
class CfnExperimentTemplate_ExperimentTemplateTargetFilterPropertyDef(BaseStruct):
    path: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The attribute path for the filter.\n')
    values: typing.Union[typing.Sequence[str], _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The attribute values for the filter.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    experiment_template_target_filter_property = fis.CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty(\n        path="path",\n        values=["values"]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['path', 'values']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateTargetProperty
class CfnExperimentTemplate_ExperimentTemplateTargetPropertyDef(BaseStruct):
    resource_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The resource type.\n')
    selection_mode: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Scopes the identified resources to a specific count or percentage.\n')
    filters: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateTargetFilterPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The filters to apply to identify target resources using specific attributes.\n')
    parameters: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='The parameters for the resource type.\n')
    resource_arns: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The Amazon Resource Names (ARNs) of the targets.\n')
    resource_tags: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='The tags for the target resources.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    experiment_template_target_property = fis.CfnExperimentTemplate.ExperimentTemplateTargetProperty(\n        resource_type="resourceType",\n        selection_mode="selectionMode",\n\n        # the properties below are optional\n        filters=[fis.CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty(\n            path="path",\n            values=["values"]\n        )],\n        parameters={\n            "parameters_key": "parameters"\n        },\n        resource_arns=["resourceArns"],\n        resource_tags={\n            "resource_tags_key": "resourceTags"\n        }\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['resource_type', 'selection_mode', 'filters', 'parameters', 'resource_arns', 'resource_tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.ExperimentTemplateTargetProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate.S3ConfigurationProperty
class CfnExperimentTemplate_S3ConfigurationPropertyDef(BaseStruct):
    bucket_name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the destination bucket.\n')
    prefix: typing.Optional[str] = pydantic.Field(None, description='The bucket prefix.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-s3configuration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    s3_configuration_property = fis.CfnExperimentTemplate.S3ConfigurationProperty(\n        bucket_name="bucketName",\n\n        # the properties below are optional\n        prefix="prefix"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['bucket_name', 'prefix']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate.S3ConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplate
class CfnExperimentTemplateDef(BaseCfnResource):
    description: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The description for the experiment template.\n')
    role_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of an IAM role.\n')
    stop_conditions: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateStopConditionPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(REQUIRED_INIT_PARAM, description='The stop conditions for the experiment.\n')
    targets: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, typing.Mapping[str, typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateTargetPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(REQUIRED_INIT_PARAM, description='The targets for the experiment.\n')
    actions: typing.Union[models.UnsupportedResource, typing.Mapping[str, typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateActionPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The actions for the experiment.\n')
    log_configuration: typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateLogConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The configuration for experiment logging.\n')
    tags: typing.Optional[typing.Mapping[str, str]] = pydantic.Field(None, description='The tags for the experiment template.')
    _init_params: typing.ClassVar[list[str]] = ['description', 'role_arn', 'stop_conditions', 'targets', 'actions', 'log_configuration', 'tags']
    _method_names: typing.ClassVar[list[str]] = ['CloudWatchLogsConfigurationProperty', 'ExperimentTemplateActionProperty', 'ExperimentTemplateLogConfigurationProperty', 'ExperimentTemplateStopConditionProperty', 'ExperimentTemplateTargetFilterProperty', 'ExperimentTemplateTargetProperty', 'S3ConfigurationProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplate'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_fis.CfnExperimentTemplateDefConfig] = pydantic.Field(None)


class CfnExperimentTemplateDefConfig(pydantic.BaseModel):
    CloudWatchLogsConfigurationProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefCloudwatchlogsconfigurationpropertyParams]] = pydantic.Field(None, description='')
    ExperimentTemplateActionProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefExperimenttemplateactionpropertyParams]] = pydantic.Field(None, description='')
    ExperimentTemplateLogConfigurationProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefExperimenttemplatelogconfigurationpropertyParams]] = pydantic.Field(None, description='')
    ExperimentTemplateStopConditionProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefExperimenttemplatestopconditionpropertyParams]] = pydantic.Field(None, description='')
    ExperimentTemplateTargetFilterProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefExperimenttemplatetargetfilterpropertyParams]] = pydantic.Field(None, description='')
    ExperimentTemplateTargetProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefExperimenttemplatetargetpropertyParams]] = pydantic.Field(None, description='')
    S3ConfigurationProperty: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefS3ConfigurationpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[models.aws_fis.CfnExperimentTemplateDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnExperimentTemplateDefCloudwatchlogsconfigurationpropertyParams(pydantic.BaseModel):
    log_group_arn: str = pydantic.Field(..., description='')
    ...

class CfnExperimentTemplateDefExperimenttemplateactionpropertyParams(pydantic.BaseModel):
    action_id: str = pydantic.Field(..., description='')
    description: typing.Optional[str] = pydantic.Field(None, description='')
    parameters: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='')
    start_after: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    targets: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='')
    ...

class CfnExperimentTemplateDefExperimenttemplatelogconfigurationpropertyParams(pydantic.BaseModel):
    log_schema_version: typing.Union[int, float] = pydantic.Field(..., description='')
    cloud_watch_logs_configuration: typing.Any = pydantic.Field(None, description='')
    s3_configuration: typing.Any = pydantic.Field(None, description='')
    ...

class CfnExperimentTemplateDefExperimenttemplatestopconditionpropertyParams(pydantic.BaseModel):
    source: str = pydantic.Field(..., description='')
    value: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnExperimentTemplateDefExperimenttemplatetargetfilterpropertyParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='')
    values: typing.Sequence[str] = pydantic.Field(..., description='')
    ...

class CfnExperimentTemplateDefExperimenttemplatetargetpropertyParams(pydantic.BaseModel):
    resource_type: str = pydantic.Field(..., description='')
    selection_mode: str = pydantic.Field(..., description='')
    filters: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateTargetFilterPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='')
    parameters: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='')
    resource_arns: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    resource_tags: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='')
    ...

class CfnExperimentTemplateDefS3ConfigurationpropertyParams(pydantic.BaseModel):
    bucket_name: str = pydantic.Field(..., description='')
    prefix: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnExperimentTemplateDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnExperimentTemplateDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnExperimentTemplateDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnExperimentTemplateDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnExperimentTemplateDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnExperimentTemplateDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnExperimentTemplateDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnExperimentTemplateDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnExperimentTemplateDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnExperimentTemplateDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnExperimentTemplateDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnExperimentTemplateDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnExperimentTemplateDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnExperimentTemplateDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_fis.CfnExperimentTemplateProps
class CfnExperimentTemplatePropsDef(BaseCfnProperty):
    description: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The description for the experiment template.\n')
    role_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of an IAM role.\n')
    stop_conditions: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateStopConditionPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(REQUIRED_INIT_PARAM, description='The stop conditions for the experiment.\n')
    targets: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, typing.Mapping[str, typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateTargetPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(REQUIRED_INIT_PARAM, description='The targets for the experiment.\n')
    actions: typing.Union[models.UnsupportedResource, typing.Mapping[str, typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateActionPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The actions for the experiment.\n')
    log_configuration: typing.Union[models.UnsupportedResource, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateLogConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The configuration for experiment logging.\n')
    tags: typing.Optional[typing.Mapping[str, str]] = pydantic.Field(None, description='The tags for the experiment template.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_fis as fis\n\n    # cloud_watch_logs_configuration: Any\n    # s3_configuration: Any\n\n    cfn_experiment_template_props = fis.CfnExperimentTemplateProps(\n        description="description",\n        role_arn="roleArn",\n        stop_conditions=[fis.CfnExperimentTemplate.ExperimentTemplateStopConditionProperty(\n            source="source",\n\n            # the properties below are optional\n            value="value"\n        )],\n        targets={\n            "targets_key": fis.CfnExperimentTemplate.ExperimentTemplateTargetProperty(\n                resource_type="resourceType",\n                selection_mode="selectionMode",\n\n                # the properties below are optional\n                filters=[fis.CfnExperimentTemplate.ExperimentTemplateTargetFilterProperty(\n                    path="path",\n                    values=["values"]\n                )],\n                parameters={\n                    "parameters_key": "parameters"\n                },\n                resource_arns=["resourceArns"],\n                resource_tags={\n                    "resource_tags_key": "resourceTags"\n                }\n            )\n        },\n\n        # the properties below are optional\n        actions={\n            "actions_key": fis.CfnExperimentTemplate.ExperimentTemplateActionProperty(\n                action_id="actionId",\n\n                # the properties below are optional\n                description="description",\n                parameters={\n                    "parameters_key": "parameters"\n                },\n                start_after=["startAfter"],\n                targets={\n                    "targets_key": "targets"\n                }\n            )\n        },\n        log_configuration=fis.CfnExperimentTemplate.ExperimentTemplateLogConfigurationProperty(\n            log_schema_version=123,\n\n            # the properties below are optional\n            cloud_watch_logs_configuration=cloud_watch_logs_configuration,\n            s3_configuration=s3_configuration\n        ),\n        tags={\n            "tags_key": "tags"\n        }\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['description', 'role_arn', 'stop_conditions', 'targets', 'actions', 'log_configuration', 'tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_fis.CfnExperimentTemplateProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




class ModuleModel(pydantic.BaseModel):
    CfnExperimentTemplate_CloudWatchLogsConfigurationProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_CloudWatchLogsConfigurationPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate_ExperimentTemplateActionProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateActionPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate_ExperimentTemplateLogConfigurationProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateLogConfigurationPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate_ExperimentTemplateStopConditionProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateStopConditionPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate_ExperimentTemplateTargetFilterProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateTargetFilterPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate_ExperimentTemplateTargetProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_ExperimentTemplateTargetPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate_S3ConfigurationProperty: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplate_S3ConfigurationPropertyDef]] = pydantic.Field(None)
    CfnExperimentTemplate: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplateDef]] = pydantic.Field(None)
    CfnExperimentTemplateProps: typing.Optional[dict[str, models.aws_fis.CfnExperimentTemplatePropsDef]] = pydantic.Field(None)
    ...

import models
