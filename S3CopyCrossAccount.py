import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
#changes
# Script generated for node Amazon S3
AmazonS3_node1705036092688 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://jan24learningsource/DYCD_after-school_programs__Neighborhood_Development_Area__NDA__Family_Support.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1705036092688",
)

# Script generated for node Amazon S3
AmazonS3_node1705036095344 = glueContext.write_dynamic_frame.from_options(
    frame=AmazonS3_node1705036092688,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://jan24learningsources/testCopyData/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1705036095344",
)

job.commit()
