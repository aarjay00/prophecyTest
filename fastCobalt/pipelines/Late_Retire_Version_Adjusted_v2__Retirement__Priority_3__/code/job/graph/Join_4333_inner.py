from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Join_4333_inner(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.MBR_INDV_BE_KEY") == col("in1.MBR_INDV_BE_KEY")), "inner")\
        .select(col("in1.`Medical EYE`").alias("Medical EYE"), col("in1.`Male Percentage`").alias("Male Percentage"), col("in1.`Member Months`").alias("Member Months"), col("in1.`Specialty Drug Counts`").alias("Specialty Drug Counts"), col("in1.`Average Age Females`").alias("Average Age Females"), col("in1.`Vision EYE`").alias("Vision EYE"), col("in1.PCBEXTRNL").alias("PCBEXTRNL"), col("in1.MBR_HOME_ADDR_ZIP_CD_5").alias("MBR_HOME_ADDR_ZIP_CD_5"), col("in1.Inpatient").alias("Inpatient"), col("in1.`Spouse Age`").alias("Spouse Age"), col("in1.MBR_GNDR_CD").alias("MBR_GNDR_CD"), col("in1.`Dental Dental Member Pay`").alias("Dental Dental Member Pay"), col("in1.`Medical FEMALE_REPRODUCTIVE_SYSTEM`").alias("Medical FEMALE_REPRODUCTIVE_SYSTEM"), col("in1.`Distinct NDC Codes`").alias("Distinct NDC Codes"), col("in1.`Drug Tier 1`").alias("Drug Tier 1"), col("in1.`Mail Order Drug Counts`").alias("Mail Order Drug Counts"), col("in1.BLUESELECT_").alias("BLUESELECT_"), col("in1.`Medical BLOOD_AND_BLOOD_FORMING_ORGANS`").alias("Medical BLOOD_AND_BLOOD_FORMING_ORGANS"), col("in1.`Medical NERVOUS_SYSTEM`").alias("Medical NERVOUS_SYSTEM"), col("in1.`Female Percentage`").alias("Female Percentage"), col("in1.`Medical PREGNANCY__CHILDBIRTH_AND_PUERPERIUM`")\
        .alias("Medical PREGNANCY__CHILDBIRTH_AND_PUERPERIUM"), col("in1.`Medical EAR__NOSE__AND_THROAT`").alias("Medical EAR__NOSE__AND_THROAT"), col("in1.`Medical MUSCULOSKETAL_SYSTEM`").alias("Medical MUSCULOSKETAL_SYSTEM"), col("in1.`Medical MYELOPROLIFERATIVE_AND_NEOPLASMS`").alias("Medical MYELOPROLIFERATIVE_AND_NEOPLASMS"), col("in1.`Distinct Diagnosis Types`").alias("Distinct Diagnosis Types"), col("in1.`Target Forecasted`").alias("Target Forecasted"), col("in1.`Medical BURNS`").alias("Medical BURNS"), col("in1.`Min_Dependent Age`").alias("Min_Dependent Age"), col("in1.`Dental SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST`").alias("Dental SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST"), col("in1.GRP_TOT_EMPL_CT").alias("GRP_TOT_EMPL_CT"), col("in1.Emergency_Room").alias("Emergency_Room"), col("in1.`Medical ALCOHOL_DRUG_USE_AND_DISORDERS`").alias("Medical ALCOHOL_DRUG_USE_AND_DISORDERS"), col("in1.`Retired With Blue`").alias("Retired With Blue"), col("in1.`Product Category`").alias("Product Category"), col("in1.Members_on_Policy").alias("Members_on_Policy"), col("in1.YMD").alias("YMD"), col("in1.Outpatient").alias("Outpatient"), col("in1.`Medical DIGESTIVE_SYSTEM`").alias("Medical DIGESTIVE_SYSTEM"), col("in1.YEARMONTH").alias("YEARMONTH"), col("in1.AGE").alias("AGE"), col("in1.`Medical KIDNEY_AND_URINARY_TRACT`").alias("Medical KIDNEY_AND_URINARY_TRACT"), col("in1.`Vision ENDOCRINE__NUTRITIONAL_AND_METABOLIC`").alias("Vision ENDOCRINE__NUTRITIONAL_AND_METABOLIC"), col("in1.`Medical MENTAL_ILLNESS`").alias("Medical MENTAL_ILLNESS"), col("in1.`Dental FACTORS_INFLUENCING_HEALTH_STATUS`").alias("Dental FACTORS_INFLUENCING_HEALTH_STATUS"), col("in1.`Dental EAR__NOSE__AND_THROAT`").alias("Dental EAR__NOSE__AND_THROAT"), col("in1.SUB_MBR_SK").alias("SUB_MBR_SK"), col("in1.PRNT_GRP_SIC_NACIS_CD").alias("PRNT_GRP_SIC_NACIS_CD"), col("in1.GRP_ID").alias("GRP_ID"), col("in1.GRP_MKT_SIZE_CAT_NM").alias("GRP_MKT_SIZE_CAT_NM"), col("in1.CLS_PLN_DESC").alias("CLS_PLN_DESC"), col("in1.`Group Months`").alias("Group Months"), col("in1.`Apt Ind`").alias("Apt Ind"), col("in1.EXPRNC_CAT_CD").alias("EXPRNC_CAT_CD"), col("in1.`Vision FACTORS_INFLUENCING_HEALTH_STATUS`").alias("Vision FACTORS_INFLUENCING_HEALTH_STATUS"), col("in1.HOST_MBR_IN").alias("HOST_MBR_IN"), col("in1.`Number of Winterizing Procedures`").alias("Number of Winterizing Procedures"), col("in1.`Med Member Pay`").alias("Med Member Pay"), col("in1.`Dental Member Pay`").alias("Dental Member Pay"), col("in1.`Dental MENTAL_ILLNESS`").alias("Dental MENTAL_ILLNESS"), col("in1.PC").alias("PC"), col("in1.GRP_ZIP_CD_5").alias("GRP_ZIP_CD_5"), col("in1.rand").alias("rand"), col("in1.`Medical ENDOCRINE__NUTRITIONAL_AND_METABOLIC`")\
        .alias("Medical ENDOCRINE__NUTRITIONAL_AND_METABOLIC"), col("in1.`Vision Member Pay`").alias("Vision Member Pay"), col("in1.BLUE_ACCESS").alias("BLUE_ACCESS"), col("in1.`Medical INJURIES__POISONINGS_AND_DRUG_EFFECTS`")\
        .alias("Medical INJURIES__POISONINGS_AND_DRUG_EFFECTS"), col("in1.PCB").alias("PCB"), col("in1.SPIRA_BNF_ID").alias("SPIRA_BNF_ID"), col("in1.PCP_FLAG").alias("PCP_FLAG"), col("in1.`Medical FACTORS_INFLUENCING_HEALTH_STATUS`").alias("Medical FACTORS_INFLUENCING_HEALTH_STATUS"), col("in0.MBR_INDV_BE_KEY").alias("MBR_INDV_BE_KEY"), col("in1.MBR_HOME_ADDR_ST_CD").alias("MBR_HOME_ADDR_ST_CD"), col("in1.MBR_DSBLTY_IN").alias("MBR_DSBLTY_IN"), col("in1.`High Deductible Ind`").alias("High Deductible Ind"), col("in1.`Spouse Retired`").alias("Spouse Retired"), col("in1.`Medical RESPIRATORY_SYSTEM`").alias("Medical RESPIRATORY_SYSTEM"), col("in1.`Medical AIDS_HIV`").alias("Medical AIDS_HIV"), col("in1.FNCL_LOB_CD").alias("FNCL_LOB_CD"), col("in1.`Medical HEPATOBILARY_SYSTEM`").alias("Medical HEPATOBILARY_SYSTEM"), col("in1.`Medical INFECTIOUS_AND_PARASITIC_DISEASES`").alias("Medical INFECTIOUS_AND_PARASITIC_DISEASES"), col("in1.`Depression Related Claims`").alias("Depression Related Claims"), col("in1.`Generic Drug Counts`").alias("Generic Drug Counts"), col("in1.BCARE").alias("BCARE"), col("in1.`Medical NEWBORNS_AND_OTHER_NEONATES`").alias("Medical NEWBORNS_AND_OTHER_NEONATES"), col("in1.`RX Member Pay`").alias("RX Member Pay"), col("in1.`Drug Tier 2`").alias("Drug Tier 2"), col("in1.`Average Age Males`").alias("Average Age Males"), col("in1.`Drug Tier 3`").alias("Drug Tier 3"), col("in1.`Medical SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST`").alias("Medical SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST"), col("in1.`Dental ALCOHOL_DRUG_USE_AND_DISORDERS`").alias("Dental ALCOHOL_DRUG_USE_AND_DISORDERS"), col("in1.SUM_CCI").alias("SUM_CCI"), col("in1.`Medical MALE_REPRODUCTIVE_SYSTEM`").alias("Medical MALE_REPRODUCTIVE_SYSTEM"), col("in1.MBR_RELSHP_NM").alias("MBR_RELSHP_NM"), col("in1.BLUE_SELECT").alias("BLUE_SELECT"), col("in1.MBR_ENR_COBRA_IN").alias("MBR_ENR_COBRA_IN"), col("in1.`Medical CIRCULATORY_SYSTEM`").alias("Medical CIRCULATORY_SYSTEM"))
