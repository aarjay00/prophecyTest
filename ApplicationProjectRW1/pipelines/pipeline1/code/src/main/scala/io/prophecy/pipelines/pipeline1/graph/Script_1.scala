package io.prophecy.pipelines.pipeline1.graph

import io.prophecy.libs._
import io.prophecy.pipelines.pipeline1.config.Context
import io.prophecy.pipelines.pipeline1.udfs.UDFs._
import io.prophecy.pipelines.pipeline1.udfs.UDFs._
import io.prophecy.pipelines.pipeline1.udfs._
import io.prophecy.pipelines.pipeline1.udfs.UDFs.PipelineInitCode._
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
    val x = pipeline1
    val out0 = in0
    out0
  }

}
