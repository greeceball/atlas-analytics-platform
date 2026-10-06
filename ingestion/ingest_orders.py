from pathlib import Path
import pandas as pd

SOURCE_PATH = Path("data/source/orders.csv")
RAW_PATH = Path("data/raw/orders.parquet")

def ingest_orders() -> None:
    df = pd.read_csv(SOURCE_PATH)

    print(f"Rows read: {len(df)}")
    print(f"Columns read: {list(df.columns)}")

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(RAW_PATH, index=False)

    print(f"Wrote raw order data to: {RAW_PATH}")

if __name__ == "__main__":
    ingest_orders()