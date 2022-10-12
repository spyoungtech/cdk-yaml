import typing  # noqa

import aws_cdk
import pydantic  # noqa

import cdk_yaml.generated  # noqa
from cdk_yaml.codegen import ConstructNode
from cdk_yaml.codegen import ConstructTree
from cdk_yaml.codegen import ModelTree

# constructs supported as resources
_SUPPORTED_CONSTRUCTS = [aws_cdk.aws_s3.Bucket, aws_cdk.aws_sns.Topic, aws_cdk.aws_rds.DatabaseInstance]

# Auto-generate pydantic models for all supported constructs (and constructs for all required arguments, recursively)
for construct in _SUPPORTED_CONSTRUCTS:
    root = ConstructNode(construct)
    tree = ConstructTree(root)
    nodes = tree.traverse()
    modeltree = ModelTree(tree)
    models = modeltree.to_models()
    for model in models:
        if hasattr(model, 'update_forward_refs'):
            model.update_forward_refs(**globals())
