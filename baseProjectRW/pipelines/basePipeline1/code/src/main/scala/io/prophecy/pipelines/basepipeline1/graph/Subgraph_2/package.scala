package io.prophecy.pipelines.basepipeline1.graph

import io.prophecy.libs._
import io.prophecy.pipelines.basepipeline1.graph.Subgraph_2.config._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_2 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_1 = Reformat_1(context, in0)
    df_Reformat_1
  }

}
