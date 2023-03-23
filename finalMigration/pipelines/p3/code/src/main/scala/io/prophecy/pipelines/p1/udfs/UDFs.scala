package io.prophecy.pipelines.p1.udfs

import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._

object UDFs extends Serializable {

  def registerUDFs(spark: SparkSession) = {
    spark.udf.register("udf11", udf11)
    spark.udf.register("udf22", udf22)
    spark.udf.register("udf33", udf33)
    spark.udf.register("udf1",  udf1)
    spark.udf.register("udf2",  udf2)
    spark.udf.register("udf3",  udf3)
    registerAllUDFs(spark)
  }

  def udf11 = {
    val x = 3
    udf(() => "")
  }

  def udf22 = {
    val x = 3
    udf(() => "")
  }

  def udf33 = {
    val x = 3
    udf(() => "")
  }

  def udf1 = {
    val x = 1
    udf(() => "")
  }

  def udf2 = {
    val x = 1
    udf(() => "")
  }

  def udf3 = {
    val x = 1
    udf(() => "")
  }

}

object PipelineInitCode extends Serializable { val x = 3 }