INSERT INTO staging.dim_books (isbn, title, author, year_of_publication, publisher)
SELECT DISTINCT isbn, title, author, year_of_publication, publisher
FROM raw.books;
