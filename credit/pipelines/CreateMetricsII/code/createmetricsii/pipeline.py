from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from createmetricsii.config.ConfigStore import *
from createmetricsii.udfs.UDFs import *
from prophecy.utils import *
from createmetricsii.graph import *

def pipeline(spark: SparkSession) -> None:
    IngestData(spark)
    df_Income = Income(spark)
    df_TransUnionFico = TransUnionFico(spark)
    df_EncryptPII = EncryptPII(spark, df_TransUnionFico)
    df_ByCustomerID = ByCustomerID(spark, df_Income, df_EncryptPII)
    df_ParseLoanAmount = ParseLoanAmount(spark, df_ByCustomerID)
    df_ParseLoanAmount = df_ParseLoanAmount.cache()
    df_LexisNexis_json = LexisNexis_json(spark)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_LexisNexis_json)
    df_Refine = Refine(spark, df_FlattenSchema_1)
    df_ByName = ByName(spark, df_ParseLoanAmount, df_Refine)
    df_ByName = df_ByName.cache()
    df_SetTypes = SetTypes(spark, df_ByName)
    Gold_Credit_DTI_SCD1_CatalogTable(spark, df_SetTypes)
    df_Reformat_1 = Reformat_1(spark, df_EncryptPII)
    Gold_Credit_DTI_SCD2_CatalogTable(spark, df_SetTypes)
    Gold_Credit_DTI_SCD3_CatalogTable(spark, df_SetTypes)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/CreateMetricsII")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/CreateMetricsII")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
