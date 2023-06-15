from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_cur.CfnReportDefinition
class CfnReportDefinitionDef(BaseCfnResource):
    compression: str = pydantic.Field(..., description='The compression format that Amazon Web Services uses for the report.\n')
    format: str = pydantic.Field(..., description='The format that Amazon Web Services saves the report in.\n')
    refresh_closed_reports: typing.Union[bool, typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef]] = pydantic.Field(..., description='Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months. These charges can include refunds, credits, or support fees.\n')
    report_name: str = pydantic.Field(..., description="The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.\n")
    report_versioning: str = pydantic.Field(..., description='Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.\n')
    s3_bucket: str = pydantic.Field(..., description='The S3 bucket where Amazon Web Services delivers the report.\n')
    s3_prefix: str = pydantic.Field(..., description="The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report. Your prefix can't include spaces.\n")
    s3_region: str = pydantic.Field(..., description='The Region of the S3 bucket that Amazon Web Services delivers the report into.\n')
    time_unit: str = pydantic.Field(..., description='The granularity of the line items in the report.\n')
    additional_artifacts: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of manifests that you want AWS to create for this report.\n')
    additional_schema_elements: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.\n')
    billing_view_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Name (ARN) of the billing view. You can get this value by using the billing view service public APIs.')
    _init_params: typing.ClassVar[list[str]] = ['compression', 'format', 'refresh_closed_reports', 'report_name', 'report_versioning', 's3_bucket', 's3_prefix', 's3_region', 'time_unit', 'additional_artifacts', 'additional_schema_elements', 'billing_view_arn']
    _method_names: typing.ClassVar[list[str]] = ['add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cur.CfnReportDefinition'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnReportDefinitionDefConfig] = pydantic.Field(None)


class CfnReportDefinitionDefConfig(pydantic.BaseModel):
    add_deletion_override: typing.Optional[list[CfnReportDefinitionDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnReportDefinitionDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnReportDefinitionDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnReportDefinitionDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnReportDefinitionDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnReportDefinitionDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnReportDefinitionDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnReportDefinitionDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnReportDefinitionDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnReportDefinitionDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnReportDefinitionDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnReportDefinitionDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnReportDefinitionDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')

class CfnReportDefinitionDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnReportDefinitionDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnReportDefinitionDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnReportDefinitionDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnReportDefinitionDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnReportDefinitionDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnReportDefinitionDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnReportDefinitionDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnReportDefinitionDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnReportDefinitionDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnReportDefinitionDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='- tree inspector to collect and process attributes.')
    ...

class CfnReportDefinitionDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnReportDefinitionDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnReportDefinitionDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_cur.CfnReportDefinitionProps
class CfnReportDefinitionPropsDef(BaseCfnProperty):
    compression: str = pydantic.Field(..., description='The compression format that Amazon Web Services uses for the report.\n')
    format: str = pydantic.Field(..., description='The format that Amazon Web Services saves the report in.\n')
    refresh_closed_reports: typing.Union[bool, typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef]] = pydantic.Field(..., description='Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months. These charges can include refunds, credits, or support fees.\n')
    report_name: str = pydantic.Field(..., description="The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.\n")
    report_versioning: str = pydantic.Field(..., description='Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.\n')
    s3_bucket: str = pydantic.Field(..., description='The S3 bucket where Amazon Web Services delivers the report.\n')
    s3_prefix: str = pydantic.Field(..., description="The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report. Your prefix can't include spaces.\n")
    s3_region: str = pydantic.Field(..., description='The Region of the S3 bucket that Amazon Web Services delivers the report into.\n')
    time_unit: str = pydantic.Field(..., description='The granularity of the line items in the report.\n')
    additional_artifacts: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of manifests that you want AWS to create for this report.\n')
    additional_schema_elements: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.\n')
    billing_view_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Name (ARN) of the billing view. You can get this value by using the billing view service public APIs.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_cur as cur\n\n    cfn_report_definition_props = cur.CfnReportDefinitionProps(\n        compression="compression",\n        format="format",\n        refresh_closed_reports=False,\n        report_name="reportName",\n        report_versioning="reportVersioning",\n        s3_bucket="s3Bucket",\n        s3_prefix="s3Prefix",\n        s3_region="s3Region",\n        time_unit="timeUnit",\n\n        # the properties below are optional\n        additional_artifacts=["additionalArtifacts"],\n        additional_schema_elements=["additionalSchemaElements"],\n        billing_view_arn="billingViewArn"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['compression', 'format', 'refresh_closed_reports', 'report_name', 'report_versioning', 's3_bucket', 's3_prefix', 's3_region', 'time_unit', 'additional_artifacts', 'additional_schema_elements', 'billing_view_arn']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_cur.CfnReportDefinitionProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnReportDefinition: typing.Optional[dict[str, CfnReportDefinitionDef]] = pydantic.Field(None)
    CfnReportDefinitionProps: typing.Optional[dict[str, CfnReportDefinitionPropsDef]] = pydantic.Field(None)
    ...