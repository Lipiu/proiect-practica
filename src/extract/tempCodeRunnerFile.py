import random
import psycopg2
from faker import Faker

# Method to generate synthetic data for our company
def generate_book_data() -> list:
    "Generate data for Tales&Tomes Company."
    
    #generate data in romanian language and cultural context
    synthetic = Faker("ro_RO")
    
    #generating data for the database fields
    transaction_id = synthetic.uuid4()
    first_name = synthetic.first_name()
    last_name = synthetic.last_name()
    age = synthetic.random_int(18,80)
    user_id = (first_name[:2] + last_name[:2]).lower() # taking first 2 letters from first and last name and create an ID
    personal_number = synthetic.ssn();
    birth_date = synthetic.date_of_birth()
    city = synthetic.city()
    iban = synthetic.iban()
    amount = synthetic.random_int(1, 200)
    currency_code = synthetic.currency_code()
    time = synthetic.date_time_between("-1d", "now")
    location = synthetic.address()

    return[
        transaction_id, first_name, last_name, age, user_id, personal_number, birth_date, city,
        iban, amount, currency_code, time, location
    ]

# Method to load data
def load_data(data: list) -> None:
    "Connecting to database and inserting data into specified tables"

    connection = psycopg2.connect(
        dbname = "TalesAndTomes",
        user = "postgres",
        password = "2805",
        host = "localhost",
        port = 5432
    )

    cursor = connection.cursor()

    sql = """
        INSERT into raw.tales_tomes_data(
            transaction_id, first_name, last_name, age, user_id, personal_number, birth_date, city,
            iban, amount, currency_code, time, location
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
    """
    cursor.execute(sql, data)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    for _ in range(100):
        synthetic_data = generate_book_data()
        load_data(synthetic_data)