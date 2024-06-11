from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Join_2692_left_UnionFullOuter(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(
          in1.alias("in1"),
          ((col("in0.MBR_INDV_BE_KEY") == col("in1.MBR_INDV_BE_KEY")) & (col("in0.YEARMONTH") == col("in1.YEARMONTH"))),
          "fullouter"
        )\
        .select(col("in0.IP_Visits___Hospital_Visits").alias("IP_Visits___Hospital_Visits"), col("in0.YEARMONTH").alias("YEARMONTH"), col("in0.DME").alias("DME"), col("in0.Vision_Exams").alias("Vision_Exams"), col("in0.IP_Visits___Newborn_Care").alias("IP_Visits___Newborn_Care"), col("in0.MBR_INDV_BE_KEY").alias("MBR_INDV_BE_KEY"), col("in0.Surgery___Male_Genital_System").alias("Surgery___Male_Genital_System"), col("in0.Surgery___Integumentary_System___Excision_of_Malignant_Lesions")\
        .alias("Surgery___Integumentary_System___Excision_of_Malignant_Lesions"), col("in0.Consults").alias("Consults"), col("in0.Glasses_Contacts").alias("Glasses_Contacts"), col("in0.Medical___Diagnostic___Biofeedback").alias("Medical___Diagnostic___Biofeedback"), col("in0.Radiology___Diagnostic___Other_Procedures").alias("Radiology___Diagnostic___Other_Procedures"), col("in0.Medical___Diagnostic___Central_Nervous_System")\
        .alias("Medical___Diagnostic___Central_Nervous_System"), col("in0.Office_Home_Visits___Prolonged_Services").alias("Office_Home_Visits___Prolonged_Services"), col("in0.Surgery___Integumentary_System___Destruction__Benign_or_Premalignant_Lesions")\
        .alias("Surgery___Integumentary_System___Destruction__Benign_or_Premalignant_Lesions"), col("in0.Psychiatric_Alcohol_Drug_Abuse").alias("Psychiatric_Alcohol_Drug_Abuse"), col("in0.Anesthesia").alias("Anesthesia"), col("in0.Office_Home_Visits___Telephonic_and_Email").alias("Office_Home_Visits___Telephonic_and_Email"), col("in0.Cardiovascular___Noninvasive_Physiologic_Studies_and_Procedures")\
        .alias("Cardiovascular___Noninvasive_Physiologic_Studies_and_Procedures"), col("in0.PDN_HH").alias("PDN_HH"), col("in0.Radiology___Therapeutic").alias("Radiology___Therapeutic"), col("in0.Pathology_and_Lab").alias("Pathology_and_Lab"), col("in0.Surgery___Urinary_System").alias("Surgery___Urinary_System"), col("in0.Cardiovascular___Diagnostic").alias("Cardiovascular___Diagnostic"), col("in0.Cardiovascular___Cardiac_Catheterization___Injection_Procedures")\
        .alias("Cardiovascular___Cardiac_Catheterization___Injection_Procedures"), col("in0.ER_Visits_and_Observation_Care").alias("ER_Visits_and_Observation_Care"), col("in0.Surgery___Endocrine_System").alias("Surgery___Endocrine_System"), col("in0.Surgery___Integumentary_System").alias("Surgery___Integumentary_System"), col("in0.Hearing_Speech_Exams").alias("Hearing_Speech_Exams"), col("in0.Maternity_Other").alias("Maternity_Other"), col("in0.Allergy_Immunotherapy").alias("Allergy_Immunotherapy"), col("in0.Radiology___CT_MRI_PET").alias("Radiology___CT_MRI_PET"), col("in0.IP_Visits___Neonatal_Visits").alias("IP_Visits___Neonatal_Visits"), col("in0.Medical___Diagnostic___Vascular").alias("Medical___Diagnostic___Vascular"), col("in0.Allergy_Testing").alias("Allergy_Testing"), col("in0.IP_Visits___Critical_Care_Services").alias("IP_Visits___Critical_Care_Services"), col("in0.Non_Standard_Benefit").alias("Non_Standard_Benefit"), col("in0.Surgery___Musculoskeletal").alias("Surgery___Musculoskeletal"), col("in0.IP_Visits___Nursing_Facility_Services").alias("IP_Visits___Nursing_Facility_Services"), col("in0.Surgery___General___Needle_Aspiration").alias("Surgery___General___Needle_Aspiration"), col("in0.Immunizations").alias("Immunizations"), col("in0.Well_Baby_Exams").alias("Well_Baby_Exams"), col("in0.Cardiovascular___Other_Procedures").alias("Cardiovascular___Other_Procedures"), col("in0.Urgent_Care_Visits").alias("Urgent_Care_Visits"), col("in0.Surgery___Cardiovascular_System").alias("Surgery___Cardiovascular_System"), col("in0.Surgery___Female_Genital_System").alias("Surgery___Female_Genital_System"), col("in0.Radiology___Diagnostic___Diagnostic_Imaging").alias("Radiology___Diagnostic___Diagnostic_Imaging"), col("in0.Surgery___Integumentary_System___Destruction__Malignant_Lesions")\
        .alias("Surgery___Integumentary_System___Destruction__Malignant_Lesions"), col("in0.Radiology___Nuclear").alias("Radiology___Nuclear"), col("in0.Non_Prescription_Drugs").alias("Non_Prescription_Drugs"), col("in0.Surgery___Auditory_System").alias("Surgery___Auditory_System"), col("in0.Maternity_Deliveries").alias("Maternity_Deliveries"), col("in0.Physical_Exams").alias("Physical_Exams"), col("in0.Miscellaneous_Medical").alias("Miscellaneous_Medical"), col("in0.Surgery___Respiratory_System").alias("Surgery___Respiratory_System"), col("in0.Radiology___Diagnostic___Bone_Joint_Studies").alias("Radiology___Diagnostic___Bone_Joint_Studies"), col("in0.Chiropractor___Chiropractic_Manipulative_Treatment")\
        .alias("Chiropractor___Chiropractic_Manipulative_Treatment"), col("in0.Medical___Diagnostic___ENT").alias("Medical___Diagnostic___ENT"), col("in0.Office_Home_Visits___Office_Visits").alias("Office_Home_Visits___Office_Visits"), col("in0.Medical___Diagnostic___Gastroenterology").alias("Medical___Diagnostic___Gastroenterology"), col("in0.Office_Home_Visits___Care_Plan_Oversight_Services")\
        .alias("Office_Home_Visits___Care_Plan_Oversight_Services"), col("in0.Medical___Diagnostic___Neurology_and_Neuromuscular_Procedures")\
        .alias("Medical___Diagnostic___Neurology_and_Neuromuscular_Procedures"), col("in0.Surgery___Nervous_System").alias("Surgery___Nervous_System"), col("in0.Physical_Therapy").alias("Physical_Therapy"), col("in0.Surgery___Digestive_System").alias("Surgery___Digestive_System"), col("in0.Office_Home_Visits___Rest_Home").alias("Office_Home_Visits___Rest_Home"), col("in0.Surgery___Eye_and_Ocular_Adnexa").alias("Surgery___Eye_and_Ocular_Adnexa"), col("in0.Surgery___Hemic_and_Lymphatic").alias("Surgery___Hemic_and_Lymphatic"))
