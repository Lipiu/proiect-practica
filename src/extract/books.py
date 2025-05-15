import requests
import psycopg2
import csv

def extract_data(file_path: str, limit: 500): #because there are 200_000 rows and it takes too long to load
    """
    Extract data from the csv file.
    """
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter = ';')
        for i, row in enumerate(csv_reader):
            if i >= limit:
                break
            data.append(row)
    return data

def parse_data(row: dict):
    """
    Parsing data
    """

    data = {
    #titlu, autor, year, publisher
        "isbn": row["ISBN"],
        "title": row["Book-Title"],
        "author": row["Book-Author"],
        "year_of_publication": row["Year-Of-Publication"],
        "publisher:": row["Publisher"]
    }

    return data

def load_data(data: dict) -> None:
    conn = psycopg2.connect(
        dbname = "talesTomes",
        user = "postgres",
        password = "2805",
        host = "localhost",
        port = 5432
    )

    cursor = conn.cursor()

    sql = """
        INSERT INTO raw.books (
            isbn, title, author, year_of_publication, publisher
        ) VALUES (
            %s, %s, %s, %s, %s
);
    """

    cursor.execute(
        sql,
        (
            data.get("isbn"),
            data.get("title"),
            data.get("author"),
            data.get("year_of_publication"),
            data.get("publisher"),
        )
    )
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    csv_data = extract_data('data/books.csv', limit=500)
    for row in csv_data:
        parsed_data = parse_data(row)
        load_data(parsed_data)
