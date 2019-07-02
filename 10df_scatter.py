import pandas as pd
import matplotlib.pyplot as plt
import re

# 绘制散点图,直方图,密度图
house = pd.read_csv('demo.tsv', sep='\t', header=0, )

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 绘制散点图
# house.plot.scatter(x='建筑面积', y='参考单价')

# 绘制直方图
house['参考单价'].plot.hist(bins=100)
# # 重铺x 标记单位
plt.xticks(range(13000, 16000, 1000), fontsize=12, rotation=90)

# 绘制密度图
# house['参考单价'].plot.kde()
# plt.xticks(range(13000, 16000, 1000), fontsize=12, rotation=90)

# plt.show()

# 列与列之间的关系
print(house.corr())
print(house.corr())
