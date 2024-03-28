package graph

import io.prophecy.libs._
import config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dsWorkingData {

  def apply(context: Context): DataFrame = {
    val Config = context.config
    context.spark.read
      .format("csv")
      .option("header", true)
      .option("quote",  "\"")
      .option("sep",    ",")
      .schema(StructType(Array()))
      .load(
        s"${Config.pUKDWTEMPFILEPATH}/${Config.pCLEANSEDDATASET}_${Config.pPIB_ID}_${Config.pTABLE_NAME}_${Config.pLOOP_NUM}.ds"
      )
  }

}
