from pathlib import Path
import duckdb

DATABASE_PATH = Path("data/warehouse/atlas.duckdb")
RAW_CUSTOMERS_PATH = Path("data/raw/customers.parquet")
RAW_ORDERS_PATH = Path("data/raw/orders.parquet")

def load_warehouse() -> None:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(DATABASE_PATH))

    conn.execute("CREATE SCHEMA IF NOT EXISTS raw")

    conn.execute(
        """
        CREATE OR REPLACE TABLE raw.customers AS
        SELECT *
        FROM read_parquet(?)
        """,
        [str(RAW_CUSTOMERS_PATH)],
    )

    customer_row_count = conn.execute(
        "SELECT COUNT(*) FROM raw.customers"
    ).fetchone()[0]

    print(f"Loaded {customer_row_count} customers into raw.customers")

    conn.execute(
        """
        CREATE OR REPLACE TABLE raw.orders AS
        SELECT *
        FROM read_parquet(?)
        """,
        [str(RAW_ORDERS_PATH)],
    )

    order_row_count = conn.execute(
        "SELECT COUNT(*) FROM raw.orders"
    ).fetchone()[0]

    print(f"Loaded {order_row_count} orders into raw.orders")

    conn.close()

if __name__ == "__main__":
    load_warehouse()