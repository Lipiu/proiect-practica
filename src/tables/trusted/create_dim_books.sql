CREATE TABLE IF NOT EXISTS trusted.dim_books (
    book_id INT PRIMARY KEY,
    isbn VARCHAR(20),
    title VARCHAR(300),
    author VARCHAR(300),
    year_of_publication INT,
    publisher VARCHAR(300)
);