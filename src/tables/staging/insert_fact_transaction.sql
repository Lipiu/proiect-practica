INSERT INTO staging.fact_transaction (
    transaction_id, user_id, book_id, amount, currency_code, time
)
SELECT
    t.transaction_id,
    t.user_id,
    b.book_id,
    t.amount,
    t.currency_code,
    t.time
FROM raw.tales_tomes_data t
JOIN raw.ratings r ON t.user_id = r.user_id
JOIN staging.dim_books b ON r.isbn = b.isbn;
