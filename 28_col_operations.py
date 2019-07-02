import pandas as pd
import numpy as np

# pandas 列操作

students = pd.read_excel('students.xlsx', sheet_name='students', )
score = pd.read_excel('students.xlsx', sheet_name='score', )
# contact 连接， axis 控制横轴还是数轴
# students = pd.concat([students, score], axis=1)

# 在最后面插入一列
# students['Age'] = 25
# students['Age'] = np.repeat(25, len(students))
students['Age'] = np.arange(0, len(students))

# 在特定列之后插入列
students.insert(1, column='Name2', value=np.arange(0, len(students)))

# 删除列
students.drop(columns=['Age', 'score3'], inplace=True)

# 重命名列名
students.rename(columns={'Name': 'NAME'}, inplace=True)

# 去重空值
for i in range(0, 6):
    students['NAME'].at[i] = np.nan

students.dropna(inplace=True)
print(students)
