import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students', index_col='id')

# 直接删除duplicate值
# students.drop_duplicates(subset='Name', inplace=True, keep='first')

# 定位dupelicat 的值
dupe = students.duplicated(subset='Name')
dupe = dupe[dupe == True]
# 等价于dupe = dupe[dupe]

# 重回源数据根据index 找到重复的值
students = students.loc[dupe.index]

print(students)
