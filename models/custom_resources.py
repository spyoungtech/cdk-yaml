from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.custom_resources.AwsCustomResourcePolicy
class AwsCustomResourcePolicyDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = ['from_sdk_calls', 'from_statements']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.AwsCustomResourcePolicy'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = ['from_sdk_calls', 'from_statements']
    ...


    from_sdk_calls: typing.Optional[AwsCustomResourcePolicyDefFromSdkCallsParams] = pydantic.Field(None, description="Generate IAM Policy Statements from the configured SDK calls.\nEach SDK call with be translated to an IAM Policy Statement in the form of: ``call.service:call.action`` (e.g ``s3:PutObject``).\n\nThis policy generator assumes the IAM policy name has the same name as the API\ncall. This is true in 99% of cases, but there are exceptions (for example,\nS3's ``PutBucketLifecycleConfiguration`` requires\n``s3:PutLifecycleConfiguration`` permissions, Lambda's ``Invoke`` requires\n``lambda:InvokeFunction`` permissions). Use ``fromStatements`` if you want to\ndo a call that requires different IAM action names.")
    from_statements: typing.Optional[AwsCustomResourcePolicyDefFromStatementsParams] = pydantic.Field(None, description='Explicit IAM Policy Statements.')

class AwsCustomResourcePolicyDefFromSdkCallsParams(pydantic.BaseModel):
    resources: typing.Sequence[str] = pydantic.Field(..., description="The resources that the calls will have access to. It is best to use specific resource ARN's when possible. However, you can also use ``AwsCustomResourcePolicy.ANY_RESOURCE`` to allow access to all resources. For example, when ``onCreate`` is used to create a resource which you don't know the physical name of in advance. Note that will apply to ALL SDK calls.")
    ...

class AwsCustomResourcePolicyDefFromStatementsParams(pydantic.BaseModel):
    statements: typing.Sequence[models.aws_iam.PolicyStatementDef] = pydantic.Field(..., description='the statements to propagate to the SDK calls.')
    ...


#  autogenerated from aws_cdk.custom_resources.PhysicalResourceId
class PhysicalResourceIdDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = ['from_response', 'of']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.PhysicalResourceId'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = ['from_response']
    ...


    from_response: typing.Optional[PhysicalResourceIdDefFromResponseParams] = pydantic.Field(None, description='Extract the physical resource id from the path (dot notation) to the data in the API call response.')
    resource_config: typing.Optional[PhysicalResourceIdDefConfig] = pydantic.Field(None)


class PhysicalResourceIdDefConfig(pydantic.BaseModel):
    of: typing.Optional[list[PhysicalResourceIdDefOfParams]] = pydantic.Field(None, description='Explicit physical resource id.')

class PhysicalResourceIdDefFromResponseParams(pydantic.BaseModel):
    response_path: str = pydantic.Field(..., description='-')
    ...

class PhysicalResourceIdDefOfParams(pydantic.BaseModel):
    id: str = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.custom_resources.PhysicalResourceIdReference
class PhysicalResourceIdReferenceDef(BaseClass):
    _init_params: typing.ClassVar[list[str]] = []
    _method_names: typing.ClassVar[list[str]] = ['resolve']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.PhysicalResourceIdReference'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[PhysicalResourceIdReferenceDefConfig] = pydantic.Field(None)


class PhysicalResourceIdReferenceDefConfig(pydantic.BaseModel):
    resolve: typing.Optional[list[PhysicalResourceIdReferenceDefResolveParams]] = pydantic.Field(None, description="Produce the Token's value at resolution time.")

class PhysicalResourceIdReferenceDefResolveParams(pydantic.BaseModel):
    _context: models.UnsupportedResource = pydantic.Field(..., description='-')
    ...


#  autogenerated from aws_cdk.custom_resources.AwsCustomResource
class AwsCustomResourceDef(BaseConstruct):
    function_name: typing.Optional[str] = pydantic.Field(None, description="A name for the singleton Lambda function implementing this custom resource. The function name will remain the same after the first AwsCustomResource is created in a stack. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.\n")
    install_latest_aws_sdk: typing.Optional[bool] = pydantic.Field(None, description="Whether to install the latest AWS SDK v2. If not specified, this uses whatever JavaScript SDK version is the default in AWS Lambda at the time of execution. Otherwise, installs the latest version from 'npmjs.com'. The installation takes around 60 seconds and requires internet connectivity. The default can be controlled using the context key ``@aws-cdk/customresources:installLatestAwsSdkDefault`` is. Default: - The value of ``@aws-cdk/customresources:installLatestAwsSdkDefault``, otherwise ``true``\n")
    log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = pydantic.Field(None, description='The number of days log events of the singleton Lambda function implementing this custom resource are kept in CloudWatch Logs. Default: logs.RetentionDays.INFINITE\n')
    on_create: typing.Union[models.custom_resources.AwsSdkCallDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The AWS SDK call to make when the resource is created. Default: - the call when the resource is updated\n')
    on_delete: typing.Union[models.custom_resources.AwsSdkCallDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The AWS SDK call to make when the resource is deleted. Default: - no call\n')
    on_update: typing.Union[models.custom_resources.AwsSdkCallDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The AWS SDK call to make when the resource is updated. Default: - no call\n')
    policy: typing.Optional[models.custom_resources.AwsCustomResourcePolicyDef] = pydantic.Field(None, description="The policy that will be added to the execution role of the Lambda function implementing this custom resource provider. The custom resource also implements ``iam.IGrantable``, making it possible to use the ``grantXxx()`` methods. As this custom resource uses a singleton Lambda function, it's important to note the that function's role will eventually accumulate the permissions/grants from all resources. Note that a policy must be specified if ``role`` is not provided, as by default a new role is created which requires policy changes to access resources. Default: - no policy added\n")
    removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy\n')
    resource_type: typing.Optional[str] = pydantic.Field(None, description='Cloudformation Resource type. Default: - Custom::AWS\n')
    role: typing.Optional[typing.Union[models.aws_iam.LazyRoleDef, models.aws_iam.RoleDef]] = pydantic.Field(None, description='The execution role for the singleton Lambda function implementing this custom resource provider. This role will apply to all ``AwsCustomResource`` instances in the stack. The role must be assumable by the ``lambda.amazonaws.com`` service principal. Default: - a new role is created\n')
    timeout: typing.Optional[models.DurationDef] = pydantic.Field(None, description='The timeout for the singleton Lambda function implementing this custom resource. Default: Duration.minutes(2)\n')
    vpc: typing.Optional[typing.Union[models.aws_ec2.VpcDef]] = pydantic.Field(None, description='The vpc to provision the lambda function in. Default: - the function is not provisioned inside a vpc.\n')
    vpc_subnets: typing.Union[models.aws_ec2.SubnetSelectionDef, dict[str, typing.Any], None] = pydantic.Field(None, description="Which subnets from the VPC to place the lambda function in. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified")
    _init_params: typing.ClassVar[list[str]] = ['function_name', 'install_latest_aws_sdk', 'log_retention', 'on_create', 'on_delete', 'on_update', 'policy', 'removal_policy', 'resource_type', 'role', 'timeout', 'vpc', 'vpc_subnets']
    _method_names: typing.ClassVar[list[str]] = ['get_response_field', 'get_response_field_reference']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.AwsCustomResource'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[AwsCustomResourceDefConfig] = pydantic.Field(None)


class AwsCustomResourceDefConfig(pydantic.BaseModel):
    get_response_field: typing.Optional[list[AwsCustomResourceDefGetResponseFieldParams]] = pydantic.Field(None, description="Returns response data for the AWS SDK call as string.\nExample for S3 / listBucket : 'Buckets.0.Name'\n\nNote that you cannot use this method if ``ignoreErrorCodesMatching``\nis configured for any of the SDK calls. This is because in such a case,\nthe response data might not exist, and will cause a CloudFormation deploy time error.")
    get_response_field_reference: typing.Optional[list[AwsCustomResourceDefGetResponseFieldReferenceParams]] = pydantic.Field(None, description="Returns response data for the AWS SDK call.\nExample for S3 / listBucket : 'Buckets.0.Name'\n\nUse ``Token.asXxx`` to encode the returned ``Reference`` as a specific type or\nuse the convenience ``getDataString`` for string attributes.\n\nNote that you cannot use this method if ``ignoreErrorCodesMatching``\nis configured for any of the SDK calls. This is because in such a case,\nthe response data might not exist, and will cause a CloudFormation deploy time error.")
    grant_principal_config: typing.Optional[models._interface_methods.AwsIamIPrincipalDefConfig] = pydantic.Field(None)

class AwsCustomResourceDefGetResponseFieldParams(pydantic.BaseModel):
    data_path: str = pydantic.Field(..., description='the path to the data.')
    ...

class AwsCustomResourceDefGetResponseFieldReferenceParams(pydantic.BaseModel):
    data_path: str = pydantic.Field(..., description='the path to the data.')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...


#  autogenerated from aws_cdk.custom_resources.Provider
class ProviderDef(BaseConstruct):
    on_event_handler: typing.Union[_REQUIRED_INIT_PARAM, models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='The AWS Lambda function to invoke for all resource lifecycle operations (CREATE/UPDATE/DELETE). This function is responsible to begin the requested resource operation (CREATE/UPDATE/DELETE) and return any additional properties to add to the event, which will later be passed to ``isComplete``. The ``PhysicalResourceId`` property must be included in the response.\n')
    is_complete_handler: typing.Optional[typing.Union[models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef]] = pydantic.Field(None, description='The AWS Lambda function to invoke in order to determine if the operation is complete. This function will be called immediately after ``onEvent`` and then periodically based on the configured query interval as long as it returns ``false``. If the function still returns ``false`` and the alloted timeout has passed, the operation will fail. Default: - provider is synchronous. This means that the ``onEvent`` handler is expected to finish all lifecycle operations within the initial invocation.\n')
    log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = pydantic.Field(None, description="The number of days framework log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE\n")
    provider_function_env_encryption: typing.Optional[typing.Union[models.aws_kms.KeyDef]] = pydantic.Field(None, description="AWS KMS key used to encrypt provider lambda's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK)\n")
    provider_function_name: typing.Optional[str] = pydantic.Field(None, description='Provider Lambda name. The provider lambda function name. Default: - CloudFormation default name from unique physical ID\n')
    query_interval: typing.Optional[models.DurationDef] = pydantic.Field(None, description='Time between calls to the ``isComplete`` handler which determines if the resource has been stabilized. The first ``isComplete`` will be called immediately after ``handler`` and then every ``queryInterval`` seconds, and until ``timeout`` has been reached or until ``isComplete`` returns ``true``. Default: Duration.seconds(5)\n')
    role: typing.Optional[typing.Union[models.aws_iam.LazyRoleDef, models.aws_iam.RoleDef]] = pydantic.Field(None, description="AWS Lambda execution role. The role that will be assumed by the AWS Lambda. Must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A default role will be created.\n")
    security_groups: typing.Optional[typing.Sequence[typing.Union[models.aws_ec2.SecurityGroupDef]]] = pydantic.Field(None, description="Security groups to attach to the provider functions. Only used if 'vpc' is supplied Default: - If ``vpc`` is not supplied, no security groups are attached. Otherwise, a dedicated security group is created for each function.\n")
    total_timeout: typing.Optional[models.DurationDef] = pydantic.Field(None, description='Total timeout for the entire operation. The maximum timeout is 1 hour (yes, it can exceed the AWS Lambda 15 minutes) Default: Duration.minutes(30)\n')
    vpc: typing.Optional[typing.Union[models.aws_ec2.VpcDef]] = pydantic.Field(None, description='The vpc to provision the lambda functions in. Default: - functions are not provisioned inside a vpc.\n')
    vpc_subnets: typing.Union[models.aws_ec2.SubnetSelectionDef, dict[str, typing.Any], None] = pydantic.Field(None, description="Which subnets from the VPC to place the lambda functions in. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified")
    _init_params: typing.ClassVar[list[str]] = ['on_event_handler', 'is_complete_handler', 'log_retention', 'provider_function_env_encryption', 'provider_function_name', 'query_interval', 'role', 'security_groups', 'total_timeout', 'vpc', 'vpc_subnets']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.Provider'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ProviderDefConfig] = pydantic.Field(None)


class ProviderDefConfig(pydantic.BaseModel):
    on_event_handler_config: typing.Optional[models._interface_methods.AwsLambdaIFunctionDefConfig] = pydantic.Field(None)


#  autogenerated from aws_cdk.custom_resources.AwsCustomResourceProps
class AwsCustomResourcePropsDef(BaseStruct):
    function_name: typing.Optional[str] = pydantic.Field(None, description="A name for the singleton Lambda function implementing this custom resource. The function name will remain the same after the first AwsCustomResource is created in a stack. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.\n")
    install_latest_aws_sdk: typing.Optional[bool] = pydantic.Field(None, description="Whether to install the latest AWS SDK v2. If not specified, this uses whatever JavaScript SDK version is the default in AWS Lambda at the time of execution. Otherwise, installs the latest version from 'npmjs.com'. The installation takes around 60 seconds and requires internet connectivity. The default can be controlled using the context key ``@aws-cdk/customresources:installLatestAwsSdkDefault`` is. Default: - The value of ``@aws-cdk/customresources:installLatestAwsSdkDefault``, otherwise ``true``\n")
    log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = pydantic.Field(None, description='The number of days log events of the singleton Lambda function implementing this custom resource are kept in CloudWatch Logs. Default: logs.RetentionDays.INFINITE\n')
    on_create: typing.Union[models.custom_resources.AwsSdkCallDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The AWS SDK call to make when the resource is created. Default: - the call when the resource is updated\n')
    on_delete: typing.Union[models.custom_resources.AwsSdkCallDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The AWS SDK call to make when the resource is deleted. Default: - no call\n')
    on_update: typing.Union[models.custom_resources.AwsSdkCallDef, dict[str, typing.Any], None] = pydantic.Field(None, description='The AWS SDK call to make when the resource is updated. Default: - no call\n')
    policy: typing.Optional[models.custom_resources.AwsCustomResourcePolicyDef] = pydantic.Field(None, description="The policy that will be added to the execution role of the Lambda function implementing this custom resource provider. The custom resource also implements ``iam.IGrantable``, making it possible to use the ``grantXxx()`` methods. As this custom resource uses a singleton Lambda function, it's important to note the that function's role will eventually accumulate the permissions/grants from all resources. Note that a policy must be specified if ``role`` is not provided, as by default a new role is created which requires policy changes to access resources. Default: - no policy added\n")
    removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy\n')
    resource_type: typing.Optional[str] = pydantic.Field(None, description='Cloudformation Resource type. Default: - Custom::AWS\n')
    role: typing.Optional[typing.Union[models.aws_iam.LazyRoleDef, models.aws_iam.RoleDef]] = pydantic.Field(None, description='The execution role for the singleton Lambda function implementing this custom resource provider. This role will apply to all ``AwsCustomResource`` instances in the stack. The role must be assumable by the ``lambda.amazonaws.com`` service principal. Default: - a new role is created\n')
    timeout: typing.Optional[models.DurationDef] = pydantic.Field(None, description='The timeout for the singleton Lambda function implementing this custom resource. Default: Duration.minutes(2)\n')
    vpc: typing.Optional[typing.Union[models.aws_ec2.VpcDef]] = pydantic.Field(None, description='The vpc to provision the lambda function in. Default: - the function is not provisioned inside a vpc.\n')
    vpc_subnets: typing.Union[models.aws_ec2.SubnetSelectionDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Which subnets from the VPC to place the lambda function in. Only used if \'vpc\' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified\n\n:exampleMetadata: infused\n\nExample::\n\n    get_parameter = cr.AwsCustomResource(self, "AssociateVPCWithHostedZone",\n        on_create=cr.AwsSdkCall(\n            assumed_role_arn="arn:aws:iam::OTHERACCOUNT:role/CrossAccount/ManageHostedZoneConnections",\n            service="Route53",\n            action="AssociateVPCWithHostedZone",\n            parameters={\n                "HostedZoneId": "hz-123",\n                "VPC": {\n                    "VPCId": "vpc-123",\n                    "VPCRegion": "region-for-vpc"\n                }\n            },\n            physical_resource_id=cr.PhysicalResourceId.of("${vpcStack.SharedVpc.VpcId}-${vpcStack.Region}-${PrivateHostedZone.HostedZoneId}")\n        ),\n        # Will ignore any resource and use the assumedRoleArn as resource and \'sts:AssumeRole\' for service:action\n        policy=cr.AwsCustomResourcePolicy.from_sdk_calls(\n            resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['function_name', 'install_latest_aws_sdk', 'log_retention', 'on_create', 'on_delete', 'on_update', 'policy', 'removal_policy', 'resource_type', 'role', 'timeout', 'vpc', 'vpc_subnets']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.AwsCustomResourceProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.custom_resources.AwsSdkCall
class AwsSdkCallDef(BaseStruct):
    action: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The service action to call. This is the name of an AWS API call, in one of the following forms: - An API call name as found in the API Reference documentation (``GetObject``) - The API call name starting with a lowercase letter (``getObject``) - The AWS SDK for JavaScript v3 command class name (``GetObjectCommand``)\n')
    service: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The service to call. This is the name of an AWS service, in one of the following forms: - An AWS SDK for JavaScript v3 package name (``@aws-sdk/client-api-gateway``) - An AWS SDK for JavaScript v3 client name (``api-gateway``) - An AWS SDK for JavaScript v2 constructor name (``APIGateway``) - A lowercase AWS SDK for JavaScript v2 constructor name (``apigateway``)\n')
    api_version: typing.Optional[str] = pydantic.Field(None, description='API version to use for the service. Default: - use latest available API version\n')
    assumed_role_arn: typing.Optional[str] = pydantic.Field(None, description='Used for running the SDK calls in underlying lambda with a different role. Can be used primarily for cross-account requests to for example connect hostedzone with a shared vpc. Region controls where assumeRole call is made. Example for Route53 / associateVPCWithHostedZone Default: - run without assuming role\n')
    ignore_error_codes_matching: typing.Optional[str] = pydantic.Field(None, description='The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors\n')
    output_paths: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description="Restrict the data returned by the custom resource to specific paths in the API response. Use this to limit the data returned by the custom resource if working with API calls that could potentially result in custom response objects exceeding the hard limit of 4096 bytes. Example for ECS / updateService: ['service.deploymentConfiguration.maximumPercent'] Default: - return all data\n")
    parameters: typing.Any = pydantic.Field(None, description='The parameters for the service action. Default: - no parameters\n')
    physical_resource_id: typing.Optional[models.custom_resources.PhysicalResourceIdDef] = pydantic.Field(None, description='The physical resource id of the custom resource for this call. Mandatory for onCreate call. In onUpdate, you can omit this to passthrough it from request. Default: - no physical resource id\n')
    region: typing.Optional[str] = pydantic.Field(None, description='The region to send service requests to. **Note: Cross-region operations are generally considered an anti-pattern.** **Consider first deploying a stack in that region.** Default: - the region where this custom resource is deployed\n\nExample::\n\n    cr.AwsCustomResource(self, "GetParameterCustomResource",\n        on_update=cr.AwsSdkCall( # will also be called for a CREATE event\n            service="SSM",\n            action="getParameter",\n            parameters={\n                "Name": "my-parameter",\n                "WithDecryption": True\n            },\n            physical_resource_id=cr.PhysicalResourceId.from_response("Parameter.ARN")),\n        policy=cr.AwsCustomResourcePolicy.from_sdk_calls(\n            resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE\n        )\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['action', 'service', 'api_version', 'assumed_role_arn', 'ignore_error_codes_matching', 'output_paths', 'parameters', 'physical_resource_id', 'region']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.AwsSdkCall'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.custom_resources.ProviderProps
class ProviderPropsDef(BaseStruct):
    on_event_handler: typing.Union[_REQUIRED_INIT_PARAM, models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='The AWS Lambda function to invoke for all resource lifecycle operations (CREATE/UPDATE/DELETE). This function is responsible to begin the requested resource operation (CREATE/UPDATE/DELETE) and return any additional properties to add to the event, which will later be passed to ``isComplete``. The ``PhysicalResourceId`` property must be included in the response.\n')
    is_complete_handler: typing.Optional[typing.Union[models.aws_lambda.FunctionBaseDef, models.aws_lambda.QualifiedFunctionBaseDef, models.aws_lambda.AliasDef, models.aws_lambda.DockerImageFunctionDef, models.aws_lambda.FunctionDef, models.aws_lambda.SingletonFunctionDef, models.aws_lambda.VersionDef, models.aws_lambda_nodejs.NodejsFunctionDef, models.triggers.TriggerFunctionDef]] = pydantic.Field(None, description='The AWS Lambda function to invoke in order to determine if the operation is complete. This function will be called immediately after ``onEvent`` and then periodically based on the configured query interval as long as it returns ``false``. If the function still returns ``false`` and the alloted timeout has passed, the operation will fail. Default: - provider is synchronous. This means that the ``onEvent`` handler is expected to finish all lifecycle operations within the initial invocation.\n')
    log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = pydantic.Field(None, description="The number of days framework log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE\n")
    provider_function_env_encryption: typing.Optional[typing.Union[models.aws_kms.KeyDef]] = pydantic.Field(None, description="AWS KMS key used to encrypt provider lambda's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK)\n")
    provider_function_name: typing.Optional[str] = pydantic.Field(None, description='Provider Lambda name. The provider lambda function name. Default: - CloudFormation default name from unique physical ID\n')
    query_interval: typing.Optional[models.DurationDef] = pydantic.Field(None, description='Time between calls to the ``isComplete`` handler which determines if the resource has been stabilized. The first ``isComplete`` will be called immediately after ``handler`` and then every ``queryInterval`` seconds, and until ``timeout`` has been reached or until ``isComplete`` returns ``true``. Default: Duration.seconds(5)\n')
    role: typing.Optional[typing.Union[models.aws_iam.LazyRoleDef, models.aws_iam.RoleDef]] = pydantic.Field(None, description="AWS Lambda execution role. The role that will be assumed by the AWS Lambda. Must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A default role will be created.\n")
    security_groups: typing.Optional[typing.Sequence[typing.Union[models.aws_ec2.SecurityGroupDef]]] = pydantic.Field(None, description="Security groups to attach to the provider functions. Only used if 'vpc' is supplied Default: - If ``vpc`` is not supplied, no security groups are attached. Otherwise, a dedicated security group is created for each function.\n")
    total_timeout: typing.Optional[models.DurationDef] = pydantic.Field(None, description='Total timeout for the entire operation. The maximum timeout is 1 hour (yes, it can exceed the AWS Lambda 15 minutes) Default: Duration.minutes(30)\n')
    vpc: typing.Optional[typing.Union[models.aws_ec2.VpcDef]] = pydantic.Field(None, description='The vpc to provision the lambda functions in. Default: - functions are not provisioned inside a vpc.\n')
    vpc_subnets: typing.Union[models.aws_ec2.SubnetSelectionDef, dict[str, typing.Any], None] = pydantic.Field(None, description='Which subnets from the VPC to place the lambda functions in. Only used if \'vpc\' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - the Vpc default strategy if not specified\n\n:exampleMetadata: infused\n\nExample::\n\n    # on_event: lambda.Function\n    # is_complete: lambda.Function\n    # my_role: iam.Role\n\n    my_provider = cr.Provider(self, "MyProvider",\n        on_event_handler=on_event,\n        is_complete_handler=is_complete,\n        log_retention=logs.RetentionDays.ONE_DAY,\n        role=my_role,\n        provider_function_name="the-lambda-name"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['on_event_handler', 'is_complete_handler', 'log_retention', 'provider_function_env_encryption', 'provider_function_name', 'query_interval', 'role', 'security_groups', 'total_timeout', 'vpc', 'vpc_subnets']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.ProviderProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ProviderPropsDefConfig] = pydantic.Field(None)


class ProviderPropsDefConfig(pydantic.BaseModel):
    on_event_handler_config: typing.Optional[models._interface_methods.AwsLambdaIFunctionDefConfig] = pydantic.Field(None)


#  autogenerated from aws_cdk.custom_resources.SdkCallsPolicyOptions
class SdkCallsPolicyOptionsDef(BaseStruct):
    resources: typing.Union[typing.Sequence[str], _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The resources that the calls will have access to. It is best to use specific resource ARN\'s when possible. However, you can also use ``AwsCustomResourcePolicy.ANY_RESOURCE`` to allow access to all resources. For example, when ``onCreate`` is used to create a resource which you don\'t know the physical name of in advance. Note that will apply to ALL SDK calls.\n\n:exampleMetadata: infused\n\nExample::\n\n    get_parameter = cr.AwsCustomResource(self, "GetParameter",\n        on_update=cr.AwsSdkCall( # will also be called for a CREATE event\n            service="SSM",\n            action="GetParameter",\n            parameters={\n                "Name": "my-parameter",\n                "WithDecryption": True\n            },\n            physical_resource_id=cr.PhysicalResourceId.of(Date.now().to_string())),\n        policy=cr.AwsCustomResourcePolicy.from_sdk_calls(\n            resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE\n        )\n    )\n\n    # Use the value in another construct with\n    get_parameter.get_response_field("Parameter.Value")\n')
    _init_params: typing.ClassVar[list[str]] = ['resources']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.custom_resources.SdkCallsPolicyOptions'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




import models

class ModuleModel(pydantic.BaseModel):
    AwsCustomResourcePolicy: typing.Optional[dict[str, AwsCustomResourcePolicyDef]] = pydantic.Field(None)
    PhysicalResourceId: typing.Optional[dict[str, PhysicalResourceIdDef]] = pydantic.Field(None)
    PhysicalResourceIdReference: typing.Optional[dict[str, PhysicalResourceIdReferenceDef]] = pydantic.Field(None)
    AwsCustomResource: typing.Optional[dict[str, AwsCustomResourceDef]] = pydantic.Field(None)
    Provider: typing.Optional[dict[str, ProviderDef]] = pydantic.Field(None)
    AwsCustomResourceProps: typing.Optional[dict[str, AwsCustomResourcePropsDef]] = pydantic.Field(None)
    AwsSdkCall: typing.Optional[dict[str, AwsSdkCallDef]] = pydantic.Field(None)
    ProviderProps: typing.Optional[dict[str, ProviderPropsDef]] = pydantic.Field(None)
    SdkCallsPolicyOptions: typing.Optional[dict[str, SdkCallsPolicyOptionsDef]] = pydantic.Field(None)
    ...
