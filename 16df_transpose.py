import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students', index_col='Name')

tbl = students.transpose()

print(tbl)
