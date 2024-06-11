from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def AlteryxSelect_596(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("J2_Running6"), 
        col("K7_Running6"), 
        col("Z09_Running3"), 
        col("E80_Running6"), 
        col("V3_Running6"), 
        col("OfLast6_Main_Rx"), 
        col("D3_Running6"), 
        col("E84_Running3"), 
        col("E05"), 
        col("W0_Running6"), 
        col("E52_Running3"), 
        col("E20"), 
        col("V2_Running6"), 
        col("V9_Running6"), 
        col("S1_Running6"), 
        col("F30"), 
        col("Z22_Running3"), 
        col("L0_Running6"), 
        col("Hearing_Speech_ExamsRunning3"), 
        col("E85"), 
        col("F39_Running3"), 
        col("E44_Running3"), 
        col("R9_Running6"), 
        col("E11_Running6"), 
        col("O8_Running6"), 
        col("Z32"), 
        col("E50_Running6"), 
        col("M15"), 
        col("R17"), 
        col("O6_Running6"), 
        col("S6_Running6"), 
        col("E46_Running3"), 
        col("K1_Running6"), 
        col("H6_Running6"), 
        col("M40_Running3"), 
        col("H1_Running6"), 
        col("Medical___Diagnostic___GastroenterologyRunning3"), 
        col("W5_Running6"), 
        col("O09"), 
        col("C6_Running6"), 
        col("E05_Running6"), 
        col("Z39_Running3"), 
        col("Z03"), 
        col("YEARMONTH"), 
        col("D5_Running6"), 
        col("E8_Running6"), 
        col("M40"), 
        col("E71_Running3"), 
        col("Office_Home_Visits___Office_VisitsRunning3"), 
        col("R15"), 
        col("E72_Running3"), 
        col("IP_Running6_Max"), 
        col("M1A_Running3"), 
        col("H5_Running6"), 
        col("Tertiary_Diagnosis_Running3"), 
        col("G1_Running6"), 
        col("Q6_Running6"), 
        col("M48"), 
        col("O28_Running3"), 
        col("E56_Running6"), 
        col("E40"), 
        col("E79"), 
        col("J3_Running6"), 
        col("M11"), 
        col("E41_Running6"), 
        col("N5_Running6"), 
        col("E89"), 
        col("E58_Running6"), 
        col("E4_Running6"), 
        col("E02_Running6"), 
        col("W7_Running6"), 
        col("M6_Running6"), 
        col("R10"), 
        col("O0_Running6"), 
        col("E29_Running6"), 
        col("F2_Running6"), 
        col("Surgery___Urinary_SystemRunning3"), 
        col("R14_Running3"), 
        col("E16_Running3"), 
        col("P1_Running6"), 
        col("Z23_Running3"), 
        col("Radiology___TherapeuticRunning3"), 
        col("W1_Running6"), 
        col("E88"), 
        col("D0_Running6"), 
        col("PDN_HHRunning3"), 
        col("E06"), 
        col("E61_Running6"), 
        col("AnesthesiaRunning3"), 
        col("L7_Running6"), 
        col("Pathology_and_LabRunning3"), 
        col("Z08"), 
        col("IP_Visits___Neonatal_VisitsRunning3"), 
        col("Primary_Diagnosis"), 
        col("B9_Running6"), 
        col("C1_Running6"), 
        col("M41"), 
        col("E54_Running3"), 
        col("M19"), 
        col("D8_Running6"), 
        col("E43_Running3"), 
        col("B0_Running6"), 
        col("E41"), 
        col("Primary_Rx_Running3"), 
        col("E88_Running6"), 
        col("E54_Running6"), 
        col("M9_Running6"), 
        col("O32"), 
        col("T7_Running6"), 
        col("E75"), 
        col("O35_Running3"), 
        col("E24_Running6"), 
        col("M49"), 
        col("Z09"), 
        col("M17"), 
        col("T2_Running6"), 
        col("S0_Running6"), 
        col("CCI"), 
        col("E66_Running3"), 
        col("Chiropractor___Chiropractic_Manipulative_TreatmentRunning3"), 
        col("F39"), 
        col("E76"), 
        col("Z33"), 
        col("E6_Running6"), 
        col("E89_Running6"), 
        col("G4_Running6"), 
        col("Office_Home_Visits___Prolonged_ServicesRunning3"), 
        col("E58"), 
        col("Y3_Running6"), 
        col("OfLast6_Main_Rx_Costs"), 
        col("E50"), 
        col("F30_Running3"), 
        col("E08"), 
        col("IP_Visits___Nursing_Facility_ServicesRunning3"), 
        col("S9_Running6"), 
        col("Y9_Running6"), 
        col("I4_Running6"), 
        col("E79_Running3"), 
        col("M10"), 
        col("M42"), 
        col("E63_Running3"), 
        col("IP_Visits___Critical_Care_ServicesRunning3"), 
        col("Q1_Running6"), 
        col("C3_Running6"), 
        col("E3_Running6"), 
        col("K0_Running6"), 
        col("ImmunizationsRunning3"), 
        col("E40_Running3"), 
        col("E68"), 
        col("Z3A"), 
        col("M47"), 
        col("Z15"), 
        col("C9_Running6"), 
        col("O24"), 
        col("Y8_Running6"), 
        col("K3_Running6"), 
        col("D7_Running6"), 
        col("E71"), 
        col("P3_Running6"), 
        col("Z22"), 
        col("Non_Standard_BenefitRunning3"), 
        col("E35_Running6"), 
        col("B8_Running6"), 
        col("E28_Running6"), 
        col("E74_Running3"), 
        col("R1_Running6"), 
        col("R3_Running6"), 
        col("E43_Running6"), 
        col("D1_Running6"), 
        col("E20_Running3"), 
        col("Z08_Running3"), 
        col("E88_Running3"), 
        col("M48_Running3"), 
        col("T8_Running6"), 
        col("E04"), 
        col("Radiology___NuclearRunning3"), 
        col("Office_Home_Visits___Care_Plan_Oversight_ServicesRunning3"), 
        col("N3_Running6"), 
        col("E01"), 
        col("OfLast6_Main_Diag"), 
        col("E10"), 
        col("R8_Running6"), 
        col("L9_Running6"), 
        col("E51_Running6"), 
        col("F1_Running6"), 
        col("Surgery___Respiratory_SystemRunning3"), 
        col("D6_Running6"), 
        col("E56_Running3"), 
        col("E53_Running6"), 
        col("B6_Running6"), 
        col("E60_Running6"), 
        col("A1_Running6"), 
        col("E61"), 
        col("E0_Running6"), 
        col("O2_Running6"), 
        col("M8_Running6"), 
        col("F32"), 
        col("S5_Running6"), 
        col("W3_Running6"), 
        col("E52"), 
        col("E04_Running6"), 
        col("E09_Running3"), 
        col("Y6_Running6"), 
        col("H7_Running6"), 
        col("Z12_Running3"), 
        col("F6_Running6"), 
        col("O30"), 
        col("Z36"), 
        col("Z30"), 
        col("N2_Running6"), 
        col("M1_Running6"), 
        col("E76_Running3"), 
        col("HighestAlbumin_Running3"), 
        col("CCI_6MoSum"), 
        col("E34"), 
        col("Physical_ExamsRunning3"), 
        col("G3_Running6"), 
        col("CountOfLabs_Running3"), 
        col("E70"), 
        col("R16"), 
        col("E73_Running6"), 
        col("E84_Running6"), 
        col("E86"), 
        col("R13"), 
        col("Z00_Running3"), 
        col("O03"), 
        col("E68_Running3"), 
        col("X0_Running6"), 
        col("T0_Running6"), 
        col("Z12"), 
        col("E27"), 
        col("C4_Running6"), 
        col("O00_Running3"), 
        col("E86_Running6"), 
        col("Cardiovascular___Other_ProceduresRunning3"), 
        col("O7_Running6"), 
        col("Z13_Running3"), 
        col("I9_Running6"), 
        col("A8_Running6"), 
        col("M13"), 
        col("J1_Running6"), 
        col("IP_Running6"), 
        col("P5_Running6"), 
        col("L5_Running6"), 
        col("R19"), 
        col("K4_Running6"), 
        col("V4_Running6"), 
        col("E07_Running3"), 
        col("E15"), 
        col("E08_Running3"), 
        col("Primary_RxCosts_Running3"), 
        col("M49_Running3"), 
        col("Z16"), 
        col("B7_Running6"), 
        col("Medical___Diagnostic___BiofeedbackRunning3"), 
        col("A5_Running6"), 
        col("M2_Running6"), 
        col("L3_Running6"), 
        col("Surgery___Nervous_SystemRunning3"), 
        col("I7_Running6"), 
        col("Z29_Running3"), 
        col("Z04"), 
        col("Q8_Running6"), 
        col("O02_Running3"), 
        col("Surgery___Digestive_SystemRunning3"), 
        col("R7_Running6"), 
        col("E02"), 
        col("E03"), 
        col("M45"), 
        col("F9_Running6"), 
        col("Z4_Running6"), 
        col("RecordID"), 
        col("E60"), 
        col("Z7_Running6"), 
        col("E52_Running6"), 
        col("E59_Running3"), 
        col("B2_Running6"), 
        col("OfLast6_Main_Diag_Cost"), 
        col("ER_Visits_and_Observation_CareRunning3"), 
        col("R13_Running3"), 
        col("Z32_Running3"), 
        col("O35"), 
        col("M4_Running6"), 
        col("E28"), 
        col("Surgery___Endocrine_SystemRunning3"), 
        col("F0_Running6"), 
        col("X9_Running6"), 
        col("I5_Running6"), 
        col("J7_Running6"), 
        col("E25_Running6"), 
        col("Tertiary_Rx_Running3"), 
        col("Surgery___Integumentary_System___Excision_of_Malignant_LesionsRunning3"), 
        col("L6_Running6"), 
        col("S4_Running6"), 
        col("Z31"), 
        col("T3_Running6"), 
        col("Z11"), 
        col("IP_PreviousMonth"), 
        col("E15_Running6"), 
        col("R10_Running3"), 
        col("I1_Running6"), 
        col("Allergy_ImmunotherapyRunning3"), 
        col("O03_Running3"), 
        col("IP_Visits___Newborn_CareRunning3"), 
        col("Z23"), 
        col("O04_Running3"), 
        col("MBR_GNDR_CD"), 
        col("Allergy_TestingRunning3"), 
        col("E07"), 
        col("G7_Running6"), 
        col("K9_Running6"), 
        col("MBR_SK"), 
        col("W6_Running6"), 
        col("E53_Running3"), 
        col("E70_Running6"), 
        col("M14"), 
        col("Relative_IP_Month"), 
        col("R16_Running3"), 
        col("Y7_Running6"), 
        col("Well_Baby_ExamsRunning3"), 
        col("E05_Running3"), 
        col("H9_Running6"), 
        col("E00_Running6"), 
        col("M46"), 
        col("O24_Running3"), 
        col("Psychiatric_Alcohol_Drug_AbuseRunning3"), 
        col("E30_Running6"), 
        col("V1_Running6"), 
        col("K6_Running6"), 
        col("O07"), 
        col("Y0_Running6"), 
        col("O32_Running3"), 
        col("I3_Running6"), 
        col("E85_Running3"), 
        col("E46"), 
        col("O20_Running3"), 
        col("L4_Running6"), 
        col("A9_Running6"), 
        col("E78"), 
        col("Z15_Running3"), 
        col("E84"), 
        col("E67_Running3"), 
        col("E74_Running6"), 
        col("S7_Running6"), 
        col("W9_Running6"), 
        col("Z31_Running3"), 
        col("O33_Running3"), 
        col("M41_Running3"), 
        col("Z37"), 
        col("O22"), 
        col("O09_Running3"), 
        col("E5_Running6"), 
        col("P2_Running6"), 
        col("I0_Running6"), 
        col("Z36_Running3"), 
        col("L1_Running6"), 
        col("Secondary_RxCosts_Running3"), 
        col("Medical___Diagnostic___Neurology_and_Neuromuscular_ProceduresRunning3"), 
        col("IP_Visits___Hospital_VisitsRunning3"), 
        col("Surgery___Female_Genital_SystemRunning3"), 
        col("H8_Running6"), 
        col("IP_Running3_Max"), 
        col("X8_Running6"), 
        col("E34_Running6"), 
        col("R5_Running6"), 
        col("E23_Running6"), 
        col("H3_Running6"), 
        col("I2_Running6"), 
        col("O21_Running3"), 
        col("A6_Running6"), 
        col("N0_Running6"), 
        col("Z17"), 
        col("Surgery___Integumentary_System___Destruction__Benign_or_Premalignant_LesionsRunning3"), 
        col("N4_Running6"), 
        col("E10_Running6"), 
        col("E30"), 
        col("R11"), 
        col("E31_Running3"), 
        col("E01_Running3"), 
        col("O26_Running3"), 
        col("E24_Running3"), 
        col("E55_Running6"), 
        col("O25_Running3"), 
        col("C8_Running6"), 
        col("E09_Running6"), 
        col("E25_Running3"), 
        col("E22_Running6"), 
        col("E65"), 
        col("X7_Running6"), 
        col("O31"), 
        col("T5_Running6"), 
        col("E66"), 
        col("E7_Running6"), 
        col("O01_Running3"), 
        col("O02"), 
        col("R14"), 
        col("M43"), 
        col("O36"), 
        col("Non_Prescription_DrugsRunning3"), 
        col("E26_Running6"), 
        col("B4_Running6"), 
        col("V6_Running6"), 
        col("Z30_Running3"), 
        col("E26_Running3"), 
        col("Z14"), 
        col("Secondary_Rx_Running3"), 
        col("P0_Running6"), 
        col("B5_Running6"), 
        col("E44_Running6"), 
        col("Z21_Running3"), 
        col("M19_Running3"), 
        col("E07_Running6"), 
        col("E31"), 
        col("E41_Running3"), 
        col("D4_Running6"), 
        col("Surgery___Cardiovascular_SystemRunning3"), 
        col("T4_Running6"), 
        col("Z02_Running3"), 
        col("R11_Running3"), 
        col("O08_Running3"), 
        col("E54"), 
        col("E08_Running6"), 
        col("S2_Running6"), 
        col("E45"), 
        col("E40_Running6"), 
        col("O9_Running6"), 
        col("M0_Running6"), 
        col("Z1_Running6"), 
        col("Z04_Running3"), 
        col("G2_Running6"), 
        col("MBR_INDV_BE_KEY"), 
        col("E06_Running6"), 
        col("O25"), 
        col("O23"), 
        col("Cardiovascular___Noninvasive_Physiologic_Studies_and_ProceduresRunning3"), 
        col("Medical___Diagnostic___ENTRunning3"), 
        col("Physical_TherapyRunning3"), 
        col("E32"), 
        col("Y2_Running6"), 
        col("J6_Running6"), 
        col("O07_Running3"), 
        col("X5_Running6"), 
        col("M16_Running3"), 
        col("E42_Running6"), 
        col("E64_Running6"), 
        col("G9_Running6"), 
        col("Q9_Running6"), 
        col("Maternity_OtherRunning3"), 
        col("E2_Running6"), 
        col("C2_Running6"), 
        col("F31"), 
        col("DMERunning3"), 
        col("Z00"), 
        col("V0_Running6"), 
        col("Z39"), 
        col("E77_Running6"), 
        col("X1_Running6"), 
        col("First_IP"), 
        col("V5_Running6"), 
        col("Miscellaneous_MedicalRunning3"), 
        col("M14_Running3"), 
        col("S8_Running6"), 
        col("Cardiovascular___Cardiac_Catheterization___Injection_ProceduresRunning3"), 
        col("E00"), 
        col("O4_Running6"), 
        col("E22"), 
        col("Surgery___Auditory_SystemRunning3"), 
        col("Z01_Running3"), 
        col("Z38_Running3"), 
        col("M16"), 
        col("E89_Running3"), 
        col("E59_Running6"), 
        col("E85_Running6"), 
        col("E83"), 
        col("K8_Running6"), 
        col("E01_Running6"), 
        col("Z3A_Running3"), 
        col("MEMBER_AGE2"), 
        col("H4_Running6"), 
        col("Surgery___Integumentary_SystemRunning3"), 
        col("TOT_MONTHS"), 
        col("P9_Running6"), 
        col("E51_Running3"), 
        col("K2_Running6"), 
        col("E04_Running3"), 
        col("E06_Running3"), 
        col("E23_Running3"), 
        col("E60_Running3"), 
        col("E80_Running3"), 
        col("Surgery___Eye_and_Ocular_AdnexaRunning3"), 
        col("E83_Running3"), 
        col("Z28"), 
        col("F7_Running6"), 
        col("E22_Running3"), 
        col("Z6_Running6"), 
        col("Q5_Running6"), 
        col("E45_Running6"), 
        col("W2_Running6"), 
        col("R2_Running6"), 
        col("M18"), 
        col("E75_Running6"), 
        col("Z02"), 
        col("M1A"), 
        col("R15_Running3"), 
        col("A2_Running6"), 
        col("J8_Running6"), 
        col("E02_Running3"), 
        col("F34_Running3"), 
        col("E42"), 
        col("E61_Running3"), 
        col("E72"), 
        col("Medical___Diagnostic___Central_Nervous_SystemRunning3"), 
        col("E11"), 
        col("M15_Running3"), 
        col("Z19"), 
        col("E67"), 
        col("E78_Running3"), 
        col("Urgent_Care_VisitsRunning3"), 
        col("E27_Running6"), 
        col("E13"), 
        col("E16"), 
        col("Z05"), 
        col("E43"), 
        col("W4_Running6"), 
        col("L2_Running6"), 
        col("E03_Running3"), 
        col("IP_Record"), 
        col("F8_Running6"), 
        col("F33"), 
        col("Z8_Running6"), 
        col("E87_Running6"), 
        col("E15_Running3"), 
        col("E36"), 
        col("M10_Running3"), 
        col("Vision_ExamsRunning3"), 
        col("E77_Running3"), 
        col("N6_Running6"), 
        col("A4_Running6"), 
        col("E45_Running3"), 
        col("Z9_Running6"), 
        col("D2_Running6"), 
        col("Q3_Running6"), 
        col("Maternity_DeliveriesRunning3"), 
        col("E58_Running3"), 
        col("O34"), 
        col("O04"), 
        col("M43_Running3"), 
        col("Z21"), 
        col("Surgery___Hemic_and_LymphaticRunning3"), 
        col("E23"), 
        col("R12_Running3"), 
        col("E70_Running3"), 
        col("E56"), 
        col("Z05_Running3"), 
        col("O00"), 
        col("M3_Running6"), 
        col("Z01"), 
        col("O29"), 
        col("Q2_Running6"), 
        col("M47_Running3"), 
        col("Z2_Running6"), 
        col("E29"), 
        col("Z29"), 
        col("F4_Running6"), 
        col("T6_Running6"), 
        col("C0_Running6"), 
        col("V7_Running6"), 
        col("Tertiary_RxCosts_Running3"), 
        col("R18_Running3"), 
        col("UniqueLabs_Running3"), 
        col("O01"), 
        col("Z37_Running3"), 
        col("Surgery___Integumentary_System___Destruction__Malignant_LesionsRunning3"), 
        col("M5_Running6"), 
        col("E64"), 
        col("Z14_Running3"), 
        col("M12_Running3"), 
        col("M45_Running3"), 
        col("E71_Running6"), 
        col("M18_Running3"), 
        col("W8_Running6"), 
        col("O29_Running3"), 
        col("G5_Running6"), 
        col("E87"), 
        col("O26"), 
        col("E75_Running3"), 
        col("E36_Running3"), 
        col("P7_Running6"), 
        col("A7_Running6"), 
        col("E67_Running6"), 
        col("X3_Running6"), 
        col("O28"), 
        col("Surgery___MusculoskeletalRunning3"), 
        col("O08"), 
        col("I8_Running6"), 
        col("R12"), 
        col("E13_Running6"), 
        col("E20_Running6"), 
        col("O31_Running3"), 
        col("E34_Running3"), 
        col("E24"), 
        col("Primary_Diagnosis_Running3"), 
        col("E80"), 
        col("Concat_ORDER_TST_NM_Running3"), 
        col("E25"), 
        col("E30_Running3"), 
        col("A0_Running6"), 
        col("G0_Running6"), 
        col("O30_Running3"), 
        col("R19_Running3"), 
        col("Z18"), 
        col("Surgery___Male_Genital_SystemRunning3"), 
        col("M46_Running3"), 
        col("E73"), 
        col("F3_Running6"), 
        col("Z0_Running6"), 
        col("S3_Running6"), 
        col("E63"), 
        col("E65_Running6"), 
        col("E31_Running6"), 
        col("E44"), 
        col("E21_Running3"), 
        col("CCI_Growth"), 
        col("Z13"), 
        col("Z34"), 
        col("Office_Home_Visits___Rest_HomeRunning3"), 
        col("N8_Running6"), 
        col("E35"), 
        col("P8_Running6"), 
        col("E09"), 
        col("E11_Running3"), 
        col("R6_Running6"), 
        col("H2_Running6"), 
        col("H0_Running6"), 
        col("J0_Running6"), 
        col("K5_Running6"), 
        col("E03_Running6"), 
        col("B1_Running6"), 
        col("Primary_DiagnosisCosts_Running3"), 
        col("C7_Running6"), 
        col("L8_Running6"), 
        col("O33"), 
        col("I6_Running6"), 
        col("E77"), 
        col("Medical___Diagnostic___VascularRunning3"), 
        col("E86_Running3"), 
        col("Radiology___Diagnostic___Diagnostic_ImagingRunning3"), 
        col("R4_Running6"), 
        col("A3_Running6"), 
        col("Z03_Running3"), 
        col("Office_Home_Visits___Telephonic_and_EmailRunning3"), 
        col("Z16_Running3"), 
        col("O1_Running6"), 
        col("Radiology___CT_MRI_PETRunning3"), 
        col("O34_Running3"), 
        col("F32_Running3"), 
        col("E65_Running3"), 
        col("P6_Running6"), 
        col("E28_Running3"), 
        col("E27_Running3"), 
        col("M7_Running6"), 
        col("E10_Running3"), 
        col("E50_Running3"), 
        col("E16_Running6"), 
        col("E21_Running6"), 
        col("E73_Running3"), 
        col("Z20"), 
        col("N1_Running6"), 
        col("O22_Running3"), 
        col("G6_Running6"), 
        col("J4_Running6"), 
        col("Q7_Running6"), 
        col("F31_Running3"), 
        col("V8_Running6"), 
        col("E36_Running6"), 
        col("E72_Running6"), 
        col("Z18_Running3"), 
        col("Radiology___Diagnostic___Other_ProceduresRunning3"), 
        col("Surgery___General___Needle_AspirationRunning3"), 
        col("E32_Running6"), 
        col("Q4_Running6"), 
        col("E63_Running6"), 
        col("E32_Running3"), 
        col("ConsultsRunning3"), 
        col("J9_Running6"), 
        col("E55"), 
        col("Z38"), 
        col("Z28_Running3"), 
        col("E59"), 
        col("B3_Running6"), 
        col("LowestGFR_Running3"), 
        col("IP_Running3"), 
        col("N9_Running6"), 
        col("E1_Running6"), 
        col("E51"), 
        col("C5_Running6"), 
        col("Q0_Running6"), 
        col("E76_Running6"), 
        col("O20"), 
        col("F34"), 
        col("E66_Running6"), 
        col("R18"), 
        col("F33_Running3"), 
        col("R0_Running6"), 
        col("Cardiovascular___DiagnosticRunning3"), 
        col("R17_Running3"), 
        col("E74"), 
        col("E78_Running6"), 
        col("E46_Running6"), 
        col("Z33_Running3"), 
        col("G8_Running6"), 
        col("O23_Running3"), 
        col("E29_Running3"), 
        col("E35_Running3"), 
        col("E42_Running3"), 
        col("IP_Month_Number"), 
        col("M11_Running3"), 
        col("E53"), 
        col("N7_Running6"), 
        col("E21"), 
        col("Z34_Running3"), 
        col("Secondary_Diagnosis_Running3"), 
        col("Z17_Running3"), 
        col("M42_Running3"), 
        col("E13_Running3"), 
        col("Z5_Running6"), 
        col("E83_Running6"), 
        col("M17_Running3"), 
        col("O21"), 
        col("M12"), 
        col("E55_Running3"), 
        col("E64_Running3"), 
        col("Z11_Running3"), 
        col("E00_Running3"), 
        col("Radiology___Diagnostic___Bone_Joint_StudiesRunning3"), 
        col("M13_Running3"), 
        col("Z20_Running3"), 
        col("E79_Running6"), 
        col("O36_Running3"), 
        col("O3_Running6"), 
        col("U0_Running6"), 
        col("Secondary_DiagnosisCosts_Running3"), 
        col("Z3_Running6"), 
        col("T1_Running6"), 
        col("Glasses_ContactsRunning3"), 
        col("E87_Running3"), 
        col("E26"), 
        col("F5_Running6"), 
        col("Z19_Running3"), 
        col("MEMBER_AGE").alias("Member_Age")
    )
