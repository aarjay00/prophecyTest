from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_866(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("`New Drug Indicator`").alias("New Drug Indicator"), col("Week"), col("MBR_INDV_BE_KEY"))
