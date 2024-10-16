from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def MultiRowFormula_2318_window(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("IP_lag1", lag(col("IP"), 1).over(Window.partitionBy(col("MBR_SK")).orderBy(col("MBR_SK").asc())))\
        .withColumn("IP_lag2", lag(col("IP"), 2).over(Window.partitionBy(col("MBR_SK")).orderBy(col("MBR_SK").asc())))\
        .withColumn("IP_lag3", lag(col("IP"), 3).over(Window.partitionBy(col("MBR_SK")).orderBy(col("MBR_SK").asc())))\
        .withColumn("IP_lag4", lag(col("IP"), 4).over(Window.partitionBy(col("MBR_SK")).orderBy(col("MBR_SK").asc())))\
        .withColumn("IP_lag5", lag(col("IP"), 5).over(Window.partitionBy(col("MBR_SK")).orderBy(col("MBR_SK").asc())))
