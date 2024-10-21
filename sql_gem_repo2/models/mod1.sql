WITH see34 AS (

  SELECT * 
  
  FROM {{ ref('see34')}}

),

sql_gem_query AS (

  {#Retrieves specific data or insights from a predefined query for further analysis.#}
  {{ sql_gem_repo2.g1('see34') }}

)

SELECT *

FROM see34
