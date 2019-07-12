import numpy as np

a = np.array([1, 2, 3], dtype=np.int32)
print(a.dtype)
a = np.array([1, 2, 3], dtype=np.float64)
print(a.dtype)

# 全为零的矩阵

zero = np.zeros((2, 3))  # 2*3 的矩阵

print(zero)

one = np.ones((2, 3))  # 2*3 的矩阵

print(one)

empty = np.empty((2, 3))  # 2*3 的矩阵, 接近于零，但是不是零
print(empty)

print('*' * 20)

e = np.arange(2, 10)
f = np.arange(2, 15, 3)
print('e:', e)
print('f: ', f)

reshape = np.arange(2, 10).reshape(2, 4)  # reshape 新的形状
print(reshape)
