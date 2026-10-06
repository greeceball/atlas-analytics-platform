select
    customer_id,
    customer_name,
    state,
    count(order_id) as order_count,
    sum(
        case 
            when status = 'completed' then amount 
            else 0 
        end
    ) as completed_revenue,
    max(order_date) as latest_order_date
from {{ ref('int_customer_orders') }}
group by
    customer_id,
    customer_name,
    state