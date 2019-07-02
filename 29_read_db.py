import pandas as pd

import pyodbc

connection = pdodbc.connect('DRIVER={SQL SERVER}; SERVER= (local);DATABASE= Personal;USER=sa;PASSWORD=123456')

query = "select FirstName from Persnal.Person"

df1 = pd.read_sql_query(query, connection)

print(df1.head())
