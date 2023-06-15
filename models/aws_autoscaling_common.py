from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams

#  autogenerated from aws_cdk.aws_autoscaling_common.Alarms
class AlarmsDef(BaseStruct):
    lower_alarm_interval_index: typing.Union[int, float, None] = pydantic.Field(None, description='')
    upper_alarm_interval_index: typing.Union[int, float, None] = pydantic.Field(None, description='')
    _init_params: typing.ClassVar[list[str]] = ['lower_alarm_interval_index', 'upper_alarm_interval_index']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_autoscaling_common.Alarms'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_autoscaling_common.ArbitraryIntervals
class ArbitraryIntervalsDef(BaseStruct):
    absolute: bool = pydantic.Field(..., description='')
    intervals: typing.Sequence[typing.Union[models.aws_autoscaling_common.ScalingIntervalDef, dict[str, typing.Any]]] = pydantic.Field(..., description='')
    _init_params: typing.ClassVar[list[str]] = ['absolute', 'intervals']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_autoscaling_common.ArbitraryIntervals'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_autoscaling_common.CompleteScalingInterval
class CompleteScalingIntervalDef(BaseStruct):
    lower: typing.Union[int, float] = pydantic.Field(..., description='')
    upper: typing.Union[int, float] = pydantic.Field(..., description='')
    change: typing.Union[int, float, None] = pydantic.Field(None, description='')
    _init_params: typing.ClassVar[list[str]] = ['lower', 'upper', 'change']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_autoscaling_common.CompleteScalingInterval'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_autoscaling_common.ScalingInterval
class ScalingIntervalDef(BaseStruct):
    change: typing.Union[int, float] = pydantic.Field(..., description='The capacity adjustment to apply in this interval. The number is interpreted differently based on AdjustmentType: - ChangeInCapacity: add the adjustment to the current capacity. The number can be positive or negative. - PercentChangeInCapacity: add or remove the given percentage of the current capacity to itself. The number can be in the range [-100..100]. - ExactCapacity: set the capacity to this number. The number must be positive.\n')
    lower: typing.Union[int, float, None] = pydantic.Field(None, description='The lower bound of the interval. The scaling adjustment will be applied if the metric is higher than this value. Default: Threshold automatically derived from neighbouring intervals\n')
    upper: typing.Union[int, float, None] = pydantic.Field(None, description='The upper bound of the interval. The scaling adjustment will be applied if the metric is lower than this value. Default: Threshold automatically derived from neighbouring intervals\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_autoscaling_common as autoscaling_common\n\n    scaling_interval = autoscaling_common.ScalingInterval(\n        change=123,\n\n        # the properties below are optional\n        lower=123,\n        upper=123\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['change', 'lower', 'upper']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_autoscaling_common.ScalingInterval'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_autoscaling_common.IRandomGenerator
#  skipping Interface

import models

class ModuleModel(pydantic.BaseModel):
    Alarms: typing.Optional[dict[str, AlarmsDef]] = pydantic.Field(None)
    ArbitraryIntervals: typing.Optional[dict[str, ArbitraryIntervalsDef]] = pydantic.Field(None)
    CompleteScalingInterval: typing.Optional[dict[str, CompleteScalingIntervalDef]] = pydantic.Field(None)
    ScalingInterval: typing.Optional[dict[str, ScalingIntervalDef]] = pydantic.Field(None)
    ...
