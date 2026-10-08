with monthly_orders as (

    select
        customer_id,
        date_trunc('month', order_date) as order_month,
        count(*) as order_count,
        sum(amount) as total_order_amount

    from {{ ref('stg_orders') }}

    group by
        customer_id,
        date_trunc('month', order_date)

)

select
    {{ dbt_utils.generate_surrogate_key([
        'customer_id',
        'order_month'
    ]) }} as customer_month_key,

    customer_id,
    order_month,
    order_count,
    total_order_amount

from monthly_orders