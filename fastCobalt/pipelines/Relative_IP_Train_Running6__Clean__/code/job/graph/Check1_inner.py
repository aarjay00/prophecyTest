from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Check1_inner(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.MBR_INDV_BE_KEY") == col("in1.MBR_INDV_BE_KEY")), "inner")\
        .select(col("in0.MBR_INDV_BE_KEY").alias("MBR_INDV_BE_KEY"), col("in1.YEARMONTH").alias("YEARMONTH"), col("in1.Relative_IP_Month").alias("Relative_IP_Month"), col("in1.MBR_INDV_BE_KEY").alias("Right_MBR_INDV_BE_KEY"))
