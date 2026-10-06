select
    customer_id,
    count(*) as row_count
from {{ ref('customer_summary') }}
group by customer_id
having count(*) > 1