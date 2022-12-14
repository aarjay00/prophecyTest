package simpledatalabs_27.applicationprojectext2.subgraph.appsg1.config

import io.prophecy.libs._
import pureconfig._
import pureconfig.generic.ProductHint
object ConfigStore { implicit var Config: Config = _ }

object Config {

  implicit val confHint: ProductHint[Config] =
    ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))

}

case class Config() extends ConfigBase
