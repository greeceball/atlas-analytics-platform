from pathlib import Path
import duckdb

DATABASE_PATH = Path("data/warehouse/atlas.duckdb")
RAW_CUSTOMERS_PATH = Path("data/raw/customers.parquet")

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

    row_count = conn.execute("SELECT COUNT(*) FROM raw.customers").fetchone()[0]
    print(f"Loaded {row_count} customers into raw.customers")

    conn.close()

if __name__ == "__main__":
    load_warehouse()