INSERT INTO staging.dim_user (
    user_id, first_name, last_name, personal_number, birth_date, city, iban, location, age
)
SELECT DISTINCT ON (user_id)
    t.user_id,
    t.first_name,
    t.last_name,
    t.personal_number,
    t.birth_date,
    t.city,
    t.iban,
    u.location,
    u.age
FROM raw.tales_tomes_data t
LEFT JOIN raw.users u ON t.user_id = u.user_id::TEXT
ORDER BY user_id, time DESC;
