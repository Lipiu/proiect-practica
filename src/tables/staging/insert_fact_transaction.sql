INSERT INTO staging.fact_transaction (
    transaction_id, user_id, book_id, amount, currency_code, time
)
SELECT
    t.transaction_id,
    t.user_id,
    (SELECT book_id FROM staging.dim_books ORDER BY RANDOM() LIMIT 1),
    t.amount,
    t.currency_code,
    t.time
FROM raw.tales_tomes_data t
JOIN staging.dim_user u ON t.user_id = u.user_id;
