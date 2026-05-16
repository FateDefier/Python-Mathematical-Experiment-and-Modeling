# ====================== 数组的运算、通用函数和广播计算 =====================

"""
1.四则运算
2.比较运算
3.ufunc 函数
4.ufunc 函数的广播机制
"""

"""
1.四则运算
（1）加法：运算符号 + ；函数 add
（2）减法：运算符号 - ；函数 substract（subtract 减去）
（3）乘法：运算符号 * ；函数 multiply（乘，繁殖）
（4）除法：运算符号 / ；函数 divide（分，分开）
（5）余数：运算符号 % ；函数 fmod
（6）整除：运算符号 // ；函数 np.modf(a/b)[1]，odf可以返回小数部分和整数部分，而整数部分就是要取的整数值
（7）幂次：运算符号 ** ；函数 power
"""

# import numpy as np
# a = np.arange(10, 15)
# b = np.arange(5, 10)
# c = a + b  # 对应元素相加
# d = a * b  # 对应元素相乘
# e = np.fmod(a, b)
# f = np.power(a, b)  # 14^9超过32位整数，溢出，显示错误的数
# e1 = np.modf(a/b)[0]  # 对应元素相除，小数部分
# e2 = np.modf(a/b)[1]  # 对应元素相除，整数部分
# print(a, '\n\n', b, '\n\n', c, '\n\n', d, '\n\n', e, '\n\n', f, '\n\n', e1, '\n\n', e2)

"""
2.比较运算：返回布尔（bool）类型（True、False）
大于：     符号 > ；函数 greater(a, b)   判断 a 的元素是够大于 b
大于等于：  符号 >= ；函数 greater_equal(a, b)
小于：      符号 < ；函数 less(a, b)
小于等于：   符号 <= ；函数 less_equal(a, b)
等于：      符号 == ；函数 equal(a, b)
不等于：    符号 != ；函数 not_equal(a, b)
多维数组通过 bool 索引返回的是一维数组
np.where 返回的数组保持原来的形状
"""

# import numpy as np
# a = np.array([[3, 4, 9], [12, 15, 1]])
# b = np.array([[2, 6, 3], [7, 8, 12]])
# print(a[a > b], '\n')
# print(a[a > 10], '\n')
# print(np.where(a > 10, -1, a), '\n')  # a 中大于10的元素改为-1
# print(np.where(a > 10, -1, 0), '\n')  # a 中大于10的元素改为-1，否则为0（<= 10 的元素改为0）

"""
3.ufunc 函数
（1）ufunc 函数全称 通用函数（universal function），是一种能对数组中的元素逐个进行操作的函数
（2）ufunc 函数是针对数组进行操作的，且都以 NumPy 数组作为输出
（3）使用 NumPy 库的 ufunc 函数比使用 math 库中的函数效率高很多
（4）NumPy 支持的通用函数：四则运算、求模、取绝对值、幂函数、指数函数、三角函数、位运算、比较运算、逻辑运算
"""

# # ufunc 函数效率示例
# import numpy as np
# import time
# import math
# x = [i * 0.01 for i in range(1000000)]
# # time.time()返回的是自 1970 年 1 月 1 日 00:00:00 UTC（协调世界时） 起经过的 秒数（浮点数），也称为 Unix 时间戳
# start = time.time()
# print(time.time())
# # enumerate(iterable, start=0)，iterable可遍历对象（list，tuple，dic，str等），开始的索引，默认为0，这里x为列表
# for (i, t) in enumerate(x):
#     x[i] = math.sin(t)
# print(time.time())
# print(f"math.sin:{time.time()-start}")
# y = np.array([i * 0.01 for i in range(1000000)])
# start = time.time()
# y = np.sin(y)  # 0.13966846466064453不固定
# print(f"numpy.sin:{time.time()-start}")  # 0.006000041961669922不固定

"""
4.ufunc 函数的广播机制
（1）广播（broadcasting）：指不同形状的数组之间执行算术运算的方式
（2）当使用 ufunc 函数进行数组计算是，ufunc 函数会对两个数组的对应元素进行计算（前提：两个数组维度相同）
（3）如果两个元素的维度不相同，则NumPy会实行广播机制
（4）数组的广播功能是有规则的，如果不满足这些规则，运算时就会出错
（5）数组的主要广播规则：
A 各输入数组的维度可以不相等，但必须确保从右到左的对应维度值相等
B 如果对应的维度值不等，就必须保证其中一个为1
"""

# import numpy as np
# # [0, 10]被重塑为(n, 1)，即列向量（1列），-1表示行数自动计算
# a = np.arange(0, 20, 10).reshape(-1, 1)
# b = np.arange(0, 3)
# print(a, '\n\n', b, '\n\n')
# # 广播：a、b两个数组形状不同，a(2,1),b(3,)：[0, 1, 2]（一维数组list，没有行列的区分）
# # 首先，b被扩展为b(1，3)：[[0, 1, 2]]（向量，二维数组）
# # 为满足加法计算，a被扩展为[[0, 0, 0], [10, 10, 10]](在列方向上复制 3 次)，b被扩展为[[0, 1, 2],[0, 1, 2](在行方向上复制 2 次)，最终均为2x3
# print(a + b)
