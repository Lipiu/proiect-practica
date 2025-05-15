CREATE TABLE IF NOT EXISTS staging.dim_user(
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    user_id VARCHAR(20) PRIMARY KEY,
    personal_number VARCHAR(20),
    birth_date DATE,
    city VARCHAR(50),
    iban VARCHAR(25)
);