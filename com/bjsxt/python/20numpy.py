import numpy as np
# 创建矩阵
# array = np.array([1,2,3])
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)

# 二维数组
# array = np.array([[1,2,3],[4,5,6]])
# print(array)
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)

# array = np.array([[[1,2],[3,4]],
#                 [[5,6],[7,8]],
#                   [[9,10],[11,12]]])
# print(array)
# print(array.ndim)
# # print(array.shape)
# # print(array.size)
# # print(array.dtype)
#
# # 生成数组
# array = np.arange(1,28).reshape(3,3,3)
# print(array)
#
# # 通过随机数生成矩阵
# array =np.random.randint(1,10,12).reshape(2,3,2)
# print(array)
#
# # 标准正态分布
# array=np.random.rand(9).reshape(3,3)
# print(array)
#
# array = np.random.randn(9).reshape(3,3)
# print(array)
#
# array = np.empty(9).reshape(3,3)
# print(array)
#
# array=np.ones(9).reshape(3,3)
# print(array)
# # where 满足条件做相应操作
# array = np.random.randint(1,10,9).reshape(3,3)
# print(np.where(array>5,array,1))

'''
切片
'''
array = np.random.randint(1,10,16).reshape(4,4)
print(array)
print("================")
# 取第一行所有值
print(array[0])
# 取第一列
print(array[:,0])

# 取第一行和第三行
print(array[0::3,:])

# 取第一列，第三列
print(array[:,0::2])

'''
    取 a00 a03  
       a20 a23
'''
print(array[0::2,0::3])