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
- **Libby** - Partner platform for providing locations of nearby libraries.\

**Tables**\
user_profile_data

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

reading_activity

| Column Name | Data Type | Description |
| ----- | ----- | ----- |
| activity_id | VARCHAR(50) | Unique identifier for the reading activity (primary key)|
| user_id | VARCHAR(20) | Associated user ID |
| book_id | VARCHAR(50) | Unique identifier for the book |
| book_title | VARCHAR(255) | Title of the book being read |
| author | VARCHAR(100) | Author of the book |
| start_date | DATE | The date the user started reading the book |
| finish_date | DATE | The date the user finished reading the book|
| status | VARCHAR(20) | Reading status: Reading, Completed, Paused, Abandoned |
| current_page | INT | Page the user is currently on
| total_pages | INT | Total number of pages in the book
| rating | INT | User's rating (eg: 1-5 stars)
| review | TEXT | Optional review or notes about a books
| genre | VARCHAR(100) | Genre / Category of the book

## Resources
To be completed...
