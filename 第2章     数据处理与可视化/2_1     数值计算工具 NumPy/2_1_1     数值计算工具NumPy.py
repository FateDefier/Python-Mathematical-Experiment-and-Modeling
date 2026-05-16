# ================ 数值计算工具NumPy ==================
import numpy as np

"""
2.1 NumPy 提供两种基本的对象：
ndarray（n-dimensional array object——n维array数组对象）：array数组，简称数组，是存储单一数据类型的多维数组
ufunc（universal function object——通用函数对象）：能够对数组进行处理的通用函数，如四则运算，sin等
"""

"""
2.1.1 数组的创建、属性和操作
  通过numpy库的array函数实现数组的创建，构成数组的元素要有相同的类型
  如果向array函数传入一个列表或元组，将构造简单的一维数组；
  如果向array函数传入嵌套的列表或元组（多维列表或元组），可以构造一个二维数组（矩阵）
"""

"""
1.数组的创建
（1）array(list or tuple)函数
（2）利用arange, empty, linspace 等函数生成数组
    arange(start, stop, step, dtype=   )
    empty((row, column), type), empty函数只分配数组所使用的内存，不对数组元素初始化，故运行速度最快，返回值随机
    linspace(start, stop, num)
（3）使用虚数单位“j”生成数组（magrid 制造网格）
    mgrid[start:stop:numj] 等价于linspace(start, stop, num)
    mgrid[row_start:row_stop:row_numj, column_start:column_stop:column_numj] 
    生成 [row_start,row_stop] x [column_start,column_stop] 的 row_num x column_num 的二维数组
"""
# 创建一维数组
# a = np.array([2, 4, 6, 8, 10])
# # 创建二维数组，输入元素中既有整形数据又有浮点型数据（但都是数值型数据），输出元素均转化为浮点型
# b = np.array(((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),
#               (10, 9, 1, 3, 2), (4, 5, 6, 8, 9.0)))
# print(f"一维数组：{a}")
# print(f"二维数组：\n{b}")

# a = np.arange(4, dtype=float)  # create float array:[0., 1., 2., 3.]
# b = np.arange(0, 10, 2, dtype=int)  # create integer array:[0, 2, 4, 6, 8]
# c = np.empty((2, 3), int)  # create 2x3 integer empty array 实际并不为空，返回值随机
# d = np.linspace(-1, 2, 5)  # creat array:[-1, -0.25, 0.5, 1.25, 2.]
# e = np.random.randint(0, 3, (2, 3))  # 生成[0, 3)上的2行3列的随机整数数组

# a = np.linspace(0, 2, 5)
# print(f"a = {a}")
# b = np.mgrid[0:2:5j]  # 等价于np.linspace(0, 2, 5)
# print(f"b = {b}")
# x, y = np.mgrid[0:2:4j, 10:20:5j]
# print(f"x = {x}\ny = {y}")

"""
2.数组的属性
（1）a.ndim：返回 int，表示数组的维数
（2)a.shape：返回元组，表示数组的尺寸，(row,column)
（3）a.size：返回 int，表示数组元素总数，等于 shape 属性返回元组中所有元素的乘积（row x column）
（4）dtype：返回数据类型
（5）itemsize：返回 int，表示数组每个元素的大小（以字节为单位）
"""

# a = np.random.randint(1, 11, (3, 5))
# print(f"维数：{a.ndim}")
# print(f"维度：{a.shape}")
# print(f"元素总数：{a.size}")
# print(f"元素类型：{a.dtype}")
# print(f"每个元素的字节数：{a.itemsize}")

# 生成数学上一维向量的三种模式
# 形状为 (n,), 即可以看成行向量，也可以看成列向量，它的转置不变
# a = np.array([1, 2, 3])
# print(f"维度为：{a.shape}")
# # 行向量
# b = np.array([[1, 2, 3]])
# print(f"维度为：{b.shape}")
# # 列向量
# c = np.array([[1], [2], [3]])
# print(f"维度为：{c.shape}")

"""
3.数组元素的索引
array数组与序列中的列表（list）的区别：array数组中只允许存储相同的数据类型，，list的元素可以是不同数据类型
（1）切片：列表名（或数组名）[start:end:step](一维),左闭右开区间 [start,end)，
（2）一般索引：
一维数组：array([index]),array([[index1], [index2], ...])；
二维数组：array[i, j], 二维列表：list[i][j]
（3）布尔索引：
A 创建布尔条件：对数组或 DataFrame 的某列应用条件表达式（常用位运算符，与、或、非），生成布尔数组（pandas库）
B 应用索引：将布尔数组作为索引，提取对应位置为 True 的数据（numpy）
（4）花式索引：索引值是一个数组
A 索引值为一维数组
    如果被索引数据是一维数组，那么索引结果为对应位置的元素
    如果被索引数据是二维数组，那么索引结果为对应下标的行
B 被索引数据为二维数组，索引值也可以是二维数据
    要索引每个元素 x[row-1, column-1],row为元素所在行，column为元素所在列
    当索引值为两个维度相同的一维数组组成的二维数组时（类似[[2, 3], 1:3]），以两个维度作为横纵坐标索引出单值后组合成新的一维数组
"""
# a = np.array([2, 4, 8, 20, 16, 30])
# b = np.array(((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),
#               (10, 9, 1, 2, 3), (4, 5, 6, 8, 9.0)))
# print(a[5])
# print(a[1:7:2])  # 类似列表的索引
# print(a[[-1, -2, -4]])  # 索引多个数用两个中括号，返回列表
# print(b[1, 2])  # 第2行第3列的元素
# print(b[2])  # 第3行
# print(b[2, :])  # 第2行所有元素
# print(b[:, 1])  # 第2列
# print(b[[2, 3], 1:4])  # 第3、4行，第2、3、4列的元素，返回二维数组
# print(b[1:3, 1:3])  # 第2、3行，第2、3列的元素，返回二维数组

# # nan 缺失值，isnan 判断是否为缺失值（NaN），返回布尔值（True，False）
# from numpy import array, nan, isnan
# a = array([[1, nan, 2], [4, nan, 3]])
# # isnan(a) 生成布尔掩码（即转化为元素均为布尔值的数组），~ 非——取反（True——False，False——True）
# b = a[~isnan(a)]  # 提取a中所用非Nan的数，数值数据
# print(a)
# print(f"b = {b}")
# # b>2 生成布尔掩码[False, False, True, True]，a[布尔掩码] 提取所有 True 位置的元素，自动展平为一维数组
# print(f"b 中大于2的元素有：{b[b>2]}")

# # 创建示例数组
# arr = np.array([10, 20, 30, 40, 50])
# # 创建布尔条件（大于30的元素）
# condition = arr > 30  # 结果：[False, False, False, True, True]
# print(condition)
# # 应用布尔索引
# filtered_arr = arr[condition]  # 结果：[40, 50]
# print(filtered_arr)

# from numpy import array
# x = array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print(f"前两行的元素为：\n {x[[0, 1]]}")  # 或 x[0:2, :]，取行的所有元素，对应column的:（冒号）可以省略，取列所有元素:不能省略
# print(f"x[0][0] 和 x[1][1] 为：{x[[0, 1], [0, 1]]}")
# print("以下两种格式时一样的：")
# print(x[[0, 1]][[0, 1],:])
# print(x[0:2, 0:2])

"""
4.数组的修改
（1）单个元素修改：x[row,col] = value
（2）删除：delete(arr, obj, axis=0或1)  
    0表示行（不能省略），1表示列，若省略axis则删除索引为obj的元素（第一行从左到右，第二行）
（3）增加：append(arr, value, axis)，value要传入数组，传入列表[[7, 8]]会有警告
    np.array([[7, 8]])(shape（1x2）数组)，np.array([7,8])(shape（2，）数组)，
    添加列也是，都要两个中括号（[]）,且维度要保持一致
"""

# x = np.array([[1, 2], [3, 4], [5, 6]])
# x[2, 0] = -1  # 修改第3行第1列元素为-1
# y = np.delete(x, 2, axis=0)  # 删除第3行
# z = np.delete(x, 0, axis=1)  # 删除第1列
# t1 = np.append(x, np.array([[7, 8]]), axis=0)  # 增加一行
# print(t1)
# t2 = np.append(x, np.array([[9], [10], [11]]), axis=1)  # 增加一列
# print(t2)

"""
5.数组的变形：改变维度，元素总数不变
    "reshape":      {"功能": "改变数组的维度",}                                        "调用方式": "a.reshape(m,n,s) 把 a 变成 m 个 n 行 s 列的数组，返回的是视图，a 本身不变"
    "resize":       {"功能": "改变数组的维度"}                                         "调用方式": "a.resize(m,n,s) 把 a 变成 m 个 n 行 s 列的数组，没有返回、改变的是 a 数组"
    "C_":           {"功能": "列组合"}                                               "调用方式": "C_[a,b]，构造分块数组 [a,b]"
    "r_":           {"功能": "行组合"}                                               "调用方式": "r_[a,b]，构造分块数组[: ]"
    "ravel":        {"功能": "水平展开数组"}                                          "调用方式": "a.ravel() 返回的是 a 的视图"
    "flatten":      {"功能": "水平展开数组"}                                          "调用方式": "a.flatten() 返回的是真实数组，需要分配新的内存空间"
    "hstack":       {"功能": "数组横向组合"}                                          "调用方式": "hstack((a,b))，输入参数为元组 (a,b)"
    "vstack":       {"功能": "数组纵向组合"}                                          "调用方式": "vstack((a,b))"
    "concatenate":  {"功能": "数组横向或纵向组合"}                                     "调用方式": "concatenate((a, b), axis=1)，同 hstack；concatenate((a, b), axis=0)，同 vstack"
    "dstack":       {"功能": "深度组合，如在一幅图像数据的二维数组上组合另一幅图像数据"}      "调用方式": "dstack((a,b))"
    "hsplit":       {"功能": "数组横向分割"}                                          "调用方式": "hsplit(a,n) 把 a 平均分成 n 个列数组"
    "vsplit":       {"功能": "数组纵向分割"}                                          "调用方式": "vsplit(a,m) 把 a 平均分成 m 个行数组"
    "split":        {"功能": "数组横向或纵向分割"}                                     "调用方式": "split(a,n,axis=1) 同 hsplit(a,n)；split(a,n,axis=0) 同 vsplit(a,n)"
    "dsplit":       {"功能": "沿深度方向分割数组"}                                     "调用方式": "dsplit(a,n) 沿深度方向平均分成 n 个数组"
    "tolist":       {"功能": "把数组转换成 Python 列表"}                               "调用方式": "a.tolist()"
"""

# 数组变形
# a = np.arange(4)
# print(a, '\n', a.reshape(2, 2))  # reshape有返回值，reshape也可用于降维
# b = np.arange(4).reshape(2, 2)
# print(b, '\n', b.resize(4,))  # reshape 无返回值

# 数组组合
# a = np.arange(4).reshape(2, 2)
# b = np.arange(4, 8).reshape(2, 2)
# c1 = np.vstack([a, b])  # 垂直方向组合
# c2 = np.r_[a, b]  # 垂直方向组合
# d1 = np.hstack([a,b])  # 水平方向组合
# d2 = np.c_[a, b]  # 水平方向组合
# print(a, '\n\n', b, '\n\n', c1, '\n\n', c2, '\n\n', d1, '\n\n', d2, '\n\n')

# 数组分割
a = np.arange(4).reshape(2, 2)
b = np.hsplit(a, 2)  # 横向分割（分成左右），把a平均分成两个列数组
c = np.vsplit(a, 2)  # 纵向分割（分成上下），把a平均分成两个行数组

print(a, '\n\n', b[0], '\n\n', b[1], '\n\n', c[0], '\n\n', c[1])
