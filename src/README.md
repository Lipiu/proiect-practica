# Arhitecture of Data Warehousing and Normalization

## Arhitecture of Data Warehousing

in `talesTomes.db` database will be created 3 layers.\

- **raw** --> source data
- **staging** --> transformed data
- **trusted** --> consumption data

##

## Raw layer

The `raw layer` is where the data lands first, exactly as it comes from the original source (this case .csv file).

#### Create `raw` layer

To create `raw` layer use the SQL query from `src/schemas/raw.sql` file.

#### Create tables

- **tales_tomes_data** --> to create `tales_tomes_data` table use the code from `src/tables/raw/create_tales_tomes_data.sql` file.

- **books_data** --> to create `books_data` table use the code from `src/tables/raw/create_books.sql` file.

- **ratings_data**\ --> to create `ratings_data` table use the code from `src/tables/raw/create_ratings.sql` file.

##

#### Insert data

**tales_tomes_data**\
To insert data into `tales_tomes_data` table use the code from `src/tables/raw/insert_tales_tomes_table.sql` file.

**books_data**\
To insert data into `books_data` table use the code from `src/ tables/raw/insert_books.sql` file.

**ratings_data**\
To insert data into `ratings_data` table use the code from `src/tables/raw/insert_ratings.sql` file.

##

#### Select data

**tales_tomes_data**\
To select data from `tales_tomes_data` table use the code from `src/tables/raw/select_tales_tomes_table.sql` file.

**books_data**\
To select data from `books_data` table use the code from `src/ tables/raw/select_books.sql` file.

**ratings_data**\
To select data from `ratings_data` table use the code from `src/tables/raw/select_ratings.sql` file.

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

| Column Name | Data Type | Description                        |
| ----------- | --------- | ---------------------------------- |
| user_id     | TEXT      | The unique id of the user          |
| isbn        | TEXT      | Numeric commercial book identifier |
| rating      | INT       | The rating of the book             |

##

## Staging layer

The `staging layer` prepares data from the `raw layer` for more serious processing. It's an intermediate zone where initial
cleaning, formatting and transformations happen.

**Create `staging` layer**\
To create `staging` layer use the SQL query from `src/schemas/staging.sql`.

**Create tables**

- **dim_book** --> to create `dim_book` (book data) table use the code from `src/tables/staging/create_dim_book.sql`
- **dim_user** --> to create `dim_user` (user data) table use the code from `src/tables/staging/create_dim_user.sql`.
- **fact_transaction** --> to create `fact_transaction` (transaction info) table use the code from `src/tables/staging/create_fact_transaction.sql`

##

**Insert data into tables**

- **dim_book** --> to insert data into `dim_book` (book data) table use the code from `src/tables/staging/insert_dim_book.sql`
- **dim_user** --> to insert data into `dim_user` (user data) table use the code from `src/tables/staging/insert_dim_user.sql`.
- **fact_transaction** --> to insert data into `fact_transaction` (transaction info) table use the code from `src/tables/staging/insert_fact_transaction.sql`

##

**Select data from tables**

- **dim_book** --> to select data from `dim_book` (book data) table use the code from `src/tables/staging/select_dim_book.sql`
- **dim_user** --> to select data from `dim_user` (user data) table use the code from `src/tables/staging/select_dim_user.sql`.
- **fact_transaction** --> to select data from `fact_transaction` (transaction info) table use the code from `src/tables/staging/select_fact_transaction.sql`

## **Staging layer Tables**

`dim_book`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| book_id | SERIAL PRIMARY KEY | staging/books/book_id |
| isbn | VARCHAR(20) UNIQUE | staging/books/isbn |
| title | VARCHAR(300) | staging/books/title|
| author | VARCHAR(300) | staging/books/author |
| year_of_publication | TEXT | staging/books/year_of_publication |
| publisher | VARCHAR(300) | staging/books/publisher |
| currency_code | VARCHAR(3) | staging/tales_tomes_data/currency_code |

##

`dim_user`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| user_id | VARCHAR(20) | staging/tales_tomes_data/last_name |
| first_name | VARCHAR (255) | staging/tales_tomes_data/first_name |
| last_name | VARCHAR(255) | staging/tales_tomes_data/last_name |
| personal_number | VARCHAR(20) | staging/tales_tomes_data/last_name |
| birth_date | DATE | staging/tales_tomes_data/last_name |
| city | VARCHAR(50) | staging/tales_tomes_data/last_name |
| iban | VARCHAR(25) | staging/tales_tomes_data/last_name |
| location | VARCHAR(100) | staging/users/location |
| age | INT | staging/users/age |

##

`fact_transaction`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| transaction_id | VARCHAR(50) PRIMARY KEY | staging/tales_tomes_data/transaction_id |
| user_id | VARCHAR(20) FOREIGN KEY | staging/user_id |
| currency_code | VARCHAR(3) | staging/tales_tomes_data/currency_code |

##

## **Trusted Layer**

The `trusted layer` contains fully cleaned, validated and integrated data and provides reliable and consistent
data that the users/apps can trust.\

**Create trusted layer**\
To create `trusted` layer use the SQL query from `src/schemas/trusted.sql`

**Create tables**

- **dim_book** --> to create `dim_book` (book data) table use the code from `src/tables/trusted/create_dim_books.sql`
- **dim_user** --> to create `dim_user` (user data) table use the code from `src/tables/trusted/create_dim_user.sql`.
- **fact_transaction** --> to create `fact_transaction` (transaction info) table use the code from `src/tables/trusted/create_fact_transaction.sql`

##

**Insert data into tables**

- **dim_book** --> to insert data into `dim_book` (book data) table use the code from `src/tables/trusted/insert_dim_books.sql`
- **dim_user** --> to insert data into `dim_user` (user data) table use the code from `src/tables/trusted/insert_dim_user.sql`.
- **fact_transaction** --> to insert data into `fact_transaction` (transaction info) table use the code from `src/tables/trusted/insert_fact_transaction.sql`

##

**Select data from tables**

- **dim_book** --> to select data from `dim_book` (book data) table use the code from `src/tables/trusted/select_dim_books.sql`
- **dim_user** --> to select data from `dim_user` (user data) table use the code from `src/tables/trusted/select_dim_user.sql`.
- **fact_transaction** --> to select data from `fact_transaction` (transaction info) table use the code from `src/tables/trusted/select_fact_transaction.sql`

## **Trusted layer Tables**

`dim_book`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| book_id | INT PRIMARY KEY | trusted/books/book_id |
| isbn | VARCHAR(20) UNIQUE | trusted/books/isbn |
| title | VARCHAR(300) | trusted/books/title|
| author | VARCHAR(300) | trusted/books/author |
| year_of_publication | TEXT | trusted/books/year_of_publication |
| publisher | VARCHAR(300) | trusted/books/publisher |

##

`dim_user`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| user_id | VARCHAR(20) PRIMARY KEY| trusted/tales_tomes_data/last_name |
| first_name | VARCHAR (255) | trusted/tales_tomes_data/first_name |
| last_name | VARCHAR(255) | trusted/tales_tomes_data/last_name |
| personal_number | VARCHAR(20) | trusted/tales_tomes_data/last_name |
| birth_date | DATE | trusted/tales_tomes_data/last_name |
| city | VARCHAR(50) | trusted/tales_tomes_data/last_name |
| iban | VARCHAR(25) | trusted/tales_tomes_data/last_name |
| location | VARCHAR(100) | trusted/users/location |
| age | INT | trusted/users/age |

##

`fact_transaction`
| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| transaction_id | VARCHAR(50) PRIMARY KEY | trusted/tales_tomes_data/transaction_id |
| user_id | VARCHAR(20) FOREIGN KEY | trusted/user_id |
| book_id | INT | trusted/fact_transaction/book_id |
| amount | INT | trusted/fact_transaction/amount |
| currency_code | VARCHAR(3) | trusted/fact_transaction/currency_code |
| time | TIMESTAMP | trusted/fact_transaction/time |
