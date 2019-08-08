import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students')

# Series 用str 转化为str field
df = students['Name'].str.split('_', expand=True)
# # print(df[0])
students['common_name'] = df[0]
students['id_name'] = df[1]

# students['common_name'], students['id_name'] = students['Name'].str.split('_').str  # 另外一种方法

# print(students)

# 拆分一行扩展成多行
df = pd.DataFrame({
    'Country': ['China', 'US', 'Japan', 'UK/Australia', 'UK/Netherland'],
    'Value': [5, 3, 2, 4, 5]
}
)

# 先拆分country 这一列
# country = df['Country'].str.split('/', expand=True).stack()  # stack 使得拆分后的数据变为行
# country = df['Country'].str.split('/', expand=True).stack().reset_index(drop=True)  # 重置索引
# country = df['Country'].str.split('/', expand=True).stack().reset_index(level=1, drop=True)  # 重置索引,level=1 是拆分前后的索引相同
country = df['Country'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename(
    'Country')  # 重置索引,level=1 是拆分前后的索引相同, rename 给Series 命名，否则是没有名字的series
print(country)
# df.drop('Country', axis=1, inplace=True)
df.drop(columns='Country', inplace=True)
print(df)
df = df.merge(country, left_index=True, right_index=True, how='inner').reset_index(drop=True)
print(df)
