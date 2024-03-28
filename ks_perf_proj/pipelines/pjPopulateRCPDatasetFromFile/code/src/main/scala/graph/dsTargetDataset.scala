package graph

import io.prophecy.libs._
import config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dsTargetDataset {

  def apply(context: Context, in: DataFrame): Unit = {
    val Config = context.config
    var writer = in.write
      .format("csv")
      .option("header", true)
      .option("quote",  "\"")
      .option("sep",    ",")
    writer = writer.mode("error")
    writer.save(s"${Config.pTargetPath}/${Config.pTargetDatasetName}")
  }

}
