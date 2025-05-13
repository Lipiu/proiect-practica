import random
import psycopg2
from faker import Faker

# Method to generate synthetic data for our company
def generateBookData() -> list:
    "Generate data for Tales&Tomes Company."
    
    #generate data in romanian language and cultural context
    synthetic = Faker("ro_RO")
    
    transaction_id = synthetic.uuid4()
    first_name = synthetic.first_name
    last_name = synthetic.last_name

    # taking first 2 letters from first and last name and create an ID
    user_id = (first_name[:2] + last_name[:2]).lower()
    personal_number = synthetic.ssn();
    birth_date = synthetic.date_of_birth()
    city = synthetic.city()
    iban = synthetic.iban()
    amount = synthetic.random_int(1, 200)
    currency_code = synthetic.currency_code()
    time = synthetic.date_time_between("-1d", "now")
