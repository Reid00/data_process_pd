import numpy as np

arr1 = np.arange(12).reshape(3, 4)
print(arr1, '\r')
# 水平方向分割
arr2, arr3 = np.split(arr1, 2, axis=1)
print('arr2', arr2)
print('arr3', arr3)

# 垂直方向分割
arr4, arr5, arr6 = np.split(arr1, 3, axis=0)
print(arr4, arr5, arr6)

# 分均等分割
arr7, arr8, arr9 = np.array_split(arr1, 3, axis=1)
print('arr7', arr7)
print('arr8', arr8)
print('arr9', arr9)
