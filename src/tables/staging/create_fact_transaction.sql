CREATE TABLE IF NOT EXISTS staging.fact_transaction(
    transaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(20) REFERENCES staging.dim_user(user_id),
    currency_code VARCHAR(3) REFERENCES staging.book(currency_code)
);