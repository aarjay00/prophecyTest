package io.prophecy.pipelines.basepipeline2.udfs

import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._

object UDFs extends Serializable {

  def registerUDFs(spark: SparkSession) = {
    spark.udf.register("createFullName", createFullName)
    registerAllUDFs(spark)
  }

  def createFullName =
    udf((a: String, b: String) => a + ' ' + b)

}

object PipelineInitCode extends Serializable
