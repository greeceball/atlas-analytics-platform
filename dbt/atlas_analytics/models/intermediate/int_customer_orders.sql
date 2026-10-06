select
    c.customer_id,
    c.customer_name,
    c.email,
    c.state,
    o.order_id,
    o.order_date,
    o.amount,
    o.status
from {{ ref('stg_customers') }} c
left join {{ ref('stg_orders') }} o
    on c.customer_id = o.customer_id