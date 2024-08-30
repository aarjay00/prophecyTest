{% macro deduplicate3(relation, partition_by, order_by) %}

    select
        distinct * from {{ relation}}
{% endmacro %}

 