import sqlite3
import pandas as pd
!pip install openpyxl

excel_file_path = 'C:/Users/alyso/Downloads/Transactions.xlsx'
df = pd.read_excel(excel_file_path)

print(df.columns)

db_file = 'paperhearts.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS "transactions_data" (
    Date DATE
    Time TIME
    Qty INT
    Discounts   INT
    "Net Sales"   INT
    Tax INT
    "Transaction ID"  ID
    "Payment ID"  ID
    "Device Name" TEXT
    Details TEXT
    "Event Type"  TEXT
    "Customer ID" ID
    "Unit"    TEXT
    "Count"   INT
    "Itemization" TEXT
    "Employee"    TEXT
    "Token"   ID
    )
'''
cursor.execute(create_table)

df.to_sql('transactions_data', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

print('Data imported successfully')

excel_file_path = 'C:/Users/alyso/Downloads/Payments.xlsx'
df = pd.read_excel(excel_file_path)

print(df.columns)

db_file = 'paperhearts.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS "payments_data" (
    "Card Entry Methods"    TEXT
    Cash INT
    "Square Gift Card"  INT
    "Other Tender"  INT
    "Other Tender Type" TEXT
    "Other Tender Note" TEXT
    Fees    INT
    "Fee Percentage Rate"   INT
    "Fee Fixed Rate"    INT
    "Cash App"  INT
    "Refund Reason" TEXT
    "Discount Name" TEXT
    "Event Type"  TEXT
    )
'''
cursor.execute(create_table)

df.to_sql('payments_data', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

print('Data imported successfully')

excel_file_path = 'C:/Users/alyso/Downloads/Customers.xlsx'
df = pd.read_excel(excel_file_path)

print(df.columns)

db_file = 'paperhearts.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS "customers_data" (
    "Customer ID" ID
    "Customer Name" TEXT
    )
'''
cursor.execute(create_table)

df.to_sql('customers_data', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

print('Data imported successfully')