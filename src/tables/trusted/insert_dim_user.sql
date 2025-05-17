INSERT INTO trusted.dim_user (
    user_id, first_name, last_name, personal_number, birth_date, city, iban, location, age
)
SELECT
    user_id,
    first_name,
    last_name,
    personal_number,
    birth_date,
    city,
    iban,
    location,
    age
FROM staging.dim_user;
