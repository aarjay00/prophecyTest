package io.prophecy.pipelines.p1.graph

import io.prophecy.libs._
import io.prophecy.pipelines.p1.config.ConfigStore._
import io.prophecy.pipelines.p1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object de {

  def apply(context: Context): DataFrame =
    context.spark.read
      .format("csv")
      .option("header",                          true)
      .option("sep",                             ",")
      .schema(StructType(Array(StructField("de", StringType, true))))
      .load("de")

}
