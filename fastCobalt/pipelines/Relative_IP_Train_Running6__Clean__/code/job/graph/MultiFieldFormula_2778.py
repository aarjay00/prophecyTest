from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def MultiFieldFormula_2778(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        when(col("LowestGFR").isNull(), lit(99999)).otherwise(col("LowestGFR")).alias("LowestGFR"), 
        col("YEARMONTH"), 
        col("MBR_INDV_BE_KEY"), 
        col("Concat_ORDER_TST_NM"), 
        col("UniqueLabs"), 
        col("mmol"), 
        col("HighestAlbumin"), 
        col("CountOfLabs")
    )
