import numpy as np

# array=np.random.randint(1,10,20).reshape(4,5)
# print(array)
# print(array.shape) # shape -> (4,5)
# array2 = np.ones(20).reshape(4,5)
# array3 = np.random.randint(1,20,20).reshape(5,4)
# print(array3)
#
# # 4x5的数组，外层为4，内层为5
# # for i in range(0,array.shape[0]):
# #     for j in range(0,array.shape[1]):
# #         print(array[i][j],end="\t")
# #         pass
# #     print()
#
# # 基本运算
# # 求所有的和
# print(array.sum())
#
# # 计算每一列的累加和
# print(array.sum(0))
#
# # 计算每一行的累加和
# print(array.sum(1))
# # 矩阵加法
# print(array+array2)
# # 矩阵减法
# print(array-array2)
# # 矩阵乘法
# array4 = np.dot(array,array3)
# print(array4)
# # 矩阵的倍数
# print(2*array4)
#
# # 居然的转秩
# print(array4.T)
#
#
# # 矩阵的逆
# array5 = np.random.randint(1,10,9).reshape(3,3)
# array6 = np.linalg.inv(array5)
# print("*********")
# print(array6)
# array7 = np.dot(array6,array5)
# print(array7)



# 矩阵的合并拆分
array = np.random.randint(1,10,9).reshape(3,3)
array2=np.ones(9).reshape(3,3)
print(array)
# print(array2)


# print(array.ravel())
# print(np.vstack((array,array2)))
# print(np.hstack((array,array2)))

# print(np.row_stack((array2,array)))
# print(np.column_stack((array,array2)))

# print(np.stack((array,array2),2))

# 切割成3个array,每一行为一个array
# print(np.split(array,3))
# 按列来切，切成3个列
# print(np.split(array,3,1))

print(np.vsplit(array,3))


