from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def yxmc_822_estimation_rank(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.drop("PERCENT_RANK_COLUMN")
