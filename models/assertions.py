from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.assertions.Annotations
class AnnotationsDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = ['find_error', 'find_info', 'find_warning', 'has_error', 'has_info', 'has_no_error', 'has_no_info', 'has_no_warning', 'has_warning']
    _classmethod_names: typing.ClassVar[list[str]] = ['from_stack']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.Annotations'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[AnnotationsDefConfig] = pydantic.Field(None)


class AnnotationsDefConfig(pydantic.BaseModel):
    find_error: typing.Optional[list[AnnotationsDefFindErrorParams]] = pydantic.Field(None, description='Get the set of matching errors of a given construct path and message.')
    find_info: typing.Optional[list[AnnotationsDefFindInfoParams]] = pydantic.Field(None, description='Get the set of matching infos of a given construct path and message.')
    find_warning: typing.Optional[list[AnnotationsDefFindWarningParams]] = pydantic.Field(None, description='Get the set of matching warning of a given construct path and message.')
    from_stack: typing.Optional[list[AnnotationsDefFromStackParams]] = pydantic.Field(None, description='Base your assertions on the messages returned by a synthesized CDK ``Stack``.')
    has_error: typing.Optional[list[AnnotationsDefHasErrorParams]] = pydantic.Field(None, description='Assert that an error with the given message exists in the synthesized CDK ``Stack``.')
    has_info: typing.Optional[list[AnnotationsDefHasInfoParams]] = pydantic.Field(None, description='Assert that an info with the given message exists in the synthesized CDK ``Stack``.')
    has_no_error: typing.Optional[list[AnnotationsDefHasNoErrorParams]] = pydantic.Field(None, description='Assert that an error with the given message does not exist in the synthesized CDK ``Stack``.')
    has_no_info: typing.Optional[list[AnnotationsDefHasNoInfoParams]] = pydantic.Field(None, description='Assert that an info with the given message does not exist in the synthesized CDK ``Stack``.')
    has_no_warning: typing.Optional[list[AnnotationsDefHasNoWarningParams]] = pydantic.Field(None, description='Assert that an warning with the given message does not exist in the synthesized CDK ``Stack``.')
    has_warning: typing.Optional[list[AnnotationsDefHasWarningParams]] = pydantic.Field(None, description='Assert that an warning with the given message exists in the synthesized CDK ``Stack``.')

class AnnotationsDefFindErrorParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the error. Provide ``'*'`` to match all errors in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the error message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefFindInfoParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the info. Provide ``'*'`` to match all infos in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the info message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefFindWarningParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the warning. Provide ``'*'`` to match all warnings in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the warning message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefFromStackParams(pydantic.BaseModel):
    stack: models.StackDef = pydantic.Field(..., description='the CDK Stack to run assertions on.')
    return_config: typing.Optional[list[models.assertions.AnnotationsDefConfig]] = pydantic.Field(None)
    ...

class AnnotationsDefHasErrorParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the error. Provide ``'*'`` to match all errors in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the error message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefHasInfoParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the info. Provide ``'*'`` to match all info in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the info message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefHasNoErrorParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the error. Provide ``'*'`` to match all errors in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the error message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefHasNoInfoParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the info. Provide ``'*'`` to match all info in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the info message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefHasNoWarningParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the warning. Provide ``'*'`` to match all warnings in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the warning message as should be expected. This should be a string or Matcher object.')
    ...

class AnnotationsDefHasWarningParams(pydantic.BaseModel):
    construct_path: str = pydantic.Field(..., description="the construct path to the warning. Provide ``'*'`` to match all warnings in the template.\n")
    message: typing.Any = pydantic.Field(..., description='the warning message as should be expected. This should be a string or Matcher object.')
    ...


#  autogenerated from aws_cdk.assertions.Capture
class CaptureDef(BaseClass):
    pattern: typing.Any = pydantic.Field(None, description='a nested pattern or Matcher. If a nested pattern is provided ``objectLike()`` matching is applied.')
    _init_params: typing.ClassVar[list[str]] = ['pattern']
    _method_names: typing.ClassVar[list[str]] = ['next', 'test']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.Capture'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CaptureDefConfig] = pydantic.Field(None)


class CaptureDefConfig(pydantic.BaseModel):
    next: typing.Optional[bool] = pydantic.Field(None, description='When multiple results are captured, move the iterator to the next result.\n:return: true if another capture is present, false otherwise')
    test: typing.Optional[list[CaptureDefTestParams]] = pydantic.Field(None, description='Test whether a target matches the provided pattern.\nEvery Matcher must implement this method.\nThis method will be invoked by the assertions framework. Do not call this method directly.')

class CaptureDefTestParams(pydantic.BaseModel):
    actual: typing.Any = pydantic.Field(..., description='-')
    return_config: typing.Optional[list[models.assertions.MatchResultDefConfig]] = pydantic.Field(None)
    ...


#  autogenerated from aws_cdk.assertions.Match
class MatchDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = ['absent', 'any_value', 'array_equals', 'array_with', 'exact', 'not_', 'object_equals', 'object_like', 'serialized_json', 'string_like_regexp']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.Match'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[MatchDefConfig] = pydantic.Field(None)


class MatchDefConfig(pydantic.BaseModel):
    absent: typing.Optional[list[MatchDefAbsentParams]] = pydantic.Field(None, description="Use this matcher in the place of a field's value, if the field must not be present.")
    any_value: typing.Optional[list[MatchDefAnyValueParams]] = pydantic.Field(None, description='Matches any non-null value at the target.')
    array_equals: typing.Optional[list[MatchDefArrayEqualsParams]] = pydantic.Field(None, description='Matches the specified pattern with the array found in the same relative path of the target.\nThe set of elements (or matchers) must match exactly and in order.')
    array_with: typing.Optional[list[MatchDefArrayWithParams]] = pydantic.Field(None, description='Matches the specified pattern with the array found in the same relative path of the target.\nThe set of elements (or matchers) must be in the same order as would be found.')
    exact: typing.Optional[list[MatchDefExactParams]] = pydantic.Field(None, description='Deep exact matching of the specified pattern to the target.')
    not_: typing.Optional[list[MatchDefNotParams]] = pydantic.Field(None, description='Matches any target which does NOT follow the specified pattern.')
    object_equals: typing.Optional[list[MatchDefObjectEqualsParams]] = pydantic.Field(None, description='Matches the specified pattern to an object found in the same relative path of the target.\nThe keys and their values (or matchers) must match exactly with the target.')
    object_like: typing.Optional[list[MatchDefObjectLikeParams]] = pydantic.Field(None, description='Matches the specified pattern to an object found in the same relative path of the target.\nThe keys and their values (or matchers) must be present in the target but the target can be a superset.')
    serialized_json: typing.Optional[list[MatchDefSerializedJsonParams]] = pydantic.Field(None, description='Matches any string-encoded JSON and applies the specified pattern after parsing it.')
    string_like_regexp: typing.Optional[list[MatchDefStringLikeRegexpParams]] = pydantic.Field(None, description='Matches targets according to a regular expression.')

class MatchDefAbsentParams(pydantic.BaseModel):
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefAnyValueParams(pydantic.BaseModel):
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefArrayEqualsParams(pydantic.BaseModel):
    pattern: typing.Sequence[typing.Any] = pydantic.Field(..., description='the pattern to match.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefArrayWithParams(pydantic.BaseModel):
    pattern: typing.Sequence[typing.Any] = pydantic.Field(..., description='the pattern to match.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefExactParams(pydantic.BaseModel):
    pattern: typing.Any = pydantic.Field(..., description='the pattern to match.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefNotParams(pydantic.BaseModel):
    pattern: typing.Any = pydantic.Field(..., description='the pattern to NOT match.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefObjectEqualsParams(pydantic.BaseModel):
    pattern: typing.Mapping[str, typing.Any] = pydantic.Field(..., description='the pattern to match.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefObjectLikeParams(pydantic.BaseModel):
    pattern: typing.Mapping[str, typing.Any] = pydantic.Field(..., description='the pattern to match.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefSerializedJsonParams(pydantic.BaseModel):
    pattern: typing.Any = pydantic.Field(..., description='the pattern to match after parsing the encoded JSON.')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...

class MatchDefStringLikeRegexpParams(pydantic.BaseModel):
    pattern: str = pydantic.Field(..., description='-')
    return_config: typing.Optional[list[models.assertions.MatcherDefConfig]] = pydantic.Field(None)
    ...


#  autogenerated from aws_cdk.assertions.Matcher
class MatcherDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = ['test']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.Matcher'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[MatcherDefConfig] = pydantic.Field(None)


class MatcherDefConfig(pydantic.BaseModel):
    test: typing.Optional[list[MatcherDefTestParams]] = pydantic.Field(None, description='Test whether a target matches the provided pattern.\nEvery Matcher must implement this method.\nThis method will be invoked by the assertions framework. Do not call this method directly.')

class MatcherDefTestParams(pydantic.BaseModel):
    actual: typing.Any = pydantic.Field(..., description='the target to match.\n')
    return_config: typing.Optional[list[models.assertions.MatchResultDefConfig]] = pydantic.Field(None)
    ...


#  autogenerated from aws_cdk.assertions.MatchResult
class MatchResultDef(BaseClass):
    target: typing.Any = pydantic.Field(..., description='-')
    _init_params: typing.ClassVar[list[str]] = ['target']
    _method_names: typing.ClassVar[list[str]] = ['compose', 'finished', 'has_failed', 'push', 'record_capture', 'record_failure', 'render_mismatch']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.MatchResult'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[MatchResultDefConfig] = pydantic.Field(None)


class MatchResultDefConfig(pydantic.BaseModel):
    compose: typing.Optional[list[MatchResultDefComposeParams]] = pydantic.Field(None, description='Compose the results of a previous match as a subtree.')
    finished: typing.Optional[list[MatchResultDefFinishedParams]] = pydantic.Field(None, description='Prepare the result to be analyzed.\nThis API *must* be called prior to analyzing these results.')
    has_failed: typing.Optional[bool] = pydantic.Field(None, description='Does the result contain any failures.\nIf not, the result is a success')
    push: typing.Optional[list[MatchResultDefPushParams]] = pydantic.Field(None, description='(deprecated) DEPRECATED.')
    record_capture: typing.Optional[list[MatchResultDefRecordCaptureParams]] = pydantic.Field(None, description='Record a capture against in this match result.')
    record_failure: typing.Optional[list[MatchResultDefRecordFailureParams]] = pydantic.Field(None, description='Record a new failure into this result at a specific path.')
    render_mismatch: typing.Optional[bool] = pydantic.Field(None, description='Do a deep render of the match result, showing the structure mismatches in context.')

class MatchResultDefComposeParams(pydantic.BaseModel):
    id: str = pydantic.Field(..., description='the id of the parent tree.\n')
    inner: models.assertions.MatchResultDef = pydantic.Field(..., description='-')
    return_config: typing.Optional[list[models.assertions.MatchResultDefConfig]] = pydantic.Field(None)
    ...

class MatchResultDefFinishedParams(pydantic.BaseModel):
    return_config: typing.Optional[list[models.assertions.MatchResultDefConfig]] = pydantic.Field(None)
    ...

class MatchResultDefPushParams(pydantic.BaseModel):
    matcher: models.assertions.MatcherDef = pydantic.Field(..., description='-\n')
    path: typing.Sequence[str] = pydantic.Field(..., description='-\n')
    message: str = pydantic.Field(..., description='-\n\n:deprecated: use recordFailure()\n\n:stability: deprecated\n')
    return_config: typing.Optional[list[models.assertions.MatchResultDefConfig]] = pydantic.Field(None)
    ...

class MatchResultDefRecordCaptureParams(pydantic.BaseModel):
    capture: models.assertions.CaptureDef = pydantic.Field(..., description='The instance of Capture class to which this capture is associated with.\n')
    value: typing.Any = pydantic.Field(..., description='The value that was captured.')
    ...

class MatchResultDefRecordFailureParams(pydantic.BaseModel):
    matcher: models.assertions.MatcherDef = pydantic.Field(..., description='The matcher that had the failure.\n')
    message: str = pydantic.Field(..., description='Failure message.\n')
    path: typing.Sequence[str] = pydantic.Field(..., description="The relative path in the target where the failure occurred. If the failure occurred at root of the match tree, set the path to an empty list. If it occurs in the 5th index of an array nested within the 'foo' key of an object, set the path as ``['/foo', '[5]']``.\n")
    cost: typing.Union[int, float, None] = pydantic.Field(None, description='The cost of this particular mismatch. Default: 1')
    return_config: typing.Optional[list[models.assertions.MatchResultDefConfig]] = pydantic.Field(None)
    ...


#  autogenerated from aws_cdk.assertions.Template
class TemplateDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = ['all_resources', 'all_resources_properties', 'find_conditions', 'find_mappings', 'find_outputs', 'find_parameters', 'find_resources', 'has_condition', 'has_mapping', 'has_output', 'has_parameter', 'has_resource', 'has_resource_properties', 'resource_count_is', 'resource_properties_count_is', 'template_matches']
    _classmethod_names: typing.ClassVar[list[str]] = ['from_json', 'from_stack', 'from_string']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.Template'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[TemplateDefConfig] = pydantic.Field(None)


class TemplateDefConfig(pydantic.BaseModel):
    all_resources: typing.Optional[list[TemplateDefAllResourcesParams]] = pydantic.Field(None, description='Assert that all resources of the given type contain the given definition in the CloudFormation template.\nBy default, performs partial matching on the resource, via the ``Match.objectLike()``.\nTo configure different behavior, use other matchers in the ``Match`` class.')
    all_resources_properties: typing.Optional[list[TemplateDefAllResourcesPropertiesParams]] = pydantic.Field(None, description='Assert that all resources of the given type contain the given properties CloudFormation template.\nBy default, performs partial matching on the ``Properties`` key of the resource, via the\n``Match.objectLike()``. To configure different behavior, use other matchers in the ``Match`` class.')
    find_conditions: typing.Optional[list[TemplateDefFindConditionsParams]] = pydantic.Field(None, description='Get the set of matching Conditions that match the given properties in the CloudFormation template.')
    find_mappings: typing.Optional[list[TemplateDefFindMappingsParams]] = pydantic.Field(None, description='Get the set of matching Mappings that match the given properties in the CloudFormation template.')
    find_outputs: typing.Optional[list[TemplateDefFindOutputsParams]] = pydantic.Field(None, description='Get the set of matching Outputs that match the given properties in the CloudFormation template.')
    find_parameters: typing.Optional[list[TemplateDefFindParametersParams]] = pydantic.Field(None, description='Get the set of matching Parameters that match the given properties in the CloudFormation template.')
    find_resources: typing.Optional[list[TemplateDefFindResourcesParams]] = pydantic.Field(None, description='Get the set of matching resources of a given type and properties in the CloudFormation template.')
    from_json: typing.Optional[list[TemplateDefFromJsonParams]] = pydantic.Field(None, description='Base your assertions from an existing CloudFormation template formatted as an in-memory JSON object.')
    from_stack: typing.Optional[list[TemplateDefFromStackParams]] = pydantic.Field(None, description='Base your assertions on the CloudFormation template synthesized by a CDK ``Stack``.')
    from_string: typing.Optional[list[TemplateDefFromStringParams]] = pydantic.Field(None, description='Base your assertions from an existing CloudFormation template formatted as a JSON string.')
    has_condition: typing.Optional[list[TemplateDefHasConditionParams]] = pydantic.Field(None, description='Assert that a Condition with the given properties exists in the CloudFormation template.\nBy default, performs partial matching on the resource, via the ``Match.objectLike()``.\nTo configure different behavior, use other matchers in the ``Match`` class.')
    has_mapping: typing.Optional[list[TemplateDefHasMappingParams]] = pydantic.Field(None, description='Assert that a Mapping with the given properties exists in the CloudFormation template.\nBy default, performs partial matching on the resource, via the ``Match.objectLike()``.\nTo configure different behavior, use other matchers in the ``Match`` class.')
    has_output: typing.Optional[list[TemplateDefHasOutputParams]] = pydantic.Field(None, description='Assert that an Output with the given properties exists in the CloudFormation template.\nBy default, performs partial matching on the resource, via the ``Match.objectLike()``.\nTo configure different behavior, use other matchers in the ``Match`` class.')
    has_parameter: typing.Optional[list[TemplateDefHasParameterParams]] = pydantic.Field(None, description='Assert that a Parameter with the given properties exists in the CloudFormation template.\nBy default, performs partial matching on the parameter, via the ``Match.objectLike()``.\nTo configure different behavior, use other matchers in the ``Match`` class.')
    has_resource: typing.Optional[list[TemplateDefHasResourceParams]] = pydantic.Field(None, description='Assert that a resource of the given type and given definition exists in the CloudFormation template.\nBy default, performs partial matching on the resource, via the ``Match.objectLike()``.\nTo configure different behavior, use other matchers in the ``Match`` class.')
    has_resource_properties: typing.Optional[list[TemplateDefHasResourcePropertiesParams]] = pydantic.Field(None, description='Assert that a resource of the given type and properties exists in the CloudFormation template.\nBy default, performs partial matching on the ``Properties`` key of the resource, via the\n``Match.objectLike()``. To configure different behavior, use other matchers in the ``Match`` class.')
    resource_count_is: typing.Optional[list[TemplateDefResourceCountIsParams]] = pydantic.Field(None, description='Assert that the given number of resources of the given type exist in the template.')
    resource_properties_count_is: typing.Optional[list[TemplateDefResourcePropertiesCountIsParams]] = pydantic.Field(None, description='Assert that the given number of resources of the given type and properties exists in the CloudFormation template.')
    template_matches: typing.Optional[list[TemplateDefTemplateMatchesParams]] = pydantic.Field(None, description='Assert that the CloudFormation template matches the given value.')

class TemplateDefAllResourcesParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the resource type; ex: ``AWS::S3::Bucket``\n')
    props: typing.Any = pydantic.Field(..., description='the entire definition of the resources as they should be expected in the template.')
    ...

class TemplateDefAllResourcesPropertiesParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the resource type; ex: ``AWS::S3::Bucket``\n')
    props: typing.Any = pydantic.Field(..., description="the 'Properties' section of the resource as should be expected in the template.")
    ...

class TemplateDefFindConditionsParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the condition. Provide ``'*'`` to match all conditions in the template.\n")
    props: typing.Any = pydantic.Field(None, description='by default, matches all Conditions in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.')
    ...

class TemplateDefFindMappingsParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the mapping. Provide ``'*'`` to match all mappings in the template.\n")
    props: typing.Any = pydantic.Field(None, description='by default, matches all Mappings in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.')
    ...

class TemplateDefFindOutputsParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the output. Provide ``'*'`` to match all outputs in the template.\n")
    props: typing.Any = pydantic.Field(None, description='by default, matches all Outputs in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.')
    ...

class TemplateDefFindParametersParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the parameter. Provide ``'*'`` to match all parameters in the template.\n")
    props: typing.Any = pydantic.Field(None, description='by default, matches all Parameters in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.')
    ...

class TemplateDefFindResourcesParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the type to match in the CloudFormation template.\n')
    props: typing.Any = pydantic.Field(None, description='by default, matches all resources with the given type. When a literal is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.')
    ...

class TemplateDefFromJsonParams(pydantic.BaseModel):
    template: typing.Mapping[str, typing.Any] = pydantic.Field(..., description='the CloudFormation template formatted as a nested set of records.\n')
    skip_cyclical_dependencies_check: typing.Optional[bool] = pydantic.Field(None, description='If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false')
    return_config: typing.Optional[list[models.assertions.TemplateDefConfig]] = pydantic.Field(None)
    ...

class TemplateDefFromStackParams(pydantic.BaseModel):
    stack: models.StackDef = pydantic.Field(..., description='the CDK Stack to run assertions on.\n')
    skip_cyclical_dependencies_check: typing.Optional[bool] = pydantic.Field(None, description='If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false')
    return_config: typing.Optional[list[models.assertions.TemplateDefConfig]] = pydantic.Field(None)
    ...

class TemplateDefFromStringParams(pydantic.BaseModel):
    template: str = pydantic.Field(..., description='the CloudFormation template in.\n')
    skip_cyclical_dependencies_check: typing.Optional[bool] = pydantic.Field(None, description='If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false')
    return_config: typing.Optional[list[models.assertions.TemplateDefConfig]] = pydantic.Field(None)
    ...

class TemplateDefHasConditionParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the mapping. Provide ``'*'`` to match all conditions in the template.\n")
    props: typing.Any = pydantic.Field(..., description='the output as should be expected in the template.')
    ...

class TemplateDefHasMappingParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the mapping. Provide ``'*'`` to match all mappings in the template.\n")
    props: typing.Any = pydantic.Field(..., description='the output as should be expected in the template.')
    ...

class TemplateDefHasOutputParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the output. Provide ``'*'`` to match all outputs in the template.\n")
    props: typing.Any = pydantic.Field(..., description='the output as should be expected in the template.')
    ...

class TemplateDefHasParameterParams(pydantic.BaseModel):
    logical_id: str = pydantic.Field(..., description="the name of the parameter. Provide ``'*'`` to match all parameters in the template.\n")
    props: typing.Any = pydantic.Field(..., description='the parameter as should be expected in the template.')
    ...

class TemplateDefHasResourceParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the resource type; ex: ``AWS::S3::Bucket``\n')
    props: typing.Any = pydantic.Field(..., description='the entire definition of the resource as should be expected in the template.')
    ...

class TemplateDefHasResourcePropertiesParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the resource type; ex: ``AWS::S3::Bucket``\n')
    props: typing.Any = pydantic.Field(..., description="the 'Properties' section of the resource as should be expected in the template.")
    ...

class TemplateDefResourceCountIsParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the resource type; ex: ``AWS::S3::Bucket``\n')
    count: typing.Union[int, float] = pydantic.Field(..., description='number of expected instances.')
    ...

class TemplateDefResourcePropertiesCountIsParams(pydantic.BaseModel):
    type: str = pydantic.Field(..., description='the resource type; ex: ``AWS::S3::Bucket``\n')
    props: typing.Any = pydantic.Field(..., description="the 'Properties' section of the resource as should be expected in the template.\n")
    count: typing.Union[int, float] = pydantic.Field(..., description='number of expected instances.')
    ...

class TemplateDefTemplateMatchesParams(pydantic.BaseModel):
    expected: typing.Any = pydantic.Field(..., description='the expected CloudFormation template as key-value pairs.')
    ...


#  autogenerated from aws_cdk.assertions.MatchCapture
class MatchCaptureDef(BaseStruct):
    capture: models.assertions.CaptureDef = pydantic.Field(..., description='The instance of Capture class to which this capture is associated with.\n')
    value: typing.Any = pydantic.Field(..., description='The value that was captured.\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import assertions\n\n    # capture: assertions.Capture\n    # value: Any\n\n    match_capture = assertions.MatchCapture(\n        capture=capture,\n        value=value\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['capture', 'value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.MatchCapture'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.assertions.MatchFailure
class MatchFailureDef(BaseStruct):
    matcher: models.assertions.MatcherDef = pydantic.Field(..., description='The matcher that had the failure.\n')
    message: str = pydantic.Field(..., description='Failure message.\n')
    path: typing.Sequence[str] = pydantic.Field(..., description="The relative path in the target where the failure occurred. If the failure occurred at root of the match tree, set the path to an empty list. If it occurs in the 5th index of an array nested within the 'foo' key of an object, set the path as ``['/foo', '[5]']``.\n")
    cost: typing.Union[int, float, None] = pydantic.Field(None, description='The cost of this particular mismatch. Default: 1\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import assertions\n\n    # matcher: assertions.Matcher\n\n    match_failure = assertions.MatchFailure(\n        matcher=matcher,\n        message="message",\n        path=["path"],\n\n        # the properties below are optional\n        cost=123\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['matcher', 'message', 'path', 'cost']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.MatchFailure'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.assertions.TemplateParsingOptions
class TemplateParsingOptionsDef(BaseStruct):
    skip_cyclical_dependencies_check: typing.Optional[bool] = pydantic.Field(None, description='If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import assertions\n\n    template_parsing_options = assertions.TemplateParsingOptions(\n        skip_cyclical_dependencies_check=False\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['skip_cyclical_dependencies_check']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.assertions.TemplateParsingOptions'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    Annotations: typing.Optional[dict[str, AnnotationsDef]] = pydantic.Field(None)
    Capture: typing.Optional[dict[str, CaptureDef]] = pydantic.Field(None)
    Match: typing.Optional[dict[str, MatchDef]] = pydantic.Field(None)
    Matcher: typing.Optional[dict[str, MatcherDef]] = pydantic.Field(None)
    MatchResult: typing.Optional[dict[str, MatchResultDef]] = pydantic.Field(None)
    Template: typing.Optional[dict[str, TemplateDef]] = pydantic.Field(None)
    MatchCapture: typing.Optional[dict[str, MatchCaptureDef]] = pydantic.Field(None)
    MatchFailure: typing.Optional[dict[str, MatchFailureDef]] = pydantic.Field(None)
    TemplateParsingOptions: typing.Optional[dict[str, TemplateParsingOptionsDef]] = pydantic.Field(None)
    ...
