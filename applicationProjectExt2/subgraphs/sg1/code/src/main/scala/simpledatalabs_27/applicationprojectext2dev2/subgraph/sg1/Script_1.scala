package simpledatalabs_27.applicationprojectext2dev2.subgraph.sg1

import io.prophecy.libs._
import simpledatalabs_27.applicationprojectext2dev2.subgraph.sg1.config.Context
import simpledatalabs_27.applicationprojectext2dev2.functions._
import _simpledatalabs_25.baseproject2.functions._
import simpledatalabs_27.applicationprojectext2dev2.subgraph.sg1.udfs.UDFs._
import simpledatalabs_27.applicationprojectext2dev2.subgraph.sg1.udfs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Script_1 {
  def apply(context: Context, in0: DataFrame): DataFrame = {
    val spark = context.spark
    val Config = context.config
    val out0 = in0
    out0
  }

}
