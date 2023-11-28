from __future__ import annotations
import typing
import aws_cdk
import constructs
import pydantic
import datetime
from ._base import BaseConstruct, BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, ConnectableMixin, BaseMethodParams, GenericApplyRemovalPolicyParams, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM

#  autogenerated from aws_cdk.aws_route53_targets.ApiGateway
class ApiGatewayDef(BaseClass):
    api: typing.Union[models.aws_apigateway.RestApiBaseDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['api']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.ApiGateway'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ApiGatewayDefConfig] = pydantic.Field(None)


class ApiGatewayDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[ApiGatewayDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class ApiGatewayDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.ApiGatewayDomain
class ApiGatewayDomainDef(BaseClass):
    domain_name: typing.Union[_REQUIRED_INIT_PARAM, models.aws_apigateway.DomainNameDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['domain_name']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.ApiGatewayDomain'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ApiGatewayDomainDefConfig] = pydantic.Field(None)


class ApiGatewayDomainDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[ApiGatewayDomainDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class ApiGatewayDomainDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.ApiGatewayv2DomainProperties
class ApiGatewayv2DomainPropertiesDef(BaseClass):
    regional_domain_name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='the domain name associated with the regional endpoint for this custom domain name.')
    regional_hosted_zone_id: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='the region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint.')
    _init_params: typing.ClassVar[list[str]] = ['regional_domain_name', 'regional_hosted_zone_id']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.ApiGatewayv2DomainProperties'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ApiGatewayv2DomainPropertiesDefConfig] = pydantic.Field(None)


class ApiGatewayv2DomainPropertiesDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[ApiGatewayv2DomainPropertiesDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class ApiGatewayv2DomainPropertiesDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.BucketWebsiteTarget
class BucketWebsiteTargetDef(BaseClass):
    bucket: typing.Union[models.aws_s3.BucketDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['bucket']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.BucketWebsiteTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[BucketWebsiteTargetDefConfig] = pydantic.Field(None)


class BucketWebsiteTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[BucketWebsiteTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class BucketWebsiteTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.ClassicLoadBalancerTarget
class ClassicLoadBalancerTargetDef(BaseClass):
    load_balancer: typing.Union[models.aws_elasticloadbalancing.LoadBalancerDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['load_balancer']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.ClassicLoadBalancerTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ClassicLoadBalancerTargetDefConfig] = pydantic.Field(None)


class ClassicLoadBalancerTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[ClassicLoadBalancerTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class ClassicLoadBalancerTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.CloudFrontTarget
class CloudFrontTargetDef(BaseClass):
    distribution: typing.Union[_REQUIRED_INIT_PARAM, models.aws_cloudfront.CloudFrontWebDistributionDef, models.aws_cloudfront.DistributionDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['distribution']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = ['get_hosted_zone_id']
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.CloudFrontTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[CloudFrontTargetDefConfig] = pydantic.Field(None)


class CloudFrontTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[CloudFrontTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')
    get_hosted_zone_id: typing.Optional[list[CloudFrontTargetDefGetHostedZoneIdParams]] = pydantic.Field(None, description='Get the hosted zone id for the current scope.')

class CloudFrontTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...

class CloudFrontTargetDefGetHostedZoneIdParams(pydantic.BaseModel):
    scope: models.AnyResource = pydantic.Field(..., description='- scope in which this resource is defined.')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.ElasticBeanstalkEnvironmentEndpointTarget
class ElasticBeanstalkEnvironmentEndpointTargetDef(BaseClass):
    environment_endpoint: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['environment_endpoint']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.ElasticBeanstalkEnvironmentEndpointTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[ElasticBeanstalkEnvironmentEndpointTargetDefConfig] = pydantic.Field(None)


class ElasticBeanstalkEnvironmentEndpointTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[ElasticBeanstalkEnvironmentEndpointTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class ElasticBeanstalkEnvironmentEndpointTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.GlobalAcceleratorDomainTarget
class GlobalAcceleratorDomainTargetDef(BaseClass):
    accelerator_domain_name: typing.Union[str, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['accelerator_domain_name']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.GlobalAcceleratorDomainTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[GlobalAcceleratorDomainTargetDefConfig] = pydantic.Field(None)


class GlobalAcceleratorDomainTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[GlobalAcceleratorDomainTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class GlobalAcceleratorDomainTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.GlobalAcceleratorTarget
class GlobalAcceleratorTargetDef(BaseClass):
    accelerator: typing.Union[_REQUIRED_INIT_PARAM, models.aws_globalaccelerator.AcceleratorDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['accelerator']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.GlobalAcceleratorTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[GlobalAcceleratorTargetDefConfig] = pydantic.Field(None)


class GlobalAcceleratorTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[GlobalAcceleratorTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class GlobalAcceleratorTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.InterfaceVpcEndpointTarget
class InterfaceVpcEndpointTargetDef(BaseClass):
    vpc_endpoint: typing.Union[models.aws_ec2.InterfaceVpcEndpointDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['vpc_endpoint']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.InterfaceVpcEndpointTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[InterfaceVpcEndpointTargetDefConfig] = pydantic.Field(None)


class InterfaceVpcEndpointTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[InterfaceVpcEndpointTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class InterfaceVpcEndpointTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.LoadBalancerTarget
class LoadBalancerTargetDef(BaseClass):
    load_balancer: typing.Union[models.UnsupportedResource, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['load_balancer']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.LoadBalancerTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[LoadBalancerTargetDefConfig] = pydantic.Field(None)


class LoadBalancerTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[LoadBalancerTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class LoadBalancerTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.Route53RecordTarget
class Route53RecordTargetDef(BaseClass):
    record: typing.Union[_REQUIRED_INIT_PARAM, models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['record']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.Route53RecordTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[Route53RecordTargetDefConfig] = pydantic.Field(None)


class Route53RecordTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[Route53RecordTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class Route53RecordTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


#  autogenerated from aws_cdk.aws_route53_targets.UserPoolDomainTarget
class UserPoolDomainTargetDef(BaseClass):
    domain: typing.Union[models.aws_cognito.UserPoolDomainDef, _REQUIRED_INIT_PARAM] = pydantic.Field(REQUIRED_INIT_PARAM, description='-')
    _init_params: typing.ClassVar[list[str]] = ['domain']
    _method_names: typing.ClassVar[list[str]] = ['bind']
    _classmethod_names: typing.ClassVar[list[str]] = []
    _cdk_class_fqn: typing.ClassVar[str] = 'aws_cdk.aws_route53_targets.UserPoolDomainTarget'
    _alternate_constructor_method_names: typing.ClassVar[list[str]] = []
    ...


    resource_config: typing.Optional[UserPoolDomainTargetDefConfig] = pydantic.Field(None)


class UserPoolDomainTargetDefConfig(pydantic.BaseModel):
    bind: typing.Optional[list[UserPoolDomainTargetDefBindParams]] = pydantic.Field(None, description='Return hosted zone ID and DNS name, usable for Route53 alias targets.')

class UserPoolDomainTargetDefBindParams(pydantic.BaseModel):
    _record: typing.Union[models.aws_route53.AaaaRecordDef, models.aws_route53.ARecordDef, models.aws_route53.CaaAmazonRecordDef, models.aws_route53.CaaRecordDef, models.aws_route53.CnameRecordDef, models.aws_route53.DsRecordDef, models.aws_route53.MxRecordDef, models.aws_route53.NsRecordDef, models.aws_route53.RecordSetDef, models.aws_route53.SrvRecordDef, models.aws_route53.TxtRecordDef, models.aws_route53.ZoneDelegationRecordDef] = pydantic.Field(..., description='-\n')
    _zone: typing.Optional[typing.Union[models.aws_route53.HostedZoneDef, models.aws_route53.PrivateHostedZoneDef, models.aws_route53.PublicHostedZoneDef]] = pydantic.Field(None, description='-')
    ...


import models

class ModuleModel(pydantic.BaseModel):
    ApiGateway: typing.Optional[dict[str, ApiGatewayDef]] = pydantic.Field(None)
    ApiGatewayDomain: typing.Optional[dict[str, ApiGatewayDomainDef]] = pydantic.Field(None)
    ApiGatewayv2DomainProperties: typing.Optional[dict[str, ApiGatewayv2DomainPropertiesDef]] = pydantic.Field(None)
    BucketWebsiteTarget: typing.Optional[dict[str, BucketWebsiteTargetDef]] = pydantic.Field(None)
    ClassicLoadBalancerTarget: typing.Optional[dict[str, ClassicLoadBalancerTargetDef]] = pydantic.Field(None)
    CloudFrontTarget: typing.Optional[dict[str, CloudFrontTargetDef]] = pydantic.Field(None)
    ElasticBeanstalkEnvironmentEndpointTarget: typing.Optional[dict[str, ElasticBeanstalkEnvironmentEndpointTargetDef]] = pydantic.Field(None)
    GlobalAcceleratorDomainTarget: typing.Optional[dict[str, GlobalAcceleratorDomainTargetDef]] = pydantic.Field(None)
    GlobalAcceleratorTarget: typing.Optional[dict[str, GlobalAcceleratorTargetDef]] = pydantic.Field(None)
    InterfaceVpcEndpointTarget: typing.Optional[dict[str, InterfaceVpcEndpointTargetDef]] = pydantic.Field(None)
    LoadBalancerTarget: typing.Optional[dict[str, LoadBalancerTargetDef]] = pydantic.Field(None)
    Route53RecordTarget: typing.Optional[dict[str, Route53RecordTargetDef]] = pydantic.Field(None)
    UserPoolDomainTarget: typing.Optional[dict[str, UserPoolDomainTargetDef]] = pydantic.Field(None)
    ...
