package graph.pscKeyGenerationVC_ARRG_ID

import io.prophecy.libs._
import udfs.PipelineInitCode._
import udfs.UDFs._
import graph.pscKeyGenerationVC_ARRG_ID.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object moDropSurrogeteKey {

  def apply(context: Context, lkAllRecs: DataFrame): DataFrame =
    lkAllRecs.select(col("TRAN_RNK_ID"), col("NATURALKEY"))

}
