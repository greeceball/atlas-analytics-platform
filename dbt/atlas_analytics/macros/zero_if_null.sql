{% macro zero_if_null(column_name) %}

    coalesce({{ column_name }}, 0)

{% endmacro %}