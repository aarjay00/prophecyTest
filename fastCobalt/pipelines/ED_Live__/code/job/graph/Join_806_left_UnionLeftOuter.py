from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Join_806_left_UnionLeftOuter(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.MBR_INDV_BE_KEY") == col("in1.MBR_INDV_BE_KEY")), "leftouter")\
        .select(col("in0.`ED Visit Alw Amt`").alias("ED Visit Alw Amt"), col("in0.MBR_INDV_BE_KEY").alias("MBR_INDV_BE_KEY"), col("in0.`Household ED Visit Tot Alw Amt`").alias("Household ED Visit Tot Alw Amt"), col("in0.`Diag Codes`").alias("Diag Codes"), col("in0.`PCMH Attributed`").alias("PCMH Attributed"), col("in0.Target").alias("Target"), col("in0.`PCP Attributed`").alias("PCP Attributed"), col("in0.`Max Claim Line Spend`").alias("Max Claim Line Spend"), col("in0.`Total Claim Spend`").alias("Total Claim Spend"), col("in0.ZIP").alias("ZIP"), col("in0.`Index Month`").alias("Index Month"), col("in0.Last_YMD").alias("Last_YMD"), col("in0.`Group ID`").alias("Group ID"), col("in0.`Service Area`").alias("Service Area"), col("in0.`CCI Score`").alias("CCI Score"), col("in0.`Non Emergent Percentage`").alias("Non Emergent Percentage"), col("in0.`Medical Home (str)`").alias("Medical Home (str)"), col("in0.`Coverage Area`").alias("Coverage Area"), col("in0.Industry").alias("Industry"), col("in0.Population").alias("Population"), col("in0.Right_MBR_INDV_BE_KEY").alias("Right_MBR_INDV_BE_KEY"), col("in0.`Household ED Visits`").alias("Household ED Visits"), col("in0.`Members in Household`").alias("Members in Household"), col("in0.`Household ED Visit Alw Amt`").alias("Household ED Visit Alw Amt"), col("in0.`ED Visits`").alias("ED Visits"), col("in0.Last_Week").alias("Last_Week"), col("in0.`Drug Counts`").alias("Drug Counts"), col("in0.CountDistinct_Week").alias("CountDistinct_Week"), col("in1.`Mental Health Claims`").alias("Mental Health Claims"), col("in0.`Historic Non Emergent Visit`").alias("Historic Non Emergent Visit"), col("in0.`Injury Related ED`").alias("Injury Related ED"), col("in0.`ED Visited`").alias("ED Visited"), col("in0.Relationship").alias("Relationship"), col("in0.`Drug Related ED`").alias("Drug Related ED"), col("in0.`Drug Classes`").alias("Drug Classes"), col("in0.Polypharmacy").alias("Polypharmacy"), col("in0.Right_CountDistinct_Week").alias("Right_CountDistinct_Week"), col("in0.`Psych Related ED`").alias("Psych Related ED"), col("in0.Gender").alias("Gender"), col("in0.`Distance to Closest ED`").alias("Distance to Closest ED"), col("in0.Race").alias("Race"), col("in0.`Member Age`").alias("Member Age"), col("in0.`SPIRA Elligible`").alias("SPIRA Elligible"), col("in0.`Medical Home`").alias("Medical Home"), col("in0.`7-12 Month ED Visit History`").alias("7-12 Month ED Visit History"), col("in0.`ED Visit Tot Alw Amt`").alias("ED Visit Tot Alw Amt"), col("in0.`Alcohol Related ED`").alias("Alcohol Related ED"))
