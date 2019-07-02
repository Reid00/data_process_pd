import pandas as pd
from datetime import date, timedelta
import random
# pandas 补充空白值，时间增量，排序等

def add_month(d, md):
    year = md // 12
    m = d.month + md % 12
    if m != 12:
        year += m // 12
        m = m % 12
    return date(d.year + year, m, d.day)


books = pd.read_excel('books.xlsx', skiprows=6, usecols='E:I',
                      dtype={'id': str, 'instore': str, 'date': str, })
# dtype 给每一列设置类型值
books['id'].at[0] = 100  # pd.Series at 方法赋值
# print(books.index)
start = date(2019, 1, 1)
for i in books.index:
    books['id'].at[i] = i + 1
    books['instore'].at[i] = 'YES' if i % 2 == 0 else 'NO'
    # books['date'].at[i] = start + timedelta(days=i)  # date 日递增
    books['date'].at[i] = add_month(start, i)  # date 月份递增
    # books['date'].at[i] = date(start.year + i, start.month, start.day)  # date 年份递增
    books['numbers'].at[i] = random.randint(1, 10)

books['numbers'] = books['numbers'].apply(lambda x: x + 2)  # pandas Series 可以使用apply 方法，后面跟一个函数
books.sort_values(by=['instore', 'numbers'], inplace=True, ascending=[True, False])
print(books)
