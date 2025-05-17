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

- Top Readers
  - A visual display of top readers

### KPIs

- Number of books read
- Number of pages read

##

## Data Warehouse Design

Server: `TalesAndTomes`\
Database: `TalesAndTomes.db`

## Sources

- **Tales&Tomes App** - Own platform data.
- **Kaggle** - Provider for the data set.

## Resources

[The dataset for the project is available here](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)

##

## Structure

The proiect-practica repository contains:

- Files:

  - `.gitignore` --> store directories and files to be ignored by Git.
  - `README.md` --> contains all instructions and documentation about this repository.

- Folders
  - `data` --> in this file you can find the datasets used for this project.
  - `src` --> here is the source code (Python + SQL)
    - `schemas`
      - raw
      - staging
      - trusted
    - `tables`
      - `raw`
        - create
        - insert
        - select
      - `staging`
        - create
        - insert
        - select
      - `trusted`
        - create
        - insert
        - select
    - `extract`
      - `books.py` --> used to extract data from `books.csv`.
      - `ratings.py` --> used to extract data from `ratings.csv`.
      - `tales_tomes.py` --> used to generate synthetic data for the users.
      - `tempCodeRunnerFile.py` --> a random file generated after running the `tales_tomes.py`.
      - `generate.py` --> used to randomize user transactions.
    - `load`
      - `loader.py` --> a script used to load data so you don't have to do it manually.
    - `transform`
      - `transformer.py` --> used for automating the process of converting the data from: raw->staging->trusted.
    - `assets`
      - contains a picture of the chart with people that read the most books.

##

## Tools you need in order to use/contribute this project:

- **Git**
  - from [here](https://git-scm.com/downloads) you can install git.
  - check if git installed correcly by using: git --version
- **Python**
  - from [here](https://www.python.org/downloads/) you can install python.
  - check if python installed correctly by using: python --version
- **PostgreSQL - pgAdmin 4**
  - needed to manage your PostgreSQL database via a GUI.
  - from [here](https://www.postgresql.org/download/) you can install PostgreSQL.
  - from [here](https://www.pgadmin.org/) you can download and install pgAdmin 4.

## Clone

Steps to clone this project:

```
1. Navigate to your desired directory/folder where you'll clone this project.
You can also:
  --> Navigate to desired folder, click on the path bar and write "cmd" and the terminal will open at that location.

Or manually navigate by using:
cd <your-repository-path>

2. After you found the perfect place to clone the repo use:
git clone https://github.com/Lipiu/proiect-practica.git

Now the repository has been successfully cloned and you can start contributing!
```
