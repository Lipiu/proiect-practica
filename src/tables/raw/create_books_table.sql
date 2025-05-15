CREATE TABLE IF NOT EXISTS raw.books(
    title VARCHAR(300),
    isbn VARCHAR(20) UNIQUE,
    author VARCHAR(300),
    year_of_publication TEXT,
    publisher VARCHAR(300)
)