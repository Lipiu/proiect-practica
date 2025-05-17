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
        "user_id": row["User-ID"],
        "isbn": row["ISBN"],
        "book_rating": row["Book-Rating"]
    }

    return data

def load_data(data: dict) -> None:
    conn = psycopg2.connect(
        dbname = "TalesAndTomes",
        user = "postgres",
        password = "2805",
        host = "localhost",
        port = 5432
    )

    cursor = conn.cursor()

    sql = """
        INSERT INTO raw.ratings (
            user_id, isbn, book_rating
        ) VALUES (
            %s, %s, %s
);
    """

    cursor.execute(
        sql,
        (
            data.get("user_id"),
            data.get("isbn"),
            data.get("book_rating"),
        )
    )
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    csv_data = extract_data('data/ratings.csv', limit=500)
    for row in csv_data:
        parsed_data = parse_data(row)
        load_data(parsed_data)
