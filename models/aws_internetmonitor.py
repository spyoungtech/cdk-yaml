from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty
class CfnMonitor_InternetMeasurementsLogDeliveryPropertyDef(BaseStruct):
    s3_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_internetmonitor.CfnMonitor_S3ConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The configuration information for publishing Amazon CloudWatch Internet Monitor internet measurements to Amazon S3. The configuration includes the bucket name and (optionally) bucket prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is ``ENABLED`` if you choose to deliver internet measurements to an S3 bucket, and ``DISABLED`` otherwise.')
    _init_params: typing.ClassVar[list[str]] = ['s3_config']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_internetmonitor.CfnMonitor.S3ConfigProperty
class CfnMonitor_S3ConfigPropertyDef(BaseStruct):
    bucket_name: typing.Optional[str] = pydantic.Field(None, description='The Amazon S3 bucket name for internet measurements publishing.\n')
    bucket_prefix: typing.Optional[str] = pydantic.Field(None, description='An optional Amazon S3 bucket prefix for internet measurements publishing.\n')
    log_delivery_status: typing.Optional[str] = pydantic.Field(None, description='The status of publishing Internet Monitor internet measurements to an Amazon S3 bucket. The delivery status is ``ENABLED`` if you choose to deliver internet measurements to an S3 bucket, and ``DISABLED`` otherwise.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_internetmonitor as internetmonitor\n\n    s3_config_property = internetmonitor.CfnMonitor.S3ConfigProperty(\n        bucket_name="bucketName",\n        bucket_prefix="bucketPrefix",\n        log_delivery_status="logDeliveryStatus"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['bucket_name', 'bucket_prefix', 'log_delivery_status']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_internetmonitor.CfnMonitor.S3ConfigProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_internetmonitor.CfnMonitor
class CfnMonitorDef(BaseCfnResource):
    monitor_name: str = pydantic.Field(..., description='The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).\n')
    internet_measurements_log_delivery: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_internetmonitor.CfnMonitor_InternetMeasurementsLogDeliveryPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket. Measurements are also published to Amazon CloudWatch Logs for the first 500 (by traffic volume) city-networks (client locations and ASNs, typically internet service providers or ISPs).\n')
    max_city_networks_to_monitor: typing.Union[int, float, None] = pydantic.Field(None, description='The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the network, such as an internet service provider, that clients access the resources through. For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .\n')
    resources: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).\n')
    resources_to_add: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description="The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs). You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add WorkSpaces directories. You can't add all three types of resources. .. epigraph:: If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.\n")
    resources_to_remove: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).\n')
    status: typing.Optional[str] = pydantic.Field(None, description='The status of a monitor. The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='The tags for a monitor, listed as a set of *key:value* pairs.\n')
    traffic_percentage_to_monitor: typing.Union[int, float, None] = pydantic.Field(None, description='The percentage of the internet-facing traffic for your application that you want to monitor. You can also, optionally, set a limit for the number of city-networks (client locations and ASNs, typically internet service providers) that Internet Monitor will monitor traffic for. The city-networks maximum limit caps the number of city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.')
    _init_params: typing.ClassVar[list[str]] = ['monitor_name', 'internet_measurements_log_delivery', 'max_city_networks_to_monitor', 'resources', 'resources_to_add', 'resources_to_remove', 'status', 'tags', 'traffic_percentage_to_monitor']
    _method_names: typing.ClassVar[list[str]] = ['InternetMeasurementsLogDeliveryProperty', 'S3ConfigProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_internetmonitor.CfnMonitor'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnMonitorDefConfig] = pydantic.Field(None)


class CfnMonitorDefConfig(pydantic.BaseModel):
    InternetMeasurementsLogDeliveryProperty: typing.Optional[list[CfnMonitorDefInternetmeasurementslogdeliverypropertyParams]] = pydantic.Field(None, description='')
    S3ConfigProperty: typing.Optional[list[CfnMonitorDefS3ConfigpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnMonitorDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnMonitorDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnMonitorDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnMonitorDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnMonitorDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnMonitorDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnMonitorDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnMonitorDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnMonitorDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnMonitorDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnMonitorDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnMonitorDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnMonitorDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnMonitorDefInternetmeasurementslogdeliverypropertyParams(pydantic.BaseModel):
    s3_config: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_internetmonitor.CfnMonitor_S3ConfigPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='')
    ...

class CfnMonitorDefS3ConfigpropertyParams(pydantic.BaseModel):
    bucket_name: typing.Optional[str] = pydantic.Field(None, description='')
    bucket_prefix: typing.Optional[str] = pydantic.Field(None, description='')
    log_delivery_status: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnMonitorDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnMonitorDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnMonitorDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnMonitorDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnMonitorDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnMonitorDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnMonitorDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnMonitorDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnMonitorDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnMonitorDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnMonitorDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='- tree inspector to collect and process attributes.')
    ...

class CfnMonitorDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnMonitorDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnMonitorDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_internetmonitor.CfnMonitorProps
class CfnMonitorPropsDef(BaseCfnProperty):
    monitor_name: str = pydantic.Field(..., description='The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).\n')
    internet_measurements_log_delivery: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_internetmonitor.CfnMonitor_InternetMeasurementsLogDeliveryPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket. Measurements are also published to Amazon CloudWatch Logs for the first 500 (by traffic volume) city-networks (client locations and ASNs, typically internet service providers or ISPs).\n')
    max_city_networks_to_monitor: typing.Union[int, float, None] = pydantic.Field(None, description='The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the network, such as an internet service provider, that clients access the resources through. For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .\n')
    resources: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).\n')
    resources_to_add: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description="The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs). You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add WorkSpaces directories. You can't add all three types of resources. .. epigraph:: If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.\n")
    resources_to_remove: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).\n')
    status: typing.Optional[str] = pydantic.Field(None, description='The status of a monitor. The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='The tags for a monitor, listed as a set of *key:value* pairs.\n')
    traffic_percentage_to_monitor: typing.Union[int, float, None] = pydantic.Field(None, description='The percentage of the internet-facing traffic for your application that you want to monitor. You can also, optionally, set a limit for the number of city-networks (client locations and ASNs, typically internet service providers) that Internet Monitor will monitor traffic for. The city-networks maximum limit caps the number of city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_internetmonitor as internetmonitor\n\n    cfn_monitor_props = internetmonitor.CfnMonitorProps(\n        monitor_name="monitorName",\n\n        # the properties below are optional\n        internet_measurements_log_delivery=internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty(\n            s3_config=internetmonitor.CfnMonitor.S3ConfigProperty(\n                bucket_name="bucketName",\n                bucket_prefix="bucketPrefix",\n                log_delivery_status="logDeliveryStatus"\n            )\n        ),\n        max_city_networks_to_monitor=123,\n        resources=["resources"],\n        resources_to_add=["resourcesToAdd"],\n        resources_to_remove=["resourcesToRemove"],\n        status="status",\n        tags=[CfnTag(\n            key="key",\n            value="value"\n        )],\n        traffic_percentage_to_monitor=123\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['monitor_name', 'internet_measurements_log_delivery', 'max_city_networks_to_monitor', 'resources', 'resources_to_add', 'resources_to_remove', 'status', 'tags', 'traffic_percentage_to_monitor']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_internetmonitor.CfnMonitorProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnMonitor_InternetMeasurementsLogDeliveryProperty: typing.Optional[dict[str, CfnMonitor_InternetMeasurementsLogDeliveryPropertyDef]] = pydantic.Field(None)
    CfnMonitor_S3ConfigProperty: typing.Optional[dict[str, CfnMonitor_S3ConfigPropertyDef]] = pydantic.Field(None)
    CfnMonitor: typing.Optional[dict[str, CfnMonitorDef]] = pydantic.Field(None)
    CfnMonitorProps: typing.Optional[dict[str, CfnMonitorPropsDef]] = pydantic.Field(None)
    ...