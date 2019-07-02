import numpy as np
import pandas as pd
# 读取和保存Excel里面的内容，并设置重置索引列

house = pd.read_csv('demo.tsv', sep='\t', header=0, )  # index_col='id' 设置索引列
print('clolumns name are:', house.columns)
# house = house.set_index(house['房屋坐落'])
# house.set_index('id', inplace=True)  # 重置索引
# print(house.index)
print(house.head(6))
print('=' * 30)
print(house.tail(3))
house.to_csv('output.csv', encoding='utf-8-sig')
