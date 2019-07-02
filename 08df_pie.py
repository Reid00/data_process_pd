import pandas as pd

import matplotlib.pyplot as plt

# 绘制饼图,默认拿index作为图例标签
books = pd.read_excel('books.xlsx', sheet_name='Sheet1', skiprows=6, usecols='E:K', index_col='book name')

# 只需要拿出某一列Series
books['numbers'].plot.pie(fontsize=10, startangle=270, counterclock=False)
plt.ylabel('numbers', fontsize=16, fontweight='bold')
plt.title('pie chart for numbers', fontsize=20)
plt.show()
