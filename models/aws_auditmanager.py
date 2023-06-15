from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment.AssessmentReportsDestinationProperty
class CfnAssessment_AssessmentReportsDestinationPropertyDef(BaseStruct):
    destination: typing.Optional[str] = pydantic.Field(None, description='The destination of the assessment report.\n')
    destination_type: typing.Optional[str] = pydantic.Field(None, description='The destination type, such as Amazon S3.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    assessment_reports_destination_property = auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(\n        destination="destination",\n        destination_type="destinationType"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['destination', 'destination_type']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment.AssessmentReportsDestinationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment.AWSAccountProperty
class CfnAssessment_AWSAccountPropertyDef(BaseStruct):
    email_address: typing.Optional[str] = pydantic.Field(None, description="The email address that's associated with the AWS account .\n")
    name: typing.Optional[str] = pydantic.Field(None, description='The name of the AWS account .\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    a_wSAccount_property = auditmanager.CfnAssessment.AWSAccountProperty(\n        email_address="emailAddress",\n        id="id",\n        name="name"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['email_address', 'name']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment.AWSAccountProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment.AWSServiceProperty
class CfnAssessment_AWSServicePropertyDef(BaseStruct):
    service_name: typing.Optional[str] = pydantic.Field(None, description='The name of the AWS service .\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    a_wSService_property = auditmanager.CfnAssessment.AWSServiceProperty(\n        service_name="serviceName"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['service_name']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment.AWSServiceProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment.DelegationProperty
class CfnAssessment_DelegationPropertyDef(BaseStruct):
    assessment_id: typing.Optional[str] = pydantic.Field(None, description="The identifier for the assessment that's associated with the delegation.\n")
    assessment_name: typing.Optional[str] = pydantic.Field(None, description="The name of the assessment that's associated with the delegation.\n")
    comment: typing.Optional[str] = pydantic.Field(None, description="The comment that's related to the delegation.\n")
    control_set_id: typing.Optional[str] = pydantic.Field(None, description="The identifier for the control set that's associated with the delegation.\n")
    created_by: typing.Optional[str] = pydantic.Field(None, description='The user or role that created the delegation. *Minimum* : ``1`` *Maximum* : ``100`` *Pattern* : ``^[a-zA-Z0-9-_()\\\\[\\\\]\\\\s]+$``\n')
    creation_time: typing.Union[int, float, None] = pydantic.Field(None, description='Specifies when the delegation was created.\n')
    last_updated: typing.Union[int, float, None] = pydantic.Field(None, description='Specifies when the delegation was last updated.\n')
    role_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Name (ARN) of the IAM role.\n')
    role_type: typing.Optional[str] = pydantic.Field(None, description='The type of customer persona. .. epigraph:: In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .\n')
    status: typing.Optional[str] = pydantic.Field(None, description='The status of the delegation.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    delegation_property = auditmanager.CfnAssessment.DelegationProperty(\n        assessment_id="assessmentId",\n        assessment_name="assessmentName",\n        comment="comment",\n        control_set_id="controlSetId",\n        created_by="createdBy",\n        creation_time=123,\n        id="id",\n        last_updated=123,\n        role_arn="roleArn",\n        role_type="roleType",\n        status="status"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['assessment_id', 'assessment_name', 'comment', 'control_set_id', 'created_by', 'creation_time', 'last_updated', 'role_arn', 'role_type', 'status']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment.DelegationProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment.RoleProperty
class CfnAssessment_RolePropertyDef(BaseStruct):
    role_arn: typing.Optional[str] = pydantic.Field(None, description='The Amazon Resource Name (ARN) of the IAM role.\n')
    role_type: typing.Optional[str] = pydantic.Field(None, description='The type of customer persona. .. epigraph:: In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    role_property = auditmanager.CfnAssessment.RoleProperty(\n        role_arn="roleArn",\n        role_type="roleType"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['role_arn', 'role_type']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment.RoleProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment.ScopeProperty
class CfnAssessment_ScopePropertyDef(BaseStruct):
    aws_accounts: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AWSAccountPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The AWS accounts that are included in the scope of the assessment.\n')
    aws_services: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AWSServicePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The AWS services that are included in the scope of the assessment.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    scope_property = auditmanager.CfnAssessment.ScopeProperty(\n        aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(\n            email_address="emailAddress",\n            id="id",\n            name="name"\n        )],\n        aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(\n            service_name="serviceName"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['aws_accounts', 'aws_services']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment.ScopeProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessment
class CfnAssessmentDef(BaseCfnResource):
    scope_: models.constructs.ConstructDef = pydantic.Field(..., description='- scope in which this resource is defined.\n')
    assessment_reports_destination: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AssessmentReportsDestinationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The destination that evidence reports are stored in for the assessment.\n')
    aws_account: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AWSAccountPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="The AWS account that's associated with the assessment.\n")
    delegations: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_DelegationPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The delegations that are associated with the assessment.\n')
    description: typing.Optional[str] = pydantic.Field(None, description='The description of the assessment.\n')
    framework_id: typing.Optional[str] = pydantic.Field(None, description='The unique identifier for the framework.\n')
    name: typing.Optional[str] = pydantic.Field(None, description='The name of the assessment.\n')
    roles: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_RolePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The roles that are associated with the assessment.\n')
    status: typing.Optional[str] = pydantic.Field(None, description='The overall status of the assessment. When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` . After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='The tags that are associated with the assessment.')
    _init_params: typing.ClassVar[list[str]] = ['scope_', 'assessment_reports_destination', 'aws_account', 'delegations', 'description', 'framework_id', 'name', 'roles', 'status', 'tags']
    _method_names: typing.ClassVar[list[str]] = ['AWSAccountProperty', 'AWSServiceProperty', 'AssessmentReportsDestinationProperty', 'DelegationProperty', 'RoleProperty', 'ScopeProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessment'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnAssessmentDefConfig] = pydantic.Field(None)


class CfnAssessmentDefConfig(pydantic.BaseModel):
    AWSAccountProperty: typing.Optional[list[CfnAssessmentDefAwsaccountpropertyParams]] = pydantic.Field(None, description='')
    AWSServiceProperty: typing.Optional[list[CfnAssessmentDefAwsservicepropertyParams]] = pydantic.Field(None, description='')
    AssessmentReportsDestinationProperty: typing.Optional[list[CfnAssessmentDefAssessmentreportsdestinationpropertyParams]] = pydantic.Field(None, description='')
    DelegationProperty: typing.Optional[list[CfnAssessmentDefDelegationpropertyParams]] = pydantic.Field(None, description='')
    RoleProperty: typing.Optional[list[CfnAssessmentDefRolepropertyParams]] = pydantic.Field(None, description='')
    ScopeProperty: typing.Optional[list[CfnAssessmentDefScopepropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnAssessmentDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnAssessmentDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnAssessmentDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnAssessmentDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnAssessmentDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnAssessmentDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnAssessmentDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnAssessmentDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnAssessmentDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnAssessmentDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnAssessmentDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnAssessmentDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnAssessmentDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    attr_creation_time_config: typing.Optional[models._interface_methods.CoreIResolvableDefConfig] = pydantic.Field(None)
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnAssessmentDefAwsaccountpropertyParams(pydantic.BaseModel):
    email_address: typing.Optional[str] = pydantic.Field(None, description='')
    id: typing.Optional[str] = pydantic.Field(None, description='')
    name: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAssessmentDefAwsservicepropertyParams(pydantic.BaseModel):
    service_name: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAssessmentDefAssessmentreportsdestinationpropertyParams(pydantic.BaseModel):
    destination: typing.Optional[str] = pydantic.Field(None, description='')
    destination_type: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAssessmentDefDelegationpropertyParams(pydantic.BaseModel):
    assessment_id: typing.Optional[str] = pydantic.Field(None, description='')
    assessment_name: typing.Optional[str] = pydantic.Field(None, description='')
    comment: typing.Optional[str] = pydantic.Field(None, description='')
    control_set_id: typing.Optional[str] = pydantic.Field(None, description='')
    created_by: typing.Optional[str] = pydantic.Field(None, description='')
    creation_time: typing.Union[int, float, None] = pydantic.Field(None, description='')
    id: typing.Optional[str] = pydantic.Field(None, description='')
    last_updated: typing.Union[int, float, None] = pydantic.Field(None, description='')
    role_arn: typing.Optional[str] = pydantic.Field(None, description='')
    role_type: typing.Optional[str] = pydantic.Field(None, description='')
    status: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAssessmentDefRolepropertyParams(pydantic.BaseModel):
    role_arn: typing.Optional[str] = pydantic.Field(None, description='')
    role_type: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnAssessmentDefScopepropertyParams(pydantic.BaseModel):
    aws_accounts: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AWSAccountPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='')
    aws_services: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AWSServicePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='')
    ...

class CfnAssessmentDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnAssessmentDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnAssessmentDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnAssessmentDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnAssessmentDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnAssessmentDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnAssessmentDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnAssessmentDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnAssessmentDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnAssessmentDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnAssessmentDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='- tree inspector to collect and process attributes.')
    ...

class CfnAssessmentDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnAssessmentDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnAssessmentDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_auditmanager.CfnAssessmentProps
class CfnAssessmentPropsDef(BaseCfnProperty):
    assessment_reports_destination: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AssessmentReportsDestinationPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The destination that evidence reports are stored in for the assessment.\n')
    aws_account: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_AWSAccountPropertyDef, dict[str, typing.Any], None] = pydantic.Field(None, description="The AWS account that's associated with the assessment.\n")
    delegations: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_DelegationPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The delegations that are associated with the assessment.\n')
    description: typing.Optional[str] = pydantic.Field(None, description='The description of the assessment.\n')
    framework_id: typing.Optional[str] = pydantic.Field(None, description='The unique identifier for the framework.\n')
    name: typing.Optional[str] = pydantic.Field(None, description='The name of the assessment.\n')
    roles: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_auditmanager.CfnAssessment_RolePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The roles that are associated with the assessment.\n')
    status: typing.Optional[str] = pydantic.Field(None, description='The overall status of the assessment. When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` . After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='The tags that are associated with the assessment.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_auditmanager as auditmanager\n\n    cfn_assessment_props = auditmanager.CfnAssessmentProps(\n        assessment_reports_destination=auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(\n            destination="destination",\n            destination_type="destinationType"\n        ),\n        aws_account=auditmanager.CfnAssessment.AWSAccountProperty(\n            email_address="emailAddress",\n            id="id",\n            name="name"\n        ),\n        delegations=[auditmanager.CfnAssessment.DelegationProperty(\n            assessment_id="assessmentId",\n            assessment_name="assessmentName",\n            comment="comment",\n            control_set_id="controlSetId",\n            created_by="createdBy",\n            creation_time=123,\n            id="id",\n            last_updated=123,\n            role_arn="roleArn",\n            role_type="roleType",\n            status="status"\n        )],\n        description="description",\n        framework_id="frameworkId",\n        name="name",\n        roles=[auditmanager.CfnAssessment.RoleProperty(\n            role_arn="roleArn",\n            role_type="roleType"\n        )],\n        scope=auditmanager.CfnAssessment.ScopeProperty(\n            aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(\n                email_address="emailAddress",\n                id="id",\n                name="name"\n            )],\n            aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(\n                service_name="serviceName"\n            )]\n        ),\n        status="status",\n        tags=[CfnTag(\n            key="key",\n            value="value"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['assessment_reports_destination', 'aws_account', 'delegations', 'description', 'framework_id', 'name', 'roles', 'status', 'tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_auditmanager.CfnAssessmentProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnAssessment_AssessmentReportsDestinationProperty: typing.Optional[dict[str, CfnAssessment_AssessmentReportsDestinationPropertyDef]] = pydantic.Field(None)
    CfnAssessment_AWSAccountProperty: typing.Optional[dict[str, CfnAssessment_AWSAccountPropertyDef]] = pydantic.Field(None)
    CfnAssessment_AWSServiceProperty: typing.Optional[dict[str, CfnAssessment_AWSServicePropertyDef]] = pydantic.Field(None)
    CfnAssessment_DelegationProperty: typing.Optional[dict[str, CfnAssessment_DelegationPropertyDef]] = pydantic.Field(None)
    CfnAssessment_RoleProperty: typing.Optional[dict[str, CfnAssessment_RolePropertyDef]] = pydantic.Field(None)
    CfnAssessment_ScopeProperty: typing.Optional[dict[str, CfnAssessment_ScopePropertyDef]] = pydantic.Field(None)
    CfnAssessment: typing.Optional[dict[str, CfnAssessmentDef]] = pydantic.Field(None)
    CfnAssessmentProps: typing.Optional[dict[str, CfnAssessmentPropsDef]] = pydantic.Field(None)
    ...
