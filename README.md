# Data Warehousing Project:
### Analysis of books read over a period of time.

## Scenario
### You are a Data Engineer in the Tales & Tomes company. Your goal is to develop an application that tracks books read over a period of time in different countries.

## Bussiness Requiremenets
Tales & Tomes provides statistical information about books read and time spent reading.

## Bussiness Goals
- **Tracking books read** - Provide the users information about how many books they read over a month/year.
- **Personalized recommendations** - Providing reading suggestions based on user's personal taste.
- **Year in Books Summary (Book Wrapped)** - At the end of the year, users receive a visual and data-driven summary of their reading journey such as: total pages read, most read author etc...

### Reports
- Books started/completed
- Pages read
- Average reading time per day
- Reading streaks
- Book Reviews

### Dashboards
- My Library
    - Stores the books that the user finished or is currently reading.

- My Wishlist
    - Books that the user wants/will buy in the future.
- Achievements Dashboard
    - By reading, users will get certain achievements.

- Reading challenges
    - Certaing challenges for the users to complete or help them set goals.
### KPIs
- Number of books read
- Number of pages read
- Users that completed most reading challenges
##
## Data Warehouse Design
Server: `talesTomes`\
Database: `talesTomes.db`

## Sources
- **Tales&Tomes App** - Own platform data.
- **Kaggle** - Provider for the data set.

**Tables**\
tales_tomes_data

| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| transaction_id | VARCHAR(50) | Unique identifier of the transaction |
| first_name | VARCHAR(255) | Customer first name |
| last_name | VARCHAR(255) | Customer last name |
| user_id | VARCHAR(20) | Platform user identifier name |
| personal_number | INT | Personal numerical identifier |
| birth_date | DATE | Birth date |
| city | VARCHAR(50) | User's city |
| iban | VARCHAR(25) | Bank account number |
| amount | INT | Amount of money of the transaction
| currency_code | VARCHAR(3) | Currency code used in the transaction |
| time | TIMESTAMP | Transaction time |

##

book

| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| title | VARCHAR(300) | Unique title of the book|
| author | VARCHAR(300) | Name of the book author |
| year_of_publication | TEXT | The year in which the book was published |
| publisher | VARCHAR(300) | The publisher of the book |

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

## Resources
[The dataset for the project is available here](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)
