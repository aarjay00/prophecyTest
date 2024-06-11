from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Unique_1982(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("row_number", row_number().over(Window.partitionBy("MBR_INDV_BE_KEY", "YEARMONTH").orderBy(lit(1))))\
        .filter(col("row_number") == lit(1))\
        .drop("row_number")
