import pandas as pd
data = pd.read_csv('file.csv')
data.to_csv('output.csv', index=False)
import pandas as pd
import sqlite3

connection = sqlite3.connect('database.db')
data = pd.read_sql_query('SELECT * FROM table_name', connection)
data.to_sql('table_name', connection, if_exists='replace', index=False)
