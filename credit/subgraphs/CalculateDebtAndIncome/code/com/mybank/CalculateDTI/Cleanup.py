from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from createmetrics.config.ConfigStore import *
from createmetrics.udfs.UDFs import *

def Cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.drop("balance")
    df2 = df1.drop("lender_name")
    df3 = df2.drop("loan_id")
    df4 = df3.drop("past_due")
    df5 = df4.drop("processor")
    df6 = df5.drop("term")

    return df6\
        .withColumn("REPORTED_INCOME", lit(None).cast(StringType()))\
        .withColumnRenamed("name", "Name")\
        .withColumn("monthly_loan_amount", col("monthly_loan_amount").cast(LongType()))
