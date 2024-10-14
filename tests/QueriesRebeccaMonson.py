#QueriesRebeccaMonson
import sqlite3
import pandas as pd
db_file='paperhearts.db'
cnn=sqlite3.connect(db_file)
cur= cnn.cursor()
results=cur.execute('SELECT [Net Sales] from transactions_data LIMIT 10')
print(results.fetchall())

import sqlite3
import pandas as pd
db_file='paperhearts.db'
cnn=sqlite3.connect(db_file)
cur= cnn.cursor()
query = '''
SELECT [Net Sales], [Event Type], [Category] 
FROM Transactions_Data t 
INNER JOIN Items_Data it ON t.Token = it.Token 
WHERE t.[Event Type] = 'Payment'
GROUP BY [Category]
Limit 10 '''
results = cur.execute(query)
print(results.fetchall())

import sqlite3
import pandas as pd
db_file='paperhearts.db'
cnn=sqlite3.connect(db_file)
cur= cnn.cursor()

customerID = 'IinsertedthisIditsnotreal'
CustomerName = 'MuffintheCorgi'

cur.execute('''
            INSERT INTO customers_data ([Customer ID], [Customer Name] VALUES (?, ?) ''' (customerID, CustomerName))
cnn.commit()
results=cur.execute('''SELECT [Customer Name] from customers_data Where [Customer Name] = 'Muffinthecorgi'''')
print(results.fetchall())