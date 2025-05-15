CREATE TABLE IF NOT EXISTS staging.dim_books (
    book_id SERIAL PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE,
    title VARCHAR(300),
    author VARCHAR(300),
    year_of_publication TEXT,
    publisher VARCHAR(300)
);
