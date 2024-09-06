from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Summarize_2655(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("MBR_INDV_BE_KEY"), col("YEARMONTH"), col("Primary_Diagnosis"))

    return df1.agg(sum(col("Primary_Diagnosis_Cost")).alias("Sum_Primary_Diagnosis_Cost"))