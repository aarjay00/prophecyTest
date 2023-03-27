from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from createmetricsii.config.ConfigStore import *
from createmetricsii.udfs.UDFs import *

def ParseJson(spark: SparkSession, in0: DataFrame) -> DataFrame:
    # to parse json schema automatically
    listOfRows = in0.select("content").take(1)
    schema = schema_of_json(listOfRows[0][0])
    out0 = in0.withColumn("content_parsed", from_json(col("content"), schema)).where("content_parsed is not null")

    return out0
