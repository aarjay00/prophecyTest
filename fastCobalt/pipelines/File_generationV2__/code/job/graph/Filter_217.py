from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Filter_217(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("Date") > lit("2024-04-01")))