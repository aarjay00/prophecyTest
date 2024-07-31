WITH content AS (

  SELECT * 
  
  FROM {{ source('dais_gen_ai.web_bronze', 'content') }}

)

SELECT *

FROM content
