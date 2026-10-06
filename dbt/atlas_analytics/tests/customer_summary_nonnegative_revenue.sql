select *
from {{ ref('customer_summary') }}
where completed_revenue < 0