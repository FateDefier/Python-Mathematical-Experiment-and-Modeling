# =================== 泰勒级数与数值导数 ========================

"""
大多数实际问题是无法求符号解的，只能求数值解，即近似解．
本节介绍调用SciPy 工具库求数值解，对其中的一些问题我们自己设计 Python 程序．
"""

"""
1.泰勒级数
"""

# 画出 sin(x) 及它在 0 点处的 1，3，5 阶泰勒展开式在 x 属于[-2*pi, 2*pi]
# 编写函数 mysin 求 f(x) = sin(x) 的近似值；调用自定义函数 mysin 画出泰勒展开式的图形
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def fac(n):
#     """
#     求阶乘,等价于 return (1 if n<1 else n*fac(n-1))
#     """
#     result = 1
#     if n > 1:
#         result = n*fac(n-1)
#     return result
#
#
# def item(k, x1):
#     """
#     sin(x)泰勒展开式中的一项
#     """
#     return (-1)**k*x1**(2*k+1)/fac(2*k+1)
#
#
# def mysin(n, x2):
#     """
#     mysin(x)
#     """
#     return 0 if n < 0 else mysin(n-1, x2)+item(n, x2)
#
#
# x = np.linspace(-2*np.pi, 2*np.pi, 101)
# plt.plot(x, np.sin(x), '*-')
# style = ['v-', 'H--', '-.', 'm-', 'y-']
# for i in [1, 2, 3, 4, 5]:
#     plt.plot(x, mysin(2*i-1, x), style[i-1])
# plt.legend(['sin', 'n=1', 'n=3', 'n=5', 'n=7', 'n=9'])
# plt.savefig("sin.png", dpi=500)
# plt.show()

"""
2.数值导数
可通过泰勒级数移项并舍弃高阶无穷小，近似计算函数导数
（1）一阶导数
一阶精度：f(x+deta)展开移项
二阶精度：f(x+h)和f(x+h)分别展开做减法得到
（2）二阶导数
"""

"""
模型建立
下面以运动学中的问题来展示数值导数的应用．
例 3.17 甲、乙、丙、丁 4 个人分别位于起始位置 (-200,200), (200,200),
(200,-200) 以及 (-200,-200) 处（单位： m), 并且以恒定的速率 lm/s 行走．在行
走过程中， 甲始终朝向乙的当前位置；同样，乙朝向丙、丙朝向丁、丁朝向甲．试绘
制 4 人行走过程的近似轨迹．
分析：在运动学中， 速度是位移相对千时间的导数， 即
v(t) = d(r(t)) /dt ,
因此， 在一段很短的时间 D>.t 内，近似地有
r(t + \deta t) 约等于  r(t) + v(t) • \deta t
成立又由千位移、速度均是矢量， 因此在xOy 平面内， 又有
rx(t + \deta t) 约等于 rx(t) + v(t) · \deta t · cos\theta(t),
ry(t + \deta t) 约等于 ry(t) + v(t) · \deta t • sin\theta(t),
其中， theta(t) 是 t 时刻与 x 轴正向的夹角
以两个二维数组xy, xyn 分别存储 4 个人的当前位置和下一时刻的位置， 具体地说，
第 i 个人的当前位置为 xy[i]， 下一时刻的位置为 xyn[i], 其中 i 取 0, 1,2,3 时分别对应甲、乙、丙、丁．
下面语句
j = (i+1)%4
dxy = xy [j] -xy [i]
dd = dxy/ng.norm(dxy) ＃单位化向量
就完成了对夹角余弦值、正弦值的计算．
二维数组Txy 存放 4个人的所有位置信息，其中 Txy[i] 存放第 t 个人所有时刻的位置信息
"""

# import numpy as np
# import numpy.linalg as ng
# import matplotlib.pyplot as plt
# N = 4
# v = 1.0
# d = 200.0
# time = 400.0
# divs = 201
# xy = np.array([[-d, d], [d, d], [d, -d], [-d, -d]])
# T = np.linspace(0, time, divs)
# dt = T[1] - T[0]
# xyn = np.empty((4, 2))
# Txy = xy
# for n in range(1, len(T)):  # 遍历时间
#     for i in [0, 1, 2, 3]:  # 遍历 4 个点
#         # 下一个顶点索引（循环），不直接用 i+1 ，因为当 i=3 时，j=i+1=4,但实际上没有第五个人，数组越界
#         j = (i+1) % 4
#         # 每个点经过时间 dt 后的位置减 dt 前的位置，可以确定速度的方向，(\deta x)/dt = v
#         dxy = xy[j]-xy[i]
#         dd = dxy/ng.norm(dxy)  # 单位化向量
#         xyn[i] = xy[i]+v*dt*dd  # 计算下一步的位置
#     # Txy 用于存储每个点（共4个）在每个时间（共201个）的位置，为 (4, 2*201) 数组(横向拼接，第一个 dt 后为 4x4)
#     Txy = np.c_[Txy, xyn]  # c_是 NumPy 的一个索引对象，用于沿列方向的拼接（横向拼接）（axis=1）
#     # 更新 xy ,保证下一个 dt 时间时运动前后坐标只差一个 dt
#     print(Txy)
#     xy = xyn.copy()  # copy():numpy函数，把 xyn 赋值给 xy，但二者内存地址不同
# print(np.shape(Txy))
# for i in range(N):
#     # 每个点的轨迹单独画，::2（0:end:2） 表示切片操作，取第奇数列（x 坐标，索引为偶数），1::2(1:end:2)偶数列（y 坐标）
#     plt.plot(Txy[i, ::2], Txy[i, 1::2])
# plt.savefig("value_derivatives.png", dpi=500)
# plt.show()
