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

## **Raw Layer Tables**

tales_tomes_data

| Column Name     | Data Type    | Description                           |
| --------------- | ------------ | ------------------------------------- |
| transaction_id  | VARCHAR(50)  | Unique identifier of the transaction  |
| first_name      | VARCHAR(255) | Customer first name                   |
| last_name       | VARCHAR(255) | Customer last name                    |
| user_id         | VARCHAR(20)  | Platform user identifier name         |
| personal_number | INT          | Personal numerical identifier         |
| birth_date      | DATE         | Birth date                            |
| city            | VARCHAR(50)  | User's city                           |
| iban            | VARCHAR(25)  | Bank account number                   |
| amount          | INT          | Amount of money of the transaction    |
| currency_code   | VARCHAR(3)   | Currency code used in the transaction |
| time            | TIMESTAMP    | Transaction time                      |

##

books

| Column Name         | Data Type    | Description                              |
| ------------------- | ------------ | ---------------------------------------- |
| title               | VARCHAR(300) | Unique title of the book                 |
| author              | VARCHAR(300) | Name of the book author                  |
| year_of_publication | TEXT         | The year in which the book was published |
| publisher           | VARCHAR(300) | The publisher of the book                |

##

ratings
|Column Name | Data Type | Description |
| ----- | ----- | ----- |
| user_id| TEXT | The unique id of the user |
| isbn | TEXT | Numeric commercial book identifier |
| rating | INT | The rating of the book |

users
|Column Name | Data Type | Description |
| ----- | ----- | ----- |
| user_id | INT | The ID of the user |
| location | VARCHAR(100) | The location of the user |
| age | INT | The age of the user |

##

## Staging layer

## ** Staging layer Tables**

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
| user_id | VARCHAR(20) | raw/tales_tomes_data/last_name |
| first_name | VARCHAR (255) | raw/tales_tomes_data/first_name |
| last_name | VARCHAR(255) | raw/tales_tomes_data/last_name |
| personal_number | VARCHAR(20) | raw/tales_tomes_data/last_name |
| birth_date | DATE | raw/tales_tomes_data/last_name |
| city | VARCHAR(50) | raw/tales_tomes_data/last_name |
| iban | VARCHAR(25) | raw/tales_tomes_data/last_name |
| location | VARCHAR(100) | raw/users/location |
| age | INT | raw/users/age |

##

`dim_book`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| book_id | SERIAL PRIMARY KEY | raw/books/book_id |
| isbn | VARCHAR(20) UNIQUE | raw/books/isbn |
| title | VARCHAR(300) | raw/books/title|
| author | VARCHAR(300) | raw/books/author |
| year_of_publication | TEXT | raw/books/year_of_publication |
| publisher | VARCHAR(300) | raw/books/publisher |
| currency_code | VARCHAR(3) | raw/tales_tomes_data/currency_code |
