{% macro deduplicate2(relation, partition_by, order_by) %}

    select
        distinct * from {{ relation}}
{% endmacro %}

 {% macro deduplicate1(relation, partition_by, order_by) %}

    select
        distinct * from {{relation}}
{% endmacro %}

 