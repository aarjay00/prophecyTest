from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def CrossTab_2351(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("MBR_SK"), col("YEARMONTH"))
    df2 = df1.pivot("CLM_SUBTYP_CD", ["IP"])

    return df2.agg(sum(col("CASES")).alias("CASES"))
