from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Formula_4312(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "AGE",
        call_spark_fcn("string_substring", col("AGE").cast(StringType()), lit(0), lit(2)).cast(IntegerType())
    )
