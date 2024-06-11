from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Summarize_14(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("`Call Type`").alias("Call Type"))

    return df1.agg(
        sum(col("Sum_Sum_TTLCalls")).alias("Sum_Sum_Sum_TTLCalls"), 
        sum(col("Sum_Sum_TTLHours")).alias("Sum_Sum_Sum_TTLHours")
    )
