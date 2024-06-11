from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_769(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("MBR_INDV_BE_KEY"), 
        col("YEARMONTH"), 
        col("DIAG_CD").alias("Secondary_Diagnosis"), 
        col("DIAG_CD_COST").alias("Secondary_Diagnosis_Cost")
    )
