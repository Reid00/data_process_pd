import pandas as pd

import matplotlib.pyplot as plt

# 绘制柱形图
books = pd.read_excel('books.xlsx', sheet_name='Sheet1', skiprows=6, usecols='E:J', index_col='id')

# 数据排序
books.sort_values(by='numbers', inplace=True, ascending=False)
# pandas 绘图
# books.plot.bar(x='book name', y='numbers', color='orange', title='book name and numbers')

# matplotlib 绘图
plt.bar(books['book name'], books.numbers, color='orange')
# 标签旋转
plt.xticks(books['book name'], rotation='90')
# 设置x,y 轴标签
plt.xlabel('book name')
plt.ylabel('numbers')
plt.title('the bar book name and numbers', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
