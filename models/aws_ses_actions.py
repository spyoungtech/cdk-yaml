from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_ses_actions.AddHeader
class AddHeaderDef(BaseClass):
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.')
    value: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\\r" or "\\n").')
    _init_params: typing.ClassVar[list[str]] = ['name', 'value']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.AddHeader'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[AddHeaderDefConfig] = pydantic.Field(None)


class AddHeaderDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[AddHeaderDefBindParams]] = pydantic.Field(None, description='Returns the receipt rule action specification.')

class AddHeaderDefBindParams(pydantic.BaseModel):
    _rule: typing.Union[models.aws_ses.ReceiptRuleDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_ses_actions.Bounce
class BounceDef(BaseClass):
    sender: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.')
    template: typing.Union[models.aws_ses_actions.BounceTemplateDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The template containing the message, reply code and status code.\n')
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the bounce action is taken. Default: no notification')
    _init_params: typing.ClassVar[list[str]] = ['sender', 'template', 'topic']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.Bounce'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[BounceDefConfig] = pydantic.Field(None)


class BounceDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[BounceDefBindParams]] = pydantic.Field(None, description='Returns the receipt rule action specification.')

class BounceDefBindParams(pydantic.BaseModel):
    _rule: typing.Union[models.aws_ses.ReceiptRuleDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_ses_actions.BounceTemplate
class BounceTemplateDef(BaseClass):
    message: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Human-readable text to include in the bounce message.')
    smtp_reply_code: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The SMTP reply code, as defined by RFC 5321.\n')
    status_code: typing.Optional[str] = pydantic.Field(None, description='The SMTP enhanced status code, as defined by RFC 3463.')
    _init_params: typing.ClassVar[list[str]] = ['message', 'smtp_reply_code', 'status_code']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.BounceTemplate'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_ses_actions.Lambda
class LambdaDef(BaseClass):
    function: typing.Union[_REQUIRED_INIT_PARAM, models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Lambda function to invoke.')
    invocation_type: typing.Optional[aws_cdk.aws_ses_actions.LambdaInvocationType] = pydantic.Field(None, description='The invocation type of the Lambda function. Default: Event\n')
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the Lambda action is taken. Default: no notification')
    _init_params: typing.ClassVar[list[str]] = ['function', 'invocation_type', 'topic']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.Lambda'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[LambdaDefConfig] = pydantic.Field(None)


class LambdaDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[LambdaDefBindParams]] = pydantic.Field(None, description='Returns the receipt rule action specification.')

class LambdaDefBindParams(pydantic.BaseModel):
    rule: typing.Union[models.aws_ses.ReceiptRuleDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_ses_actions.S3
class S3Def(BaseClass):
    bucket: typing.Union[models.aws_s3.BucketDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The S3 bucket that incoming email will be saved to.')
    kms_key: typing.Optional[typing.Union[models.aws_kms.KeyDef]] = pydantic.Field(None, description='The master key that SES should use to encrypt your emails before saving them to the S3 bucket. Default: no encryption\n')
    object_key_prefix: typing.Optional[str] = pydantic.Field(None, description='The key prefix of the S3 bucket. Default: no prefix\n')
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the S3 action is taken. Default: no notification')
    _init_params: typing.ClassVar[list[str]] = ['bucket', 'kms_key', 'object_key_prefix', 'topic']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.S3'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[S3DefConfig] = pydantic.Field(None)


class S3DefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[S3DefBindParams]] = pydantic.Field(None, description='Returns the receipt rule action specification.')

class S3DefBindParams(pydantic.BaseModel):
    rule: typing.Union[models.aws_ses.ReceiptRuleDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_ses_actions.Sns
class SnsDef(BaseClass):
    topic: typing.Union[_REQUIRED_INIT_PARAM, models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='The SNS topic to notify.')
    encoding: typing.Optional[aws_cdk.aws_ses_actions.EmailEncoding] = pydantic.Field(None, description='The encoding to use for the email within the Amazon SNS notification. Default: UTF-8')
    _init_params: typing.ClassVar[list[str]] = ['topic', 'encoding']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.Sns'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[SnsDefConfig] = pydantic.Field(None)


class SnsDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[SnsDefBindParams]] = pydantic.Field(None, description='Returns the receipt rule action specification.')

class SnsDefBindParams(pydantic.BaseModel):
    _rule: typing.Union[models.aws_ses.ReceiptRuleDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_ses_actions.Stop
class StopDef(BaseClass):
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the stop action is taken.')
    _init_params: typing.ClassVar[list[str]] = ['topic']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.Stop'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[StopDefConfig] = pydantic.Field(None)


class StopDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[StopDefBindParams]] = pydantic.Field(None, description='Returns the receipt rule action specification.')

class StopDefBindParams(pydantic.BaseModel):
    _rule: typing.Union[models.aws_ses.ReceiptRuleDef] = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.aws_ses_actions.AddHeaderProps
class AddHeaderPropsDef(BaseStruct):
    name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.\n')
    value: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\\r" or "\\n").\n\n:exampleMetadata: infused\n\nExample::\n\n    import aws_cdk.aws_s3 as s3\n    import aws_cdk.aws_ses_actions as actions\n\n\n    bucket = s3.Bucket(self, "Bucket")\n    topic = sns.Topic(self, "Topic")\n\n    ses.ReceiptRuleSet(self, "RuleSet",\n        rules=[ses.ReceiptRuleOptions(\n            recipients=["hello@aws.com"],\n            actions=[\n                actions.AddHeader(\n                    name="X-Special-Header",\n                    value="aws"\n                ),\n                actions.S3(\n                    bucket=bucket,\n                    object_key_prefix="emails/",\n                    topic=topic\n                )\n            ]\n        ), ses.ReceiptRuleOptions(\n            recipients=["aws.com"],\n            actions=[\n                actions.Sns(\n                    topic=topic\n                )\n            ]\n        )\n        ]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['name', 'value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.AddHeaderProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_ses_actions.BounceProps
class BouncePropsDef(BaseStruct):
    sender: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.\n')
    template: typing.Union[models.aws_ses_actions.BounceTemplateDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The template containing the message, reply code and status code.\n')
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the bounce action is taken. Default: no notification\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_ses_actions as ses_actions\n    from aws_cdk import aws_sns as sns\n\n    # bounce_template: ses_actions.BounceTemplate\n    # topic: sns.Topic\n\n    bounce_props = ses_actions.BounceProps(\n        sender="sender",\n        template=bounce_template,\n\n        # the properties below are optional\n        topic=topic\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['sender', 'template', 'topic']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.BounceProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_ses_actions.BounceTemplateProps
class BounceTemplatePropsDef(BaseStruct):
    message: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='Human-readable text to include in the bounce message.\n')
    smtp_reply_code: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The SMTP reply code, as defined by RFC 5321.\n')
    status_code: typing.Optional[str] = pydantic.Field(None, description='The SMTP enhanced status code, as defined by RFC 3463.\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_ses_actions as ses_actions\n\n    bounce_template_props = ses_actions.BounceTemplateProps(\n        message="message",\n        smtp_reply_code="smtpReplyCode",\n\n        # the properties below are optional\n        status_code="statusCode"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['message', 'smtp_reply_code', 'status_code']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.BounceTemplateProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_ses_actions.LambdaProps
class LambdaPropsDef(BaseStruct):
    function: typing.Union[_REQUIRED_INIT_PARAM, models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Lambda function to invoke.\n')
    invocation_type: typing.Optional[aws_cdk.aws_ses_actions.LambdaInvocationType] = pydantic.Field(None, description='The invocation type of the Lambda function. Default: Event\n')
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the Lambda action is taken. Default: no notification\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_lambda as lambda_\n    from aws_cdk import aws_ses_actions as ses_actions\n    from aws_cdk import aws_sns as sns\n\n    # function_: lambda.Function\n    # topic: sns.Topic\n\n    lambda_props = ses_actions.LambdaProps(\n        function=function_,\n\n        # the properties below are optional\n        invocation_type=ses_actions.LambdaInvocationType.EVENT,\n        topic=topic\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['function', 'invocation_type', 'topic']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.LambdaProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[LambdaPropsDefConfig] = pydantic.Field(None)


class LambdaPropsDefConfig(pydantic.BaseModel):
    function_config: typing.Optional[models._interface_methods.AwsLambdaIFunctionDefConfig] = pydantic.Field(None)


#  autogenerated from aws_cdk.aws_ses_actions.S3Props
class S3PropsDef(BaseStruct):
    bucket: typing.Union[models.aws_s3.BucketDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The S3 bucket that incoming email will be saved to.\n')
    kms_key: typing.Optional[typing.Union[models.aws_kms.KeyDef]] = pydantic.Field(None, description='The master key that SES should use to encrypt your emails before saving them to the S3 bucket. Default: no encryption\n')
    object_key_prefix: typing.Optional[str] = pydantic.Field(None, description='The key prefix of the S3 bucket. Default: no prefix\n')
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the S3 action is taken. Default: no notification\n\n:exampleMetadata: infused\n\nExample::\n\n    import aws_cdk.aws_s3 as s3\n    import aws_cdk.aws_ses_actions as actions\n\n\n    bucket = s3.Bucket(self, "Bucket")\n    topic = sns.Topic(self, "Topic")\n\n    ses.ReceiptRuleSet(self, "RuleSet",\n        rules=[ses.ReceiptRuleOptions(\n            recipients=["hello@aws.com"],\n            actions=[\n                actions.AddHeader(\n                    name="X-Special-Header",\n                    value="aws"\n                ),\n                actions.S3(\n                    bucket=bucket,\n                    object_key_prefix="emails/",\n                    topic=topic\n                )\n            ]\n        ), ses.ReceiptRuleOptions(\n            recipients=["aws.com"],\n            actions=[\n                actions.Sns(\n                    topic=topic\n                )\n            ]\n        )\n        ]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['bucket', 'kms_key', 'object_key_prefix', 'topic']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.S3Props'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[S3PropsDefConfig] = pydantic.Field(None)


class S3PropsDefConfig(pydantic.BaseModel):
    bucket_config: typing.Optional[models._interface_methods.AwsS3IBucketDefConfig] = pydantic.Field(None)


#  autogenerated from aws_cdk.aws_ses_actions.SnsProps
class SnsPropsDef(BaseStruct):
    topic: typing.Union[_REQUIRED_INIT_PARAM, models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='The SNS topic to notify.\n')
    encoding: typing.Optional[aws_cdk.aws_ses_actions.EmailEncoding] = pydantic.Field(None, description='The encoding to use for the email within the Amazon SNS notification. Default: UTF-8\n\n:exampleMetadata: infused\n\nExample::\n\n    import aws_cdk.aws_s3 as s3\n    import aws_cdk.aws_ses_actions as actions\n\n\n    bucket = s3.Bucket(self, "Bucket")\n    topic = sns.Topic(self, "Topic")\n\n    ses.ReceiptRuleSet(self, "RuleSet",\n        rules=[ses.ReceiptRuleOptions(\n            recipients=["hello@aws.com"],\n            actions=[\n                actions.AddHeader(\n                    name="X-Special-Header",\n                    value="aws"\n                ),\n                actions.S3(\n                    bucket=bucket,\n                    object_key_prefix="emails/",\n                    topic=topic\n                )\n            ]\n        ), ses.ReceiptRuleOptions(\n            recipients=["aws.com"],\n            actions=[\n                actions.Sns(\n                    topic=topic\n                )\n            ]\n        )\n        ]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['topic', 'encoding']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.SnsProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[SnsPropsDefConfig] = pydantic.Field(None)


class SnsPropsDefConfig(pydantic.BaseModel):
    topic_config: typing.Optional[models._interface_methods.AwsSnsITopicDefConfig] = pydantic.Field(None)


#  autogenerated from aws_cdk.aws_ses_actions.StopProps
class StopPropsDef(BaseStruct):
    topic: typing.Optional[typing.Union[models.aws_sns.TopicBaseDef, models.aws_sns.TopicDef]] = pydantic.Field(None, description='The SNS topic to notify when the stop action is taken.\n\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_ses_actions as ses_actions\n    from aws_cdk import aws_sns as sns\n\n    # topic: sns.Topic\n\n    stop_props = ses_actions.StopProps(\n        topic=topic\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['topic']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_ses_actions.StopProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_ses_actions.EmailEncoding
# skipping emum

#  autogenerated from aws_cdk.aws_ses_actions.LambdaInvocationType
# skipping emum

import models

class ModuleModel(pydantic.BaseModel):
    AddHeader: typing.Optional[dict[str, AddHeaderDef]] = pydantic.Field(None)
    Bounce: typing.Optional[dict[str, BounceDef]] = pydantic.Field(None)
    BounceTemplate: typing.Optional[dict[str, BounceTemplateDef]] = pydantic.Field(None)
    Lambda: typing.Optional[dict[str, LambdaDef]] = pydantic.Field(None)
    S3: typing.Optional[dict[str, S3Def]] = pydantic.Field(None)
    Sns: typing.Optional[dict[str, SnsDef]] = pydantic.Field(None)
    Stop: typing.Optional[dict[str, StopDef]] = pydantic.Field(None)
    AddHeaderProps: typing.Optional[dict[str, AddHeaderPropsDef]] = pydantic.Field(None)
    BounceProps: typing.Optional[dict[str, BouncePropsDef]] = pydantic.Field(None)
    BounceTemplateProps: typing.Optional[dict[str, BounceTemplatePropsDef]] = pydantic.Field(None)
    LambdaProps: typing.Optional[dict[str, LambdaPropsDef]] = pydantic.Field(None)
    S3Props: typing.Optional[dict[str, S3PropsDef]] = pydantic.Field(None)
    SnsProps: typing.Optional[dict[str, SnsPropsDef]] = pydantic.Field(None)
    StopProps: typing.Optional[dict[str, StopPropsDef]] = pydantic.Field(None)
    ...
