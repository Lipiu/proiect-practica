CREATE TABLE IF NOT EXISTS staging.book(
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(300),
    author VARCHAR(300),
    year_of_publication TEXT,
    publisher VARCHAR(300),
    currency_code VARCHAR(3)
);