import psycopg2
import os


def read_sql(file_path: str) -> str:
    """
    Read a SQL file and return its content.
    """
    with open(file_path, "r") as file:
        return file.read()


def execute_query(sql: str, connection) -> None:
    """
    Execute a single SQL statement using a given connection.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
        print("✅ Successfully executed SQL script.")
    except Exception as e:
        connection.rollback()
        print(f"❌ Error executing SQL: {e}")
    finally:
        cursor.close()


def load_queries(query_paths: list):
    """
    Run a list of SQL files against the database.
    """
    conn = psycopg2.connect(
        dbname="TalesAndTomes",
        user="postgres",
        password="2805",
        host="localhost",
        port=5432
    )

    for path in query_paths:
        print(f"Executing: {path}")
        sql = read_sql(path)
        execute_query(sql, conn)

    conn.close()
    print("🎉 All queries executed.")


if __name__ == "__main__":
    query_paths = [
        "src/tables/trusted/insert_user.sql",
        "src/tables/trusted/insert_books.sql",
        "src/tables/trusted/insert_transaction.sql"
    ]
    load_queries(query_paths)
