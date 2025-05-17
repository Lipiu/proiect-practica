import psycopg2
import random
from dotenv import load_dotenv
import os

def get_all_user_ids(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT user_id FROM trusted.dim_user;")
        return [row[0] for row in cur.fetchall()]

def get_all_book_ids(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT book_id FROM trusted.dim_books;")
        return [row[0] for row in cur.fetchall()]

def insert_random_transactions(conn, user_ids, book_ids, max_books_per_user=5):
    with conn.cursor() as cur:
        transaction_id_prefix = "tx"
        tx_counter = 1

        for user_id in user_ids:
            books_to_read = random.randint(1, max_books_per_user)
            books_sample = random.sample(book_ids, k=min(books_to_read, len(book_ids)))

            for book_id in books_sample:
                transaction_id = f"{transaction_id_prefix}_{user_id}_{tx_counter}"
                tx_counter += 1
                amount = 1  # or random if you want different amounts
                currency_code = 'USD'  # or your currency
                time = 'NOW()'  # current timestamp

                cur.execute("""
                    INSERT INTO trusted.fact_transaction
                    (transaction_id, user_id, book_id, amount, currency_code, time)
                    VALUES (%s, %s, %s, %s, %s, NOW())
                    ON CONFLICT (transaction_id) DO NOTHING;
                """, (transaction_id, user_id, book_id, amount, currency_code))
        conn.commit()

if __name__ == "__main__":
    load_dotenv()
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'TalesAndTomes'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', '2805'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )

    users = get_all_user_ids(conn)
    books = get_all_book_ids(conn)

    insert_random_transactions(conn, users, books, max_books_per_user=5)

    conn.close()
    print("Randomized transactions inserted successfully!")
