import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

def get_top_readers():
    load_dotenv() 
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'TalesAndTomes'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', '2805'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )
    query = f"""
        SELECT 
            u.first_name || ' ' || u.last_name AS full_name, 
            COUNT(DISTINCT ft.book_id) AS books_read
        FROM trusted.fact_transaction ft
        JOIN trusted.dim_user u ON ft.user_id = u.user_id
        GROUP BY full_name
        ORDER BY books_read DESC
        LIMIT 100;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def plot_top_readers(df):
    plt.figure(figsize=(25,10))
    plt.bar(df['full_name'], df['books_read'], color='skyblue')
    plt.title('Top Readers by Number of Books Read')
    plt.xlabel('User Name')
    plt.ylabel('Books Read')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    top_readers_df = get_top_readers()
    plot_top_readers(top_readers_df)
