INSERT INTO staging.dim_user (
    user_id, first_name, last_name, personal_number, birth_date, city, iban, location, age
)
SELECT DISTINCT
    user_id,
    first_name,
    last_name,
    personal_number,
    birth_date,
    city,
    iban,
    location,
    age
FROM raw.tales_tomes_data
WHERE user_id IS NOT NULL;
