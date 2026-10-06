select
    order_id,
    customer_id,
    cast(order_date as date) as order_date,
    cast(amount as decimal(10, 2)) as amount,
    status,
    cast(updated_at as timestamp) as updated_at
from {{ source('raw', 'orders') }}