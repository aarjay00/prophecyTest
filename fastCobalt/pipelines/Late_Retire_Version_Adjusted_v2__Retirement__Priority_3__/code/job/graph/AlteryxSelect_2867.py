from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_2867(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("ACTVTY_YR_MO_SK"), 
        col("GRP_ID"), 
        col("Avg_MBR_AGE_AT_ACTVTY_YR_MO").alias("Average Age Females")
    )
