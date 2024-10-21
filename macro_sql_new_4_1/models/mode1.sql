WITH all_type_non_partitioned AS (

  SELECT * 
  
  FROM {{ source('qa-team.qa_database', 'all_type_non_partitioned') }}

),

deduplicate1_1 AS (

  {{
    macros_sql.deduplicate2(
      relation = 'all_type_non_partitioned', 
      partition_by = c_int, 
      order_by = c_float
    )
  }}

)

SELECT *

FROM deduplicate1_1
