select
    customer_id,
    name as customer_name,
    email,
    state,
    cast(created_at as date) as created_at
from {{ source('raw', 'customers') }}