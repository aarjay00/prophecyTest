WITH seed2 AS (

  SELECT * 
  
  FROM {{ ref('seed2')}}

)

SELECT *

FROM seed2
