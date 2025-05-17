import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

class TrustedDataLoader:

    def __init__(self):
        load_dotenv()
        self.db_config = {
            'dbname': os.getenv('DB_NAME', 'TalesAndTomes'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', '2805'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', 5432))
        }
        self.conn = None
        self.base_path = Path(__file__).resolve().parent.parent / "tables" / "trusted"

    def connect_db(self):
        """Establish connection to database."""
        self.conn = psycopg2.connect(**self.db_config)

    def close_db(self):
        """Close database connection if it exists."""
        if self.conn:
            self.conn.close()

    def load_sql(self, file_path):
        """Load SQL query from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def execute_sql(self, sql_file):
        """Execute SQL statement from a file."""
        sql = self.load_sql(sql_file)
        with self.conn.cursor() as crs:
            crs.execute(sql)
            print(f"Executed SQL from {sql_file.name}")

    def create_trusted_tables(self):
        """Create all trusted tables."""
        try:
            print("Ensuring trusted tables exist...")
            self.execute_sql(self.base_path / 'create_dim_books.sql')
            self.execute_sql(self.base_path / 'create_dim_user.sql')
            self.execute_sql(self.base_path / 'create_fact_transaction.sql')
            self.conn.commit()
            print("Trusted table creation completed successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error during trusted table creation: {e}")
            raise

    def insert_trusted_data(self):
        """Insert data into trusted tables."""
        try:
            print("Loading data into trusted tables...")
            self.execute_sql(self.base_path / 'insert_dim_user.sql')
            self.execute_sql(self.base_path / 'insert_dim_books.sql')
            self.execute_sql(self.base_path / 'insert_fact_transaction.sql')
            self.conn.commit()
            print("Trusted data loading completed successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error during trusted data loading: {e}")
            raise

    def run_trusted_load(self):
        """Run the full trusted layer load process."""
        try:
            self.connect_db()
            self.create_trusted_tables()
            self.insert_trusted_data()
        finally:
            self.close_db()

if __name__ == "__main__":
    loader = TrustedDataLoader()
    loader.run_trusted_load()
