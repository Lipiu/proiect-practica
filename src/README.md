# Arhitecture of Data Warehousing and Normalization

## Arhitecture of Data Warehousing
in `talesTomes.db` database will be created 3 layers.\
- **raw** --> source data
- **staging** --> transformed data
- **trusted** --> consumption data

##
## Raw layer

#### Create layer
To create `raw` layer use the SQL query from `src/schemas/raw.sql` file.

#### Create tables

**tales_tomes_data**\
To create `tales_tomes_data` table use the code from `src/tables/raw/create_tales_tomes_data.sql` file.

**books_data**\
To create `books_data` table use the code from `src/tables/raw/create_books.sql` file.

**ratings_data**\
To create `ratings_data` table use the code from `src/tables/raw/create_ratings.sql` file.

**users_data**\
To create `users_data` table use the code from `src/tables/raw/create_users.sql` file.
##

#### Insert data
**tales_tomes_data**\
To insert data into `tales_tomes_data` table use the code from `src/tables/raw/insert_tales_tomes_table.sql` file.

**books_data**\
To insert data into `books_data` table use the code from `src/ tables/raw/insert_books.sql` file.

**ratings_data**\
To insert data into `ratings_data` table use the code from `src/tables/raw/insert_ratings.sql` file.

**users_data**\
To insert data into `users_data` table use the code from `src/tables/raw/insert_users.sql` file.
##
#### Select data
**tales_tomes_data**\
To select data from `tales_tomes_data` table use the code from `src/tables/raw/select_tales_tomes_table.sql` file.

**books_data**\
To select data from `books_data` table use the code from `src/ tables/raw/select_books.sql` file.

**ratings_data**\
To select data from `ratings_data` table use the code from `src/tables/raw/select_ratings.sql` file.

**users_data**\
To select data from `users_data` table use the code from `src/tables/raw/select_users.sql` file.

##
## Staging layer

`fact_transaction`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| transaction_id | VARCHAR(50) PRIMARY KEY | raw/tales_tomes_data/transaction_id |
| user_id | VARCHAR(20) FOREIGN KEY | raw/user_id |
| currency_code | VARCHAR(3) | raw/tales_tomes_data/currency_code |

##
`dim_user`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| first_name | VARCHAR (255) | src/tales_tomes_data/first_name |
| last_name | VARCHAR(255) | src/tales_tomes_data/last_name |
| user_id | VARCHAR(20) | src/tales_tomes_data/last_name |
| personal_number | VARCHAR(20) | src/tales_tomes_data/last_name |
| birth_date | DATE | src/tales_tomes_data/last_name |
| city | VARCHAR(50) | src/tales_tomes_data/last_name |
| iban | VARCHAR(25) | src/tales_tomes_data/last_name |

##
`dim_book`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| title | VARCHAR(300) | src/books/title|
| author | VARCHAR(300) | src/books/author |
| year_of_publication | TEXT | src/books/year_of_publication |
| publisher | VARCHAR(300) | src/books/publisher |
| currency_code | VARCHAR(3) | src/tales_tomes_data/currency_code |
