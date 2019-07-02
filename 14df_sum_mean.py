import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students', index_col='id')

# 拿出Dataframe 的子集
df_scores = students[['score', 'score2', 'score3']]

# 按行求值
row_ave = df_scores.mean(axis=1)
row_sum = df_scores.sum(axis=1)
students['sum'] = row_sum
students['average'] = row_ave

# 按列求值
col_ave = students[['score', 'score2', 'score3', 'sum', 'average']].mean()
col_ave['Name'] = 'Summary'
# print(col_ave)
# series 如何添加到dataframe 里面
students = students.append(col_ave, ignore_index=True)
# 部分columns 转化为int 类型
students[['score', 'score2', 'score3', 'sum']] = students[['score', 'score2', 'score3', 'sum']].astype(int)

print(students)
