from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.udfs.UDFs import *

def ds1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("id1", StringType(), True), StructField("id2", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dede")