package simpledatalabs_27.rohitmigrationtesting

import org.apache.spark.sql._
package object functions {
  val addNumbers10 = AddNumbers10.addNumbers10
  val addNumbers11 = AddNumbers11.addNumbers11

  def registerFunctions(spark: SparkSession) = {
    spark.udf.register("addNumbers10", addNumbers10)
    spark.udf.register("addNumbers11", addNumbers11)
  }

}
