from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_2879(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("FNCL_LOB_CD"), 
        col("PROD_SH_NM_DLVRY_METH_CD"), 
        col("YEARMONTH"), 
        col("AGE"), 
        col("MBR_DSBLTY_IN"), 
        col("Avg_BLUE_SELECT"), 
        col("Product"), 
        col("`Switch to Retirement`").alias("Switch to Retirement"), 
        col("GRP_BILL_LVL_NM"), 
        col("Avg_BLUESELECT_"), 
        col("MBR_ENR_COBRA_IN"), 
        col("MBR_UNIQ_KEY"), 
        col("`Product Counter`").alias("Product Counter"), 
        col("PROD_SH_NM"), 
        col("HOST_MBR_IN"), 
        col("YMD"), 
        col("Avg_PCBEXTRNL"), 
        col("EXPRNC_CAT_CD"), 
        col("FUND_CAT_CD"), 
        col("MBR_HOME_ADDR_LN_2"), 
        col("MBR_LAST_NM"), 
        col("MBR_GNDR_CD"), 
        col("GRP_TOT_EMPL_CT"), 
        col("MBR_SK"), 
        col("MBR_HOME_ADDR_ZIP_CD_5"), 
        col("Retire"), 
        col("MBR_HOME_ADDR_LN_1"), 
        col("PCP_FLAG"), 
        col("`Marketing Restricted`").alias("Marketing Restricted"), 
        col("GRP_NM"), 
        col("MBR_INDV_BE_KEY"), 
        col("SPIRA_BNF_ID"), 
        col("Avg_BLUE_ACCESS"), 
        col("SUB_MBR_SK"), 
        col("`Target Forecasted`").alias("Target Forecasted"), 
        col("MBR_HOME_ADDR_ST_CD"), 
        col("CLS_PLN_DESC"), 
        col("PRNT_GRP_SIC_NACIS_CD"), 
        col("MBR_FIRST_NM"), 
        col("FNCL_MKT_SEG_NM"), 
        col("GRP_MKT_SIZE_CAT_NM"), 
        col("`Retired With Blue`").alias("Retired With Blue"), 
        col("Avg_PC"), 
        col("`Product Category`").alias("Product Category"), 
        col("Avg_HPEXTRNL"), 
        col("MBR_RELSHP_NM"), 
        col("GRP_BUS_SUB_CAT_SH_NM"), 
        col("Avg_PCB"), 
        col("GRP_ZIP_CD_5"), 
        col("GRP_ID"), 
        col("GRP_SK"), 
        col("Avg_BCARE"), 
        col("`Spouse's Product`").alias("Spouse's Product")
    )
