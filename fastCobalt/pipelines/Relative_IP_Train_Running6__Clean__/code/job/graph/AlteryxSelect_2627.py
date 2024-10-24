from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_2627(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("Z09_Running3"), 
        col("E84_Running3"), 
        col("E52_Running3"), 
        col("Z22_Running3"), 
        col("F39_Running3"), 
        col("E44_Running3"), 
        col("E46_Running3"), 
        col("M40_Running3"), 
        col("Z39_Running3"), 
        col("YEARMONTH"), 
        col("E71_Running3"), 
        col("E72_Running3"), 
        col("M1A_Running3"), 
        col("O28_Running3"), 
        col("R14_Running3"), 
        col("E16_Running3"), 
        col("Z23_Running3"), 
        col("E54_Running3"), 
        col("E43_Running3"), 
        col("O35_Running3"), 
        col("E66_Running3"), 
        col("F30_Running3"), 
        col("E79_Running3"), 
        col("E63_Running3"), 
        col("E40_Running3"), 
        col("E74_Running3"), 
        col("E20_Running3"), 
        col("Z08_Running3"), 
        col("E88_Running3"), 
        col("M48_Running3"), 
        col("E56_Running3"), 
        col("E09_Running3"), 
        col("Z12_Running3"), 
        col("E76_Running3"), 
        col("Z00_Running3"), 
        col("E68_Running3"), 
        col("O00_Running3"), 
        col("Z13_Running3"), 
        col("E07_Running3"), 
        col("E08_Running3"), 
        col("M49_Running3"), 
        col("Z29_Running3"), 
        col("O02_Running3"), 
        col("E59_Running3"), 
        col("R13_Running3"), 
        col("Z32_Running3"), 
        col("R10_Running3"), 
        col("O03_Running3"), 
        col("O04_Running3"), 
        col("E53_Running3"), 
        col("R16_Running3"), 
        col("E05_Running3"), 
        col("O24_Running3"), 
        col("O32_Running3"), 
        col("E85_Running3"), 
        col("O20_Running3"), 
        col("Z15_Running3"), 
        col("E67_Running3"), 
        col("Z31_Running3"), 
        col("O33_Running3"), 
        col("M41_Running3"), 
        col("O09_Running3"), 
        col("Z36_Running3"), 
        col("O21_Running3"), 
        col("E31_Running3"), 
        col("E01_Running3"), 
        col("O26_Running3"), 
        col("E24_Running3"), 
        col("O25_Running3"), 
        col("E25_Running3"), 
        col("O01_Running3"), 
        col("Z30_Running3"), 
        col("E26_Running3"), 
        col("Z21_Running3"), 
        col("M19_Running3"), 
        col("E41_Running3"), 
        col("Z02_Running3"), 
        col("R11_Running3"), 
        col("O08_Running3"), 
        col("Z04_Running3"), 
        col("MBR_INDV_BE_KEY"), 
        col("O07_Running3"), 
        col("M16_Running3"), 
        col("M14_Running3"), 
        col("Z01_Running3"), 
        col("Z38_Running3"), 
        col("E89_Running3"), 
        col("Z3A_Running3"), 
        col("E51_Running3"), 
        col("E04_Running3"), 
        col("E06_Running3"), 
        col("E23_Running3"), 
        col("E60_Running3"), 
        col("E80_Running3"), 
        col("E83_Running3"), 
        col("E22_Running3"), 
        col("R15_Running3"), 
        col("E02_Running3"), 
        col("F34_Running3"), 
        col("E61_Running3"), 
        col("M15_Running3"), 
        col("E78_Running3"), 
        col("E03_Running3"), 
        col("E15_Running3"), 
        col("M10_Running3"), 
        col("E77_Running3"), 
        col("E45_Running3"), 
        col("E58_Running3"), 
        col("M43_Running3"), 
        col("R12_Running3"), 
        col("E70_Running3"), 
        col("Z05_Running3"), 
        col("M47_Running3"), 
        col("R18_Running3"), 
        col("Z37_Running3"), 
        col("Z14_Running3"), 
        col("M12_Running3"), 
        col("M45_Running3"), 
        col("M18_Running3"), 
        col("O29_Running3"), 
        col("E75_Running3"), 
        col("E36_Running3"), 
        col("O31_Running3"), 
        col("E34_Running3"), 
        col("E30_Running3"), 
        col("O30_Running3"), 
        col("R19_Running3"), 
        col("M46_Running3"), 
        col("E21_Running3"), 
        col("E11_Running3"), 
        col("E86_Running3"), 
        col("Z03_Running3"), 
        col("Z16_Running3"), 
        col("O34_Running3"), 
        col("F32_Running3"), 
        col("E65_Running3"), 
        col("E28_Running3"), 
        col("E27_Running3"), 
        col("E10_Running3"), 
        col("E50_Running3"), 
        col("E73_Running3"), 
        col("O22_Running3"), 
        col("F31_Running3"), 
        col("Z18_Running3"), 
        col("E32_Running3"), 
        col("Z28_Running3"), 
        col("F33_Running3"), 
        col("R17_Running3"), 
        col("Z33_Running3"), 
        col("O23_Running3"), 
        col("E29_Running3"), 
        col("E35_Running3"), 
        col("E42_Running3"), 
        col("M11_Running3"), 
        col("Z34_Running3"), 
        col("Z17_Running3"), 
        col("M42_Running3"), 
        col("E13_Running3"), 
        col("M17_Running3"), 
        col("E55_Running3"), 
        col("E64_Running3"), 
        col("Z11_Running3"), 
        col("E00_Running3"), 
        col("M13_Running3"), 
        col("Z20_Running3"), 
        col("O36_Running3"), 
        col("E87_Running3"), 
        col("Z19_Running3")
    )
