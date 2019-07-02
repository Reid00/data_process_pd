import pandas as pd

import matplotlib.pyplot as plt

# 绘制分组柱形图
books = pd.read_excel('books.xlsx', sheet_name='Sheet1',skiprows=6, usecols='E:J', index_col='id')
# 数据排序
books.sort_values(by='numbers_2019', inplace=True, ascending=False)

books.plot.bar(x='book name', y=['numbers', 'numbers_2019'], color=['orange', 'blue'])

plt.title('books numbers on 2019 and 2019', fontsize=16, fontweight='bold')
plt.xlabel('book name', fontweight='bold')
plt.ylabel('book numbers', fontweight='bold')

# 图表的axis 区域，非figure 区域
ax = plt.gca()  # gca get current axis
ax.set_xticklabels(books['book name'], rotation=45, ha='right')

f = plt.gcf()  # get current figure
f.subplots_adjust(left=0.2, bottom=0.8)

# plt.tight_layout()
plt.show()

# print(books)
