{{
  config({    
    "materialized": "incremental",
    "incremental_predicates": ["content < 10"],
    "incremental_strategy": "merge",
    "on_schema_change": 'ignore'
  })
}}

WITH content AS (

  SELECT * 
  
  FROM {{ source('dais_gen_ai.web_bronze', 'content') }}

)

SELECT *

FROM content
