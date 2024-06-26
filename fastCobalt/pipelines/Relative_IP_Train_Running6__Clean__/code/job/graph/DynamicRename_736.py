from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def DynamicRename_736(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("MBR_INDV_BE_KEY"), 
        col("YEARMONTH"), 
        col("Sum_E75").alias("E75_Running6"), 
        col("Sum_E55").alias("E55_Running6"), 
        col("Sum_E44").alias("E44_Running6"), 
        col("Sum_E21").alias("E21_Running6"), 
        col("Sum_E31").alias("E31_Running6"), 
        col("Sum_E86").alias("E86_Running6"), 
        col("Sum_E71").alias("E71_Running6"), 
        col("Sum_E60").alias("E60_Running6"), 
        col("Sum_E07").alias("E07_Running6"), 
        col("Sum_E10").alias("E10_Running6"), 
        col("Sum_E88").alias("E88_Running6"), 
        col("Sum_E26").alias("E26_Running6"), 
        col("Sum_E56").alias("E56_Running6"), 
        col("Sum_E42").alias("E42_Running6"), 
        col("Sum_E25").alias("E25_Running6"), 
        col("Sum_E64").alias("E64_Running6"), 
        col("Sum_E53").alias("E53_Running6"), 
        col("Sum_E77").alias("E77_Running6"), 
        col("Sum_E03").alias("E03_Running6"), 
        col("Sum_E67").alias("E67_Running6"), 
        col("Sum_E09").alias("E09_Running6"), 
        col("Sum_E00").alias("E00_Running6"), 
        col("Sum_E59").alias("E59_Running6"), 
        col("Sum_E36").alias("E36_Running6"), 
        col("Sum_E04").alias("E04_Running6"), 
        col("Sum_E15").alias("E15_Running6"), 
        col("Sum_E76").alias("E76_Running6"), 
        col("Sum_E61").alias("E61_Running6"), 
        col("Sum_E87").alias("E87_Running6"), 
        col("Sum_E20").alias("E20_Running6"), 
        col("Sum_E50").alias("E50_Running6"), 
        col("Sum_E32").alias("E32_Running6"), 
        col("Sum_E66").alias("E66_Running6"), 
        col("Sum_E72").alias("E72_Running6"), 
        col("Sum_E65").alias("E65_Running6"), 
        col("Sum_E16").alias("E16_Running6"), 
        col("Sum_E11").alias("E11_Running6"), 
        col("Sum_E83").alias("E83_Running6"), 
        col("Sum_E43").alias("E43_Running6"), 
        col("Sum_E22").alias("E22_Running6"), 
        col("Sum_E27").alias("E27_Running6"), 
        col("Sum_E54").alias("E54_Running6"), 
        col("Sum_E08").alias("E08_Running6"), 
        col("Sum_E35").alias("E35_Running6"), 
        col("Sum_E01").alias("E01_Running6"), 
        col("Sum_E46").alias("E46_Running6"), 
        col("Sum_E80").alias("E80_Running6"), 
        col("Sum_E40").alias("E40_Running6"), 
        col("Sum_E05").alias("E05_Running6"), 
        col("Sum_E84").alias("E84_Running6"), 
        col("Sum_E73").alias("E73_Running6"), 
        col("Sum_E51").alias("E51_Running6"), 
        col("Sum_E79").alias("E79_Running6"), 
        col("Sum_E23").alias("E23_Running6"), 
        col("Sum_E28").alias("E28_Running6"), 
        col("Sum_E58").alias("E58_Running6"), 
        col("Sum_E41").alias("E41_Running6"), 
        col("Sum_E30").alias("E30_Running6"), 
        col("Sum_E06").alias("E06_Running6"), 
        col("Sum_E70").alias("E70_Running6"), 
        col("Sum_E85").alias("E85_Running6"), 
        col("Sum_E45").alias("E45_Running6"), 
        col("Sum_E34").alias("E34_Running6"), 
        col("Sum_E02").alias("E02_Running6"), 
        col("Sum_E74").alias("E74_Running6"), 
        col("Sum_E89").alias("E89_Running6"), 
        col("Sum_E78").alias("E78_Running6"), 
        col("Sum_E24").alias("E24_Running6"), 
        col("Sum_E13").alias("E13_Running6"), 
        col("Sum_E52").alias("E52_Running6"), 
        col("Sum_E29").alias("E29_Running6"), 
        col("Sum_E63").alias("E63_Running6")
    )
