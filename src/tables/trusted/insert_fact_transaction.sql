INSERT INTO trusted.fact_transaction (
    transaction_id, user_id, book_id, amount, currency_code, time
)
SELECT
    transaction_id,
    user_id,
    book_id,
    amount,
    currency_code,
    time
FROM staging.fact_transaction;
