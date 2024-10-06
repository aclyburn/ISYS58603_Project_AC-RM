import sqlite3
import pandas as pd

# Enable installation of openpyxl, if needed (comment this line if you have it installed)
# !pip install openpyxl

# Define the database file
db_file = 'paperhearts.db'

# Function to import data from an Excel file to a SQLite table
def import_data_from_excel(excel_file_path, table_name, create_table_query):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)
    print(df.columns)

    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table
    cursor.execute(create_table_query)

    # Import the DataFrame into the SQL table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

    print(f'Data imported successfully into {table_name}')

# 1. Import Items data
items_excel_path = 'C:/Users/alyso/Downloads/Items.xlsx'
items_create_table = '''
CREATE TABLE IF NOT EXISTS "Items_data" (
    "Token" VARCHAR,
    "Category" TEXT,
    "Price Point" TEXT,
    "SKU" VARCHAR,
    "Gross Sales" INT
);
'''
import_data_from_excel(items_excel_path, 'Items_data', items_create_table)

# 2. Import Transactions data
transactions_excel_path = 'C:/Users/alyso/Downloads/Transactions.xlsx'
transactions_create_table = '''
CREATE TABLE IF NOT EXISTS "transactions_data" (
    "Date" DATE,
    "Time" TIME,
    "Qty" INT,
    "Discounts" INT,
    "Net Sales" INT,
    "Tax" INT,
    "Transaction ID" INTEGER,
    "Payment ID" INTEGER,
    "Device Name" TEXT,
    "Details" TEXT,
    "Event Type" TEXT,
    "Customer ID" INTEGER,
    "Unit" TEXT,
    "Count" INT,
    "Itemization" TEXT,
    "Employee" TEXT,
    "Token" INTEGER
);
'''
import_data_from_excel(transactions_excel_path, 'transactions_data', transactions_create_table)

# 3. Import Payments data
payments_excel_path = 'C:/Users/alyso/Downloads/Payments.xlsx'
payments_create_table = '''
CREATE TABLE IF NOT EXISTS "payments_data" (
    "Card Entry Methods" TEXT,
    "Cash" INT,
    "Square Gift Card" INT,
    "Other Tender" INT,
    "Other Tender Type" TEXT,
    "Other Tender Note" TEXT,
    "Fees" INT,
    "Fee Percentage Rate" INT,
    "Fee Fixed Rate" INT,
    "Cash App" INT,
    "Refund Reason" TEXT,
    "Discount Name" TEXT,
    "Event Type" TEXT
);
'''
import_data_from_excel(payments_excel_path, 'payments_data', payments_create_table)

# 4. Import Customers data
customers_excel_path = 'C:/Users/alyso/Downloads/Customers.xlsx'
customers_create_table = '''
CREATE TABLE IF NOT EXISTS "customers_data" (
    "Customer ID" INTEGER,
    "Customer Name" TEXT
);
'''
import_data_from_excel(customers_excel_path, 'customers_data', customers_create_table)

#importdata2.py
import sqlite3
import pandas as pd 
excel_file_path = 'C:/Users/alyso/Downloads/Items.xlsx'
df= pd.read_excel(excel_file_path)

print(df.columns)

db_file = 'paperhearts.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS "Items_data" (
    "Token" VARCHAR
    "Category" TEXT
    "Price Point" TEXT
    "SKU VARCHAR"
    "Gross Sales" INT
)'''

cursor.execute(create_table)

df.to_sql('Items_data', conn, if_exists= 'replace', index=False)
conn.commit()
conn.close()

print("heck yes it worked!")

excel_file_path = 'C:/Users/alyso/Downloads/Deposits.xlsx'
df= pd.read_excel(excel_file_path)

print(df.columns)

db_file = 'paperhearts.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS "DepositData_data" (
    "Deposit ID" ID
    "Deposit Date" DATE
    "Deposit Details" VARCHAR
)'''

cursor.execute(create_table)

df.to_sql('DepositData_data', conn, if_exists= 'replace', index=False)
conn.commit()
conn.close()

print("heck yes it worked!")