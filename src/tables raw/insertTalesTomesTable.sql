INSERT INTO raw.talesTomesData(
    transaction_id,
    first_name,
    last_name,
    user_id,
    personal_number,
    birth_date,
    city,
    iban, 
    amount, 
    currency_code,
    time 
) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)