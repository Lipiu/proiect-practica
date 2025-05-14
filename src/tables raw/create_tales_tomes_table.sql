CREATE TABLE IF NOT EXISTS raw.tales_tomes_data(
    transaction_id VARCHAR(50),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    user_id VARCHAR(20),
    personal_number VARCHAR(20),
    birth_date DATE,
    city VARCHAR(50),
    iban VARCHAR(25),
    amount INT,
    currency_code VARCHAR(3),
    time TIMESTAMP
)