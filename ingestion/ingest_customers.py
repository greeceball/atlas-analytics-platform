from pathlib import Path
import pandas as pd

SOURCE_PATH = Path("data/source/customers.csv")
RAW_PATH = Path("data/raw/customers.parquet")

def ingest_customers() -> None:
    df = pd.read_csv(SOURCE_PATH)

    print(f"Rows read: {len(df)}")
    print(f"Columns read: {list(df.columns)}")

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(RAW_PATH, index=False)

    print(f"Wrote raw customer data to: {RAW_PATH}")

if __name__ == "__main__":
    ingest_customers()
