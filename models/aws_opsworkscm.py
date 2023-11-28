from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_opsworkscm.CfnServer.EngineAttributeProperty
class CfnServer_EngineAttributePropertyDef(BaseStruct):
    name: typing.Optional[str] = pydantic.Field(None, description='The name of the engine attribute. *Attribute name for Chef Automate servers:* - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` *Attribute names for Puppet Enterprise servers:* - ``PUPPET_ADMIN_PASSWORD`` - ``PUPPET_R10K_REMOTE`` - ``PUPPET_R10K_PRIVATE_KEY``\n')
    value: typing.Optional[str] = pydantic.Field(None, description='The value of the engine attribute. *Attribute value for Chef Automate servers:* - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. You can generate this key by running the following `OpenSSL <https://docs.aws.amazon.com/https://www.openssl.org/>`_ command on Linux-based computers. ``openssl genrsa -out *pivotal_key_file_name* .pem 2048`` On Windows-based computers, you can use the PuTTYgen utility to generate a base64-encoded RSA private key. For more information, see `PuTTYgen - Key Generator for PuTTY on Windows <https://docs.aws.amazon.com/https://www.ssh.com/ssh/putty/windows/puttygen>`_ on SSH.com. *Attribute values for Puppet Enterprise servers:* - ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console webpage after the server is online. The password must use between 8 and 32 ASCII characters. - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170. - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add ``PUPPET_R10K_PRIVATE_KEY`` to specify a PEM-encoded private SSH key.\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_opsworkscm as opsworkscm\n\n    engine_attribute_property = opsworkscm.CfnServer.EngineAttributeProperty(\n        name="name",\n        value="value"\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['name', 'value']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_opsworkscm.CfnServer.EngineAttributeProperty'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




#  autogenerated from aws_cdk.aws_opsworkscm.CfnServer
class CfnServerDef(BaseCfnResource):
    instance_profile_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The ARN of the instance profile that your Amazon EC2 instances use.\n')
    instance_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon EC2 instance type to use. For example, ``m5.large`` .\n')
    service_role_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need.\n')
    associate_public_ip_address: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='Associate a public IP address with a server that you are launching. Valid values are ``true`` or ``false`` . The default value is ``true`` .\n')
    backup_id: typing.Optional[str] = pydantic.Field(None, description='If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.\n')
    backup_retention_count: typing.Union[int, float, None] = pydantic.Field(None, description='The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is ``1`` .\n')
    custom_certificate: typing.Optional[str] = pydantic.Field(None, description="Supported on servers running Chef Automate 2.0 only. A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for ``CustomDomain`` and ``CustomPrivateKey`` . The following are requirements for the ``CustomCertificate`` value:. - You can provide either a self-signed, custom certificate, or the full certificate chain. - The certificate must be a valid X509 certificate, or a certificate chain in PEM format. - The certificate must be valid at the time of upload. A certificate can't be used before its validity period begins (the certificate's ``NotBefore`` date), or after it expires (the certificate's ``NotAfter`` date). - The certificate’s common name or subject alternative names (SANs), if present, must match the value of ``CustomDomain`` . - The certificate must match the value of ``CustomPrivateKey`` .\n")
    custom_domain: typing.Optional[str] = pydantic.Field(None, description='Supported on servers running Chef Automate 2.0 only. An optional public endpoint of a server, such as ``https://aws.my-company.com`` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated ``Endpoint`` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for ``CustomCertificate`` and ``CustomPrivateKey`` .\n')
    custom_private_key: typing.Optional[str] = pydantic.Field(None, description='Supported on servers running Chef Automate 2.0 only. A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for ``CustomDomain`` and ``CustomCertificate`` .\n')
    disable_automated_backup: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='Enable or disable scheduled backups. Valid values are ``true`` or ``false`` . The default value is ``true`` .\n')
    engine: typing.Optional[str] = pydantic.Field(None, description='The configuration management engine to use. Valid values include ``ChefAutomate`` and ``Puppet`` .\n')
    engine_attributes: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_opsworkscm.CfnServer_EngineAttributePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='Optional engine attributes on a specified server. **Attributes accepted in a Chef createServer request:** - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response. When you are specifying the value of CHEF_AUTOMATE_PIVOTAL_KEY as a parameter in the AWS CloudFormation console, you must add newline ( ``\\n`` ) characters at the end of each line of the pivotal key value. - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response. **Attributes accepted in a Puppet createServer request:** - ``PUPPET_ADMIN_PASSWORD`` : To work with the Puppet Enterprise console, a password must use ASCII characters. - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170. - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.\n')
    engine_model: typing.Optional[str] = pydantic.Field(None, description='The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef.\n')
    engine_version: typing.Optional[str] = pydantic.Field(None, description='The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently ``2`` . For a Puppet server, valid values are ``2019`` or ``2017`` .\n')
    key_pair: typing.Optional[str] = pydantic.Field(None, description='The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.\n')
    preferred_backup_window: typing.Optional[str] = pydantic.Field(None, description='The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats: - ``HH:MM`` for daily backups - ``DDD:HH:MM`` for weekly backups ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random, daily start time. *Example:* ``08:00`` , which represents a daily start time of 08:00 UTC. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)\n')
    preferred_maintenance_window: typing.Optional[str] = pydantic.Field(None, description='The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: ``DDD:HH:MM`` . ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See ``TimeWindowDefinition`` for more information. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)\n')
    security_group_ids: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by ``SubnetIds`` . If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).\n')
    server_name: typing.Optional[str] = pydantic.Field(None, description='')
    subnet_ids: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The IDs of subnets in which to launch the server EC2 instance. Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have "Auto Assign Public IP" enabled. EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign Public IP" enabled. For more information about supported Amazon EC2 platforms, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server. - The key cannot be empty. - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /')
    _init_params: typing.ClassVar[list[str]] = ['instance_profile_arn', 'instance_type', 'service_role_arn', 'associate_public_ip_address', 'backup_id', 'backup_retention_count', 'custom_certificate', 'custom_domain', 'custom_private_key', 'disable_automated_backup', 'engine', 'engine_attributes', 'engine_model', 'engine_version', 'key_pair', 'preferred_backup_window', 'preferred_maintenance_window', 'security_group_ids', 'server_name', 'subnet_ids', 'tags']
    _method_names: typing.ClassVar[list[str]] = ['EngineAttributeProperty', 'add_deletion_override', 'add_dependency', 'add_depends_on', 'add_metadata', 'add_override', 'add_property_deletion_override', 'add_property_override', 'apply_removal_policy', 'get_att', 'get_metadata', 'inspect', 'obtain_dependencies', 'obtain_resource_dependencies', 'override_logical_id', 'remove_dependency', 'replace_dependency']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_opsworkscm.CfnServer'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[models.aws_opsworkscm.CfnServerDefConfig] = pydantic.Field(None)


class CfnServerDefConfig(pydantic.BaseModel):
    EngineAttributeProperty: typing.Optional[list[models.aws_opsworkscm.CfnServerDefEngineattributepropertyParams]] = pydantic.Field(None, description='')
    add_deletion_override: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddDeletionOverrideParams]] = pydantic.Field(None, description='Syntactic sugar for ``addOverride(path, undefined)``.')
    add_dependency: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddDependencyParams]] = pydantic.Field(None, description='Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.\nThis can be used for resources across stacks (or nested stack) boundaries\nand the dependency will automatically be transferred to the relevant scope.')
    add_depends_on: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddDependsOnParams]] = pydantic.Field(None, description='(deprecated) Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.')
    add_metadata: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddMetadataParams]] = pydantic.Field(None, description='Add a value to the CloudFormation Resource Metadata.')
    add_override: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddOverrideParams]] = pydantic.Field(None, description='Adds an override to the synthesized CloudFormation resource.\nTo add a\nproperty override, either use ``addPropertyOverride`` or prefix ``path`` with\n"Properties." (i.e. ``Properties.TopicName``).\n\nIf the override is nested, separate each nested level using a dot (.) in the path parameter.\nIf there is an array as part of the nesting, specify the index in the path.\n\nTo include a literal ``.`` in the property name, prefix with a ``\\``. In most\nprogramming languages you will need to write this as ``"\\\\."`` because the\n``\\`` itself will need to be escaped.\n\nFor example::\n\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])\n   cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")\n\nwould add the overrides Example::\n\n   "Properties": {\n     "GlobalSecondaryIndexes": [\n       {\n         "Projection": {\n           "NonKeyAttributes": [ "myattribute" ]\n           ...\n         }\n         ...\n       },\n       {\n         "ProjectionType": "INCLUDE"\n         ...\n       },\n     ]\n     ...\n   }\n\nThe ``value`` argument to ``addOverride`` will not be processed or translated\nin any way. Pass raw JSON values in here with the correct capitalization\nfor CloudFormation. If you pass CDK classes or structs, they will be\nrendered with lowercased key names, and CloudFormation will reject the\ntemplate.')
    add_property_deletion_override: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddPropertyDeletionOverrideParams]] = pydantic.Field(None, description='Adds an override that deletes the value of a property from the resource definition.')
    add_property_override: typing.Optional[list[models.aws_opsworkscm.CfnServerDefAddPropertyOverrideParams]] = pydantic.Field(None, description='Adds an override to a resource property.\nSyntactic sugar for ``addOverride("Properties.<...>", value)``.')
    apply_removal_policy: typing.Optional[list[models.GenericApplyRemovalPolicyParams]] = pydantic.Field(None)
    get_att: typing.Optional[list[models.aws_opsworkscm.CfnServerDefGetAttParams]] = pydantic.Field(None, description='Returns a token for an runtime attribute of this resource.\nIdeally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility\nin case there is no generated attribute.')
    get_metadata: typing.Optional[list[models.aws_opsworkscm.CfnServerDefGetMetadataParams]] = pydantic.Field(None, description='Retrieve a value value from the CloudFormation Resource Metadata.')
    inspect: typing.Optional[list[models.aws_opsworkscm.CfnServerDefInspectParams]] = pydantic.Field(None, description='Examines the CloudFormation resource and discloses attributes.')
    obtain_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Retrieves an array of resources this resource depends on.\nThis assembles dependencies on resources across stacks (including nested stacks)\nautomatically.')
    obtain_resource_dependencies: typing.Optional[bool] = pydantic.Field(None, description='Get a shallow copy of dependencies between this resource and other resources in the same stack.')
    override_logical_id: typing.Optional[list[models.aws_opsworkscm.CfnServerDefOverrideLogicalIdParams]] = pydantic.Field(None, description='Overrides the auto-generated logical ID with a specific ID.')
    remove_dependency: typing.Optional[list[models.aws_opsworkscm.CfnServerDefRemoveDependencyParams]] = pydantic.Field(None, description='Indicates that this resource no longer depends on another resource.\nThis can be used for resources across stacks (including nested stacks)\nand the dependency will automatically be removed from the relevant scope.')
    replace_dependency: typing.Optional[list[models.aws_opsworkscm.CfnServerDefReplaceDependencyParams]] = pydantic.Field(None, description='Replaces one dependency with another.')
    tags_config: typing.Optional[models.core.TagManagerDefConfig] = pydantic.Field(None)

class CfnServerDefEngineattributepropertyParams(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(None, description='')
    value: typing.Optional[str] = pydantic.Field(None, description='')
    ...

class CfnServerDefAddDeletionOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='The path of the value to delete.')
    ...

class CfnServerDefAddDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnServerDefAddDependsOnParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-\n\n:deprecated: use addDependency\n\n:stability: deprecated\n')
    ...

class CfnServerDefAddMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n')
    value: typing.Any = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnServerDefAddOverrideParams(pydantic.BaseModel):
    path: str = pydantic.Field(..., description='- The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.\n')
    value: typing.Any = pydantic.Field(..., description='- The value. Could be primitive or complex.')
    ...

class CfnServerDefAddPropertyDeletionOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path to the property.')
    ...

class CfnServerDefAddPropertyOverrideParams(pydantic.BaseModel):
    property_path: str = pydantic.Field(..., description='The path of the property.\n')
    value: typing.Any = pydantic.Field(..., description='The value.')
    ...

class CfnServerDefApplyRemovalPolicyParams(pydantic.BaseModel):
    policy: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description='-\n')
    apply_to_update_replace_policy: typing.Optional[bool] = pydantic.Field(None, description='Apply the same deletion policy to the resource\'s "UpdateReplacePolicy". Default: true\n')
    default: typing.Optional[aws_cdk.RemovalPolicy] = pydantic.Field(None, description="The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resource, please consult that specific resource's documentation.\n\n:see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options\n")
    ...

class CfnServerDefGetAttParams(pydantic.BaseModel):
    attribute_name: str = pydantic.Field(..., description='The name of the attribute.\n')
    type_hint: typing.Optional[aws_cdk.ResolutionTypeHint] = pydantic.Field(None, description='-')
    return_config: typing.Optional[list[models.core.ReferenceDefConfig]] = pydantic.Field(None)
    ...

class CfnServerDefGetMetadataParams(pydantic.BaseModel):
    key: str = pydantic.Field(..., description='-\n\n:see:\n\nhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html\n\nNote that this is a different set of metadata from CDK node metadata; this\nmetadata ends up in the stack template under the resource, whereas CDK\nnode metadata ends up in the Cloud Assembly.\n')
    ...

class CfnServerDefInspectParams(pydantic.BaseModel):
    inspector: models.TreeInspectorDef = pydantic.Field(..., description='tree inspector to collect and process attributes.')
    ...

class CfnServerDefOverrideLogicalIdParams(pydantic.BaseModel):
    new_logical_id: str = pydantic.Field(..., description='The new logical ID to use for this stack element.')
    ...

class CfnServerDefRemoveDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='-')
    ...

class CfnServerDefReplaceDependencyParams(pydantic.BaseModel):
    target: models.CfnResourceDef = pydantic.Field(..., description='The dependency to replace.\n')
    new_target: models.CfnResourceDef = pydantic.Field(..., description='The new dependency to add.')
    ...


#  autogenerated from aws_cdk.aws_opsworkscm.CfnServerProps
class CfnServerPropsDef(BaseCfnProperty):
    instance_profile_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The ARN of the instance profile that your Amazon EC2 instances use.\n')
    instance_type: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The Amazon EC2 instance type to use. For example, ``m5.large`` .\n')
    service_role_arn: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='The service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need.\n')
    associate_public_ip_address: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='Associate a public IP address with a server that you are launching. Valid values are ``true`` or ``false`` . The default value is ``true`` .\n')
    backup_id: typing.Optional[str] = pydantic.Field(None, description='If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.\n')
    backup_retention_count: typing.Union[int, float, None] = pydantic.Field(None, description='The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is ``1`` .\n')
    custom_certificate: typing.Optional[str] = pydantic.Field(None, description="Supported on servers running Chef Automate 2.0 only. A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for ``CustomDomain`` and ``CustomPrivateKey`` . The following are requirements for the ``CustomCertificate`` value:. - You can provide either a self-signed, custom certificate, or the full certificate chain. - The certificate must be a valid X509 certificate, or a certificate chain in PEM format. - The certificate must be valid at the time of upload. A certificate can't be used before its validity period begins (the certificate's ``NotBefore`` date), or after it expires (the certificate's ``NotAfter`` date). - The certificate’s common name or subject alternative names (SANs), if present, must match the value of ``CustomDomain`` . - The certificate must match the value of ``CustomPrivateKey`` .\n")
    custom_domain: typing.Optional[str] = pydantic.Field(None, description='Supported on servers running Chef Automate 2.0 only. An optional public endpoint of a server, such as ``https://aws.my-company.com`` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated ``Endpoint`` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for ``CustomCertificate`` and ``CustomPrivateKey`` .\n')
    custom_private_key: typing.Optional[str] = pydantic.Field(None, description='Supported on servers running Chef Automate 2.0 only. A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for ``CustomDomain`` and ``CustomCertificate`` .\n')
    disable_automated_backup: typing.Union[bool, models.UnsupportedResource, None] = pydantic.Field(None, description='Enable or disable scheduled backups. Valid values are ``true`` or ``false`` . The default value is ``true`` .\n')
    engine: typing.Optional[str] = pydantic.Field(None, description='The configuration management engine to use. Valid values include ``ChefAutomate`` and ``Puppet`` .\n')
    engine_attributes: typing.Union[models.UnsupportedResource, typing.Sequence[typing.Union[models.UnsupportedResource, models.aws_opsworkscm.CfnServer_EngineAttributePropertyDef, dict[str, typing.Any]]], None] = pydantic.Field(None, description='Optional engine attributes on a specified server. **Attributes accepted in a Chef createServer request:** - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response. When you are specifying the value of CHEF_AUTOMATE_PIVOTAL_KEY as a parameter in the AWS CloudFormation console, you must add newline ( ``\\n`` ) characters at the end of each line of the pivotal key value. - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response. **Attributes accepted in a Puppet createServer request:** - ``PUPPET_ADMIN_PASSWORD`` : To work with the Puppet Enterprise console, a password must use ASCII characters. - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170. - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.\n')
    engine_model: typing.Optional[str] = pydantic.Field(None, description='The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef.\n')
    engine_version: typing.Optional[str] = pydantic.Field(None, description='The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently ``2`` . For a Puppet server, valid values are ``2019`` or ``2017`` .\n')
    key_pair: typing.Optional[str] = pydantic.Field(None, description='The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.\n')
    preferred_backup_window: typing.Optional[str] = pydantic.Field(None, description='The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats: - ``HH:MM`` for daily backups - ``DDD:HH:MM`` for weekly backups ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random, daily start time. *Example:* ``08:00`` , which represents a daily start time of 08:00 UTC. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)\n')
    preferred_maintenance_window: typing.Optional[str] = pydantic.Field(None, description='The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: ``DDD:HH:MM`` . ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See ``TimeWindowDefinition`` for more information. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)\n')
    security_group_ids: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by ``SubnetIds`` . If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).\n')
    server_name: typing.Optional[str] = pydantic.Field(None, description='')
    subnet_ids: typing.Optional[typing.Sequence[str]] = pydantic.Field(None, description='The IDs of subnets in which to launch the server EC2 instance. Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have "Auto Assign Public IP" enabled. EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign Public IP" enabled. For more information about supported Amazon EC2 platforms, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .\n')
    tags: typing.Optional[typing.Sequence[typing.Union[models.CfnTagDef, dict[str, typing.Any]]]] = pydantic.Field(None, description='A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server. - The key cannot be empty. - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /\n\n:see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html\n:exampleMetadata: fixture=_generated\n\nExample::\n\n    # The code below shows an example of how to instantiate this type.\n    # The values are placeholders you should change.\n    from aws_cdk import aws_opsworkscm as opsworkscm\n\n    cfn_server_props = opsworkscm.CfnServerProps(\n        instance_profile_arn="instanceProfileArn",\n        instance_type="instanceType",\n        service_role_arn="serviceRoleArn",\n\n        # the properties below are optional\n        associate_public_ip_address=False,\n        backup_id="backupId",\n        backup_retention_count=123,\n        custom_certificate="customCertificate",\n        custom_domain="customDomain",\n        custom_private_key="customPrivateKey",\n        disable_automated_backup=False,\n        engine="engine",\n        engine_attributes=[opsworkscm.CfnServer.EngineAttributeProperty(\n            name="name",\n            value="value"\n        )],\n        engine_model="engineModel",\n        engine_version="engineVersion",\n        key_pair="keyPair",\n        preferred_backup_window="preferredBackupWindow",\n        preferred_maintenance_window="preferredMaintenanceWindow",\n        security_group_ids=["securityGroupIds"],\n        server_name="serverName",\n        subnet_ids=["subnetIds"],\n        tags=[CfnTag(\n            key="key",\n            value="value"\n        )]\n    )\n')
    _init_params: typing.ClassVar[list[str]] = ['instance_profile_arn', 'instance_type', 'service_role_arn', 'associate_public_ip_address', 'backup_id', 'backup_retention_count', 'custom_certificate', 'custom_domain', 'custom_private_key', 'disable_automated_backup', 'engine', 'engine_attributes', 'engine_model', 'engine_version', 'key_pair', 'preferred_backup_window', 'preferred_maintenance_window', 'security_group_ids', 'server_name', 'subnet_ids', 'tags']
    _method_names: typing.ClassVar[list[str]] = []
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_opsworkscm.CfnServerProps'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...




class ModuleModel(pydantic.BaseModel):
    CfnServer_EngineAttributeProperty: typing.Optional[dict[str, models.aws_opsworkscm.CfnServer_EngineAttributePropertyDef]] = pydantic.Field(None)
    CfnServer: typing.Optional[dict[str, models.aws_opsworkscm.CfnServerDef]] = pydantic.Field(None)
    CfnServerProps: typing.Optional[dict[str, models.aws_opsworkscm.CfnServerPropsDef]] = pydantic.Field(None)
    ...

import models
