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

object luRefExists_reject {

  def apply(
    context:              Context,
    lkRefExists_reject:   DataFrame,
    lkCheckExists_reject: DataFrame
  ): DataFrame =
    lkRefExists_reject
      .as("lkRefExists_reject")
      .join(
        lkCheckExists_reject.as("lkRefExists"),
        (col("lkCheckExists.KEY4") === col("lkRefExists.KEY4"))
          .and(col("lkCheckExists.KEY5") === col("lkRefExists.KEY5"))
          .and(col("lkCheckExists.KEY1") === col("lkRefExists.KEY1"))
          .and(col("lkCheckExists.KEY2") === col("lkRefExists.KEY2"))
          .and(col("lkCheckExists.KEY6") === col("lkRefExists.KEY6"))
          .and(col("lkCheckExists.KEY3") === col("lkRefExists.KEY3")),
        "inner"
      )
      .select(
        col("lkRefExists_reject.KEY4").as("KEY4"),
        col("lkRefExists_reject.KEY5").as("KEY5"),
        col("lkRefExists_reject.KEY1").as("KEY1"),
        col("lkRefExists_reject.KEY2").as("KEY2"),
        col("lkRefExists_reject.KEY6").as("KEY6"),
        col("lkRefExists_reject.KEY3").as("KEY3")
      )

}