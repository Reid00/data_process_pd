import pandas as pd
import numpy as np
from datetime import date

books = pd.read_excel('books.xlsx', sheet_name='Sheet1', skiprows=6, usecols='E:H,I', index_col='id')

# books = books.loc[books['numbers'].apply(lambda num: num > 10)].loc[
#     books['date'].apply(lambda x: x > pd.Timestamp(2019, 6, 1))]

books = books[books['numbers'].apply(lambda num: num > 10)].loc[
    books['date'].apply(lambda x: x > pd.Timestamp(2019, 6, 1))]

# loc 定位某一行，[‘numbers’]Series 使用apply 进行比较。
# pandas 时间比较用Timestamp

# loc 使用索引值进行定位，'index0','col0' >> df.loc['index0','col0']
# iloc 使用索引编号进行定位，第一个行索引，第几个列索引 >> df.iloc[0,0]
# ix 上面两个都可以使用

print(books)
# 添加新的过滤方法
df = pd.DataFrame({'name': ['a', 'b', 'c'], 'score': [0, 1, 2]})
# np.where 满足某个条件进行分组
df['sign'] = np.where(df['score'] < 2, np.nan, df['score'])
# 满足某个条件进行修改
df.loc[df['sign'].isnull(), 'name'] = 'true'
