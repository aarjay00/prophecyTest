from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_2938(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("FNCL_LOB_CD"), 
        col("`Generic Drug Counts`").alias("Generic Drug Counts"), 
        col("`Medical ALCOHOL_DRUG_USE_AND_DISORDERS`").alias("Medical ALCOHOL_DRUG_USE_AND_DISORDERS"), 
        col("Emergency_Room"), 
        col("PROD_SH_NM_DLVRY_METH_CD"), 
        col("YEARMONTH"), 
        col("`Medical RESPIRATORY_SYSTEM`").alias("Medical RESPIRATORY_SYSTEM"), 
        col("`Female Percentage`").alias("Female Percentage"), 
        col("`Average Age Females`").alias("Average Age Females"), 
        col("`Min_Dependent Age`").alias("Min_Dependent Age"), 
        col("AGE"), 
        col("Outpatient"), 
        col("Members_on_Policy"), 
        col("MBR_DSBLTY_IN"), 
        col("Avg_BLUE_SELECT"), 
        col("`Dental NOT_APPLICABLE`").alias("Dental NOT_APPLICABLE"), 
        col("`Medical BLOOD_AND_BLOOD_FORMING_ORGANS`").alias("Medical BLOOD_AND_BLOOD_FORMING_ORGANS"), 
        col("`Average Age Males`").alias("Average Age Males"), 
        col("`Med Member Pay`").alias("Med Member Pay"), 
        col("Product"), 
        col("`Switch to Retirement`").alias("Switch to Retirement"), 
        col("GRP_BILL_LVL_NM"), 
        col("`Spouse Age`").alias("Spouse Age"), 
        col("Avg_BLUESELECT_"), 
        col("`Specialty Drug Counts`").alias("Specialty Drug Counts"), 
        col("`Dental FACTORS_INFLUENCING_HEALTH_STATUS`").alias("Dental FACTORS_INFLUENCING_HEALTH_STATUS"), 
        col("MBR_ENR_COBRA_IN"), 
        col("`Vision Member Pay`").alias("Vision Member Pay"), 
        col("`Number of Winterizing Procedures`").alias("Number of Winterizing Procedures"), 
        col("`Medical NOT_APPLICABLE`").alias("Medical NOT_APPLICABLE"), 
        col("`Distinct NDC Codes`").alias("Distinct NDC Codes"), 
        col("MBR_UNIQ_KEY"), 
        col("`Product Counter`").alias("Product Counter"), 
        col("`Dental Received Date`").alias("Dental Received Date"), 
        col("PROD_SH_NM"), 
        col("`Group Months`").alias("Group Months"), 
        col("`Medical ENDOCRINE__NUTRITIONAL_AND_METABOLIC`").alias("Medical ENDOCRINE__NUTRITIONAL_AND_METABOLIC"), 
        col("`Medical NERVOUS_SYSTEM`").alias("Medical NERVOUS_SYSTEM"), 
        col("HOST_MBR_IN"), 
        col("YMD"), 
        col("Avg_PCBEXTRNL"), 
        col("`Vision NO_DIAGNOSTIC_CATEGORY`").alias("Vision NO_DIAGNOSTIC_CATEGORY"), 
        col("`Medical UNKNOWN`").alias("Medical UNKNOWN"), 
        col("`Recent Mover`").alias("Recent Mover"), 
        col("EXPRNC_CAT_CD"), 
        col("`Medical Received Date`").alias("Medical Received Date"), 
        col("`Vision ENDOCRINE__NUTRITIONAL_AND_METABOLIC`").alias("Vision ENDOCRINE__NUTRITIONAL_AND_METABOLIC"), 
        col("`Medical FACTORS_INFLUENCING_HEALTH_STATUS`").alias("Medical FACTORS_INFLUENCING_HEALTH_STATUS"), 
        col("`Medical EYE`").alias("Medical EYE"), 
        col("FUND_CAT_CD"), 
        col("MBR_HOME_ADDR_LN_2"), 
        col("`Vision EYE`").alias("Vision EYE"), 
        col("`Dental ALCOHOL_DRUG_USE_AND_DISORDERS`").alias("Dental ALCOHOL_DRUG_USE_AND_DISORDERS"), 
        col("MBR_LAST_NM"), 
        col("MBR_GNDR_CD"), 
        col("GRP_TOT_EMPL_CT"), 
        col("`Medical PREGNANCY__CHILDBIRTH_AND_PUERPERIUM`").alias("Medical PREGNANCY__CHILDBIRTH_AND_PUERPERIUM"), 
        col("MBR_SK"), 
        col("`Medical EAR__NOSE__AND_THROAT`").alias("Medical EAR__NOSE__AND_THROAT"), 
        col("MBR_HOME_ADDR_ZIP_CD_5"), 
        col("`Medical MALE_REPRODUCTIVE_SYSTEM`").alias("Medical MALE_REPRODUCTIVE_SYSTEM"), 
        col("`Drug Tier 2`").alias("Drug Tier 2"), 
        col("Retire"), 
        col("`Medical KIDNEY_AND_URINARY_TRACT`").alias("Medical KIDNEY_AND_URINARY_TRACT"), 
        col("MBR_HOME_ADDR_LN_1"), 
        col("PCP_FLAG"), 
        col("`Vision FACTORS_INFLUENCING_HEALTH_STATUS`").alias("Vision FACTORS_INFLUENCING_HEALTH_STATUS"), 
        col("`Marketing Restricted`").alias("Marketing Restricted"), 
        col("`Medical NO_DIAGNOSTIC_CATEGORY`").alias("Medical NO_DIAGNOSTIC_CATEGORY"), 
        col("`Medical MENTAL_ILLNESS`").alias("Medical MENTAL_ILLNESS"), 
        col("GRP_NM"), 
        col("`RX Member Pay`").alias("RX Member Pay"), 
        col("`Depression Related Claims`").alias("Depression Related Claims"), 
        col("MBR_INDV_BE_KEY"), 
        col("`Dental MENTAL_ILLNESS`").alias("Dental MENTAL_ILLNESS"), 
        col("`Medical SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST`").alias("Medical SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST"), 
        col("`Unkown Drug Tier`").alias("Unkown Drug Tier"), 
        col("`Dental Dental Member Pay`").alias("Dental Dental Member Pay"), 
        col("SPIRA_BNF_ID"), 
        col("Avg_BLUE_ACCESS"), 
        col("SUB_MBR_SK"), 
        col("`Target Forecasted`").alias("Target Forecasted"), 
        col("MBR_HOME_ADDR_ST_CD"), 
        col("`Dental SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST`").alias("Dental SKIN_SUBCUTANEOUS_TISSUE_AND_BREAST"), 
        col("`Mail Order Drug Counts`").alias("Mail Order Drug Counts"), 
        col("`Medical MUSCULOSKETAL_SYSTEM`").alias("Medical MUSCULOSKETAL_SYSTEM"), 
        col("CLS_PLN_DESC"), 
        col("`Retiree in Household Indicator`").alias("Retiree in Household Indicator"), 
        col("`Distinct Diagnosis Types`").alias("Distinct Diagnosis Types"), 
        col("PRNT_GRP_SIC_NACIS_CD"), 
        col("`Drug Tier 3`").alias("Drug Tier 3"), 
        col("`Medical DIGESTIVE_SYSTEM`").alias("Medical DIGESTIVE_SYSTEM"), 
        col("`Medical HEPATOBILARY_SYSTEM`").alias("Medical HEPATOBILARY_SYSTEM"), 
        col("`Medical FEMALE_REPRODUCTIVE_SYSTEM`").alias("Medical FEMALE_REPRODUCTIVE_SYSTEM"), 
        col("MBR_FIRST_NM"), 
        col("FNCL_MKT_SEG_NM"), 
        col("GRP_MKT_SIZE_CAT_NM"), 
        col("`Retired With Blue`").alias("Retired With Blue"), 
        col("Inpatient"), 
        col("Avg_PC"), 
        col("`Dental NO_DIAGNOSTIC_CATEGORY`").alias("Dental NO_DIAGNOSTIC_CATEGORY"), 
        col("`Product Category`").alias("Product Category"), 
        col("`Medical INFECTIOUS_AND_PARASITIC_DISEASES`").alias("Medical INFECTIOUS_AND_PARASITIC_DISEASES"), 
        col("Avg_HPEXTRNL"), 
        col("MBR_RELSHP_NM"), 
        col("`Dental Member Pay`").alias("Dental Member Pay"), 
        col("`Medical CIRCULATORY_SYSTEM`").alias("Medical CIRCULATORY_SYSTEM"), 
        col("`Medical AIDS_HIV`").alias("Medical AIDS_HIV"), 
        col("`Medical INJURIES__POISONINGS_AND_DRUG_EFFECTS`").alias("Medical INJURIES__POISONINGS_AND_DRUG_EFFECTS"), 
        col("`Dental EYE`").alias("Dental EYE"), 
        col("`Spouse's Product`").alias("Spouse's Product"), 
        col("GRP_BUS_SUB_CAT_SH_NM"), 
        col("`Medical NEWBORNS_AND_OTHER_NEONATES`").alias("Medical NEWBORNS_AND_OTHER_NEONATES"), 
        col("`Member Months`").alias("Member Months"), 
        col("`Drug Tier 1`").alias("Drug Tier 1"), 
        col("SUM_CCI"), 
        col("`Medical MYELOPROLIFERATIVE_AND_NEOPLASMS`").alias("Medical MYELOPROLIFERATIVE_AND_NEOPLASMS"), 
        col("Avg_PCB"), 
        col("`Male Percentage`").alias("Male Percentage"), 
        col("`Dental EAR__NOSE__AND_THROAT`").alias("Dental EAR__NOSE__AND_THROAT"), 
        col("GRP_ZIP_CD_5"), 
        col("GRP_ID"), 
        col("GRP_SK"), 
        col("Avg_BCARE"), 
        col("`Medical BURNS`").alias("Medical BURNS")
    )
