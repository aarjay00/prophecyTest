package basetest.pipeline9

import io.prophecy.libs._
import basetest.pipeline9.config.Context
import basetest.pipeline9.config._
import basetest.pipeline9.udfs.UDFs._
import basetest.pipeline9.udfs._
import basetest.pipeline9.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_ds1 = ds1(context)
    Lookup_1(context, df_ds1)
    val df_Reformat_1 = Reformat_1(context, df_ds1)
    val df_Script_1   = Script_1(context,   df_Reformat_1)
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.fromCLI(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
      .newSession()
    val context = Context(spark, config)
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/kaajri12312")
    registerUDFs(spark)
    MetricsCollector.start(spark, "pipelines/kaajri12312")
    apply(context)
    MetricsCollector.end(spark)
  }

}
