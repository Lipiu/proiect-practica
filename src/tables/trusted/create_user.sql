CREATE TABLE IF NOT EXISTS trusted.user(
    user_id VARCHAR(20) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    personal_number VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    city VARCHAR(50) NOT NULL,
    iban VARCHAR(25) NOT NULL,
    location VARCHAR(100) NOT NULL,
    age INT NOT NULL
)