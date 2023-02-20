package io.prophecy.pipelines.pipeline1.udfs

import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._

object UDFs extends Serializable {

  def registerUDFs(spark: SparkSession) = {
    spark.udf.register("square",  square)
    spark.udf.register("trimUDF", trimUDF)
    spark.udf.register("square2", square2)
  }

  def square = {
    val x = 10
    udf((value: Int) => value * value)
  }

  def trimUDF = {
    val y = 10
    udf((value: String) => value.trim())
  }

  def square2 =
    udf((value2: Int) => value2 * value2)

}

object PipelineInitCode extends Serializable
