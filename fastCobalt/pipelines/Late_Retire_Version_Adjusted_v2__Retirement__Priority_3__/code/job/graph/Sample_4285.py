from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Sample_4285(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(["MBR_INDV_BE_KEY"])
