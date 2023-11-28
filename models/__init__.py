import typing
import pydantic
from ._base import BaseClass, BaseStruct, BaseCfnResource, BaseCfnProperty, BaseConstruct, UnsupportedResource, AnyResource, REQUIRED_INIT_PARAM, _REQUIRED_INIT_PARAM
from .core import *
from . import core
from . import alexa_ask
from . import assertions
from . import assets
from . import aws_accessanalyzer
from . import aws_acmpca
from . import aws_amazonmq
from . import aws_amplify
from . import aws_amplifyuibuilder
from . import aws_apigateway
from . import aws_apigatewayv2
from . import aws_appconfig
from . import aws_appflow
from . import aws_appintegrations
from . import aws_applicationautoscaling
from . import aws_applicationinsights
from . import aws_appmesh
from . import aws_apprunner
from . import aws_appstream
from . import aws_appsync
from . import aws_aps
from . import aws_athena
from . import aws_auditmanager
from . import aws_autoscaling
from . import aws_autoscaling_common
from . import aws_autoscaling_hooktargets
from . import aws_autoscalingplans
from . import aws_backup
from . import aws_backupgateway
from . import aws_batch
from . import aws_billingconductor
from . import aws_budgets
from . import aws_cassandra
from . import aws_ce
from . import aws_certificatemanager
from . import aws_chatbot
from . import aws_cleanrooms
from . import aws_cloud9
from . import aws_cloudformation
from . import aws_cloudfront
from . import aws_cloudfront_origins
from . import aws_cloudtrail
from . import aws_cloudwatch
from . import aws_cloudwatch_actions
from . import aws_codebuild
from . import aws_codecommit
from . import aws_codedeploy
from . import aws_codeguruprofiler
from . import aws_codegurureviewer
from . import aws_codepipeline
from . import aws_codepipeline_actions
from . import aws_codestar
from . import aws_codestarconnections
from . import aws_codestarnotifications
from . import aws_cognito
from . import aws_comprehend
from . import aws_config
from . import aws_connect
from . import aws_connectcampaigns
from . import aws_controltower
from . import aws_cur
from . import aws_customerprofiles
from . import aws_databrew
from . import aws_datapipeline
from . import aws_datasync
from . import aws_dax
from . import aws_detective
from . import aws_devicefarm
from . import aws_devopsguru
from . import aws_directoryservice
from . import aws_dlm
from . import aws_dms
from . import aws_docdb
from . import aws_docdbelastic
from . import aws_dynamodb
from . import aws_ec2
from . import aws_ecr
from . import aws_ecr_assets
from . import aws_ecs
from . import aws_ecs_patterns
from . import aws_efs
from . import aws_eks
from . import aws_elasticache
from . import aws_elasticbeanstalk
from . import aws_elasticloadbalancing
from . import aws_elasticloadbalancingv2
from . import aws_elasticloadbalancingv2_actions
from . import aws_elasticloadbalancingv2_targets
from . import aws_elasticsearch
from . import aws_emr
from . import aws_emrcontainers
from . import aws_emrserverless
from . import aws_entityresolution
from . import aws_events
from . import aws_events_targets
from . import aws_eventschemas
from . import aws_evidently
from . import aws_finspace
from . import aws_fis
from . import aws_fms
from . import aws_forecast
from . import aws_frauddetector
from . import aws_fsx
from . import aws_gamelift
from . import aws_globalaccelerator
from . import aws_globalaccelerator_endpoints
from . import aws_glue
from . import aws_grafana
from . import aws_greengrass
from . import aws_greengrassv2
from . import aws_groundstation
from . import aws_guardduty
from . import aws_healthimaging
from . import aws_healthlake
from . import aws_iam
from . import aws_identitystore
from . import aws_imagebuilder
from . import aws_inspector
from . import aws_inspectorv2
from . import aws_internetmonitor
from . import aws_iot
from . import aws_iot1click
from . import aws_iotanalytics
from . import aws_iotcoredeviceadvisor
from . import aws_iotevents
from . import aws_iotfleethub
from . import aws_iotfleetwise
from . import aws_iotsitewise
from . import aws_iotthingsgraph
from . import aws_iottwinmaker
from . import aws_iotwireless
from . import aws_ivs
from . import aws_ivschat
from . import aws_kafkaconnect
from . import aws_kendra
from . import aws_kendraranking
from . import aws_kinesis
from . import aws_kinesisanalytics
from . import aws_kinesisanalyticsv2
from . import aws_kinesisfirehose
from . import aws_kinesisvideo
from . import aws_kms
from . import aws_lakeformation
from . import aws_lambda
from . import aws_lambda_destinations
from . import aws_lambda_event_sources
from . import aws_lambda_nodejs
from . import aws_lex
from . import aws_licensemanager
from . import aws_lightsail
from . import aws_location
from . import aws_logs
from . import aws_logs_destinations
from . import aws_lookoutequipment
from . import aws_lookoutmetrics
from . import aws_lookoutvision
from . import aws_m2
from . import aws_macie
from . import aws_managedblockchain
from . import aws_mediaconnect
from . import aws_mediaconvert
from . import aws_medialive
from . import aws_mediapackage
from . import aws_mediapackagev2
from . import aws_mediastore
from . import aws_mediatailor
from . import aws_memorydb
from . import aws_msk
from . import aws_mwaa
from . import aws_neptune
from . import aws_networkfirewall
from . import aws_networkmanager
from . import aws_nimblestudio
from . import aws_oam
from . import aws_omics
from . import aws_opensearchserverless
from . import aws_opensearchservice
from . import aws_opsworks
from . import aws_opsworkscm
from . import aws_organizations
from . import aws_osis
from . import aws_panorama
from . import aws_pcaconnectorad
from . import aws_personalize
from . import aws_pinpoint
from . import aws_pinpointemail
from . import aws_pipes
from . import aws_proton
from . import aws_qldb
from . import aws_quicksight
from . import aws_ram
from . import aws_rds
from . import aws_redshift
from . import aws_redshiftserverless
from . import aws_refactorspaces
from . import aws_rekognition
from . import aws_resiliencehub
from . import aws_resourceexplorer2
from . import aws_resourcegroups
from . import aws_robomaker
from . import aws_rolesanywhere
from . import aws_route53
from . import aws_route53_patterns
from . import aws_route53_targets
from . import aws_route53recoverycontrol
from . import aws_route53recoveryreadiness
from . import aws_route53resolver
from . import aws_rum
from . import aws_s3
from . import aws_s3_assets
from . import aws_s3_deployment
from . import aws_s3_notifications
from . import aws_s3objectlambda
from . import aws_s3outposts
from . import aws_sagemaker
from . import aws_sam
from . import aws_scheduler
from . import aws_sdb
from . import aws_secretsmanager
from . import aws_securityhub
from . import aws_servicecatalog
from . import aws_servicecatalogappregistry
from . import aws_servicediscovery
from . import aws_ses
from . import aws_ses_actions
from . import aws_shield
from . import aws_signer
from . import aws_simspaceweaver
from . import aws_sns
from . import aws_sns_subscriptions
from . import aws_sqs
from . import aws_ssm
from . import aws_ssmcontacts
from . import aws_ssmincidents
from . import aws_sso
from . import aws_stepfunctions
from . import aws_stepfunctions_tasks
from . import aws_supportapp
from . import aws_synthetics
from . import aws_systemsmanagersap
from . import aws_timestream
from . import aws_transfer
from . import aws_verifiedpermissions
from . import aws_voiceid
from . import aws_vpclattice
from . import aws_waf
from . import aws_wafregional
from . import aws_wafv2
from . import aws_wisdom
from . import aws_workspaces
from . import aws_workspacesweb
from . import aws_xray
from . import cloud_assembly_schema
from . import cloudformation_include
from . import custom_resources
from . import cx_api
from . import lambda_layer_awscli
from . import lambda_layer_kubectl
from . import lambda_layer_node_proxy_agent
from . import pipelines
from . import region_info
from . import triggers
from . import constructs
from . import _interface_methods
from . import _utils
from . import core
for mod in [
    core,
    alexa_ask,
    assertions,
    assets,
    aws_accessanalyzer,
    aws_acmpca,
    aws_amazonmq,
    aws_amplify,
    aws_amplifyuibuilder,
    aws_apigateway,
    aws_apigatewayv2,
    aws_appconfig,
    aws_appflow,
    aws_appintegrations,
    aws_applicationautoscaling,
    aws_applicationinsights,
    aws_appmesh,
    aws_apprunner,
    aws_appstream,
    aws_appsync,
    aws_aps,
    aws_athena,
    aws_auditmanager,
    aws_autoscaling,
    aws_autoscaling_common,
    aws_autoscaling_hooktargets,
    aws_autoscalingplans,
    aws_backup,
    aws_backupgateway,
    aws_batch,
    aws_billingconductor,
    aws_budgets,
    aws_cassandra,
    aws_ce,
    aws_certificatemanager,
    aws_chatbot,
    aws_cleanrooms,
    aws_cloud9,
    aws_cloudformation,
    aws_cloudfront,
    aws_cloudfront_origins,
    aws_cloudtrail,
    aws_cloudwatch,
    aws_cloudwatch_actions,
    aws_codebuild,
    aws_codecommit,
    aws_codedeploy,
    aws_codeguruprofiler,
    aws_codegurureviewer,
    aws_codepipeline,
    aws_codepipeline_actions,
    aws_codestar,
    aws_codestarconnections,
    aws_codestarnotifications,
    aws_cognito,
    aws_comprehend,
    aws_config,
    aws_connect,
    aws_connectcampaigns,
    aws_controltower,
    aws_cur,
    aws_customerprofiles,
    aws_databrew,
    aws_datapipeline,
    aws_datasync,
    aws_dax,
    aws_detective,
    aws_devicefarm,
    aws_devopsguru,
    aws_directoryservice,
    aws_dlm,
    aws_dms,
    aws_docdb,
    aws_docdbelastic,
    aws_dynamodb,
    aws_ec2,
    aws_ecr,
    aws_ecr_assets,
    aws_ecs,
    aws_ecs_patterns,
    aws_efs,
    aws_eks,
    aws_elasticache,
    aws_elasticbeanstalk,
    aws_elasticloadbalancing,
    aws_elasticloadbalancingv2,
    aws_elasticloadbalancingv2_actions,
    aws_elasticloadbalancingv2_targets,
    aws_elasticsearch,
    aws_emr,
    aws_emrcontainers,
    aws_emrserverless,
    aws_entityresolution,
    aws_events,
    aws_events_targets,
    aws_eventschemas,
    aws_evidently,
    aws_finspace,
    aws_fis,
    aws_fms,
    aws_forecast,
    aws_frauddetector,
    aws_fsx,
    aws_gamelift,
    aws_globalaccelerator,
    aws_globalaccelerator_endpoints,
    aws_glue,
    aws_grafana,
    aws_greengrass,
    aws_greengrassv2,
    aws_groundstation,
    aws_guardduty,
    aws_healthimaging,
    aws_healthlake,
    aws_iam,
    aws_identitystore,
    aws_imagebuilder,
    aws_inspector,
    aws_inspectorv2,
    aws_internetmonitor,
    aws_iot,
    aws_iot1click,
    aws_iotanalytics,
    aws_iotcoredeviceadvisor,
    aws_iotevents,
    aws_iotfleethub,
    aws_iotfleetwise,
    aws_iotsitewise,
    aws_iotthingsgraph,
    aws_iottwinmaker,
    aws_iotwireless,
    aws_ivs,
    aws_ivschat,
    aws_kafkaconnect,
    aws_kendra,
    aws_kendraranking,
    aws_kinesis,
    aws_kinesisanalytics,
    aws_kinesisanalyticsv2,
    aws_kinesisfirehose,
    aws_kinesisvideo,
    aws_kms,
    aws_lakeformation,
    aws_lambda,
    aws_lambda_destinations,
    aws_lambda_event_sources,
    aws_lambda_nodejs,
    aws_lex,
    aws_licensemanager,
    aws_lightsail,
    aws_location,
    aws_logs,
    aws_logs_destinations,
    aws_lookoutequipment,
    aws_lookoutmetrics,
    aws_lookoutvision,
    aws_m2,
    aws_macie,
    aws_managedblockchain,
    aws_mediaconnect,
    aws_mediaconvert,
    aws_medialive,
    aws_mediapackage,
    aws_mediapackagev2,
    aws_mediastore,
    aws_mediatailor,
    aws_memorydb,
    aws_msk,
    aws_mwaa,
    aws_neptune,
    aws_networkfirewall,
    aws_networkmanager,
    aws_nimblestudio,
    aws_oam,
    aws_omics,
    aws_opensearchserverless,
    aws_opensearchservice,
    aws_opsworks,
    aws_opsworkscm,
    aws_organizations,
    aws_osis,
    aws_panorama,
    aws_pcaconnectorad,
    aws_personalize,
    aws_pinpoint,
    aws_pinpointemail,
    aws_pipes,
    aws_proton,
    aws_qldb,
    aws_quicksight,
    aws_ram,
    aws_rds,
    aws_redshift,
    aws_redshiftserverless,
    aws_refactorspaces,
    aws_rekognition,
    aws_resiliencehub,
    aws_resourceexplorer2,
    aws_resourcegroups,
    aws_robomaker,
    aws_rolesanywhere,
    aws_route53,
    aws_route53_patterns,
    aws_route53_targets,
    aws_route53recoverycontrol,
    aws_route53recoveryreadiness,
    aws_route53resolver,
    aws_rum,
    aws_s3,
    aws_s3_assets,
    aws_s3_deployment,
    aws_s3_notifications,
    aws_s3objectlambda,
    aws_s3outposts,
    aws_sagemaker,
    aws_sam,
    aws_scheduler,
    aws_sdb,
    aws_secretsmanager,
    aws_securityhub,
    aws_servicecatalog,
    aws_servicecatalogappregistry,
    aws_servicediscovery,
    aws_ses,
    aws_ses_actions,
    aws_shield,
    aws_signer,
    aws_simspaceweaver,
    aws_sns,
    aws_sns_subscriptions,
    aws_sqs,
    aws_ssm,
    aws_ssmcontacts,
    aws_ssmincidents,
    aws_sso,
    aws_stepfunctions,
    aws_stepfunctions_tasks,
    aws_supportapp,
    aws_synthetics,
    aws_systemsmanagersap,
    aws_timestream,
    aws_transfer,
    aws_verifiedpermissions,
    aws_voiceid,
    aws_vpclattice,
    aws_waf,
    aws_wafregional,
    aws_wafv2,
    aws_wisdom,
    aws_workspaces,
    aws_workspacesweb,
    aws_xray,
    cloud_assembly_schema,
    cloudformation_include,
    custom_resources,
    cx_api,
    lambda_layer_awscli,
    lambda_layer_kubectl,
    lambda_layer_node_proxy_agent,
    pipelines,
    region_info,
    triggers,
    constructs,
]:
    for name in dir(mod):
        obj = getattr(mod, name)
        if hasattr(obj, 'update_forward_refs'):
            try:
                obj.update_forward_refs()
            except Exception as e:
                print('f', mod, name, e)

core.ModuleModel.update_forward_refs()
constructs.ModuleModel.update_forward_refs()
alexa_ask.ModuleModel.update_forward_refs()
assertions.ModuleModel.update_forward_refs()
assets.ModuleModel.update_forward_refs()
aws_accessanalyzer.ModuleModel.update_forward_refs()
aws_acmpca.ModuleModel.update_forward_refs()
aws_amazonmq.ModuleModel.update_forward_refs()
aws_amplify.ModuleModel.update_forward_refs()
aws_amplifyuibuilder.ModuleModel.update_forward_refs()
aws_apigateway.ModuleModel.update_forward_refs()
aws_apigatewayv2.ModuleModel.update_forward_refs()
aws_appconfig.ModuleModel.update_forward_refs()
aws_appflow.ModuleModel.update_forward_refs()
aws_appintegrations.ModuleModel.update_forward_refs()
aws_applicationautoscaling.ModuleModel.update_forward_refs()
aws_applicationinsights.ModuleModel.update_forward_refs()
aws_appmesh.ModuleModel.update_forward_refs()
aws_apprunner.ModuleModel.update_forward_refs()
aws_appstream.ModuleModel.update_forward_refs()
aws_appsync.ModuleModel.update_forward_refs()
aws_aps.ModuleModel.update_forward_refs()
aws_athena.ModuleModel.update_forward_refs()
aws_auditmanager.ModuleModel.update_forward_refs()
aws_autoscaling.ModuleModel.update_forward_refs()
aws_autoscaling_common.ModuleModel.update_forward_refs()
aws_autoscaling_hooktargets.ModuleModel.update_forward_refs()
aws_autoscalingplans.ModuleModel.update_forward_refs()
aws_backup.ModuleModel.update_forward_refs()
aws_backupgateway.ModuleModel.update_forward_refs()
aws_batch.ModuleModel.update_forward_refs()
aws_billingconductor.ModuleModel.update_forward_refs()
aws_budgets.ModuleModel.update_forward_refs()
aws_cassandra.ModuleModel.update_forward_refs()
aws_ce.ModuleModel.update_forward_refs()
aws_certificatemanager.ModuleModel.update_forward_refs()
aws_chatbot.ModuleModel.update_forward_refs()
aws_cleanrooms.ModuleModel.update_forward_refs()
aws_cloud9.ModuleModel.update_forward_refs()
aws_cloudformation.ModuleModel.update_forward_refs()
aws_cloudfront.ModuleModel.update_forward_refs()
aws_cloudfront_origins.ModuleModel.update_forward_refs()
aws_cloudtrail.ModuleModel.update_forward_refs()
aws_cloudwatch.ModuleModel.update_forward_refs()
aws_cloudwatch_actions.ModuleModel.update_forward_refs()
aws_codebuild.ModuleModel.update_forward_refs()
aws_codecommit.ModuleModel.update_forward_refs()
aws_codedeploy.ModuleModel.update_forward_refs()
aws_codeguruprofiler.ModuleModel.update_forward_refs()
aws_codegurureviewer.ModuleModel.update_forward_refs()
aws_codepipeline.ModuleModel.update_forward_refs()
aws_codepipeline_actions.ModuleModel.update_forward_refs()
aws_codestar.ModuleModel.update_forward_refs()
aws_codestarconnections.ModuleModel.update_forward_refs()
aws_codestarnotifications.ModuleModel.update_forward_refs()
aws_cognito.ModuleModel.update_forward_refs()
aws_comprehend.ModuleModel.update_forward_refs()
aws_config.ModuleModel.update_forward_refs()
aws_connect.ModuleModel.update_forward_refs()
aws_connectcampaigns.ModuleModel.update_forward_refs()
aws_controltower.ModuleModel.update_forward_refs()
aws_cur.ModuleModel.update_forward_refs()
aws_customerprofiles.ModuleModel.update_forward_refs()
aws_databrew.ModuleModel.update_forward_refs()
aws_datapipeline.ModuleModel.update_forward_refs()
aws_datasync.ModuleModel.update_forward_refs()
aws_dax.ModuleModel.update_forward_refs()
aws_detective.ModuleModel.update_forward_refs()
aws_devicefarm.ModuleModel.update_forward_refs()
aws_devopsguru.ModuleModel.update_forward_refs()
aws_directoryservice.ModuleModel.update_forward_refs()
aws_dlm.ModuleModel.update_forward_refs()
aws_dms.ModuleModel.update_forward_refs()
aws_docdb.ModuleModel.update_forward_refs()
aws_docdbelastic.ModuleModel.update_forward_refs()
aws_dynamodb.ModuleModel.update_forward_refs()
aws_ec2.ModuleModel.update_forward_refs()
aws_ecr.ModuleModel.update_forward_refs()
aws_ecr_assets.ModuleModel.update_forward_refs()
aws_ecs.ModuleModel.update_forward_refs()
aws_ecs_patterns.ModuleModel.update_forward_refs()
aws_efs.ModuleModel.update_forward_refs()
aws_eks.ModuleModel.update_forward_refs()
aws_elasticache.ModuleModel.update_forward_refs()
aws_elasticbeanstalk.ModuleModel.update_forward_refs()
aws_elasticloadbalancing.ModuleModel.update_forward_refs()
aws_elasticloadbalancingv2.ModuleModel.update_forward_refs()
aws_elasticloadbalancingv2_actions.ModuleModel.update_forward_refs()
aws_elasticloadbalancingv2_targets.ModuleModel.update_forward_refs()
aws_elasticsearch.ModuleModel.update_forward_refs()
aws_emr.ModuleModel.update_forward_refs()
aws_emrcontainers.ModuleModel.update_forward_refs()
aws_emrserverless.ModuleModel.update_forward_refs()
aws_entityresolution.ModuleModel.update_forward_refs()
aws_events.ModuleModel.update_forward_refs()
aws_events_targets.ModuleModel.update_forward_refs()
aws_eventschemas.ModuleModel.update_forward_refs()
aws_evidently.ModuleModel.update_forward_refs()
aws_finspace.ModuleModel.update_forward_refs()
aws_fis.ModuleModel.update_forward_refs()
aws_fms.ModuleModel.update_forward_refs()
aws_forecast.ModuleModel.update_forward_refs()
aws_frauddetector.ModuleModel.update_forward_refs()
aws_fsx.ModuleModel.update_forward_refs()
aws_gamelift.ModuleModel.update_forward_refs()
aws_globalaccelerator.ModuleModel.update_forward_refs()
aws_globalaccelerator_endpoints.ModuleModel.update_forward_refs()
aws_glue.ModuleModel.update_forward_refs()
aws_grafana.ModuleModel.update_forward_refs()
aws_greengrass.ModuleModel.update_forward_refs()
aws_greengrassv2.ModuleModel.update_forward_refs()
aws_groundstation.ModuleModel.update_forward_refs()
aws_guardduty.ModuleModel.update_forward_refs()
aws_healthimaging.ModuleModel.update_forward_refs()
aws_healthlake.ModuleModel.update_forward_refs()
aws_iam.ModuleModel.update_forward_refs()
aws_identitystore.ModuleModel.update_forward_refs()
aws_imagebuilder.ModuleModel.update_forward_refs()
aws_inspector.ModuleModel.update_forward_refs()
aws_inspectorv2.ModuleModel.update_forward_refs()
aws_internetmonitor.ModuleModel.update_forward_refs()
aws_iot.ModuleModel.update_forward_refs()
aws_iot1click.ModuleModel.update_forward_refs()
aws_iotanalytics.ModuleModel.update_forward_refs()
aws_iotcoredeviceadvisor.ModuleModel.update_forward_refs()
aws_iotevents.ModuleModel.update_forward_refs()
aws_iotfleethub.ModuleModel.update_forward_refs()
aws_iotfleetwise.ModuleModel.update_forward_refs()
aws_iotsitewise.ModuleModel.update_forward_refs()
aws_iotthingsgraph.ModuleModel.update_forward_refs()
aws_iottwinmaker.ModuleModel.update_forward_refs()
aws_iotwireless.ModuleModel.update_forward_refs()
aws_ivs.ModuleModel.update_forward_refs()
aws_ivschat.ModuleModel.update_forward_refs()
aws_kafkaconnect.ModuleModel.update_forward_refs()
aws_kendra.ModuleModel.update_forward_refs()
aws_kendraranking.ModuleModel.update_forward_refs()
aws_kinesis.ModuleModel.update_forward_refs()
aws_kinesisanalytics.ModuleModel.update_forward_refs()
aws_kinesisanalyticsv2.ModuleModel.update_forward_refs()
aws_kinesisfirehose.ModuleModel.update_forward_refs()
aws_kinesisvideo.ModuleModel.update_forward_refs()
aws_kms.ModuleModel.update_forward_refs()
aws_lakeformation.ModuleModel.update_forward_refs()
aws_lambda.ModuleModel.update_forward_refs()
aws_lambda_destinations.ModuleModel.update_forward_refs()
aws_lambda_event_sources.ModuleModel.update_forward_refs()
aws_lambda_nodejs.ModuleModel.update_forward_refs()
aws_lex.ModuleModel.update_forward_refs()
aws_licensemanager.ModuleModel.update_forward_refs()
aws_lightsail.ModuleModel.update_forward_refs()
aws_location.ModuleModel.update_forward_refs()
aws_logs.ModuleModel.update_forward_refs()
aws_logs_destinations.ModuleModel.update_forward_refs()
aws_lookoutequipment.ModuleModel.update_forward_refs()
aws_lookoutmetrics.ModuleModel.update_forward_refs()
aws_lookoutvision.ModuleModel.update_forward_refs()
aws_m2.ModuleModel.update_forward_refs()
aws_macie.ModuleModel.update_forward_refs()
aws_managedblockchain.ModuleModel.update_forward_refs()
aws_mediaconnect.ModuleModel.update_forward_refs()
aws_mediaconvert.ModuleModel.update_forward_refs()
aws_medialive.ModuleModel.update_forward_refs()
aws_mediapackage.ModuleModel.update_forward_refs()
aws_mediapackagev2.ModuleModel.update_forward_refs()
aws_mediastore.ModuleModel.update_forward_refs()
aws_mediatailor.ModuleModel.update_forward_refs()
aws_memorydb.ModuleModel.update_forward_refs()
aws_msk.ModuleModel.update_forward_refs()
aws_mwaa.ModuleModel.update_forward_refs()
aws_neptune.ModuleModel.update_forward_refs()
aws_networkfirewall.ModuleModel.update_forward_refs()
aws_networkmanager.ModuleModel.update_forward_refs()
aws_nimblestudio.ModuleModel.update_forward_refs()
aws_oam.ModuleModel.update_forward_refs()
aws_omics.ModuleModel.update_forward_refs()
aws_opensearchserverless.ModuleModel.update_forward_refs()
aws_opensearchservice.ModuleModel.update_forward_refs()
aws_opsworks.ModuleModel.update_forward_refs()
aws_opsworkscm.ModuleModel.update_forward_refs()
aws_organizations.ModuleModel.update_forward_refs()
aws_osis.ModuleModel.update_forward_refs()
aws_panorama.ModuleModel.update_forward_refs()
aws_pcaconnectorad.ModuleModel.update_forward_refs()
aws_personalize.ModuleModel.update_forward_refs()
aws_pinpoint.ModuleModel.update_forward_refs()
aws_pinpointemail.ModuleModel.update_forward_refs()
aws_pipes.ModuleModel.update_forward_refs()
aws_proton.ModuleModel.update_forward_refs()
aws_qldb.ModuleModel.update_forward_refs()
aws_quicksight.ModuleModel.update_forward_refs()
aws_ram.ModuleModel.update_forward_refs()
aws_rds.ModuleModel.update_forward_refs()
aws_redshift.ModuleModel.update_forward_refs()
aws_redshiftserverless.ModuleModel.update_forward_refs()
aws_refactorspaces.ModuleModel.update_forward_refs()
aws_rekognition.ModuleModel.update_forward_refs()
aws_resiliencehub.ModuleModel.update_forward_refs()
aws_resourceexplorer2.ModuleModel.update_forward_refs()
aws_resourcegroups.ModuleModel.update_forward_refs()
aws_robomaker.ModuleModel.update_forward_refs()
aws_rolesanywhere.ModuleModel.update_forward_refs()
aws_route53.ModuleModel.update_forward_refs()
aws_route53_patterns.ModuleModel.update_forward_refs()
aws_route53_targets.ModuleModel.update_forward_refs()
aws_route53recoverycontrol.ModuleModel.update_forward_refs()
aws_route53recoveryreadiness.ModuleModel.update_forward_refs()
aws_route53resolver.ModuleModel.update_forward_refs()
aws_rum.ModuleModel.update_forward_refs()
aws_s3.ModuleModel.update_forward_refs()
aws_s3_assets.ModuleModel.update_forward_refs()
aws_s3_deployment.ModuleModel.update_forward_refs()
aws_s3_notifications.ModuleModel.update_forward_refs()
aws_s3objectlambda.ModuleModel.update_forward_refs()
aws_s3outposts.ModuleModel.update_forward_refs()
aws_sagemaker.ModuleModel.update_forward_refs()
aws_sam.ModuleModel.update_forward_refs()
aws_scheduler.ModuleModel.update_forward_refs()
aws_sdb.ModuleModel.update_forward_refs()
aws_secretsmanager.ModuleModel.update_forward_refs()
aws_securityhub.ModuleModel.update_forward_refs()
aws_servicecatalog.ModuleModel.update_forward_refs()
aws_servicecatalogappregistry.ModuleModel.update_forward_refs()
aws_servicediscovery.ModuleModel.update_forward_refs()
aws_ses.ModuleModel.update_forward_refs()
aws_ses_actions.ModuleModel.update_forward_refs()
aws_shield.ModuleModel.update_forward_refs()
aws_signer.ModuleModel.update_forward_refs()
aws_simspaceweaver.ModuleModel.update_forward_refs()
aws_sns.ModuleModel.update_forward_refs()
aws_sns_subscriptions.ModuleModel.update_forward_refs()
aws_sqs.ModuleModel.update_forward_refs()
aws_ssm.ModuleModel.update_forward_refs()
aws_ssmcontacts.ModuleModel.update_forward_refs()
aws_ssmincidents.ModuleModel.update_forward_refs()
aws_sso.ModuleModel.update_forward_refs()
aws_stepfunctions.ModuleModel.update_forward_refs()
aws_stepfunctions_tasks.ModuleModel.update_forward_refs()
aws_supportapp.ModuleModel.update_forward_refs()
aws_synthetics.ModuleModel.update_forward_refs()
aws_systemsmanagersap.ModuleModel.update_forward_refs()
aws_timestream.ModuleModel.update_forward_refs()
aws_transfer.ModuleModel.update_forward_refs()
aws_verifiedpermissions.ModuleModel.update_forward_refs()
aws_voiceid.ModuleModel.update_forward_refs()
aws_vpclattice.ModuleModel.update_forward_refs()
aws_waf.ModuleModel.update_forward_refs()
aws_wafregional.ModuleModel.update_forward_refs()
aws_wafv2.ModuleModel.update_forward_refs()
aws_wisdom.ModuleModel.update_forward_refs()
aws_workspaces.ModuleModel.update_forward_refs()
aws_workspacesweb.ModuleModel.update_forward_refs()
aws_xray.ModuleModel.update_forward_refs()
cloud_assembly_schema.ModuleModel.update_forward_refs()
cloudformation_include.ModuleModel.update_forward_refs()
custom_resources.ModuleModel.update_forward_refs()
cx_api.ModuleModel.update_forward_refs()
lambda_layer_awscli.ModuleModel.update_forward_refs()
lambda_layer_kubectl.ModuleModel.update_forward_refs()
lambda_layer_node_proxy_agent.ModuleModel.update_forward_refs()
pipelines.ModuleModel.update_forward_refs()
region_info.ModuleModel.update_forward_refs()
triggers.ModuleModel.update_forward_refs()


class MegaModel(pydantic.BaseModel):
    alexa_ask_: typing.Optional[alexa_ask.ModuleModel] = pydantic.Field(None, alias='alexa_ask')
    assertions_: typing.Optional[assertions.ModuleModel] = pydantic.Field(None, alias='assertions')
    assets_: typing.Optional[assets.ModuleModel] = pydantic.Field(None, alias='assets')
    aws_accessanalyzer_: typing.Optional[aws_accessanalyzer.ModuleModel] = pydantic.Field(None, alias='aws_accessanalyzer')
    aws_acmpca_: typing.Optional[aws_acmpca.ModuleModel] = pydantic.Field(None, alias='aws_acmpca')
    aws_amazonmq_: typing.Optional[aws_amazonmq.ModuleModel] = pydantic.Field(None, alias='aws_amazonmq')
    aws_amplify_: typing.Optional[aws_amplify.ModuleModel] = pydantic.Field(None, alias='aws_amplify')
    aws_amplifyuibuilder_: typing.Optional[aws_amplifyuibuilder.ModuleModel] = pydantic.Field(None, alias='aws_amplifyuibuilder')
    aws_apigateway_: typing.Optional[aws_apigateway.ModuleModel] = pydantic.Field(None, alias='aws_apigateway')
    aws_apigatewayv2_: typing.Optional[aws_apigatewayv2.ModuleModel] = pydantic.Field(None, alias='aws_apigatewayv2')
    aws_appconfig_: typing.Optional[aws_appconfig.ModuleModel] = pydantic.Field(None, alias='aws_appconfig')
    aws_appflow_: typing.Optional[aws_appflow.ModuleModel] = pydantic.Field(None, alias='aws_appflow')
    aws_appintegrations_: typing.Optional[aws_appintegrations.ModuleModel] = pydantic.Field(None, alias='aws_appintegrations')
    aws_applicationautoscaling_: typing.Optional[aws_applicationautoscaling.ModuleModel] = pydantic.Field(None, alias='aws_applicationautoscaling')
    aws_applicationinsights_: typing.Optional[aws_applicationinsights.ModuleModel] = pydantic.Field(None, alias='aws_applicationinsights')
    aws_appmesh_: typing.Optional[aws_appmesh.ModuleModel] = pydantic.Field(None, alias='aws_appmesh')
    aws_apprunner_: typing.Optional[aws_apprunner.ModuleModel] = pydantic.Field(None, alias='aws_apprunner')
    aws_appstream_: typing.Optional[aws_appstream.ModuleModel] = pydantic.Field(None, alias='aws_appstream')
    aws_appsync_: typing.Optional[aws_appsync.ModuleModel] = pydantic.Field(None, alias='aws_appsync')
    aws_aps_: typing.Optional[aws_aps.ModuleModel] = pydantic.Field(None, alias='aws_aps')
    aws_athena_: typing.Optional[aws_athena.ModuleModel] = pydantic.Field(None, alias='aws_athena')
    aws_auditmanager_: typing.Optional[aws_auditmanager.ModuleModel] = pydantic.Field(None, alias='aws_auditmanager')
    aws_autoscaling_: typing.Optional[aws_autoscaling.ModuleModel] = pydantic.Field(None, alias='aws_autoscaling')
    aws_autoscaling_common_: typing.Optional[aws_autoscaling_common.ModuleModel] = pydantic.Field(None, alias='aws_autoscaling_common')
    aws_autoscaling_hooktargets_: typing.Optional[aws_autoscaling_hooktargets.ModuleModel] = pydantic.Field(None, alias='aws_autoscaling_hooktargets')
    aws_autoscalingplans_: typing.Optional[aws_autoscalingplans.ModuleModel] = pydantic.Field(None, alias='aws_autoscalingplans')
    aws_backup_: typing.Optional[aws_backup.ModuleModel] = pydantic.Field(None, alias='aws_backup')
    aws_backupgateway_: typing.Optional[aws_backupgateway.ModuleModel] = pydantic.Field(None, alias='aws_backupgateway')
    aws_batch_: typing.Optional[aws_batch.ModuleModel] = pydantic.Field(None, alias='aws_batch')
    aws_billingconductor_: typing.Optional[aws_billingconductor.ModuleModel] = pydantic.Field(None, alias='aws_billingconductor')
    aws_budgets_: typing.Optional[aws_budgets.ModuleModel] = pydantic.Field(None, alias='aws_budgets')
    aws_cassandra_: typing.Optional[aws_cassandra.ModuleModel] = pydantic.Field(None, alias='aws_cassandra')
    aws_ce_: typing.Optional[aws_ce.ModuleModel] = pydantic.Field(None, alias='aws_ce')
    aws_certificatemanager_: typing.Optional[aws_certificatemanager.ModuleModel] = pydantic.Field(None, alias='aws_certificatemanager')
    aws_chatbot_: typing.Optional[aws_chatbot.ModuleModel] = pydantic.Field(None, alias='aws_chatbot')
    aws_cleanrooms_: typing.Optional[aws_cleanrooms.ModuleModel] = pydantic.Field(None, alias='aws_cleanrooms')
    aws_cloud9_: typing.Optional[aws_cloud9.ModuleModel] = pydantic.Field(None, alias='aws_cloud9')
    aws_cloudformation_: typing.Optional[aws_cloudformation.ModuleModel] = pydantic.Field(None, alias='aws_cloudformation')
    aws_cloudfront_: typing.Optional[aws_cloudfront.ModuleModel] = pydantic.Field(None, alias='aws_cloudfront')
    aws_cloudfront_origins_: typing.Optional[aws_cloudfront_origins.ModuleModel] = pydantic.Field(None, alias='aws_cloudfront_origins')
    aws_cloudtrail_: typing.Optional[aws_cloudtrail.ModuleModel] = pydantic.Field(None, alias='aws_cloudtrail')
    aws_cloudwatch_: typing.Optional[aws_cloudwatch.ModuleModel] = pydantic.Field(None, alias='aws_cloudwatch')
    aws_cloudwatch_actions_: typing.Optional[aws_cloudwatch_actions.ModuleModel] = pydantic.Field(None, alias='aws_cloudwatch_actions')
    aws_codebuild_: typing.Optional[aws_codebuild.ModuleModel] = pydantic.Field(None, alias='aws_codebuild')
    aws_codecommit_: typing.Optional[aws_codecommit.ModuleModel] = pydantic.Field(None, alias='aws_codecommit')
    aws_codedeploy_: typing.Optional[aws_codedeploy.ModuleModel] = pydantic.Field(None, alias='aws_codedeploy')
    aws_codeguruprofiler_: typing.Optional[aws_codeguruprofiler.ModuleModel] = pydantic.Field(None, alias='aws_codeguruprofiler')
    aws_codegurureviewer_: typing.Optional[aws_codegurureviewer.ModuleModel] = pydantic.Field(None, alias='aws_codegurureviewer')
    aws_codepipeline_: typing.Optional[aws_codepipeline.ModuleModel] = pydantic.Field(None, alias='aws_codepipeline')
    aws_codepipeline_actions_: typing.Optional[aws_codepipeline_actions.ModuleModel] = pydantic.Field(None, alias='aws_codepipeline_actions')
    aws_codestar_: typing.Optional[aws_codestar.ModuleModel] = pydantic.Field(None, alias='aws_codestar')
    aws_codestarconnections_: typing.Optional[aws_codestarconnections.ModuleModel] = pydantic.Field(None, alias='aws_codestarconnections')
    aws_codestarnotifications_: typing.Optional[aws_codestarnotifications.ModuleModel] = pydantic.Field(None, alias='aws_codestarnotifications')
    aws_cognito_: typing.Optional[aws_cognito.ModuleModel] = pydantic.Field(None, alias='aws_cognito')
    aws_comprehend_: typing.Optional[aws_comprehend.ModuleModel] = pydantic.Field(None, alias='aws_comprehend')
    aws_config_: typing.Optional[aws_config.ModuleModel] = pydantic.Field(None, alias='aws_config')
    aws_connect_: typing.Optional[aws_connect.ModuleModel] = pydantic.Field(None, alias='aws_connect')
    aws_connectcampaigns_: typing.Optional[aws_connectcampaigns.ModuleModel] = pydantic.Field(None, alias='aws_connectcampaigns')
    aws_controltower_: typing.Optional[aws_controltower.ModuleModel] = pydantic.Field(None, alias='aws_controltower')
    aws_cur_: typing.Optional[aws_cur.ModuleModel] = pydantic.Field(None, alias='aws_cur')
    aws_customerprofiles_: typing.Optional[aws_customerprofiles.ModuleModel] = pydantic.Field(None, alias='aws_customerprofiles')
    aws_databrew_: typing.Optional[aws_databrew.ModuleModel] = pydantic.Field(None, alias='aws_databrew')
    aws_datapipeline_: typing.Optional[aws_datapipeline.ModuleModel] = pydantic.Field(None, alias='aws_datapipeline')
    aws_datasync_: typing.Optional[aws_datasync.ModuleModel] = pydantic.Field(None, alias='aws_datasync')
    aws_dax_: typing.Optional[aws_dax.ModuleModel] = pydantic.Field(None, alias='aws_dax')
    aws_detective_: typing.Optional[aws_detective.ModuleModel] = pydantic.Field(None, alias='aws_detective')
    aws_devicefarm_: typing.Optional[aws_devicefarm.ModuleModel] = pydantic.Field(None, alias='aws_devicefarm')
    aws_devopsguru_: typing.Optional[aws_devopsguru.ModuleModel] = pydantic.Field(None, alias='aws_devopsguru')
    aws_directoryservice_: typing.Optional[aws_directoryservice.ModuleModel] = pydantic.Field(None, alias='aws_directoryservice')
    aws_dlm_: typing.Optional[aws_dlm.ModuleModel] = pydantic.Field(None, alias='aws_dlm')
    aws_dms_: typing.Optional[aws_dms.ModuleModel] = pydantic.Field(None, alias='aws_dms')
    aws_docdb_: typing.Optional[aws_docdb.ModuleModel] = pydantic.Field(None, alias='aws_docdb')
    aws_docdbelastic_: typing.Optional[aws_docdbelastic.ModuleModel] = pydantic.Field(None, alias='aws_docdbelastic')
    aws_dynamodb_: typing.Optional[aws_dynamodb.ModuleModel] = pydantic.Field(None, alias='aws_dynamodb')
    aws_ec2_: typing.Optional[aws_ec2.ModuleModel] = pydantic.Field(None, alias='aws_ec2')
    aws_ecr_: typing.Optional[aws_ecr.ModuleModel] = pydantic.Field(None, alias='aws_ecr')
    aws_ecr_assets_: typing.Optional[aws_ecr_assets.ModuleModel] = pydantic.Field(None, alias='aws_ecr_assets')
    aws_ecs_: typing.Optional[aws_ecs.ModuleModel] = pydantic.Field(None, alias='aws_ecs')
    aws_ecs_patterns_: typing.Optional[aws_ecs_patterns.ModuleModel] = pydantic.Field(None, alias='aws_ecs_patterns')
    aws_efs_: typing.Optional[aws_efs.ModuleModel] = pydantic.Field(None, alias='aws_efs')
    aws_eks_: typing.Optional[aws_eks.ModuleModel] = pydantic.Field(None, alias='aws_eks')
    aws_elasticache_: typing.Optional[aws_elasticache.ModuleModel] = pydantic.Field(None, alias='aws_elasticache')
    aws_elasticbeanstalk_: typing.Optional[aws_elasticbeanstalk.ModuleModel] = pydantic.Field(None, alias='aws_elasticbeanstalk')
    aws_elasticloadbalancing_: typing.Optional[aws_elasticloadbalancing.ModuleModel] = pydantic.Field(None, alias='aws_elasticloadbalancing')
    aws_elasticloadbalancingv2_: typing.Optional[aws_elasticloadbalancingv2.ModuleModel] = pydantic.Field(None, alias='aws_elasticloadbalancingv2')
    aws_elasticloadbalancingv2_actions_: typing.Optional[aws_elasticloadbalancingv2_actions.ModuleModel] = pydantic.Field(None, alias='aws_elasticloadbalancingv2_actions')
    aws_elasticloadbalancingv2_targets_: typing.Optional[aws_elasticloadbalancingv2_targets.ModuleModel] = pydantic.Field(None, alias='aws_elasticloadbalancingv2_targets')
    aws_elasticsearch_: typing.Optional[aws_elasticsearch.ModuleModel] = pydantic.Field(None, alias='aws_elasticsearch')
    aws_emr_: typing.Optional[aws_emr.ModuleModel] = pydantic.Field(None, alias='aws_emr')
    aws_emrcontainers_: typing.Optional[aws_emrcontainers.ModuleModel] = pydantic.Field(None, alias='aws_emrcontainers')
    aws_emrserverless_: typing.Optional[aws_emrserverless.ModuleModel] = pydantic.Field(None, alias='aws_emrserverless')
    aws_entityresolution_: typing.Optional[aws_entityresolution.ModuleModel] = pydantic.Field(None, alias='aws_entityresolution')
    aws_events_: typing.Optional[aws_events.ModuleModel] = pydantic.Field(None, alias='aws_events')
    aws_events_targets_: typing.Optional[aws_events_targets.ModuleModel] = pydantic.Field(None, alias='aws_events_targets')
    aws_eventschemas_: typing.Optional[aws_eventschemas.ModuleModel] = pydantic.Field(None, alias='aws_eventschemas')
    aws_evidently_: typing.Optional[aws_evidently.ModuleModel] = pydantic.Field(None, alias='aws_evidently')
    aws_finspace_: typing.Optional[aws_finspace.ModuleModel] = pydantic.Field(None, alias='aws_finspace')
    aws_fis_: typing.Optional[aws_fis.ModuleModel] = pydantic.Field(None, alias='aws_fis')
    aws_fms_: typing.Optional[aws_fms.ModuleModel] = pydantic.Field(None, alias='aws_fms')
    aws_forecast_: typing.Optional[aws_forecast.ModuleModel] = pydantic.Field(None, alias='aws_forecast')
    aws_frauddetector_: typing.Optional[aws_frauddetector.ModuleModel] = pydantic.Field(None, alias='aws_frauddetector')
    aws_fsx_: typing.Optional[aws_fsx.ModuleModel] = pydantic.Field(None, alias='aws_fsx')
    aws_gamelift_: typing.Optional[aws_gamelift.ModuleModel] = pydantic.Field(None, alias='aws_gamelift')
    aws_globalaccelerator_: typing.Optional[aws_globalaccelerator.ModuleModel] = pydantic.Field(None, alias='aws_globalaccelerator')
    aws_globalaccelerator_endpoints_: typing.Optional[aws_globalaccelerator_endpoints.ModuleModel] = pydantic.Field(None, alias='aws_globalaccelerator_endpoints')
    aws_glue_: typing.Optional[aws_glue.ModuleModel] = pydantic.Field(None, alias='aws_glue')
    aws_grafana_: typing.Optional[aws_grafana.ModuleModel] = pydantic.Field(None, alias='aws_grafana')
    aws_greengrass_: typing.Optional[aws_greengrass.ModuleModel] = pydantic.Field(None, alias='aws_greengrass')
    aws_greengrassv2_: typing.Optional[aws_greengrassv2.ModuleModel] = pydantic.Field(None, alias='aws_greengrassv2')
    aws_groundstation_: typing.Optional[aws_groundstation.ModuleModel] = pydantic.Field(None, alias='aws_groundstation')
    aws_guardduty_: typing.Optional[aws_guardduty.ModuleModel] = pydantic.Field(None, alias='aws_guardduty')
    aws_healthimaging_: typing.Optional[aws_healthimaging.ModuleModel] = pydantic.Field(None, alias='aws_healthimaging')
    aws_healthlake_: typing.Optional[aws_healthlake.ModuleModel] = pydantic.Field(None, alias='aws_healthlake')
    aws_iam_: typing.Optional[aws_iam.ModuleModel] = pydantic.Field(None, alias='aws_iam')
    aws_identitystore_: typing.Optional[aws_identitystore.ModuleModel] = pydantic.Field(None, alias='aws_identitystore')
    aws_imagebuilder_: typing.Optional[aws_imagebuilder.ModuleModel] = pydantic.Field(None, alias='aws_imagebuilder')
    aws_inspector_: typing.Optional[aws_inspector.ModuleModel] = pydantic.Field(None, alias='aws_inspector')
    aws_inspectorv2_: typing.Optional[aws_inspectorv2.ModuleModel] = pydantic.Field(None, alias='aws_inspectorv2')
    aws_internetmonitor_: typing.Optional[aws_internetmonitor.ModuleModel] = pydantic.Field(None, alias='aws_internetmonitor')
    aws_iot_: typing.Optional[aws_iot.ModuleModel] = pydantic.Field(None, alias='aws_iot')
    aws_iot1click_: typing.Optional[aws_iot1click.ModuleModel] = pydantic.Field(None, alias='aws_iot1click')
    aws_iotanalytics_: typing.Optional[aws_iotanalytics.ModuleModel] = pydantic.Field(None, alias='aws_iotanalytics')
    aws_iotcoredeviceadvisor_: typing.Optional[aws_iotcoredeviceadvisor.ModuleModel] = pydantic.Field(None, alias='aws_iotcoredeviceadvisor')
    aws_iotevents_: typing.Optional[aws_iotevents.ModuleModel] = pydantic.Field(None, alias='aws_iotevents')
    aws_iotfleethub_: typing.Optional[aws_iotfleethub.ModuleModel] = pydantic.Field(None, alias='aws_iotfleethub')
    aws_iotfleetwise_: typing.Optional[aws_iotfleetwise.ModuleModel] = pydantic.Field(None, alias='aws_iotfleetwise')
    aws_iotsitewise_: typing.Optional[aws_iotsitewise.ModuleModel] = pydantic.Field(None, alias='aws_iotsitewise')
    aws_iotthingsgraph_: typing.Optional[aws_iotthingsgraph.ModuleModel] = pydantic.Field(None, alias='aws_iotthingsgraph')
    aws_iottwinmaker_: typing.Optional[aws_iottwinmaker.ModuleModel] = pydantic.Field(None, alias='aws_iottwinmaker')
    aws_iotwireless_: typing.Optional[aws_iotwireless.ModuleModel] = pydantic.Field(None, alias='aws_iotwireless')
    aws_ivs_: typing.Optional[aws_ivs.ModuleModel] = pydantic.Field(None, alias='aws_ivs')
    aws_ivschat_: typing.Optional[aws_ivschat.ModuleModel] = pydantic.Field(None, alias='aws_ivschat')
    aws_kafkaconnect_: typing.Optional[aws_kafkaconnect.ModuleModel] = pydantic.Field(None, alias='aws_kafkaconnect')
    aws_kendra_: typing.Optional[aws_kendra.ModuleModel] = pydantic.Field(None, alias='aws_kendra')
    aws_kendraranking_: typing.Optional[aws_kendraranking.ModuleModel] = pydantic.Field(None, alias='aws_kendraranking')
    aws_kinesis_: typing.Optional[aws_kinesis.ModuleModel] = pydantic.Field(None, alias='aws_kinesis')
    aws_kinesisanalytics_: typing.Optional[aws_kinesisanalytics.ModuleModel] = pydantic.Field(None, alias='aws_kinesisanalytics')
    aws_kinesisanalyticsv2_: typing.Optional[aws_kinesisanalyticsv2.ModuleModel] = pydantic.Field(None, alias='aws_kinesisanalyticsv2')
    aws_kinesisfirehose_: typing.Optional[aws_kinesisfirehose.ModuleModel] = pydantic.Field(None, alias='aws_kinesisfirehose')
    aws_kinesisvideo_: typing.Optional[aws_kinesisvideo.ModuleModel] = pydantic.Field(None, alias='aws_kinesisvideo')
    aws_kms_: typing.Optional[aws_kms.ModuleModel] = pydantic.Field(None, alias='aws_kms')
    aws_lakeformation_: typing.Optional[aws_lakeformation.ModuleModel] = pydantic.Field(None, alias='aws_lakeformation')
    aws_lambda_: typing.Optional[aws_lambda.ModuleModel] = pydantic.Field(None, alias='aws_lambda')
    aws_lambda_destinations_: typing.Optional[aws_lambda_destinations.ModuleModel] = pydantic.Field(None, alias='aws_lambda_destinations')
    aws_lambda_event_sources_: typing.Optional[aws_lambda_event_sources.ModuleModel] = pydantic.Field(None, alias='aws_lambda_event_sources')
    aws_lambda_nodejs_: typing.Optional[aws_lambda_nodejs.ModuleModel] = pydantic.Field(None, alias='aws_lambda_nodejs')
    aws_lex_: typing.Optional[aws_lex.ModuleModel] = pydantic.Field(None, alias='aws_lex')
    aws_licensemanager_: typing.Optional[aws_licensemanager.ModuleModel] = pydantic.Field(None, alias='aws_licensemanager')
    aws_lightsail_: typing.Optional[aws_lightsail.ModuleModel] = pydantic.Field(None, alias='aws_lightsail')
    aws_location_: typing.Optional[aws_location.ModuleModel] = pydantic.Field(None, alias='aws_location')
    aws_logs_: typing.Optional[aws_logs.ModuleModel] = pydantic.Field(None, alias='aws_logs')
    aws_logs_destinations_: typing.Optional[aws_logs_destinations.ModuleModel] = pydantic.Field(None, alias='aws_logs_destinations')
    aws_lookoutequipment_: typing.Optional[aws_lookoutequipment.ModuleModel] = pydantic.Field(None, alias='aws_lookoutequipment')
    aws_lookoutmetrics_: typing.Optional[aws_lookoutmetrics.ModuleModel] = pydantic.Field(None, alias='aws_lookoutmetrics')
    aws_lookoutvision_: typing.Optional[aws_lookoutvision.ModuleModel] = pydantic.Field(None, alias='aws_lookoutvision')
    aws_m2_: typing.Optional[aws_m2.ModuleModel] = pydantic.Field(None, alias='aws_m2')
    aws_macie_: typing.Optional[aws_macie.ModuleModel] = pydantic.Field(None, alias='aws_macie')
    aws_managedblockchain_: typing.Optional[aws_managedblockchain.ModuleModel] = pydantic.Field(None, alias='aws_managedblockchain')
    aws_mediaconnect_: typing.Optional[aws_mediaconnect.ModuleModel] = pydantic.Field(None, alias='aws_mediaconnect')
    aws_mediaconvert_: typing.Optional[aws_mediaconvert.ModuleModel] = pydantic.Field(None, alias='aws_mediaconvert')
    aws_medialive_: typing.Optional[aws_medialive.ModuleModel] = pydantic.Field(None, alias='aws_medialive')
    aws_mediapackage_: typing.Optional[aws_mediapackage.ModuleModel] = pydantic.Field(None, alias='aws_mediapackage')
    aws_mediapackagev2_: typing.Optional[aws_mediapackagev2.ModuleModel] = pydantic.Field(None, alias='aws_mediapackagev2')
    aws_mediastore_: typing.Optional[aws_mediastore.ModuleModel] = pydantic.Field(None, alias='aws_mediastore')
    aws_mediatailor_: typing.Optional[aws_mediatailor.ModuleModel] = pydantic.Field(None, alias='aws_mediatailor')
    aws_memorydb_: typing.Optional[aws_memorydb.ModuleModel] = pydantic.Field(None, alias='aws_memorydb')
    aws_msk_: typing.Optional[aws_msk.ModuleModel] = pydantic.Field(None, alias='aws_msk')
    aws_mwaa_: typing.Optional[aws_mwaa.ModuleModel] = pydantic.Field(None, alias='aws_mwaa')
    aws_neptune_: typing.Optional[aws_neptune.ModuleModel] = pydantic.Field(None, alias='aws_neptune')
    aws_networkfirewall_: typing.Optional[aws_networkfirewall.ModuleModel] = pydantic.Field(None, alias='aws_networkfirewall')
    aws_networkmanager_: typing.Optional[aws_networkmanager.ModuleModel] = pydantic.Field(None, alias='aws_networkmanager')
    aws_nimblestudio_: typing.Optional[aws_nimblestudio.ModuleModel] = pydantic.Field(None, alias='aws_nimblestudio')
    aws_oam_: typing.Optional[aws_oam.ModuleModel] = pydantic.Field(None, alias='aws_oam')
    aws_omics_: typing.Optional[aws_omics.ModuleModel] = pydantic.Field(None, alias='aws_omics')
    aws_opensearchserverless_: typing.Optional[aws_opensearchserverless.ModuleModel] = pydantic.Field(None, alias='aws_opensearchserverless')
    aws_opensearchservice_: typing.Optional[aws_opensearchservice.ModuleModel] = pydantic.Field(None, alias='aws_opensearchservice')
    aws_opsworks_: typing.Optional[aws_opsworks.ModuleModel] = pydantic.Field(None, alias='aws_opsworks')
    aws_opsworkscm_: typing.Optional[aws_opsworkscm.ModuleModel] = pydantic.Field(None, alias='aws_opsworkscm')
    aws_organizations_: typing.Optional[aws_organizations.ModuleModel] = pydantic.Field(None, alias='aws_organizations')
    aws_osis_: typing.Optional[aws_osis.ModuleModel] = pydantic.Field(None, alias='aws_osis')
    aws_panorama_: typing.Optional[aws_panorama.ModuleModel] = pydantic.Field(None, alias='aws_panorama')
    aws_pcaconnectorad_: typing.Optional[aws_pcaconnectorad.ModuleModel] = pydantic.Field(None, alias='aws_pcaconnectorad')
    aws_personalize_: typing.Optional[aws_personalize.ModuleModel] = pydantic.Field(None, alias='aws_personalize')
    aws_pinpoint_: typing.Optional[aws_pinpoint.ModuleModel] = pydantic.Field(None, alias='aws_pinpoint')
    aws_pinpointemail_: typing.Optional[aws_pinpointemail.ModuleModel] = pydantic.Field(None, alias='aws_pinpointemail')
    aws_pipes_: typing.Optional[aws_pipes.ModuleModel] = pydantic.Field(None, alias='aws_pipes')
    aws_proton_: typing.Optional[aws_proton.ModuleModel] = pydantic.Field(None, alias='aws_proton')
    aws_qldb_: typing.Optional[aws_qldb.ModuleModel] = pydantic.Field(None, alias='aws_qldb')
    aws_quicksight_: typing.Optional[aws_quicksight.ModuleModel] = pydantic.Field(None, alias='aws_quicksight')
    aws_ram_: typing.Optional[aws_ram.ModuleModel] = pydantic.Field(None, alias='aws_ram')
    aws_rds_: typing.Optional[aws_rds.ModuleModel] = pydantic.Field(None, alias='aws_rds')
    aws_redshift_: typing.Optional[aws_redshift.ModuleModel] = pydantic.Field(None, alias='aws_redshift')
    aws_redshiftserverless_: typing.Optional[aws_redshiftserverless.ModuleModel] = pydantic.Field(None, alias='aws_redshiftserverless')
    aws_refactorspaces_: typing.Optional[aws_refactorspaces.ModuleModel] = pydantic.Field(None, alias='aws_refactorspaces')
    aws_rekognition_: typing.Optional[aws_rekognition.ModuleModel] = pydantic.Field(None, alias='aws_rekognition')
    aws_resiliencehub_: typing.Optional[aws_resiliencehub.ModuleModel] = pydantic.Field(None, alias='aws_resiliencehub')
    aws_resourceexplorer2_: typing.Optional[aws_resourceexplorer2.ModuleModel] = pydantic.Field(None, alias='aws_resourceexplorer2')
    aws_resourcegroups_: typing.Optional[aws_resourcegroups.ModuleModel] = pydantic.Field(None, alias='aws_resourcegroups')
    aws_robomaker_: typing.Optional[aws_robomaker.ModuleModel] = pydantic.Field(None, alias='aws_robomaker')
    aws_rolesanywhere_: typing.Optional[aws_rolesanywhere.ModuleModel] = pydantic.Field(None, alias='aws_rolesanywhere')
    aws_route53_: typing.Optional[aws_route53.ModuleModel] = pydantic.Field(None, alias='aws_route53')
    aws_route53_patterns_: typing.Optional[aws_route53_patterns.ModuleModel] = pydantic.Field(None, alias='aws_route53_patterns')
    aws_route53_targets_: typing.Optional[aws_route53_targets.ModuleModel] = pydantic.Field(None, alias='aws_route53_targets')
    aws_route53recoverycontrol_: typing.Optional[aws_route53recoverycontrol.ModuleModel] = pydantic.Field(None, alias='aws_route53recoverycontrol')
    aws_route53recoveryreadiness_: typing.Optional[aws_route53recoveryreadiness.ModuleModel] = pydantic.Field(None, alias='aws_route53recoveryreadiness')
    aws_route53resolver_: typing.Optional[aws_route53resolver.ModuleModel] = pydantic.Field(None, alias='aws_route53resolver')
    aws_rum_: typing.Optional[aws_rum.ModuleModel] = pydantic.Field(None, alias='aws_rum')
    aws_s3_: typing.Optional[aws_s3.ModuleModel] = pydantic.Field(None, alias='aws_s3')
    aws_s3_assets_: typing.Optional[aws_s3_assets.ModuleModel] = pydantic.Field(None, alias='aws_s3_assets')
    aws_s3_deployment_: typing.Optional[aws_s3_deployment.ModuleModel] = pydantic.Field(None, alias='aws_s3_deployment')
    aws_s3_notifications_: typing.Optional[aws_s3_notifications.ModuleModel] = pydantic.Field(None, alias='aws_s3_notifications')
    aws_s3objectlambda_: typing.Optional[aws_s3objectlambda.ModuleModel] = pydantic.Field(None, alias='aws_s3objectlambda')
    aws_s3outposts_: typing.Optional[aws_s3outposts.ModuleModel] = pydantic.Field(None, alias='aws_s3outposts')
    aws_sagemaker_: typing.Optional[aws_sagemaker.ModuleModel] = pydantic.Field(None, alias='aws_sagemaker')
    aws_sam_: typing.Optional[aws_sam.ModuleModel] = pydantic.Field(None, alias='aws_sam')
    aws_scheduler_: typing.Optional[aws_scheduler.ModuleModel] = pydantic.Field(None, alias='aws_scheduler')
    aws_sdb_: typing.Optional[aws_sdb.ModuleModel] = pydantic.Field(None, alias='aws_sdb')
    aws_secretsmanager_: typing.Optional[aws_secretsmanager.ModuleModel] = pydantic.Field(None, alias='aws_secretsmanager')
    aws_securityhub_: typing.Optional[aws_securityhub.ModuleModel] = pydantic.Field(None, alias='aws_securityhub')
    aws_servicecatalog_: typing.Optional[aws_servicecatalog.ModuleModel] = pydantic.Field(None, alias='aws_servicecatalog')
    aws_servicecatalogappregistry_: typing.Optional[aws_servicecatalogappregistry.ModuleModel] = pydantic.Field(None, alias='aws_servicecatalogappregistry')
    aws_servicediscovery_: typing.Optional[aws_servicediscovery.ModuleModel] = pydantic.Field(None, alias='aws_servicediscovery')
    aws_ses_: typing.Optional[aws_ses.ModuleModel] = pydantic.Field(None, alias='aws_ses')
    aws_ses_actions_: typing.Optional[aws_ses_actions.ModuleModel] = pydantic.Field(None, alias='aws_ses_actions')
    aws_shield_: typing.Optional[aws_shield.ModuleModel] = pydantic.Field(None, alias='aws_shield')
    aws_signer_: typing.Optional[aws_signer.ModuleModel] = pydantic.Field(None, alias='aws_signer')
    aws_simspaceweaver_: typing.Optional[aws_simspaceweaver.ModuleModel] = pydantic.Field(None, alias='aws_simspaceweaver')
    aws_sns_: typing.Optional[aws_sns.ModuleModel] = pydantic.Field(None, alias='aws_sns')
    aws_sns_subscriptions_: typing.Optional[aws_sns_subscriptions.ModuleModel] = pydantic.Field(None, alias='aws_sns_subscriptions')
    aws_sqs_: typing.Optional[aws_sqs.ModuleModel] = pydantic.Field(None, alias='aws_sqs')
    aws_ssm_: typing.Optional[aws_ssm.ModuleModel] = pydantic.Field(None, alias='aws_ssm')
    aws_ssmcontacts_: typing.Optional[aws_ssmcontacts.ModuleModel] = pydantic.Field(None, alias='aws_ssmcontacts')
    aws_ssmincidents_: typing.Optional[aws_ssmincidents.ModuleModel] = pydantic.Field(None, alias='aws_ssmincidents')
    aws_sso_: typing.Optional[aws_sso.ModuleModel] = pydantic.Field(None, alias='aws_sso')
    aws_stepfunctions_: typing.Optional[aws_stepfunctions.ModuleModel] = pydantic.Field(None, alias='aws_stepfunctions')
    aws_stepfunctions_tasks_: typing.Optional[aws_stepfunctions_tasks.ModuleModel] = pydantic.Field(None, alias='aws_stepfunctions_tasks')
    aws_supportapp_: typing.Optional[aws_supportapp.ModuleModel] = pydantic.Field(None, alias='aws_supportapp')
    aws_synthetics_: typing.Optional[aws_synthetics.ModuleModel] = pydantic.Field(None, alias='aws_synthetics')
    aws_systemsmanagersap_: typing.Optional[aws_systemsmanagersap.ModuleModel] = pydantic.Field(None, alias='aws_systemsmanagersap')
    aws_timestream_: typing.Optional[aws_timestream.ModuleModel] = pydantic.Field(None, alias='aws_timestream')
    aws_transfer_: typing.Optional[aws_transfer.ModuleModel] = pydantic.Field(None, alias='aws_transfer')
    aws_verifiedpermissions_: typing.Optional[aws_verifiedpermissions.ModuleModel] = pydantic.Field(None, alias='aws_verifiedpermissions')
    aws_voiceid_: typing.Optional[aws_voiceid.ModuleModel] = pydantic.Field(None, alias='aws_voiceid')
    aws_vpclattice_: typing.Optional[aws_vpclattice.ModuleModel] = pydantic.Field(None, alias='aws_vpclattice')
    aws_waf_: typing.Optional[aws_waf.ModuleModel] = pydantic.Field(None, alias='aws_waf')
    aws_wafregional_: typing.Optional[aws_wafregional.ModuleModel] = pydantic.Field(None, alias='aws_wafregional')
    aws_wafv2_: typing.Optional[aws_wafv2.ModuleModel] = pydantic.Field(None, alias='aws_wafv2')
    aws_wisdom_: typing.Optional[aws_wisdom.ModuleModel] = pydantic.Field(None, alias='aws_wisdom')
    aws_workspaces_: typing.Optional[aws_workspaces.ModuleModel] = pydantic.Field(None, alias='aws_workspaces')
    aws_workspacesweb_: typing.Optional[aws_workspacesweb.ModuleModel] = pydantic.Field(None, alias='aws_workspacesweb')
    aws_xray_: typing.Optional[aws_xray.ModuleModel] = pydantic.Field(None, alias='aws_xray')
    cloud_assembly_schema_: typing.Optional[cloud_assembly_schema.ModuleModel] = pydantic.Field(None, alias='cloud_assembly_schema')
    cloudformation_include_: typing.Optional[cloudformation_include.ModuleModel] = pydantic.Field(None, alias='cloudformation_include')
    custom_resources_: typing.Optional[custom_resources.ModuleModel] = pydantic.Field(None, alias='custom_resources')
    cx_api_: typing.Optional[cx_api.ModuleModel] = pydantic.Field(None, alias='cx_api')
    lambda_layer_awscli_: typing.Optional[lambda_layer_awscli.ModuleModel] = pydantic.Field(None, alias='lambda_layer_awscli')
    lambda_layer_kubectl_: typing.Optional[lambda_layer_kubectl.ModuleModel] = pydantic.Field(None, alias='lambda_layer_kubectl')
    lambda_layer_node_proxy_agent_: typing.Optional[lambda_layer_node_proxy_agent.ModuleModel] = pydantic.Field(None, alias='lambda_layer_node_proxy_agent')
    pipelines_: typing.Optional[pipelines.ModuleModel] = pydantic.Field(None, alias='pipelines')
    region_info_: typing.Optional[region_info.ModuleModel] = pydantic.Field(None, alias='region_info')
    triggers_: typing.Optional[triggers.ModuleModel] = pydantic.Field(None, alias='triggers')
    constructs_: typing.Optional[constructs.ModuleModel] = pydantic.Field(None, alias='constructs')
