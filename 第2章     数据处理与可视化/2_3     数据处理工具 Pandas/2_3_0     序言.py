# ================= 序言 ====================

"""
Pandas (panel data,面板数据) 是在 NUmPy 的基础上开发的，是 Python 最清大的数据分析和探索工具之一，
作为金融数据分析工具而开发，支持类似于SQL语句的模型，支持时间序列分析

该工具库可以帮助数据分析师轻松地解决数据的预处理问题，
如数据类型的转换、缺失值的处理、描述性统计分析、数据的汇总等

Pandas 中最重要的是 Series 和 DataFrame 子类，导入方法如下
from pandas import Series
from pandas import DataFrame

Pandas 可以进行统计特征计算
包括均值、方差、分位数、相关系数和协方差等，这些统计特征能反应数据的整体分布
（1）mean()：计算样本数据平均值
（2）std()：计算样本数据标准差   （standard deviation)
（3）cov()：计算样本数据的协方差矩阵   (covariance)
（4）var()：计算样本的方差   (variance)
（5）describe()：描述样本数据的情况
    包括非 NaN 数据个数，均值，标准差、最小值、最大值以及样本的 25%，50%，75% 分位数
"""

# 查看 Pandas 库中包含的函数
import pandas as pd
print(dir(pd))
