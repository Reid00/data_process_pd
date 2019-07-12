import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# 垂直合并
array3 = np.vstack((array1, array2))
print(array3)

# 水平合并
array4 = np.hstack((array1, array2))

print(array4)
