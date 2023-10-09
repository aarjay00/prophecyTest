from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from p1.config.ConfigStore import *
from p1.udfs.UDFs import *

def snow1_1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("snowflake")\
        .options(
          **{
            "sfUrl": "",
            "sfUser": "sa",
            "sfPassword": "as",
            "sfDatabase": "",
            "sfSchema": "",
            "sfWarehouse": "",
            "sfRole": ""
          }
        )\
        .option("dbtable", "as")\
        .load()
