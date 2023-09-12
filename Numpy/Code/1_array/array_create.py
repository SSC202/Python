import numpy as np

"""
    数组创建
"""
# 从列表创建数组
# x = np.array([1,2,3,4,5])

# 从嵌套列表创建数组
# x = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 创建零数组
# x = np.zeros(5,dtype=np.uint8)

# 创建单位数组
# x = np.ones(10,dtype=np.float32)
x = np.eye(3)

# 创建同值数组
# x = np.full((3,5),3.14)

# 创建线性序列
# x = np.arange(0, 20, 2)
# x = np.linspace(0, 1, 5)

# 创建随机数组
# x = np.random.random((2,3))           # 均匀分布
# x = np.random.normal(0, 1, (2, 3))    # 正态分布
# x = np.random.randint(0, 10, (3, 3))  # 随机整型

# 创建空数组
# x = np.empty(3)
# print(x)

"""
    数组属性
"""
# print(x.shape)
# print(x.ndim)
# print(x.size)
# print(x.dtype)

"""
    索引和切片
"""
# y = x[1, 1]
# y = x[:2,:2]    # 获取2行2列
# print(y)
