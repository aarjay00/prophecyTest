package simpledatalabs_27.baseprojectrw.subgraph.basesg1.config

import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
import org.apache.spark.sql.SparkSession

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Config(config1: String = "conf2value") extends ConfigBase
case class Context(spark: SparkSession, config: Config)