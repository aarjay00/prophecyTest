package io.prophecy.pipelines.basepipeline1.graph

import io.prophecy.libs._
import io.prophecy.pipelines.basepipeline1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object baseDS2 {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("csv")
      .option("header", true)
      .option("sep",    ",")
      .mode("overwrite")
      .save("dbfs:/Prophecy/123@mm.com/baseDS2")

}
