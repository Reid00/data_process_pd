import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students', usecols='A,B')
score = pd.read_excel('students.xlsx', sheet_name='score')
# print(score.describe())

# 多表联合,merge method
# tbl = students.merge(score, how='left', on='id').fillna(0)
# 多表联合,join method,默认用index
tbl = students.join(score, how='left', on='id').fillna(0)

tbl['score'] = tbl['score'].astype(int)  # 把float 转为int
print(tbl)

# print(students.head())
# print(score.head())
