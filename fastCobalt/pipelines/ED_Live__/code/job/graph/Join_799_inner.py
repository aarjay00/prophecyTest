from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Join_799_inner(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.MBR_INDV_BE_KEY") == col("in1.MBR_INDV_BE_KEY")), "inner")\
        .select(col("in0.Mode_SUB_MKTNG_METRO_RURAL_CD").alias("Service Area"), col("in0.`Household ED Visit Alw Amt`").alias("Household ED Visit Alw Amt"), col("in0.`Mode_Medical Home`").alias("Medical Home (str)"), col("in0.Mode_MBR_HOME_ADDR_ZIP_CD_5").alias("ZIP"), col("in0.Sum_drug").alias("Drug Related ED"), col("in0.Min_DistaneMiles").alias("Distance to Closest ED"), col("in0.Sum_psych").alias("Psych Related ED"), col("in0.`Last_Members in Household`").alias("Members in Household"), col("in0.Mode_PROD_CAT").alias("Population"), col("in0.Sum_alcohol").alias("Alcohol Related ED"), col("in0.Mode_SPIRA_BNF_ID").alias("SPIRA Elligible"), col("in0.Mode_GRP_ID").alias("Group ID"), col("in0.CountDistinct_Week").alias("CountDistinct_Week"), col("in0.`7-12 Month ED Visit History`").alias("7-12 Month ED Visit History"), col("in1.CountDistinct_Week").alias("Right_CountDistinct_Week"), col("in0.Max_CCI_Score").alias("CCI Score"), col("in0.Mode_PRNT_GRP_SIC_NACIS_CD").alias("Industry"), col("in0.Mode_SUB_CNTGS_CNTY_CD").alias("Coverage Area"), col("in0.`Sum_ED Visits from Members in Household (Not Member)`").alias("Household ED Visits"), col("in0.Mode_DRUG_CLASS_COUNT").alias("Drug Classes"), col("in0.Mode_MED_HOME_ID").alias("Medical Home"), col("in0.Mode_MBR_RELSHP_NM").alias("Relationship"), col("in0.`Household ED Visit Tot Alw Amt`").alias("Household ED Visit Tot Alw Amt"), col("in0.Sum_injury").alias("Injury Related ED"), col("in0.Mode_Race").alias("Race"), col("in0.Mode_PCMH_flag").alias("PCMH Attributed"), col("in0.Last_Month").alias("Index Month"), col("in0.MBR_INDV_BE_KEY").alias("MBR_INDV_BE_KEY"), col("in1.Max_Target").alias("Target"), col("in0.`ED Visits`").alias("ED Visits"), col("in0.Last_YMD").alias("Last_YMD"), col("in0.Max_mbr_age").alias("Member Age"), col("in0.Last_Week").alias("Last_Week"), col("in0.`ED Visit Alw Amt`").alias("ED Visit Alw Amt"), col("in0.Mode_POLYPHARMACY_IN").alias("Polypharmacy"), col("in0.Mode_DRUG_COUNT").alias("Drug Counts"), col("in0.`Max_Non Emergent Likelihood`").alias("Non Emergent Percentage"), col("in0.Mode_MBR_GNDR_CD").alias("Gender"), col("in0.`ED Visit Tot Alw Amt`").alias("ED Visit Tot Alw Amt"), col("in0.`Max_Non Emergent Binary`").alias("Historic Non Emergent Visit"), col("in0.Mode_PCP_FLAG").alias("PCP Attributed"))