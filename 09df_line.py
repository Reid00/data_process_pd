import pandas as pd

import matplotlib.pyplot as plt

# 绘制折线图
books = pd.read_excel('books.xlsx', sheet_name='Sheet1', skiprows=6, usecols='E:K', index_col='id')
# 折线图
# books.plot(y=['numbers', 'numbers_2019', 'numbers_2020?'])
# 叠加区域图
books.plot.area(y=['numbers', 'numbers_2019', 'numbers_2020?'])

plt.title('line chart for books number with years', fontsize=20, fontweight='bold')
plt.ylabel('number values', fontsize=12, fontweight='bold')

# x/ytick指定 ticks 为递增值向量；例如 [0 2 4 6]。此命令作用于当前坐标区。
plt.xticks(books.index, fontsize=8)

plt.show()
