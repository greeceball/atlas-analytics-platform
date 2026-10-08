{% snapshot orders_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='order_id',
        strategy='timestamp',
        updated_at='updated_at'
    )
}}

select
    order_id,
    customer_id,
    order_date,
    amount,
    status,
    cast(updated_at as timestamp) as updated_at
from {{ source('raw', 'orders') }}

{% endsnapshot %}