from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Formula_143(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn("Percent of Calls", (col("Sum_Sum_TTLCalls") / col("`TTL Calls`")))
