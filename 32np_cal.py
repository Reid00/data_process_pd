import numpy as np

array1 = np.arange(1, 11).reshape(2, 5)

array2 = np.arange(5, 15).reshape(2, 5)

print(array1, '\n', array2)

# 矩阵的加法, 按位置相加， 形状必须相同， 如若不同不能进行操作

print(array2 + array1)
print(array2 - array1)
print(array2 * array1)
print(array2 ** array1)  # 幂运算
print(array2 / array1)
print(array2 % array1)  # 去余数
print(array2 // array1)  # 取整数操作

print(array1 + 2)  # 所有的元素加2

array3 = array1 > 3
print(array3)

array4 = np.ones((3, 5))

print('****' * 20)
# array5 = array1.dot(array4)
# print(array5)

# 随机数
sample1 = np.random.random((3, 2))  # 三行两列，0-1 的随机数
print(sample1)

sample2 = np.random.randint(0, 10, size=(3, 2))  # 3*2 的，0-10 的随机整数
sample3 = np.random.randint(0, 10, size=(10))  # 10个 的，0-10 的随机整数
print('sample2', sample2)
print('sample3', sample3)

print(np.sum(sample2))
print(np.min(sample2))
print(np.max(sample2))
# 对行求和
print(np.sum(sample2, axis=1))
print(np.sum(sample2, axis=0))
print('***' * 3)
print(sample2[0])
print(np.sort(sample3))
