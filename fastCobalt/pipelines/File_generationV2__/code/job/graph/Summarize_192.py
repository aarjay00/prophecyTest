from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Summarize_192(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("ds"))

    return df1.agg(
        sum(col("yhat")).alias("yhat"), 
        sum(col("yhat_lower")).alias("yhat_lower"), 
        sum(col("yhat_upper")).alias("yhat_upper")
    )
