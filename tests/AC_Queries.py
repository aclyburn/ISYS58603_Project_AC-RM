# Query 1: Retrieve the first 10 rows from the Items_data table

# Create connection
import sqlite3
import pandas as pd

# Set the name of the database file to be used for this exercise
db_file = 'paperhearts.db'

# Make a connection to the database
cnn = sqlite3.connect(db_file)

# Pull back list of table names
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", cnn)
print(tables)

# Pull top 10 rows from items_data table
data = pd.read_sql_query("SELECT * FROM TRANSACTIONS_DATA LIMIT 10", cnn)
cnn.close()

data

# Query 2: Pull transaction activity for the date input by the user

# Create connection
import sqlite3
import pandas as pd

date = input("Which dates would you like to see transactions for? (YYYY-MM-DD): ")

# Set the name of the database file to be used for this exercise
db_file = 'paperhearts.db'

# Make a connection to the database
cnn = sqlite3.connect(db_file)
query = """
SELECT distinct t.Date, t.Qty, t.[Net Sales], i.Item, i.[Gross Sales] as Price
FROM transactions_data t
join items_data i on t.Token = i.Token
WHERE DATE(t.date) = ?
"""
data = pd.read_sql_query(query, cnn,params=[date])
cnn.close()

data

# Query 3: Pull sales totals by month

# Create connection
import sqlite3
import pandas as pd

# Set the name of the database file to be used for this exercise
db_file = 'paperhearts.db'

# Make a connection to the database
cnn = sqlite3.connect(db_file)
query = """
SELECT sum([Net Sales]) as "Monthly Sales", strftime('%m',Date) as Month, sum(Qty) as "Total Items Sold"
FROM transactions_data
group by strftime('%m',Date)
"""
data = pd.read_sql_query(query, cnn)
cnn.close()

data