package rohitjain27simpledatalabs.com_team.pm3rework

import org.apache.spark.sql._
package object functions {
  val trimUDF   = TrimUDF.trimUDF
  val square    = Square.square
  val square212 = Square212.square212
  val trimUDF1  = TrimUDF1.trimUDF1
  val square1   = Square1.square1
  val trimUDF2  = TrimUDF2.trimUDF2
  val square3   = Square3.square3

  def registerFunctions(spark: SparkSession) = {
    spark.udf.register("trimUDF",   trimUDF)
    spark.udf.register("square",    square)
    spark.udf.register("square212", square212)
    spark.udf.register("trimUDF1",  trimUDF1)
    spark.udf.register("square1",   square1)
    spark.udf.register("trimUDF2",  trimUDF2)
    spark.udf.register("square3",   square3)
  }

}
