from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_rum.CfnAppMonitor.AppMonitorConfigurationProperty
class CfnAppMonitor_AppMonitorConfigurationPropertyDef(BaseStruct):
    allow_cookies: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='If you set this to ``true`` , the CloudWatch RUM web client sets two cookies, a session cookie and a user cookie. The cookies allow the CloudWatch RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.\n')
    enable_x_ray: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='If you set this to ``true`` , CloudWatch RUM sends client-side traces to X-Ray for each sampled session. You can then see traces and segments from these user sessions in the RUM dashboard and the CloudWatch ServiceLens console. For more information, see `What is AWS X-Ray ? <https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html>`_\n')
    excluded_pages: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description="A list of URLs in your website or application to exclude from RUM data collection. You can't include both ``ExcludedPages`` and ``IncludedPages`` in the same app monitor.\n")
    favorite_pages: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of pages in your application that are to be displayed with a "favorite" icon in the CloudWatch RUM console.\n')
    guest_role_arn: typing.Optional[str] = pydantic.Field(None, description='The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to CloudWatch RUM.\n')
    identity_pool_id: typing.Optional[str] = pydantic.Field(None, description='The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to CloudWatch RUM.\n')
    included_pages: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description="If this app monitor is to collect data from only certain pages in your application, this structure lists those pages. You can't include both ``ExcludedPages`` and ``IncludedPages`` in the same app monitor.\n")
    metric_destinations: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_MetricDestinationPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='An array of structures that each define a destination that this app monitor will send extended metrics to.\n')
    session_sample_rate: typing.Union[int, float, None] = pydantic.Field(None, description='Specifies the portion of user sessions to use for CloudWatch RUM data collection. Choosing a higher portion gives you more data but also incurs more costs. The range for this value is 0 to 1 inclusive. Setting this to 1 means that 100% of user sessions are sampled, and setting it to 0.1 means that 10% of user sessions are sampled. If you omit this parameter, the default of 0.1 is used, and 10% of sessions will be sampled.\n')
    telemetries: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='An array that lists the types of telemetry data that this app monitor is to collect. - ``errors`` indicates that RUM collects data about unhandled JavaScript errors raised by your application. - ``performance`` indicates that RUM collects performance data about how your application and its resources are loaded and rendered. This includes Core Web Vitals. - ``http`` indicates that RUM collects data about HTTP errors thrown by your application.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_rum as rum\n\n    app_monitor_configuration_property = rum.CfnAppMonitor.AppMonitorConfigurationProperty(\n        allow_cookies=False,\n        enable_xRay=False,\n        excluded_pages=["excludedPages"],\n        favorite_pages=["favoritePages"],\n        guest_role_arn="guestRoleArn",\n        identity_pool_id="identityPoolId",\n        included_pages=["includedPages"],\n        metric_destinations=[rum.CfnAppMonitor.MetricDestinationProperty(\n            destination="destination",\n\n            # the properties below are optional\n            destination_arn="destinationArn",\n            iam_role_arn="iamRoleArn",\n            metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(\n                name="name",\n\n                # the properties below are optional\n                dimension_keys={\n                    "dimension_keys_key": "dimensionKeys"\n                },\n                event_pattern="eventPattern",\n                namespace="namespace",\n                unit_label="unitLabel",\n                value_key="valueKey"\n            )]\n        )],\n        session_sample_rate=123,\n        telemetries=["telemetries"]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['allow_cookies', 'enable_x_ray', 'excluded_pages', 'favorite_pages', 'guest_role_arn', 'identity_pool_id', 'included_pages', 'metric_destinations', 'session_sample_rate', 'telemetries']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_rum.CfnAppMonitor.AppMonitorConfigurationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_rum.CfnAppMonitor.CustomEventsProperty
class CfnAppMonitor_CustomEventsPropertyDef(BaseStruct):
    status: typing.Optional[str] = pydantic.Field(None, description='Set this to ``ENABLED`` to allow the web client to send custom events for this app monitor. Valid values are ``ENABLED`` and ``DISABLED`` .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-customevents.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_rum as rum\n\n    custom_events_property = rum.CfnAppMonitor.CustomEventsProperty(\n        status="status"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['status']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_rum.CfnAppMonitor.CustomEventsProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_rum.CfnAppMonitor.MetricDefinitionProperty
class CfnAppMonitor_MetricDefinitionPropertyDef(BaseStruct):
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the metric that is defined in this structure.\n')
    dimension_keys: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch . The value of this field is used only if the metric destination is ``CloudWatch`` . If the metric destination is ``Evidently`` , the value of ``DimensionKeys`` is ignored.\n')
    event_pattern: typing.Optional[str] = pydantic.Field(None, description="The pattern that defines the metric. RUM checks events that happen in a user's session against the pattern, and events that match the pattern are sent to the metric destination. If the metrics destination is ``CloudWatch`` and the event also matches a value in ``DimensionKeys`` , then the metric is published with the specified dimensions.\n")
    namespace: typing.Optional[str] = pydantic.Field(None, description="If you are creating a custom metric instead of an extended metrics, use this parameter to define the metric namespace for that custom metric. Do not specify this parameter if you are creating an extended metric. You can't use any string that starts with ``AWS/`` for your namespace.\n")
    unit_label: typing.Optional[str] = pydantic.Field(None, description='Use this field only if you are sending this metric to CloudWatch . It defines the CloudWatch metric unit that this metric is measured in.\n')
    value_key: typing.Optional[str] = pydantic.Field(None, description='The field within the event object that the metric value is sourced from.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_rum as rum\n\n    metric_definition_property = rum.CfnAppMonitor.MetricDefinitionProperty(\n        name="name",\n\n        # the properties below are optional\n        dimension_keys={\n            "dimension_keys_key": "dimensionKeys"\n        },\n        event_pattern="eventPattern",\n        namespace="namespace",\n        unit_label="unitLabel",\n        value_key="valueKey"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['name', 'dimension_keys', 'event_pattern', 'namespace', 'unit_label', 'value_key']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_rum.CfnAppMonitor.MetricDefinitionProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_rum.CfnAppMonitor.MetricDestinationProperty
class CfnAppMonitor_MetricDestinationPropertyDef(BaseStruct):
    destination: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Defines the destination to send the metrics to. Valid values are ``CloudWatch`` and ``Evidently`` . If you specify ``Evidently`` , you must also specify the ARN of the CloudWatch Evidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.\n')
    destination_arn: typing.Optional[str] = pydantic.Field(None, description='Use this parameter only if ``Destination`` is ``Evidently`` . This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics.\n')
    iam_role_arn: typing.Optional[str] = pydantic.Field(None, description='This parameter is required if ``Destination`` is ``Evidently`` . If ``Destination`` is ``CloudWatch`` , do not use this parameter. This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.\n')
    metric_definitions: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_MetricDefinitionPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='An array of structures which define the metrics that you want to send.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_rum as rum\n\n    metric_destination_property = rum.CfnAppMonitor.MetricDestinationProperty(\n        destination="destination",\n\n        # the properties below are optional\n        destination_arn="destinationArn",\n        iam_role_arn="iamRoleArn",\n        metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(\n            name="name",\n\n            # the properties below are optional\n            dimension_keys={\n                "dimension_keys_key": "dimensionKeys"\n            },\n            event_pattern="eventPattern",\n            namespace="namespace",\n            unit_label="unitLabel",\n            value_key="valueKey"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['destination', 'destination_arn', 'iam_role_arn', 'metric_definitions']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_rum.CfnAppMonitor.MetricDestinationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_rum.CfnAppMonitor
class CfnAppMonitorDef(BaseCfnResource):
    domain: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The top-level internet domain name for which your application has administrative authority. This parameter is required.\n')
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='A name for the app monitor. This parameter is required.\n')
    app_monitor_configuration: typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_AppMonitorConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include ``AppMonitorConfiguration`` , you must set up your own authorization method. For more information, see `Authorize your application to send data to AWS <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html>`_ . If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.\n")
    custom_events: typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_CustomEventsPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Specifies whether this app monitor allows the web client to define and send custom events. If you omit this parameter, custom events are ``DISABLED`` .\n')
    cw_log_enabled: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges. If you omit this parameter, the default is ``false`` .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description="Assigns one or more tags (key-value pairs) to the app monitor. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an app monitor. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .")
    _init_params: typing.ClassVar[list[str]] = ['domain', 'name', 'app_monitor_configuration', 'custom_events', 'cw_log_enabled', 'tags']
    _method_names: typing.ClassVar[list[str]] = ['AppMonitorConfigurationProperty', 'CustomEventsProperty', 'MetricDefinitionProperty', 'MetricDestinationProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_rum.CfnAppMonitor'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnAppMonitorDefConfig] = pydantic.Field(None)


class CfnAppMonitorDefConfig(pydantic.BaseModel):
    AppMonitorConfigurationProperty: typing.Optional[list[CfnAppMonitorDefAppmonitorconfigurationpropertyParams]] = pydantic.Field(None, description='')
    CustomEventsProperty: typing.Optional[list[CfnAppMonitorDefCustomeventspropertyParams]] = pydantic.Field(None, description='')
    MetricDefinitionProperty: typing.Optional[list[CfnAppMonitorDefMetricdefinitionpropertyParams]] = pydantic.Field(None, description='')
    MetricDestinationProperty: typing.Optional[list[CfnAppMonitorDefMetricdestinationpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnAppMonitorDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnAppMonitorDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnAppMonitorDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnAppMonitorDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnAppMonitorDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnAppMonitorDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnAppMonitorDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnAppMonitorDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnAppMonitorDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnAppMonitorDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnAppMonitorDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnAppMonitorDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnAppMonitorDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnAppMonitorDefAppmonitorconfigurationpropertyParams(pydantic.BaseModel):
    allow_cookies: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='')
    enable_x_ray: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='')
    excluded_pages: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    favorite_pages: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    guest_role_arn: typing.Optional[str] = pydantic.Field(None, description='')
    identity_pool_id: typing.Optional[str] = pydantic.Field(None, description='')
    included_pages: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    metric_destinations: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_MetricDestinationPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='')
    session_sample_rate: typing.Union[int, float, None] = pydantic.Field(None, description='')
    telemetries: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='')
    ...

class CfnAppMonitorDefCustomeventspropertyParams(pydantic.BaseModel):
    status: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAppMonitorDefMetricdefinitionpropertyParams(pydantic.BaseModel):
    name: str = pydantic.Field(..., description='')
    dimension_keys: typing.Union[models.UnsupportedResource, typing.Mapping[str, str], None] = pydantic.Field(None, description='')
    event_pattern: typing.Optional[str] = pydantic.Field(None, description='')
    namespace: typing.Optional[str] = pydantic.Field(None, description='')
    unit_label: typing.Optional[str] = pydantic.Field(None, description='')
    value_key: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAppMonitorDefMetricdestinationpropertyParams(pydantic.BaseModel):
    destination: str = pydantic.Field(..., description='')
    destination_arn: typing.Optional[str] = pydantic.Field(None, description='')
    iam_role_arn: typing.Optional[str] = pydantic.Field(None, description='')
    metric_definitions: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_MetricDefinitionPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='')
    ...

class CfnAppMonitorDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnAppMonitorDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnAppMonitorDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnAppMonitorDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnAppMonitorDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnAppMonitorDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnAppMonitorDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnAppMonitorDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnAppMonitorDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnAppMonitorDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnAppMonitorDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnAppMonitorDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnAppMonitorDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnAppMonitorDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_rum.CfnAppMonitorProps
class CfnAppMonitorPropsDef(BaseCfnProperty):
    domain: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The top-level internet domain name for which your application has administrative authority. This parameter is required.\n')
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='A name for the app monitor. This parameter is required.\n')
    app_monitor_configuration: typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_AppMonitorConfigurationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include ``AppMonitorConfiguration`` , you must set up your own authorization method. For more information, see `Authorize your application to send data to AWS <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html>`_ . If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.\n")
    custom_events: typing.Union[models.UnsupportedResource, models.aws_rum.CfnAppMonitor_CustomEventsPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Specifies whether this app monitor allows the web client to define and send custom events. If you omit this parameter, custom events are ``DISABLED`` .\n')
    cw_log_enabled: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges. If you omit this parameter, the default is ``false`` .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='Assigns one or more tags (key-value pairs) to the app monitor. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don\'t have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an app monitor. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_rum as rum\n\n    cfn_app_monitor_props = rum.CfnAppMonitorProps(\n        domain="domain",\n        name="name",\n\n        # the properties below are optional\n        app_monitor_configuration=rum.CfnAppMonitor.AppMonitorConfigurationProperty(\n            allow_cookies=False,\n            enable_xRay=False,\n            excluded_pages=["excludedPages"],\n            favorite_pages=["favoritePages"],\n            guest_role_arn="guestRoleArn",\n            identity_pool_id="identityPoolId",\n            included_pages=["includedPages"],\n            metric_destinations=[rum.CfnAppMonitor.MetricDestinationProperty(\n                destination="destination",\n\n                # the properties below are optional\n                destination_arn="destinationArn",\n                iam_role_arn="iamRoleArn",\n                metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(\n                    name="name",\n\n                    # the properties below are optional\n                    dimension_keys={\n                        "dimension_keys_key": "dimensionKeys"\n                    },\n                    event_pattern="eventPattern",\n                    namespace="namespace",\n                    unit_label="unitLabel",\n                    value_key="valueKey"\n                )]\n            )],\n            session_sample_rate=123,\n            telemetries=["telemetries"]\n        ),\n        custom_events=rum.CfnAppMonitor.CustomEventsProperty(\n            status="status"\n        ),\n        cw_log_enabled=False,\n        tags=[CfnTag(\n            key="key",\n            value="value"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['domain', 'name', 'app_monitor_configuration', 'custom_events', 'cw_log_enabled', 'tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_rum.CfnAppMonitorProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnAppMonitor_AppMonitorConfigurationProperty: typing.Optional[dict[str, CfnAppMonitor_AppMonitorConfigurationPropertyDef]] = pydantic.Field(None)
    CfnAppMonitor_CustomEventsProperty: typing.Optional[dict[str, CfnAppMonitor_CustomEventsPropertyDef]] = pydantic.Field(None)
    CfnAppMonitor_MetricDefinitionProperty: typing.Optional[dict[str, CfnAppMonitor_MetricDefinitionPropertyDef]] = pydantic.Field(None)
    CfnAppMonitor_MetricDestinationProperty: typing.Optional[dict[str, CfnAppMonitor_MetricDestinationPropertyDef]] = pydantic.Field(None)
    CfnAppMonitor: typing.Optional[dict[str, CfnAppMonitorDef]] = pydantic.Field(None)
    CfnAppMonitorProps: typing.Optional[dict[str, CfnAppMonitorPropsDef]] = pydantic.Field(None)
    ...
