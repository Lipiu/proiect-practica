CREATE TABLE IF NOT EXISTS trusted.fact_transaction (
    transaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(20),
    book_id INT,
    amount INT,
    currency_code VARCHAR(3),
    time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES trusted.dim_user(user_id),
    FOREIGN KEY (book_id) REFERENCES trusted.dim_books(book_id)
);