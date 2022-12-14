package simpledatalabs_27.applicationprojectext2.subgraph

import io.prophecy.libs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
import simpledatalabs_27.applicationprojectext2.subgraph.appsg1.config._
package object appsg1 {

  def apply(spark: SparkSession, config: Config, in0: DataFrame): DataFrame = {
    ConfigStore.Config = config
    val df_Reformat_2 = Reformat_2(spark, in0)
    val df_Reformat_3 = Reformat_3(spark, df_Reformat_2)
    df_Reformat_3
  }

}
