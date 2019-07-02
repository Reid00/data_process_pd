import pandas as pd

import matplotlib.pyplot as plt

# 绘制叠加柱形图

books = pd.read_excel('books.xlsx', sheet_name='Sheet1', skiprows=6, usecols='E:K', index_col='id')

books['total_num'] = books['numbers'] + books['numbers_2019'] + books['numbers_2020?']

# 数据排序
books.sort_values(by='total_num', inplace=True, ascending=False)

# 叠加柱状图
# books.plot.bar(x='book name', y=['numbers', 'numbers_2019', 'numbers_2020?'], stacked=True)
# 水平柱状图
books.plot.barh(x='book name', y=['numbers', 'numbers_2019', 'numbers_2020?'], stacked=True)
plt.title('book number change with years', fontsize=16, fontweight='bold')

plt.show()
