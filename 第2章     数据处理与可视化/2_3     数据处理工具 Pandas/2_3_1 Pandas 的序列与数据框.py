# ================ Pandas 的序列与数据框 ====================

"""
Pandas 数据结构的范围可以从一维到三维
  Series（序列）是一维的；DataFrame（数据框）是二维的；pandel（面板）是三维甚至更高维的数据结构
  通常 Series 和 DataFrame 可以用于大多数统计、工程、财务和社会科学的场景中

Series 是一个带标签的一维数组，可以用于存储任意类型数据（整形、浮点型、字符串和其他有效的 python 对象），它的行标签乘坐 index

DataFrame 是一个带标签的二维数组，有行和列。列可以有多个类型
    DataFrame 可以看作二维结构的数组，例如，电子表格和数据库表格
    DataFrame 也可以看作包含多个不同类型的 Series 的集合

Panel：在统计学和经济学中，Panel data（面板数据）指多维数据，这个多维数据包括不同时间的不同测量结果
       该数据结构的名称来源于其概念。与 Series 和 DataFrame 相比，面板数据是不太常用的一种数据结构
"""

"""
1.序列
构造一个序列可以使用如下方式实现：
（1）通过同类型的列表或元组创建
（2）通过字典创建
（3）通过 NumPy 中的一维数组创建
（4）通过数据框中的某一列创建

通过下面实验可以看出，序列有两列构成
    数组 构成的序列，第一列是序列的索引（行号），自动从 0 开始，第二列是序列的实际值
    字典 构成的序列，第一列是具体的行名称（index），对应字典中的键，第二列是序列的实际值，对应字典中的值
    Series(data, index=['', '', ...])
序列与一维数组具有高度的相似性，获取一维数组元素的所有方法都可以应用在序列上，而且数组的数学和统计函数也可以应用到序列对象上，不同的是，序列会有更多的其他处理方法
"""

# import pandas as pd
# import numpy as np
# s1 = pd.Series(np.array([10.5, 20.5, 30.5]))  # 数组构造序列
# s2 = pd.Series({"北京": 10.5, "上海": 20.5, "广东": 30.5})  # 字典构造序列
# s3 = pd.Series([10.5, 20.5, 30.5], index=['b', 'c', 'd'])  # 给出行标签命名
# print(s1)
# print("--------------------")
# print(s2)
# print("--------------------")
# print(s3)

# 构造序列
# import pandas as pd
# import numpy as np
# s = pd.Series([10.5, 20.5, 98], index=['a', 'b', 'c'])
# a = s['b']
# b1 = np.mean(s)
# b2 = s.mean()  # 通过数列方法求平均值，面向对象
# print(b1, b2)

"""
2.数据框
DataFrame 是由行和列构成的二维数据结构。虽然索引和列名称是可选的，但是最好把它们设置一下
    索引可以看成是行标签，列名称可以看成是列标签
DataFrame(data=二维数据[, index=行索引[, columns=列索引[, dtype=数据类型]]])
以上为数据框的创建，其中，data 可以是二维 NumPy 数组；data 如果是字典时，其值为一维数组，键维数据框的列名
"""

# 构造数据框
# import pandas as pd
# import numpy as np
# a = np.arange(1, 7).reshape(3, 2)
# df1 = pd.DataFrame(a)  # 列名行名自动从行开始
# df2 = pd.DataFrame(a, index=['a', 'b', 'c'], columns=['x1', 'x2'])  # 列名行名按定义
# df3 = pd.DataFrame({'x1': a[:, 0], 'x2': a[:, 1]})  # 键为列名，行名自动从 0 开始
# print(df1)
# print("------------------")
# print(df2)
# print("------------------")
# print(df3)
