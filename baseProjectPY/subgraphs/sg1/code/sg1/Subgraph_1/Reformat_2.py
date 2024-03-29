from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from basepipeline1.udfs.UDFs import *

def Reformat_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        udfConcat(col("first_name"), col("last_name")).alias("name"), 
        udfConcatold(col("first_name"), col("last_name")).alias("nameold")
    )
