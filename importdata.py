import sqlite3
import pandas as pd 

excel_file_path = '/Users/rebeccamonson/Library/CloudStorage/OneDrive-Personal/Documents/University of Arkansas/Fall 2024 Semester 4/Advanced Data Management ISYS 57103/ItemsTable.xlsx'
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
