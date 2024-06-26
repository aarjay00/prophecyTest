from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def MultiFieldFormula_627(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        when(col("A0").isNull(), lit(0)).otherwise(col("A0")).alias("A0"), 
        when(col("A1").isNull(), lit(0)).otherwise(col("A1")).alias("A1"), 
        when(col("A2").isNull(), lit(0)).otherwise(col("A2")).alias("A2"), 
        when(col("A3").isNull(), lit(0)).otherwise(col("A3")).alias("A3"), 
        when(col("A4").isNull(), lit(0)).otherwise(col("A4")).alias("A4"), 
        when(col("A5").isNull(), lit(0)).otherwise(col("A5")).alias("A5"), 
        when(col("A6").isNull(), lit(0)).otherwise(col("A6")).alias("A6"), 
        when(col("A7").isNull(), lit(0)).otherwise(col("A7")).alias("A7"), 
        when(col("A8").isNull(), lit(0)).otherwise(col("A8")).alias("A8"), 
        when(col("A9").isNull(), lit(0)).otherwise(col("A9")).alias("A9"), 
        when(col("B0").isNull(), lit(0)).otherwise(col("B0")).alias("B0"), 
        when(col("B1").isNull(), lit(0)).otherwise(col("B1")).alias("B1"), 
        when(col("B2").isNull(), lit(0)).otherwise(col("B2")).alias("B2"), 
        when(col("B3").isNull(), lit(0)).otherwise(col("B3")).alias("B3"), 
        when(col("B4").isNull(), lit(0)).otherwise(col("B4")).alias("B4"), 
        when(col("B5").isNull(), lit(0)).otherwise(col("B5")).alias("B5"), 
        when(col("B6").isNull(), lit(0)).otherwise(col("B6")).alias("B6"), 
        when(col("B7").isNull(), lit(0)).otherwise(col("B7")).alias("B7"), 
        when(col("B8").isNull(), lit(0)).otherwise(col("B8")).alias("B8"), 
        when(col("B9").isNull(), lit(0)).otherwise(col("B9")).alias("B9"), 
        when(col("C0").isNull(), lit(0)).otherwise(col("C0")).alias("C0"), 
        when(col("C1").isNull(), lit(0)).otherwise(col("C1")).alias("C1"), 
        when(col("C2").isNull(), lit(0)).otherwise(col("C2")).alias("C2"), 
        when(col("C3").isNull(), lit(0)).otherwise(col("C3")).alias("C3"), 
        when(col("C4").isNull(), lit(0)).otherwise(col("C4")).alias("C4"), 
        when(col("C5").isNull(), lit(0)).otherwise(col("C5")).alias("C5"), 
        when(col("C6").isNull(), lit(0)).otherwise(col("C6")).alias("C6"), 
        when(col("C7").isNull(), lit(0)).otherwise(col("C7")).alias("C7"), 
        when(col("C8").isNull(), lit(0)).otherwise(col("C8")).alias("C8"), 
        when(col("C9").isNull(), lit(0)).otherwise(col("C9")).alias("C9"), 
        when(col("D0").isNull(), lit(0)).otherwise(col("D0")).alias("D0"), 
        when(col("D1").isNull(), lit(0)).otherwise(col("D1")).alias("D1"), 
        when(col("D2").isNull(), lit(0)).otherwise(col("D2")).alias("D2"), 
        when(col("D3").isNull(), lit(0)).otherwise(col("D3")).alias("D3"), 
        when(col("D4").isNull(), lit(0)).otherwise(col("D4")).alias("D4"), 
        when(col("D5").isNull(), lit(0)).otherwise(col("D5")).alias("D5"), 
        when(col("D6").isNull(), lit(0)).otherwise(col("D6")).alias("D6"), 
        when(col("D7").isNull(), lit(0)).otherwise(col("D7")).alias("D7"), 
        when(col("D8").isNull(), lit(0)).otherwise(col("D8")).alias("D8"), 
        when(col("E0").isNull(), lit(0)).otherwise(col("E0")).alias("E0"), 
        when(col("E1").isNull(), lit(0)).otherwise(col("E1")).alias("E1"), 
        when(col("E2").isNull(), lit(0)).otherwise(col("E2")).alias("E2"), 
        when(col("E3").isNull(), lit(0)).otherwise(col("E3")).alias("E3"), 
        when(col("E4").isNull(), lit(0)).otherwise(col("E4")).alias("E4"), 
        when(col("E5").isNull(), lit(0)).otherwise(col("E5")).alias("E5"), 
        when(col("E6").isNull(), lit(0)).otherwise(col("E6")).alias("E6"), 
        when(col("E7").isNull(), lit(0)).otherwise(col("E7")).alias("E7"), 
        when(col("E8").isNull(), lit(0)).otherwise(col("E8")).alias("E8"), 
        when(col("F0").isNull(), lit(0)).otherwise(col("F0")).alias("F0"), 
        when(col("F1").isNull(), lit(0)).otherwise(col("F1")).alias("F1"), 
        when(col("F2").isNull(), lit(0)).otherwise(col("F2")).alias("F2"), 
        when(col("F3").isNull(), lit(0)).otherwise(col("F3")).alias("F3"), 
        when(col("F4").isNull(), lit(0)).otherwise(col("F4")).alias("F4"), 
        when(col("F5").isNull(), lit(0)).otherwise(col("F5")).alias("F5"), 
        when(col("F6").isNull(), lit(0)).otherwise(col("F6")).alias("F6"), 
        when(col("F7").isNull(), lit(0)).otherwise(col("F7")).alias("F7"), 
        when(col("F8").isNull(), lit(0)).otherwise(col("F8")).alias("F8"), 
        when(col("F9").isNull(), lit(0)).otherwise(col("F9")).alias("F9"), 
        when(col("G0").isNull(), lit(0)).otherwise(col("G0")).alias("G0"), 
        when(col("G1").isNull(), lit(0)).otherwise(col("G1")).alias("G1"), 
        when(col("G2").isNull(), lit(0)).otherwise(col("G2")).alias("G2"), 
        when(col("G3").isNull(), lit(0)).otherwise(col("G3")).alias("G3"), 
        when(col("G4").isNull(), lit(0)).otherwise(col("G4")).alias("G4"), 
        when(col("G5").isNull(), lit(0)).otherwise(col("G5")).alias("G5"), 
        when(col("G6").isNull(), lit(0)).otherwise(col("G6")).alias("G6"), 
        when(col("G7").isNull(), lit(0)).otherwise(col("G7")).alias("G7"), 
        when(col("G8").isNull(), lit(0)).otherwise(col("G8")).alias("G8"), 
        when(col("G9").isNull(), lit(0)).otherwise(col("G9")).alias("G9"), 
        when(col("H0").isNull(), lit(0)).otherwise(col("H0")).alias("H0"), 
        when(col("H1").isNull(), lit(0)).otherwise(col("H1")).alias("H1"), 
        when(col("H2").isNull(), lit(0)).otherwise(col("H2")).alias("H2"), 
        when(col("H3").isNull(), lit(0)).otherwise(col("H3")).alias("H3"), 
        when(col("H4").isNull(), lit(0)).otherwise(col("H4")).alias("H4"), 
        when(col("H5").isNull(), lit(0)).otherwise(col("H5")).alias("H5"), 
        when(col("H6").isNull(), lit(0)).otherwise(col("H6")).alias("H6"), 
        when(col("H7").isNull(), lit(0)).otherwise(col("H7")).alias("H7"), 
        when(col("H8").isNull(), lit(0)).otherwise(col("H8")).alias("H8"), 
        when(col("H9").isNull(), lit(0)).otherwise(col("H9")).alias("H9"), 
        when(col("I0").isNull(), lit(0)).otherwise(col("I0")).alias("I0"), 
        when(col("I1").isNull(), lit(0)).otherwise(col("I1")).alias("I1"), 
        when(col("I2").isNull(), lit(0)).otherwise(col("I2")).alias("I2"), 
        when(col("I3").isNull(), lit(0)).otherwise(col("I3")).alias("I3"), 
        when(col("I4").isNull(), lit(0)).otherwise(col("I4")).alias("I4"), 
        when(col("I5").isNull(), lit(0)).otherwise(col("I5")).alias("I5"), 
        when(col("I6").isNull(), lit(0)).otherwise(col("I6")).alias("I6"), 
        when(col("I7").isNull(), lit(0)).otherwise(col("I7")).alias("I7"), 
        when(col("I8").isNull(), lit(0)).otherwise(col("I8")).alias("I8"), 
        when(col("I9").isNull(), lit(0)).otherwise(col("I9")).alias("I9"), 
        when(col("J0").isNull(), lit(0)).otherwise(col("J0")).alias("J0"), 
        when(col("J1").isNull(), lit(0)).otherwise(col("J1")).alias("J1"), 
        when(col("J2").isNull(), lit(0)).otherwise(col("J2")).alias("J2"), 
        when(col("J3").isNull(), lit(0)).otherwise(col("J3")).alias("J3"), 
        when(col("J4").isNull(), lit(0)).otherwise(col("J4")).alias("J4"), 
        when(col("J6").isNull(), lit(0)).otherwise(col("J6")).alias("J6"), 
        when(col("J7").isNull(), lit(0)).otherwise(col("J7")).alias("J7"), 
        when(col("J8").isNull(), lit(0)).otherwise(col("J8")).alias("J8"), 
        when(col("J9").isNull(), lit(0)).otherwise(col("J9")).alias("J9"), 
        when(col("K0").isNull(), lit(0)).otherwise(col("K0")).alias("K0"), 
        when(col("K1").isNull(), lit(0)).otherwise(col("K1")).alias("K1"), 
        when(col("K2").isNull(), lit(0)).otherwise(col("K2")).alias("K2"), 
        when(col("K3").isNull(), lit(0)).otherwise(col("K3")).alias("K3"), 
        when(col("K4").isNull(), lit(0)).otherwise(col("K4")).alias("K4"), 
        when(col("K5").isNull(), lit(0)).otherwise(col("K5")).alias("K5"), 
        when(col("K6").isNull(), lit(0)).otherwise(col("K6")).alias("K6"), 
        when(col("K7").isNull(), lit(0)).otherwise(col("K7")).alias("K7"), 
        when(col("K8").isNull(), lit(0)).otherwise(col("K8")).alias("K8"), 
        when(col("K9").isNull(), lit(0)).otherwise(col("K9")).alias("K9"), 
        when(col("L0").isNull(), lit(0)).otherwise(col("L0")).alias("L0"), 
        when(col("L1").isNull(), lit(0)).otherwise(col("L1")).alias("L1"), 
        when(col("L2").isNull(), lit(0)).otherwise(col("L2")).alias("L2"), 
        when(col("L3").isNull(), lit(0)).otherwise(col("L3")).alias("L3"), 
        when(col("L4").isNull(), lit(0)).otherwise(col("L4")).alias("L4"), 
        when(col("L5").isNull(), lit(0)).otherwise(col("L5")).alias("L5"), 
        when(col("L6").isNull(), lit(0)).otherwise(col("L6")).alias("L6"), 
        when(col("L7").isNull(), lit(0)).otherwise(col("L7")).alias("L7"), 
        when(col("L8").isNull(), lit(0)).otherwise(col("L8")).alias("L8"), 
        when(col("L9").isNull(), lit(0)).otherwise(col("L9")).alias("L9"), 
        when(col("M0").isNull(), lit(0)).otherwise(col("M0")).alias("M0"), 
        when(col("M1").isNull(), lit(0)).otherwise(col("M1")).alias("M1"), 
        when(col("M2").isNull(), lit(0)).otherwise(col("M2")).alias("M2"), 
        when(col("M3").isNull(), lit(0)).otherwise(col("M3")).alias("M3"), 
        when(col("M4").isNull(), lit(0)).otherwise(col("M4")).alias("M4"), 
        when(col("M5").isNull(), lit(0)).otherwise(col("M5")).alias("M5"), 
        when(col("M6").isNull(), lit(0)).otherwise(col("M6")).alias("M6"), 
        when(col("M7").isNull(), lit(0)).otherwise(col("M7")).alias("M7"), 
        when(col("M8").isNull(), lit(0)).otherwise(col("M8")).alias("M8"), 
        when(col("M9").isNull(), lit(0)).otherwise(col("M9")).alias("M9"), 
        when(col("N0").isNull(), lit(0)).otherwise(col("N0")).alias("N0"), 
        when(col("N1").isNull(), lit(0)).otherwise(col("N1")).alias("N1"), 
        when(col("N2").isNull(), lit(0)).otherwise(col("N2")).alias("N2"), 
        when(col("N3").isNull(), lit(0)).otherwise(col("N3")).alias("N3"), 
        when(col("N4").isNull(), lit(0)).otherwise(col("N4")).alias("N4"), 
        when(col("N5").isNull(), lit(0)).otherwise(col("N5")).alias("N5"), 
        when(col("N6").isNull(), lit(0)).otherwise(col("N6")).alias("N6"), 
        when(col("N7").isNull(), lit(0)).otherwise(col("N7")).alias("N7"), 
        when(col("N8").isNull(), lit(0)).otherwise(col("N8")).alias("N8"), 
        when(col("N9").isNull(), lit(0)).otherwise(col("N9")).alias("N9"), 
        when(col("O0").isNull(), lit(0)).otherwise(col("O0")).alias("O0"), 
        when(col("O1").isNull(), lit(0)).otherwise(col("O1")).alias("O1"), 
        when(col("O2").isNull(), lit(0)).otherwise(col("O2")).alias("O2"), 
        when(col("O3").isNull(), lit(0)).otherwise(col("O3")).alias("O3"), 
        when(col("O4").isNull(), lit(0)).otherwise(col("O4")).alias("O4"), 
        when(col("O6").isNull(), lit(0)).otherwise(col("O6")).alias("O6"), 
        when(col("O7").isNull(), lit(0)).otherwise(col("O7")).alias("O7"), 
        when(col("O8").isNull(), lit(0)).otherwise(col("O8")).alias("O8"), 
        when(col("O9").isNull(), lit(0)).otherwise(col("O9")).alias("O9"), 
        when(col("P0").isNull(), lit(0)).otherwise(col("P0")).alias("P0"), 
        when(col("P1").isNull(), lit(0)).otherwise(col("P1")).alias("P1"), 
        when(col("P2").isNull(), lit(0)).otherwise(col("P2")).alias("P2"), 
        when(col("P3").isNull(), lit(0)).otherwise(col("P3")).alias("P3"), 
        when(col("P5").isNull(), lit(0)).otherwise(col("P5")).alias("P5"), 
        when(col("P6").isNull(), lit(0)).otherwise(col("P6")).alias("P6"), 
        when(col("P7").isNull(), lit(0)).otherwise(col("P7")).alias("P7"), 
        when(col("P8").isNull(), lit(0)).otherwise(col("P8")).alias("P8"), 
        when(col("P9").isNull(), lit(0)).otherwise(col("P9")).alias("P9"), 
        when(col("Q0").isNull(), lit(0)).otherwise(col("Q0")).alias("Q0"), 
        when(col("Q1").isNull(), lit(0)).otherwise(col("Q1")).alias("Q1"), 
        when(col("Q2").isNull(), lit(0)).otherwise(col("Q2")).alias("Q2"), 
        when(col("Q3").isNull(), lit(0)).otherwise(col("Q3")).alias("Q3"), 
        when(col("Q4").isNull(), lit(0)).otherwise(col("Q4")).alias("Q4"), 
        when(col("Q5").isNull(), lit(0)).otherwise(col("Q5")).alias("Q5"), 
        when(col("Q6").isNull(), lit(0)).otherwise(col("Q6")).alias("Q6"), 
        when(col("Q7").isNull(), lit(0)).otherwise(col("Q7")).alias("Q7"), 
        when(col("Q8").isNull(), lit(0)).otherwise(col("Q8")).alias("Q8"), 
        when(col("Q9").isNull(), lit(0)).otherwise(col("Q9")).alias("Q9"), 
        when(col("R0").isNull(), lit(0)).otherwise(col("R0")).alias("R0"), 
        when(col("R1").isNull(), lit(0)).otherwise(col("R1")).alias("R1"), 
        when(col("R2").isNull(), lit(0)).otherwise(col("R2")).alias("R2"), 
        when(col("R3").isNull(), lit(0)).otherwise(col("R3")).alias("R3"), 
        when(col("R4").isNull(), lit(0)).otherwise(col("R4")).alias("R4"), 
        when(col("R5").isNull(), lit(0)).otherwise(col("R5")).alias("R5"), 
        when(col("R6").isNull(), lit(0)).otherwise(col("R6")).alias("R6"), 
        when(col("R7").isNull(), lit(0)).otherwise(col("R7")).alias("R7"), 
        when(col("R8").isNull(), lit(0)).otherwise(col("R8")).alias("R8"), 
        when(col("R9").isNull(), lit(0)).otherwise(col("R9")).alias("R9"), 
        when(col("S0").isNull(), lit(0)).otherwise(col("S0")).alias("S0"), 
        when(col("S1").isNull(), lit(0)).otherwise(col("S1")).alias("S1"), 
        when(col("S2").isNull(), lit(0)).otherwise(col("S2")).alias("S2"), 
        when(col("S3").isNull(), lit(0)).otherwise(col("S3")).alias("S3"), 
        when(col("S4").isNull(), lit(0)).otherwise(col("S4")).alias("S4"), 
        when(col("S5").isNull(), lit(0)).otherwise(col("S5")).alias("S5"), 
        when(col("S6").isNull(), lit(0)).otherwise(col("S6")).alias("S6"), 
        when(col("S7").isNull(), lit(0)).otherwise(col("S7")).alias("S7"), 
        when(col("S8").isNull(), lit(0)).otherwise(col("S8")).alias("S8"), 
        when(col("S9").isNull(), lit(0)).otherwise(col("S9")).alias("S9"), 
        when(col("T0").isNull(), lit(0)).otherwise(col("T0")).alias("T0"), 
        when(col("T1").isNull(), lit(0)).otherwise(col("T1")).alias("T1"), 
        when(col("T2").isNull(), lit(0)).otherwise(col("T2")).alias("T2"), 
        when(col("T3").isNull(), lit(0)).otherwise(col("T3")).alias("T3"), 
        when(col("T4").isNull(), lit(0)).otherwise(col("T4")).alias("T4"), 
        when(col("T5").isNull(), lit(0)).otherwise(col("T5")).alias("T5"), 
        when(col("T6").isNull(), lit(0)).otherwise(col("T6")).alias("T6"), 
        when(col("T7").isNull(), lit(0)).otherwise(col("T7")).alias("T7"), 
        when(col("T8").isNull(), lit(0)).otherwise(col("T8")).alias("T8"), 
        when(col("U0").isNull(), lit(0)).otherwise(col("U0")).alias("U0"), 
        when(col("V0").isNull(), lit(0)).otherwise(col("V0")).alias("V0"), 
        when(col("V1").isNull(), lit(0)).otherwise(col("V1")).alias("V1"), 
        when(col("V2").isNull(), lit(0)).otherwise(col("V2")).alias("V2"), 
        when(col("V3").isNull(), lit(0)).otherwise(col("V3")).alias("V3"), 
        when(col("V4").isNull(), lit(0)).otherwise(col("V4")).alias("V4"), 
        when(col("V5").isNull(), lit(0)).otherwise(col("V5")).alias("V5"), 
        when(col("V6").isNull(), lit(0)).otherwise(col("V6")).alias("V6"), 
        when(col("V7").isNull(), lit(0)).otherwise(col("V7")).alias("V7"), 
        when(col("V8").isNull(), lit(0)).otherwise(col("V8")).alias("V8"), 
        when(col("V9").isNull(), lit(0)).otherwise(col("V9")).alias("V9"), 
        when(col("W0").isNull(), lit(0)).otherwise(col("W0")).alias("W0"), 
        when(col("W1").isNull(), lit(0)).otherwise(col("W1")).alias("W1"), 
        when(col("W2").isNull(), lit(0)).otherwise(col("W2")).alias("W2"), 
        when(col("W3").isNull(), lit(0)).otherwise(col("W3")).alias("W3"), 
        when(col("W4").isNull(), lit(0)).otherwise(col("W4")).alias("W4"), 
        when(col("W5").isNull(), lit(0)).otherwise(col("W5")).alias("W5"), 
        when(col("W6").isNull(), lit(0)).otherwise(col("W6")).alias("W6"), 
        when(col("W7").isNull(), lit(0)).otherwise(col("W7")).alias("W7"), 
        when(col("W8").isNull(), lit(0)).otherwise(col("W8")).alias("W8"), 
        when(col("W9").isNull(), lit(0)).otherwise(col("W9")).alias("W9"), 
        when(col("X0").isNull(), lit(0)).otherwise(col("X0")).alias("X0"), 
        when(col("X1").isNull(), lit(0)).otherwise(col("X1")).alias("X1"), 
        when(col("X3").isNull(), lit(0)).otherwise(col("X3")).alias("X3"), 
        when(col("X5").isNull(), lit(0)).otherwise(col("X5")).alias("X5"), 
        when(col("X7").isNull(), lit(0)).otherwise(col("X7")).alias("X7"), 
        when(col("X8").isNull(), lit(0)).otherwise(col("X8")).alias("X8"), 
        when(col("X9").isNull(), lit(0)).otherwise(col("X9")).alias("X9"), 
        when(col("Y0").isNull(), lit(0)).otherwise(col("Y0")).alias("Y0"), 
        when(col("Y2").isNull(), lit(0)).otherwise(col("Y2")).alias("Y2"), 
        when(col("Y3").isNull(), lit(0)).otherwise(col("Y3")).alias("Y3"), 
        when(col("Y6").isNull(), lit(0)).otherwise(col("Y6")).alias("Y6"), 
        when(col("Y7").isNull(), lit(0)).otherwise(col("Y7")).alias("Y7"), 
        when(col("Y8").isNull(), lit(0)).otherwise(col("Y8")).alias("Y8"), 
        when(col("Y9").isNull(), lit(0)).otherwise(col("Y9")).alias("Y9"), 
        when(col("Z0").isNull(), lit(0)).otherwise(col("Z0")).alias("Z0"), 
        when(col("Z1").isNull(), lit(0)).otherwise(col("Z1")).alias("Z1"), 
        when(col("Z2").isNull(), lit(0)).otherwise(col("Z2")).alias("Z2"), 
        when(col("Z3").isNull(), lit(0)).otherwise(col("Z3")).alias("Z3"), 
        when(col("Z4").isNull(), lit(0)).otherwise(col("Z4")).alias("Z4"), 
        when(col("Z5").isNull(), lit(0)).otherwise(col("Z5")).alias("Z5"), 
        when(col("Z6").isNull(), lit(0)).otherwise(col("Z6")).alias("Z6"), 
        when(col("Z7").isNull(), lit(0)).otherwise(col("Z7")).alias("Z7"), 
        when(col("Z8").isNull(), lit(0)).otherwise(col("Z8")).alias("Z8"), 
        when(col("Z9").isNull(), lit(0)).otherwise(col("Z9")).alias("Z9"), 
        col("YEARMONTH"), 
        col("MBR_INDV_BE_KEY")
    )
