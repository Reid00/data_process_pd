import numpy as np

array1 = np.arange(1, 11).reshape(2, 5)

print(array1)
# 迭代行

print('**' * 6)
for item in array1:
    print(item)

# 迭代列
for item in array1.T:
    print(item)

# 迭代元素
for item in array1.flat:
    print(item)
