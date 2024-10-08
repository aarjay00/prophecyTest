from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def MultiFieldFormula_730(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        when(col("E00").isNull(), lit(0)).otherwise(col("E00")).alias("E00"), 
        when(col("E01").isNull(), lit(0)).otherwise(col("E01")).alias("E01"), 
        when(col("E02").isNull(), lit(0)).otherwise(col("E02")).alias("E02"), 
        when(col("E03").isNull(), lit(0)).otherwise(col("E03")).alias("E03"), 
        when(col("E04").isNull(), lit(0)).otherwise(col("E04")).alias("E04"), 
        when(col("E05").isNull(), lit(0)).otherwise(col("E05")).alias("E05"), 
        when(col("E06").isNull(), lit(0)).otherwise(col("E06")).alias("E06"), 
        when(col("E07").isNull(), lit(0)).otherwise(col("E07")).alias("E07"), 
        when(col("E08").isNull(), lit(0)).otherwise(col("E08")).alias("E08"), 
        when(col("E09").isNull(), lit(0)).otherwise(col("E09")).alias("E09"), 
        when(col("E10").isNull(), lit(0)).otherwise(col("E10")).alias("E10"), 
        when(col("E11").isNull(), lit(0)).otherwise(col("E11")).alias("E11"), 
        when(col("E13").isNull(), lit(0)).otherwise(col("E13")).alias("E13"), 
        when(col("E15").isNull(), lit(0)).otherwise(col("E15")).alias("E15"), 
        when(col("E16").isNull(), lit(0)).otherwise(col("E16")).alias("E16"), 
        when(col("E20").isNull(), lit(0)).otherwise(col("E20")).alias("E20"), 
        when(col("E21").isNull(), lit(0)).otherwise(col("E21")).alias("E21"), 
        when(col("E22").isNull(), lit(0)).otherwise(col("E22")).alias("E22"), 
        when(col("E23").isNull(), lit(0)).otherwise(col("E23")).alias("E23"), 
        when(col("E24").isNull(), lit(0)).otherwise(col("E24")).alias("E24"), 
        when(col("E25").isNull(), lit(0)).otherwise(col("E25")).alias("E25"), 
        when(col("E26").isNull(), lit(0)).otherwise(col("E26")).alias("E26"), 
        when(col("E27").isNull(), lit(0)).otherwise(col("E27")).alias("E27"), 
        when(col("E28").isNull(), lit(0)).otherwise(col("E28")).alias("E28"), 
        when(col("E29").isNull(), lit(0)).otherwise(col("E29")).alias("E29"), 
        when(col("E30").isNull(), lit(0)).otherwise(col("E30")).alias("E30"), 
        when(col("E31").isNull(), lit(0)).otherwise(col("E31")).alias("E31"), 
        when(col("E32").isNull(), lit(0)).otherwise(col("E32")).alias("E32"), 
        when(col("E34").isNull(), lit(0)).otherwise(col("E34")).alias("E34"), 
        when(col("E35").isNull(), lit(0)).otherwise(col("E35")).alias("E35"), 
        when(col("E36").isNull(), lit(0)).otherwise(col("E36")).alias("E36"), 
        when(col("E40").isNull(), lit(0)).otherwise(col("E40")).alias("E40"), 
        when(col("E41").isNull(), lit(0)).otherwise(col("E41")).alias("E41"), 
        when(col("E42").isNull(), lit(0)).otherwise(col("E42")).alias("E42"), 
        when(col("E43").isNull(), lit(0)).otherwise(col("E43")).alias("E43"), 
        when(col("E44").isNull(), lit(0)).otherwise(col("E44")).alias("E44"), 
        when(col("E45").isNull(), lit(0)).otherwise(col("E45")).alias("E45"), 
        when(col("E46").isNull(), lit(0)).otherwise(col("E46")).alias("E46"), 
        when(col("E50").isNull(), lit(0)).otherwise(col("E50")).alias("E50"), 
        when(col("E51").isNull(), lit(0)).otherwise(col("E51")).alias("E51"), 
        when(col("E52").isNull(), lit(0)).otherwise(col("E52")).alias("E52"), 
        when(col("E53").isNull(), lit(0)).otherwise(col("E53")).alias("E53"), 
        when(col("E54").isNull(), lit(0)).otherwise(col("E54")).alias("E54"), 
        when(col("E55").isNull(), lit(0)).otherwise(col("E55")).alias("E55"), 
        when(col("E56").isNull(), lit(0)).otherwise(col("E56")).alias("E56"), 
        when(col("E58").isNull(), lit(0)).otherwise(col("E58")).alias("E58"), 
        when(col("E59").isNull(), lit(0)).otherwise(col("E59")).alias("E59"), 
        when(col("E60").isNull(), lit(0)).otherwise(col("E60")).alias("E60"), 
        when(col("E61").isNull(), lit(0)).otherwise(col("E61")).alias("E61"), 
        when(col("E63").isNull(), lit(0)).otherwise(col("E63")).alias("E63"), 
        when(col("E64").isNull(), lit(0)).otherwise(col("E64")).alias("E64"), 
        when(col("E65").isNull(), lit(0)).otherwise(col("E65")).alias("E65"), 
        when(col("E66").isNull(), lit(0)).otherwise(col("E66")).alias("E66"), 
        when(col("E67").isNull(), lit(0)).otherwise(col("E67")).alias("E67"), 
        when(col("E68").isNull(), lit(0)).otherwise(col("E68")).alias("E68"), 
        when(col("E70").isNull(), lit(0)).otherwise(col("E70")).alias("E70"), 
        when(col("E71").isNull(), lit(0)).otherwise(col("E71")).alias("E71"), 
        when(col("E72").isNull(), lit(0)).otherwise(col("E72")).alias("E72"), 
        when(col("E73").isNull(), lit(0)).otherwise(col("E73")).alias("E73"), 
        when(col("E74").isNull(), lit(0)).otherwise(col("E74")).alias("E74"), 
        when(col("E75").isNull(), lit(0)).otherwise(col("E75")).alias("E75"), 
        when(col("E76").isNull(), lit(0)).otherwise(col("E76")).alias("E76"), 
        when(col("E77").isNull(), lit(0)).otherwise(col("E77")).alias("E77"), 
        when(col("E78").isNull(), lit(0)).otherwise(col("E78")).alias("E78"), 
        when(col("E79").isNull(), lit(0)).otherwise(col("E79")).alias("E79"), 
        when(col("E80").isNull(), lit(0)).otherwise(col("E80")).alias("E80"), 
        when(col("E83").isNull(), lit(0)).otherwise(col("E83")).alias("E83"), 
        when(col("E84").isNull(), lit(0)).otherwise(col("E84")).alias("E84"), 
        when(col("E85").isNull(), lit(0)).otherwise(col("E85")).alias("E85"), 
        when(col("E86").isNull(), lit(0)).otherwise(col("E86")).alias("E86"), 
        when(col("E87").isNull(), lit(0)).otherwise(col("E87")).alias("E87"), 
        when(col("E88").isNull(), lit(0)).otherwise(col("E88")).alias("E88"), 
        when(col("E89").isNull(), lit(0)).otherwise(col("E89")).alias("E89"), 
        when(col("F30").isNull(), lit(0)).otherwise(col("F30")).alias("F30"), 
        when(col("F31").isNull(), lit(0)).otherwise(col("F31")).alias("F31"), 
        when(col("F32").isNull(), lit(0)).otherwise(col("F32")).alias("F32"), 
        when(col("F33").isNull(), lit(0)).otherwise(col("F33")).alias("F33"), 
        when(col("F34").isNull(), lit(0)).otherwise(col("F34")).alias("F34"), 
        when(col("F39").isNull(), lit(0)).otherwise(col("F39")).alias("F39"), 
        when(col("M1A").isNull(), lit(0)).otherwise(col("M1A")).alias("M1A"), 
        when(col("M10").isNull(), lit(0)).otherwise(col("M10")).alias("M10"), 
        when(col("M11").isNull(), lit(0)).otherwise(col("M11")).alias("M11"), 
        when(col("M12").isNull(), lit(0)).otherwise(col("M12")).alias("M12"), 
        when(col("M13").isNull(), lit(0)).otherwise(col("M13")).alias("M13"), 
        when(col("M14").isNull(), lit(0)).otherwise(col("M14")).alias("M14"), 
        when(col("M15").isNull(), lit(0)).otherwise(col("M15")).alias("M15"), 
        when(col("M16").isNull(), lit(0)).otherwise(col("M16")).alias("M16"), 
        when(col("M17").isNull(), lit(0)).otherwise(col("M17")).alias("M17"), 
        when(col("M18").isNull(), lit(0)).otherwise(col("M18")).alias("M18"), 
        when(col("M19").isNull(), lit(0)).otherwise(col("M19")).alias("M19"), 
        when(col("M40").isNull(), lit(0)).otherwise(col("M40")).alias("M40"), 
        when(col("M41").isNull(), lit(0)).otherwise(col("M41")).alias("M41"), 
        when(col("M42").isNull(), lit(0)).otherwise(col("M42")).alias("M42"), 
        when(col("M43").isNull(), lit(0)).otherwise(col("M43")).alias("M43"), 
        when(col("M45").isNull(), lit(0)).otherwise(col("M45")).alias("M45"), 
        when(col("M46").isNull(), lit(0)).otherwise(col("M46")).alias("M46"), 
        when(col("M47").isNull(), lit(0)).otherwise(col("M47")).alias("M47"), 
        when(col("M48").isNull(), lit(0)).otherwise(col("M48")).alias("M48"), 
        when(col("M49").isNull(), lit(0)).otherwise(col("M49")).alias("M49"), 
        when(col("O00").isNull(), lit(0)).otherwise(col("O00")).alias("O00"), 
        when(col("O01").isNull(), lit(0)).otherwise(col("O01")).alias("O01"), 
        when(col("O02").isNull(), lit(0)).otherwise(col("O02")).alias("O02"), 
        when(col("O03").isNull(), lit(0)).otherwise(col("O03")).alias("O03"), 
        when(col("O04").isNull(), lit(0)).otherwise(col("O04")).alias("O04"), 
        when(col("O07").isNull(), lit(0)).otherwise(col("O07")).alias("O07"), 
        when(col("O08").isNull(), lit(0)).otherwise(col("O08")).alias("O08"), 
        when(col("O09").isNull(), lit(0)).otherwise(col("O09")).alias("O09"), 
        when(col("O20").isNull(), lit(0)).otherwise(col("O20")).alias("O20"), 
        when(col("O21").isNull(), lit(0)).otherwise(col("O21")).alias("O21"), 
        when(col("O22").isNull(), lit(0)).otherwise(col("O22")).alias("O22"), 
        when(col("O23").isNull(), lit(0)).otherwise(col("O23")).alias("O23"), 
        when(col("O24").isNull(), lit(0)).otherwise(col("O24")).alias("O24"), 
        when(col("O25").isNull(), lit(0)).otherwise(col("O25")).alias("O25"), 
        when(col("O26").isNull(), lit(0)).otherwise(col("O26")).alias("O26"), 
        when(col("O28").isNull(), lit(0)).otherwise(col("O28")).alias("O28"), 
        when(col("O29").isNull(), lit(0)).otherwise(col("O29")).alias("O29"), 
        when(col("O30").isNull(), lit(0)).otherwise(col("O30")).alias("O30"), 
        when(col("O31").isNull(), lit(0)).otherwise(col("O31")).alias("O31"), 
        when(col("O32").isNull(), lit(0)).otherwise(col("O32")).alias("O32"), 
        when(col("O33").isNull(), lit(0)).otherwise(col("O33")).alias("O33"), 
        when(col("O34").isNull(), lit(0)).otherwise(col("O34")).alias("O34"), 
        when(col("O35").isNull(), lit(0)).otherwise(col("O35")).alias("O35"), 
        when(col("O36").isNull(), lit(0)).otherwise(col("O36")).alias("O36"), 
        when(col("R10").isNull(), lit(0)).otherwise(col("R10")).alias("R10"), 
        when(col("R11").isNull(), lit(0)).otherwise(col("R11")).alias("R11"), 
        when(col("R12").isNull(), lit(0)).otherwise(col("R12")).alias("R12"), 
        when(col("R13").isNull(), lit(0)).otherwise(col("R13")).alias("R13"), 
        when(col("R14").isNull(), lit(0)).otherwise(col("R14")).alias("R14"), 
        when(col("R15").isNull(), lit(0)).otherwise(col("R15")).alias("R15"), 
        when(col("R16").isNull(), lit(0)).otherwise(col("R16")).alias("R16"), 
        when(col("R17").isNull(), lit(0)).otherwise(col("R17")).alias("R17"), 
        when(col("R18").isNull(), lit(0)).otherwise(col("R18")).alias("R18"), 
        when(col("R19").isNull(), lit(0)).otherwise(col("R19")).alias("R19"), 
        when(col("Z00").isNull(), lit(0)).otherwise(col("Z00")).alias("Z00"), 
        when(col("Z01").isNull(), lit(0)).otherwise(col("Z01")).alias("Z01"), 
        when(col("Z02").isNull(), lit(0)).otherwise(col("Z02")).alias("Z02"), 
        when(col("Z3A").isNull(), lit(0)).otherwise(col("Z3A")).alias("Z3A"), 
        when(col("Z03").isNull(), lit(0)).otherwise(col("Z03")).alias("Z03"), 
        when(col("Z04").isNull(), lit(0)).otherwise(col("Z04")).alias("Z04"), 
        when(col("Z05").isNull(), lit(0)).otherwise(col("Z05")).alias("Z05"), 
        when(col("Z08").isNull(), lit(0)).otherwise(col("Z08")).alias("Z08"), 
        when(col("Z09").isNull(), lit(0)).otherwise(col("Z09")).alias("Z09"), 
        when(col("Z11").isNull(), lit(0)).otherwise(col("Z11")).alias("Z11"), 
        when(col("Z12").isNull(), lit(0)).otherwise(col("Z12")).alias("Z12"), 
        when(col("Z13").isNull(), lit(0)).otherwise(col("Z13")).alias("Z13"), 
        when(col("Z14").isNull(), lit(0)).otherwise(col("Z14")).alias("Z14"), 
        when(col("Z15").isNull(), lit(0)).otherwise(col("Z15")).alias("Z15"), 
        when(col("Z16").isNull(), lit(0)).otherwise(col("Z16")).alias("Z16"), 
        when(col("Z17").isNull(), lit(0)).otherwise(col("Z17")).alias("Z17"), 
        when(col("Z18").isNull(), lit(0)).otherwise(col("Z18")).alias("Z18"), 
        when(col("Z19").isNull(), lit(0)).otherwise(col("Z19")).alias("Z19"), 
        when(col("Z20").isNull(), lit(0)).otherwise(col("Z20")).alias("Z20"), 
        when(col("Z21").isNull(), lit(0)).otherwise(col("Z21")).alias("Z21"), 
        when(col("Z22").isNull(), lit(0)).otherwise(col("Z22")).alias("Z22"), 
        when(col("Z23").isNull(), lit(0)).otherwise(col("Z23")).alias("Z23"), 
        when(col("Z28").isNull(), lit(0)).otherwise(col("Z28")).alias("Z28"), 
        when(col("Z29").isNull(), lit(0)).otherwise(col("Z29")).alias("Z29"), 
        when(col("Z30").isNull(), lit(0)).otherwise(col("Z30")).alias("Z30"), 
        when(col("Z31").isNull(), lit(0)).otherwise(col("Z31")).alias("Z31"), 
        when(col("Z32").isNull(), lit(0)).otherwise(col("Z32")).alias("Z32"), 
        when(col("Z33").isNull(), lit(0)).otherwise(col("Z33")).alias("Z33"), 
        when(col("Z34").isNull(), lit(0)).otherwise(col("Z34")).alias("Z34"), 
        when(col("Z36").isNull(), lit(0)).otherwise(col("Z36")).alias("Z36"), 
        when(col("Z37").isNull(), lit(0)).otherwise(col("Z37")).alias("Z37"), 
        when(col("Z38").isNull(), lit(0)).otherwise(col("Z38")).alias("Z38"), 
        when(col("Z39").isNull(), lit(0)).otherwise(col("Z39")).alias("Z39"), 
        col("YEARMONTH"), 
        col("MBR_INDV_BE_KEY")
    )
