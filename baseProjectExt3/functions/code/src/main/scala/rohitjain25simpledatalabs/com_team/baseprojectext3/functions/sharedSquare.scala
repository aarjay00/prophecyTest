package rohitjain25simpledatalabs.com_team.baseprojectext3.functions
import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._
object SharedSquare extends Serializable { def sharedSquare = udf { (i: Int) => i * i } }