INSERT INTO trusted.dim_books (
    book_id, isbn, title, author, year_of_publication, publisher
)
SELECT
    book_id,
    isbn,
    title,
    author,
    NULLIF(year_of_publication, '')::INT,
    publisher
FROM staging.dim_books;
