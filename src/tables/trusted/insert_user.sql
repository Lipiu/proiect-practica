INSERT INTO trusted.user(
    user_id,
    book_title,
    author,
    first_name,
    last_name,
    personal_number,
    birth_date,
    city,
    iban,
    location,
    age
)
SELECT
    u.user_id,
    b.title AS book_title,
    b.author,
    u.first_name,
    u.last_name,
    u.personal_number,
    u.birth_date,
    u.city,
    u.iban,
    u.location,
    u.age
FROM
    staging.dim_user u
LEFT JOIN
    staging.fact_transaction t ON u.user_id = t.user_id
LEFT JOIN
    staging.dim_books b ON t.book_id = b.book_id