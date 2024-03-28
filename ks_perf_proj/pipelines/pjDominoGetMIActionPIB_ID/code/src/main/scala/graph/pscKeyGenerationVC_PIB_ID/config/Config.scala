package graph.pscKeyGenerationVC_PIB_ID.config

import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession
import graph.pscKeyGenerationVC_PIB_ID.pscMessageHandlingSCtrC235.config.{
  Config => pscMessageHandlingSCtrC235_Config
}

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Config() extends ConfigBase
case class Context(spark: SparkSession, config: Config)
