from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline.FieldProperty
class CfnPipeline_FieldPropertyDef(BaseStruct):
    key: str = pydantic.Field(..., description='Specifies the name of a field for a particular object. To view valid values for a particular field, see `Pipeline Object Reference <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-objects.html>`_ in the *AWS Data Pipeline Developer Guide* .\n')
    ref_value: typing.Optional[str] = pydantic.Field(None, description='A field value that you specify as an identifier of another object in the same pipeline definition. .. epigraph:: You can specify the field value as either a string value ( ``StringValue`` ) or a reference to another object ( ``RefValue`` ), but not both. Required if the key that you are using requires it.\n')
    string_value: typing.Optional[str] = pydantic.Field(None, description='A field value that you specify as a string. To view valid values for a particular field, see `Pipeline Object Reference <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-objects.html>`_ in the *AWS Data Pipeline Developer Guide* . .. epigraph:: You can specify the field value as either a string value ( ``StringValue`` ) or a reference to another object ( ``RefValue`` ), but not both. Required if the key that you are using requires it.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-field.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_datapipeline as datapipeline\n\n    field_property = datapipeline.CfnPipeline.FieldProperty(\n        key="key",\n\n        # the properties below are optional\n        ref_value="refValue",\n        string_value="stringValue"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['key', 'ref_value', 'string_value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline.FieldProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline.ParameterAttributeProperty
class CfnPipeline_ParameterAttributePropertyDef(BaseStruct):
    key: str = pydantic.Field(..., description='The field identifier.\n')
    string_value: str = pydantic.Field(..., description='The field value, expressed as a String.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterattribute.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_datapipeline as datapipeline\n\n    parameter_attribute_property = datapipeline.CfnPipeline.ParameterAttributeProperty(\n        key="key",\n        string_value="stringValue"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['key', 'string_value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline.ParameterAttributeProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline.ParameterObjectProperty
class CfnPipeline_ParameterObjectPropertyDef(BaseStruct):
    attributes: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_ParameterAttributePropertyDef, dict[str, typing.Any]]]] = pydantic.Field(..., description='The attributes of the parameter object.\n')
    _init_params: typing.ClassVar[list[str]] = ['attributes']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline.ParameterObjectProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline.ParameterValueProperty
class CfnPipeline_ParameterValuePropertyDef(BaseStruct):
    string_value: str = pydantic.Field(..., description='The field value, expressed as a String.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalue.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_datapipeline as datapipeline\n\n    parameter_value_property = datapipeline.CfnPipeline.ParameterValueProperty(\n        id="id",\n        string_value="stringValue"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['string_value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline.ParameterValueProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline.PipelineObjectProperty
class CfnPipeline_PipelineObjectPropertyDef(BaseStruct):
    fields: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_FieldPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(..., description='Key-value pairs that define the properties of the object.\n')
    name: str = pydantic.Field(..., description='The name of the object.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobject.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_datapipeline as datapipeline\n\n    pipeline_object_property = datapipeline.CfnPipeline.PipelineObjectProperty(\n        fields=[datapipeline.CfnPipeline.FieldProperty(\n            key="key",\n\n            # the properties below are optional\n            ref_value="refValue",\n            string_value="stringValue"\n        )],\n        id="id",\n        name="name"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['fields', 'name']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline.PipelineObjectProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline.PipelineTagProperty
class CfnPipeline_PipelineTagPropertyDef(BaseStruct):
    key: str = pydantic.Field(..., description='The key name of a tag.\n')
    value: str = pydantic.Field(..., description='The value to associate with the key name.\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetag.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_datapipeline as datapipeline\n\n    pipeline_tag_property = datapipeline.CfnPipeline.PipelineTagProperty(\n        key="key",\n        value="value"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['key', 'value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline.PipelineTagProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_datapipeline.CfnPipeline
class CfnPipelineDef(BaseCfnResource):
    name: str = pydantic.Field(..., description='The name of the pipeline.\n')
    activate: typing.Union[bool, typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], None] = pydantic.Field(None, description='Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to ``true`` .\n')
    description: typing.Optional[str] = pydantic.Field(None, description='A description of the pipeline.\n')
    parameter_objects: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_ParameterObjectPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The parameter objects used with the pipeline.\n')
    parameter_values: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_ParameterValuePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The parameter values used with the pipeline.\n')
    pipeline_objects: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_PipelineObjectPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see `Editing Your Pipeline <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-modify-console.html>`_ in the *AWS Data Pipeline Developer Guide* .\n')
    pipeline_tags: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_PipelineTagPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see `Controlling Access to Pipelines and Resources <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`_ in the *AWS Data Pipeline Developer Guide* .')
    _init_params: typing.ClassVar[list[str]] = ['name', 'activate', 'description', 'parameter_objects', 'parameter_values', 'pipeline_objects', 'pipeline_tags']
    _method_names: typing.ClassVar[list[str]] = ['FieldProperty', 'ParameterAttributeProperty', 'ParameterObjectProperty', 'ParameterValueProperty', 'PipelineObjectProperty', 'PipelineTagProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipeline'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CfnPipelineDefConfig] = pydantic.Field(None)


class CfnPipelineDefConfig(pydantic.BaseModel):
    FieldProperty: typing.Optional[list[CfnPipelineDefFieldpropertyParams]] = pydantic.Field(None, description='')
    ParameterAttributeProperty: typing.Optional[list[CfnPipelineDefParameterattributepropertyParams]] = pydantic.Field(None, description='')
    ParameterObjectProperty: typing.Optional[list[CfnPipelineDefParameterobjectpropertyParams]] = pydantic.Field(None, description='')
    ParameterValueProperty: typing.Optional[list[CfnPipelineDefParametervaluepropertyParams]] = pydantic.Field(None, description='')
    PipelineObjectProperty: typing.Optional[list[CfnPipelineDefPipelineobjectpropertyParams]] = pydantic.Field(None, description='')
    PipelineTagProperty: typing.Optional[list[CfnPipelineDefPipelinetagpropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[CfnPipelineDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[CfnPipelineDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[CfnPipelineDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[CfnPipelineDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[CfnPipelineDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[CfnPipelineDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[CfnPipelineDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[CfnPipelineDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[CfnPipelineDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[CfnPipelineDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[CfnPipelineDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[CfnPipelineDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[CfnPipelineDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')

class CfnPipelineDefFieldpropertyParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='')
    ref_value: typing.Optional[str] = pydantic.Field(None, description='')
    string_value: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnPipelineDefParameterattributepropertyParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='')
    string_value: str = pydantic.Field(..., description='')
    ...

class CfnPipelineDefParameterobjectpropertyParams(pydantic.BaseModel):
    attributes: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_ParameterAttributePropertyDef, dict[str, typing.Any]]]] = pydantic.Field(..., description='')
    id: str = pydantic.Field(..., description='')
    ...

class CfnPipelineDefParametervaluepropertyParams(pydantic.BaseModel):
    id: str = pydantic.Field(..., description='')
    string_value: str = pydantic.Field(..., description='')
    ...

class CfnPipelineDefPipelineobjectpropertyParams(pydantic.BaseModel):
    fields: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_FieldPropertyDef, dict[str, typing.Any]]]] = pydantic.Field(..., description='')
    id: str = pydantic.Field(..., description='')
    name: str = pydantic.Field(..., description='')
    ...

class CfnPipelineDefPipelinetagpropertyParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='')
    value: str = pydantic.Field(..., description='')
    ...

class CfnPipelineDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnPipelineDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnPipelineDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnPipelineDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnPipelineDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnPipelineDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnPipelineDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnPipelineDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnPipelineDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnPipelineDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnPipelineDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='- tree inspector to collect and process attributes.')
    ...

class CfnPipelineDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnPipelineDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnPipelineDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_datapipeline.CfnPipelineProps
class CfnPipelinePropsDef(BaseCfnProperty):
    name: str = pydantic.Field(..., description='The name of the pipeline.\n')
    activate: typing.Union[bool, typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], None] = pydantic.Field(None, description='Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to ``true`` .\n')
    description: typing.Optional[str] = pydantic.Field(None, description='A description of the pipeline.\n')
    parameter_objects: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_ParameterObjectPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The parameter objects used with the pipeline.\n')
    parameter_values: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_ParameterValuePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The parameter values used with the pipeline.\n')
    pipeline_objects: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_PipelineObjectPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see `Editing Your Pipeline <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-manage-pipeline-modify-console.html>`_ in the *AWS Data Pipeline Developer Guide* .\n')
    pipeline_tags: typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], typing.Sequence[typing.Union[typing.Union[models.CfnDynamicReferenceDef, models.IntrinsicDef, models.JsonNullDef, models.ReferenceDef, models.SecretValueDef, models.CfnConditionDef, models.CfnJsonDef, models.aws_events.EventFieldDef, models.aws_events.MatchDef, models.aws_iam.PolicyDocumentDef, models.custom_resources.PhysicalResourceIdReferenceDef], models.aws_datapipeline.CfnPipeline_PipelineTagPropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see `Controlling Access to Pipelines and Resources <https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`_ in the *AWS Data Pipeline Developer Guide* .\n\n:link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_datapipeline as datapipeline\n\n    cfn_pipeline_props = datapipeline.CfnPipelineProps(\n        name="name",\n\n        # the properties below are optional\n        activate=False,\n        description="description",\n        parameter_objects=[datapipeline.CfnPipeline.ParameterObjectProperty(\n            attributes=[datapipeline.CfnPipeline.ParameterAttributeProperty(\n                key="key",\n                string_value="stringValue"\n            )],\n            id="id"\n        )],\n        parameter_values=[datapipeline.CfnPipeline.ParameterValueProperty(\n            id="id",\n            string_value="stringValue"\n        )],\n        pipeline_objects=[datapipeline.CfnPipeline.PipelineObjectProperty(\n            fields=[datapipeline.CfnPipeline.FieldProperty(\n                key="key",\n\n                # the properties below are optional\n                ref_value="refValue",\n                string_value="stringValue"\n            )],\n            id="id",\n            name="name"\n        )],\n        pipeline_tags=[datapipeline.CfnPipeline.PipelineTagProperty(\n            key="key",\n            value="value"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['name', 'activate', 'description', 'parameter_objects', 'parameter_values', 'pipeline_objects', 'pipeline_tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_datapipeline.CfnPipelineProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    CfnPipeline_FieldProperty: typing.Optional[dict[str, CfnPipeline_FieldPropertyDef]] = pydantic.Field(None)
    CfnPipeline_ParameterAttributeProperty: typing.Optional[dict[str, CfnPipeline_ParameterAttributePropertyDef]] = pydantic.Field(None)
    CfnPipeline_ParameterObjectProperty: typing.Optional[dict[str, CfnPipeline_ParameterObjectPropertyDef]] = pydantic.Field(None)
    CfnPipeline_ParameterValueProperty: typing.Optional[dict[str, CfnPipeline_ParameterValuePropertyDef]] = pydantic.Field(None)
    CfnPipeline_PipelineObjectProperty: typing.Optional[dict[str, CfnPipeline_PipelineObjectPropertyDef]] = pydantic.Field(None)
    CfnPipeline_PipelineTagProperty: typing.Optional[dict[str, CfnPipeline_PipelineTagPropertyDef]] = pydantic.Field(None)
    CfnPipeline: typing.Optional[dict[str, CfnPipelineDef]] = pydantic.Field(None)
    CfnPipelineProps: typing.Optional[dict[str, CfnPipelinePropsDef]] = pydantic.Field(None)
    ...
