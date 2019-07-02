import pandas as pd
# pandas Series 练习，创建dataframe

d = {'x': 100, 'y': 200, 'z': 300}

s1 = pd.Series(d)
print(s1)

li = [1, 2, 3]
print(pd.Series(li))
index = ['x', 'y', 'z']
s2 = pd.Series(li, index=index)
print('s2', s2)
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

df = pd.DataFrame({s1.name: s1,
                   s2.name: s2,
                   s3.name: s3,
                   })

print(df)
