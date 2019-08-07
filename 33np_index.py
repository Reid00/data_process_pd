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

# 条件索引
print(array1[array1 > 3])

# 通用函数
arr = np.random.randn(2, 3)
print('**' * 6)
print(arr)
# np.where 矢量的三元表达式
# 大于3 的为1，小于三的-1
print(np.where(arr > 3, 1, -1))

# 条件索引
print(arr[arr > 0.5])

# np.all, np.any,np.unique
