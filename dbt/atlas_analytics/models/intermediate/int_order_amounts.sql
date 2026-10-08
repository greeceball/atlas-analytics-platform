select
    order_id,
    amount,
    {{ zero_if_null('amount') }} as amount_no_null
from {{ ref('stg_orders') }}