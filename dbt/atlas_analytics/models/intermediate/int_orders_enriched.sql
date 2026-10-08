select
    o.order_id,
    o.customer_id,
    o.order_date,
    o.amount,
    o.status,
    m.status_group,
    o.updated_at
from {{ ref('stg_orders') }} o
left join {{ ref('order_status_mapping') }} m
    on o.status = m.status