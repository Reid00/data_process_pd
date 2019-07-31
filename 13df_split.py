import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students')

# Series 用str 转化为str field
df = students['Name'].str.split('_', expand=True)
# # print(df[0])
students['common_name'] = df[0]
students['id_name'] = df[1]

# students['common_name'], students['id_name'] = students['Name'].str.split('_').str  # 另外一种方法

print(students)
