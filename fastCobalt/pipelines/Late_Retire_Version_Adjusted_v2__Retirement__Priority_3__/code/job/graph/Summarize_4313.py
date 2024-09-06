from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Summarize_4313(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("AGE"))

    return df1.agg(
        sum(col("Positives")).alias("Sum_Positives"), 
        sum(col("Negatives")).alias("Sum_Negatives"), 
        sum(col("`Total Selection`")).alias("Sum_Total Selection"), 
        sum(col("`Positive Selection`")).alias("Sum_Positive Selection")
    )