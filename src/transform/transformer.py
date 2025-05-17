import psycopg2
from pathlib import Path
import os

def read_sql(file_path: Path) -> str:
    with file_path.open("r", encoding="utf-8") as f:
        return f.read()

def execute_query(sql: str, conn) -> None:
    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()

def run_transformations(sql_files: list[Path], db_config: dict):
    with psycopg2.connect(**db_config) as conn:
        for sql_file in sql_files:
            print(f"Running SQL from: {sql_file}")
            sql = read_sql(sql_file)
            execute_query(sql, conn)
        print("All transformations completed successfully.")

if __name__ == "__main__":
    base_path = Path(__file__).parent.parent / "tables" / "staging"
    sql_paths = [
        base_path / "insert_dim_books.sql",
        base_path / "insert_dim_user.sql",
        base_path / "insert_fact_transaction.sql"
    ]

    missing_files = [str(p) for p in sql_paths if not p.exists()]
    if missing_files:
        print("ERROR: These SQL files were not found:")
        for mf in missing_files:
            print(" -", mf)
        exit(1)

    db_config = {
        "dbname": "TalesAndTomes",
        "user": "postgres",
        "password": "2805",
        "host": "localhost",
        "port": 5432
    }

    run_transformations(sql_paths, db_config)
