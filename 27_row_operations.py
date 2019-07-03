import pandas as pd
from datetime import date

# pandas 行操作

students = pd.read_excel('students.xlsx', sheet_name='students', dtype={'date': date, 'id': int})

# 在尾部插入一行,或者二多行dataframe 用 append， reset_index(drop=True)
stu = pd.Series({'id': 45,
                 'Name': 'Tom',
                 'score': 99,
                 'score2': 98,
                 'score3': 86,
                 'date': date(2019, 7, 2)
                 })

students = students.append(stu, ignore_index=True)

# 更改已经有的值,at 为index 的值，'Name' 为columns 名称
students.at[21, 'Name'] = 'Hobby'
# or students['Name'].at[21] = 'Hobby'
# print(students)
# 整行替换,没有指定的列为NaN
stu2 = pd.Series({'id': 00, 'Name': 'Emma', 'score': 100})
students.iloc[20] = stu2
# students.date.astype(.date)

# 插入一行
stu3 = pd.Series({'id': 1, 'Name': 'Lila', 'score': 101})
part1 = students[:18]
part2 = students[18:]
students = part1.append(stu3, ignore_index=True).append(part2, ignore_index=True)

# 删除数据行
# students.drop(index=[0, 1, 2], inplace=True)
# students.drop(index=range(3, 5), inplace=True)
# students.drop(index=students[6:8].index, inplace=True)
# 按条件删除行
for i in range(2, 5):
    students.at[i, 'Name'] = ''

missing = students.loc[students['Name'] == '']
students.drop(index=missing.index, inplace=True)
students = students.reset_index(drop=True)

print(students)

# 重置行索引
students.reindex(index=list('abcde'), fill_value=0)
# method 只对行有用，ffill 用前一行的填充，bfill 用后一行
students.reindex(index=list('abcde'), method='ffill')
students.reindex(index=list('abcde'), method='bfill')
