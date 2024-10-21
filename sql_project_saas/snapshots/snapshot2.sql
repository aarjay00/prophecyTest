{% snapshot snapshot2 %}
{{
  config({    
    "strategy": 'timestamp',
    "target_schema": "schema_non_default",
    "unique_key": "content",
    "updated_at": "content"
  })
}}

WITH content AS (

  SELECT *
  
  FROM {{ source('dais_gen_ai.web_bronze', 'content') }}

)

SELECT *

FROM content

{% endsnapshot %}
