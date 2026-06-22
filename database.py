import pymysql
import pandas as pd
from config import DB_CONFIG

# ----------------------------------------
# Database Connection
# ----------------------------------------
def get_connection():
    return pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )

# ----------------------------------------
# Create Table
# ----------------------------------------
def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS transactions(

        id INT AUTO_INCREMENT PRIMARY KEY,

        transaction_id VARCHAR(30),

        customer_id VARCHAR(30),

        transaction_time DATETIME,

        amount DOUBLE,

        vendor VARCHAR(100),

        merchant_category VARCHAR(100),

        location VARCHAR(100),

        transaction_type VARCHAR(100),

        payment_method VARCHAR(100),

        device_type VARCHAR(100),

        previous_transactions INT,

        average_amount DOUBLE,

        fraud_label INT

    )

    """)

    conn.commit()
    conn.close()

    print("Table Created Successfully")

# ----------------------------------------
# Insert CSV Data
# ----------------------------------------
def insert_dataset(csv_file):

    conn = get_connection()

    cursor = conn.cursor()

    df = pd.read_csv(csv_file)

    sql = """

    INSERT INTO transactions(

    transaction_id,

    customer_id,

    transaction_time,

    amount,

    vendor,

    merchant_category,

    location,

    transaction_type,

    payment_method,

    device_type,

    previous_transactions,

    average_amount,

    fraud_label

    )

    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

    """

    for _, row in df.iterrows():

        cursor.execute(sql, (

            row.transaction_id,

            row.customer_id,

            row.transaction_time,

            row.amount,

            row.vendor,

            row.merchant_category,

            row.location,

            row.transaction_type,

            row.payment_method,

            row.device_type,

            row.previous_transactions,

            row.average_amount,

            row.fraud_label

        ))

    conn.commit()

    conn.close()

    print("Dataset Inserted Successfully")

# ----------------------------------------
# Read Data
# ----------------------------------------
def load_data():

    conn = get_connection()

    query = "SELECT * FROM transactions"

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    conn.close()

    return df


if __name__ == "__main__":

    create_table()

    insert_dataset("transactions.csv")