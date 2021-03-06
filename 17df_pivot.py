import pandas as pd
import numpy as np

students = pd.read_excel('students.xlsx', sheet_name='students', index_col='id')

# 查看data数据类型
# print(students['date'].dtype)

# 取出date 列的年份
students['Year'] = pd.DatetimeIndex(students['date']).year

# 绘制pivot table
pt1 = students.pivot_table(index='Name', columns='Year', values='score', aggfunc=np.sum)

groups = students.groupby('Year')

sum = groups('score').sum()

print(sum)

# 用groupby 的方法
groups2 = students.groupby(['Name'])
s = groups2['score'].sum()
c = groups2['Year'].count()
pt2 = pd.DataFrame({
    'Sum': s,
    'Count': c
})

# print(students)
# print(pt1)
