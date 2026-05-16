# =============== 导入模块 ===================


# 从function导入时会执行function的所有代码在该文件中输出，故function内只写函数
# from function import factorial
# print(factorial(5))

# 模块：公共类、函数可以放在独立的文件中，这样其他多个程序都可以使用，而不必把这些公共类、函数等在每个程序中复制一份，这样独立的文件就叫模块
# 标准库模块（部分）：
# time，datetime ：时间相关模块
# random ：随机数模块
# os ：操作系统交互
# sys ：对python解释器相关操作
# math ：数学计算

# 安装的库
# NumPy：科学计算和数据分析的基础库
# SciPy：NumPy 基础上的科学计算库
# SymPy：符号计算库
# Pandas：NumPy 基础上的数据分析库
# Matplotlib：数据可视化库
# Scikit-learn：机器学习库
# Statsmodels：SciPy 统计函数的补充库
# NetworkX：图论和复杂网络库
# cvxpy：凸优化库
# TensorFlow：深度学习库
# NLTK：自然语言看
# python-louvain：社交网络挖掘的社区发现算法库
# PIL：数字图像处理库
# OpenCV：计算机视觉库

# 查看所有模块，pycharm的python控制台输入
# help("modules")

# 查看 os 模块的所有函数,选中import os按Ctrl+B快捷键会出现os.py文件或在控制台输入下列代码
# import os;dir(os)

# 导入模块的 4 种方式
# 1.import 模块名 [as 你命名的名字]（[]可加可不加）

# import numpy as np
# # 导入numpy库下linalg（线性代数，liner algebra）
# import numpy.linalg as LA
# a = np.linspace(0, 10, 5)
# print(a)
# b = LA.norm(a)  # 求a的模
# print(f"a的长度为{b}")
# 导入多个模块又逗号分隔
# import time, random

# 2.from 模块名 import 对象名 [as 别名]
# 导入明确的的对象，且为导入对象确定一个别名，可见超查询次数，提高访问速度；同时，可减少代码量，因为不需要模块名作为前缀

# random时python基础库的模块，numpy.random是numpy库的random模块
# 尽量使用numpy库中的函数，可以对向量进行计算，基础库random只能对标量进行运算
# from numpy import random as rd
# from math import sin, cos
# from random import randint
# a = rd.randint(0, 10, (1, 3))  # 产生[0, 10)的3个元素的随机整数数组
# b = randint(0, 10)  # 产生[0, 10]上的一个随机数，不能产生向量
# print(f"sin({b}) = {sin(b)}")
# print(f"cos({b}) = {cos(b)}")

# 3.from 模块名 import *
# 这是第二种用法的极端情况，可以一次导入模块中通过 __all__ 变量指定的所有对象
# 不推荐：一旦多个模块又同名的对象，会导致混乱

# from math import log, exp, sin, pi
# f = lambda n: (1 + log(n) + sin(n)) / (2*pi)
# y = exp(2)
# for n in range(1, 101):
#     y += f(n)
# print(f"y = {y}")

# 查看 NumPy 库的帮助
# help(numpy)  # 先预先加载模块
# help("numpy")  # 控制台输入，不需要预先加载
# help("numpy.random")  # 可以看到numpy.random中所有对象的信息
# dir("numpy.random")  # 只查看numpy.random模块中的函数名

# 可运行查看
# from numpy.random import randint
# help(randint)

# 4.自定义模块的导入
# 用户将多个函数收集在一个脚本文件中，创建一个用户自定义的模块

# 第一种调用模式
# import function as ft
# print(f"{ft.f(1)},\t {ft.g(2) },\t {ft.h(3)}")

# 第二种调用模式
# from function import f, g, h
# print(f"{f(1)} , {g(2) } , {h(3)}")
