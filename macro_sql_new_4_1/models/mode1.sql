WITH all_type_non_partitioned AS (

  SELECT * 
  
  FROM {{ source('qa-team.qa_database', 'all_type_non_partitioned') }}

),

deduplicate1_1 AS (

  {{ macros_sql.deduplicate2('all_type_non_partitioned', 'c_int', c_int) }}

)

SELECT *

FROM deduplicate1_1
