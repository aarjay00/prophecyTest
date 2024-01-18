package io.prophecy.pipelines.p1.graph

import io.prophecy.libs._
import io.prophecy.pipelines.p1.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object jdbc_databricks {

  def apply(context: Context): DataFrame = {
    var reader = context.spark.read.format("jdbc")
    reader = reader
      .option(
        "url",
        "jdbc:databricks://dbc-ac0e9adb-13fb.cloud.databricks.com:443/default;transportMode=http;ssl=1;AuthMech=3;httpPath=/sql/1.0/warehouses/2dc4d06bcada6a51;"
      )
      .option("user", {
                import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
                dbutils.secrets.get(scope = "tanmay", key = "username")
              }
      )
      .option("password", {
                import com.databricks.dbutils_v1.DBUtilsHolder.dbutils
                dbutils.secrets.get(scope = "tanmay", key = "password")
              }
      )
      .option("pushDownPredicate",    true)
      .option("driver",               "org.postgressql.Driver")
    reader = reader.option("dbtable", "tablename")
    reader.load()
  }

}
