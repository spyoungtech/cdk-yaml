from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_codestarnotifications.NotificationRule
class NotificationRuleDef(BaseConstruct):
    events: typing.Union[typing.Sequence[str], _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='A list of event types associated with this notification rule. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.\n')
    source: typing.Union[models.UnsupportedResource, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Currently, Supported sources include pipelines in AWS CodePipeline, build projects in AWS CodeBuild, and repositories in AWS CodeCommit in this L2 constructor.\n')
    targets: typing.Optional[typing.Sequence[models.UnsupportedResource]] = pydantic.Field(None, description='The targets to register for the notification destination. Default: - No targets are added to the rule. Use ``addTarget()`` to add a target.\n')
    detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = pydantic.Field(None, description='The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL\n')
    enabled: typing.Optional[bool] = pydantic.Field(None, description="The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true\n")
    notification_rule_name: typing.Optional[str] = pydantic.Field(None, description='The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``')
    _init_params: typing.ClassVar[list[str]] = ['events', 'source', 'targets', 'detail_type', 'enabled', 'notification_rule_name']
    _method_names: typing.ClassVar[list[str]] = ['add_target', 'apply_removal_policy']
    _classmethod_names: typing.ClassVar[list[str]] = ['from_notification_rule_arn']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.NotificationRule'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = ['from_notification_rule_arn']
    ...


    from_notification_rule_arn: typing.Optional[models.aws_codestarnotifications.NotificationRuleDefFromNotificationRuleArnParams] = pydantic.Field(None, description='Import an existing notification rule provided an ARN.')
    resource_config: typing.Optional[models.aws_codestarnotifications.NotificationRuleDefConfig] = pydantic.Field(None)


class NotificationRuleDefConfig(pydantic.BaseModel):
    add_target: typing.Optional[list[models.aws_codestarnotifications.NotificationRuleDefAddTargetParams]] = pydantic.Field(None, description='Adds target to notification rule.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)

class NotificationRuleDefAddTargetParams(pydantic.BaseModel):
    target: models.UnsupportedResource = pydantic.Field(..., description='The SNS topic or AWS Chatbot Slack target.')
    ...

class NotificationRuleDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: aws_cdk.RemovalPolicy = pydantic.Field(..., description='-')
    ...

class NotificationRuleDefFromNotificationRuleArnParams(pydantic.BaseModel):
    scope: models.constructs.ConstructDef = pydantic.Field(..., description='The parent creating construct.\n')
    id: str = pydantic.Field(..., description="The construct's name.\n")
    notification_rule_arn: str = pydantic.Field(..., description='Notification rule ARN (i.e. arn:aws:codestar-notifications:::notificationrule/01234abcde).')
    ...


#  autogenerated from aws_cdk.aws_codestarnotifications.CfnNotificationRule.TargetProperty
class CfnNotificationRule_TargetPropertyDef(BaseStruct):
    target_address: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the AWS Chatbot topic or AWS Chatbot client.\n')
    target_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The target type. Can be an Amazon Simple Notification Service topic or AWS Chatbot client. - Amazon Simple Notification Service topics are specified as ``SNS`` . - AWS Chatbot clients are specified as ``AWSChatbotSlack`` .\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_codestarnotifications as codestarnotifications\n\n    target_property = codestarnotifications.CfnNotificationRule.TargetProperty(\n        target_address="targetAddress",\n        target_type="targetType"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['target_address', 'target_type']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.CfnNotificationRule.TargetProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_codestarnotifications.NotificationRuleOptions
class NotificationRuleOptionsDef(BaseStruct):
    detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = pydantic.Field(None, description='The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL\n')
    enabled: typing.Optional[bool] = pydantic.Field(None, description="The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true\n")
    notification_rule_name: typing.Optional[str] = pydantic.Field(None, description='The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_codestarnotifications as codestarnotifications\n\n    notification_rule_options = codestarnotifications.NotificationRuleOptions(\n        detail_type=codestarnotifications.DetailType.BASIC,\n        enabled=False,\n        notification_rule_name="notificationRuleName"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['detail_type', 'enabled', 'notification_rule_name']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.NotificationRuleOptions'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_codestarnotifications.NotificationRuleProps
class NotificationRulePropsDef(BaseStruct):
    detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = pydantic.Field(None, description='The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL\n')
    enabled: typing.Optional[bool] = pydantic.Field(None, description="The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true\n")
    notification_rule_name: typing.Optional[str] = pydantic.Field(None, description='The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``\n')
    events: typing.Union[typing.Sequence[str], _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='A list of event types associated with this notification rule. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.\n')
    source: typing.Union[models.UnsupportedResource, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Currently, Supported sources include pipelines in AWS CodePipeline, build projects in AWS CodeBuild, and repositories in AWS CodeCommit in this L2 constructor.\n')
    targets: typing.Optional[typing.Sequence[models.UnsupportedResource]] = pydantic.Field(None, description='The targets to register for the notification destination. Default: - No targets are added to the rule. Use ``addTarget()`` to add a target.\n\n:exampleMetadata: infused\n\nExample::\n\n    import aws_cdk.aws_codestarnotifications as notifications\n    import aws_cdk.aws_codebuild as codebuild\n    import aws_cdk.aws_sns as sns\n    import aws_cdk.aws_chatbot as chatbot\n\n\n    project = codebuild.PipelineProject(self, "MyProject")\n\n    topic = sns.Topic(self, "MyTopic1")\n\n    slack = chatbot.SlackChannelConfiguration(self, "MySlackChannel",\n        slack_channel_configuration_name="YOUR_CHANNEL_NAME",\n        slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",\n        slack_channel_id="YOUR_SLACK_CHANNEL_ID"\n    )\n\n    rule = notifications.NotificationRule(self, "NotificationRule",\n        source=project,\n        events=["codebuild-project-build-state-succeeded", "codebuild-project-build-state-failed"\n        ],\n        targets=[topic]\n    )\n    rule.add_target(slack)\n')
    _init_params: typing.ClassVar[list[str]] = ['detail_type', 'enabled', 'notification_rule_name', 'events', 'source', 'targets']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.NotificationRuleProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_codestarnotifications.NotificationRulePropsDefConfig] = pydantic.Field(None)


class NotificationRulePropsDefConfig(pydantic.BaseModel):
    source_config: typing.Optional[models._interface_methods.AwsCodestarnotificationsINotificationRuleSourceDefConfig] = pydantic.Field(None)


#  autogenerated from aws_cdk.aws_codestarnotifications.NotificationRuleSourceConfig
class NotificationRuleSourceConfigDef(BaseStruct):
    source_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the notification source.\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_codestarnotifications as codestarnotifications\n\n    notification_rule_source_config = codestarnotifications.NotificationRuleSourceConfig(\n        source_arn="sourceArn"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['source_arn']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.NotificationRuleSourceConfig'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_codestarnotifications.NotificationRuleTargetConfig
class NotificationRuleTargetConfigDef(BaseStruct):
    target_address: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the Amazon SNS topic or AWS Chatbot client.\n')
    target_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The target type. Can be an Amazon SNS topic or AWS Chatbot client.\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_codestarnotifications as codestarnotifications\n\n    notification_rule_target_config = codestarnotifications.NotificationRuleTargetConfig(\n        target_address="targetAddress",\n        target_type="targetType"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['target_address', 'target_type']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.NotificationRuleTargetConfig'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_codestarnotifications.DetailType
# skipping emum

#  autogenerated from aws_cdk.aws_codestarnotifications.INotificationRule
#  skipping Interface

#  autogenerated from aws_cdk.aws_codestarnotifications.INotificationRuleSource
#  skipping Interface

#  autogenerated from aws_cdk.aws_codestarnotifications.INotificationRuleTarget
#  skipping Interface

#  autogenerated from aws_cdk.aws_codestarnotifications.CfnNotificationRule
class CfnNotificationRuleDef(BaseCfnResource):
    detail_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The level of detail to include in the notifications for this resource. ``BASIC`` will include only the contents of the event as it would appear in Amazon CloudWatch. ``FULL`` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.\n')
    event_type_ids: typing.Union[typing.Sequence[str], _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='A list of event types associated with this notification rule. For a complete list of event types and IDs, see `Notification concepts <https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api>`_ in the *Developer Tools Console User Guide* .\n')
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name for the notification rule. Notification rule names must be unique in your AWS account .\n')
    resource: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in AWS CodePipeline , repositories in AWS CodeCommit , and build projects in AWS CodeBuild .\n')
    targets: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_codestarnotifications.CfnNotificationRule_TargetPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(REQUIRED_INIT_PARAM, description='A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and AWS Chatbot clients to associate with the notification rule.\n')
    created_by: typing.Optional[str] = pydantic.Field(None, description='')
    event_type_id: typing.Optional[str] = pydantic.Field(None, description='')
    status: typing.Optional[str] = pydantic.Field(None, description="The status of the notification rule. The default value is ``ENABLED`` . If the status is set to ``DISABLED`` , notifications aren't sent for the notification rule.\n")
    tags: typing.Optional[typing.Mapping[str, str]] = pydantic.Field(None, description='A list of tags to apply to this notification rule. Key names cannot start with " ``aws`` ".\n')
    target_address: typing.Optional[str] = pydantic.Field(None, description='')
    _init_params: typing.ClassVar[list[str]] = ['detail_type', 'event_type_ids', 'name', 'resource', 'targets', 'created_by', 'event_type_id', 'status', 'tags', 'target_address']
    _method_names: typing.ClassVar[list[str]] = ['TargetProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.CfnNotificationRule'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_codestarnotifications.CfnNotificationRuleDefConfig] = pydantic.Field(None)


class CfnNotificationRuleDefConfig(pydantic.BaseModel):
    TargetProperty: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefTargetpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[models.aws_codestarnotifications.CfnNotificationRuleDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnNotificationRuleDefTargetpropertyParams(pydantic.BaseModel):
    target_address: str = pydantic.Field(..., description='')
    target_type: str = pydantic.Field(..., description='')
    ...

class CfnNotificationRuleDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnNotificationRuleDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnNotificationRuleDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnNotificationRuleDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnNotificationRuleDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnNotificationRuleDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnNotificationRuleDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnNotificationRuleDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnNotificationRuleDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnNotificationRuleDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnNotificationRuleDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnNotificationRuleDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnNotificationRuleDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnNotificationRuleDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_codestarnotifications.CfnNotificationRuleProps
class CfnNotificationRulePropsDef(BaseCfnProperty):
    detail_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The level of detail to include in the notifications for this resource. ``BASIC`` will include only the contents of the event as it would appear in Amazon CloudWatch. ``FULL`` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.\n')
    event_type_ids: typing.Union[typing.Sequence[str], _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='A list of event types associated with this notification rule. For a complete list of event types and IDs, see `Notification concepts <https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api>`_ in the *Developer Tools Console User Guide* .\n')
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name for the notification rule. Notification rule names must be unique in your AWS account .\n')
    resource: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in AWS CodePipeline , repositories in AWS CodeCommit , and build projects in AWS CodeBuild .\n')
    targets: typing.Union[_REQUIRED_INIT_PARAM, models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_codestarnotifications.CfnNotificationRule_TargetPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(REQUIRED_INIT_PARAM, description='A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and AWS Chatbot clients to associate with the notification rule.\n')
    created_by: typing.Optional[str] = pydantic.Field(None, description='')
    event_type_id: typing.Optional[str] = pydantic.Field(None, description='')
    status: typing.Optional[str] = pydantic.Field(None, description="The status of the notification rule. The default value is ``ENABLED`` . If the status is set to ``DISABLED`` , notifications aren't sent for the notification rule.\n")
    tags: typing.Optional[typing.Mapping[str, str]] = pydantic.Field(None, description='A list of tags to apply to this notification rule. Key names cannot start with " ``aws`` ".\n')
    target_address: typing.Optional[str] = pydantic.Field(None, description='')
    _init_params: typing.ClassVar[list[str]] = ['detail_type', 'event_type_ids', 'name', 'resource', 'targets', 'created_by', 'event_type_id', 'status', 'tags', 'target_address']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_codestarnotifications.CfnNotificationRuleProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




class ModuleModel(pydantic.BaseModel):
    NotificationRule: typing.Optional[dict[str, models.aws_codestarnotifications.NotificationRuleDef]] = pydantic.Field(None)
    CfnNotificationRule_TargetProperty: typing.Optional[dict[str, models.aws_codestarnotifications.CfnNotificationRule_TargetPropertyDef]] = pydantic.Field(None)
    NotificationRuleOptions: typing.Optional[dict[str, models.aws_codestarnotifications.NotificationRuleOptionsDef]] = pydantic.Field(None)
    NotificationRuleProps: typing.Optional[dict[str, models.aws_codestarnotifications.NotificationRulePropsDef]] = pydantic.Field(None)
    NotificationRuleSourceConfig: typing.Optional[dict[str, models.aws_codestarnotifications.NotificationRuleSourceConfigDef]] = pydantic.Field(None)
    NotificationRuleTargetConfig: typing.Optional[dict[str, models.aws_codestarnotifications.NotificationRuleTargetConfigDef]] = pydantic.Field(None)
    CfnNotificationRule: typing.Optional[dict[str, models.aws_codestarnotifications.CfnNotificationRuleDef]] = pydantic.Field(None)
    CfnNotificationRuleProps: typing.Optional[dict[str, models.aws_codestarnotifications.CfnNotificationRulePropsDef]] = pydantic.Field(None)
    ...

import models
