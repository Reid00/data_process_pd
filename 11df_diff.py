import pandas as pd

df1 = pd.read_csv('1.tsv', sep='\t', header=None, names=['sk', 'sid', 'alias', 'comments'])
df2 = pd.read_csv('2.tsv', sep='\t', header=None, names=['sk', 'sid', 'alias', 'comments'])
# merge 方法 outer 方式联合, indicator=True, 添加一列_merge, 显示来源，left_only,right_only,both
# 使用索引做连接key, 使用参数left_index,right_index=True

# merged = df1.merge(df2, on='sk',how='outer', indicator=True)
# 不可以指定on 的条件， 两个表有相同的列名，所有会以所有的列作为on
merged = df1.merge(df2, how='outer', indicator=True)
merged.to_csv('merged.tsv', sep='\t', index=False, header=None)

# 过滤，只在左表里面有的
condi = merged.loc[merged['_merge'] == 'left_only']
print(condi)

# left_only = merged[condi.index]
# left_only.to_csv('left_only.tsv', sep='\t', index=False, header=None)
