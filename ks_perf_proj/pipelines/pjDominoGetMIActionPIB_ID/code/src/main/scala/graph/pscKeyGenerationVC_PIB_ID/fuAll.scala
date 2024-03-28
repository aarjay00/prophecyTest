package graph.pscKeyGenerationVC_PIB_ID

import io.prophecy.libs._
import udfs.PipelineInitCode._
import udfs.UDFs._
import graph.pscKeyGenerationVC_PIB_ID.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object fuAll {

  def apply(
    context:        Context,
    lkNewKeysFound: DataFrame,
    lkFound:        DataFrame
  ): DataFrame =
    List(lkNewKeysFound, lkFound).flatMap(Option(_)).reduce(_.unionAll(_))

}
