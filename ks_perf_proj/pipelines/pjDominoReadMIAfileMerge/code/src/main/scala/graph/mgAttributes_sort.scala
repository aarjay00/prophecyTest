package graph

import io.prophecy.libs._
import udfs.PipelineInitCode._
import udfs.UDFs._
import config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object mgAttributes_sort {

  def apply(context: Context, V65S4_union_sort: DataFrame): DataFrame =
    V65S4_union_sort.orderBy(lit("0(1)(3)key").asc)

}
