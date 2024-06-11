from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def CreateYRMO(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "ACTVTY_YR_MO_SK",
        concat(
          concat(call_spark_fcn("string_substring", col("ACTVTY_YR_MO_SK"), lit(0), lit(4)), lit("-")), 
          call_spark_fcn("string_substring", col("ACTVTY_YR_MO_SK"), (lit(- 1) * lit(2).cast(IntegerType())), lit(2))
        )
    )
