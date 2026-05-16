# ============== SymPy 做符号函数画图 =============================

"""
用 SymPy 做符号函数画图很方便
"""

"""
1.二维曲线画图
plot 的基本使用格式为
    plot(表达式, 变量取值范围, 属性 = 属性值)
多重绘制的使用格式为
    plot(表达式1, 表达式2, 变量取值范围, 属性 = 属性值)
    或者
    plot((表达式1, 变量取值范围1), (表达式2, 变量取值范围2))
"""

#  在同一图形界面上画出 y1 = 2sinx, x 属于 ［-6，6］；y2 ＝ cos (x+pi/4), X属于[-5, 5]
# from sympy.plotting import plot
# from sympy.abc import x, pi  # 引进符号常量 x 及常量 pi
# from sympy.functions import sin, cos
# plot((2*sin(x), (x, -6, 6)), (cos(x+pi/4), (x, -5, 5)))

"""
2.三维曲面绘图
| 参数             | 类型/取值      | 说明                                |
| -------------- | ---------- | --------------------------------- |
| expr           | 表达式        | 仅含两个自由符号的数学表达式                    |
| (x,xmin,xmax)  | 三元组        | 变量x的绘图区间                          |
| (y,ymin,ymax)  | 三元组        | 变量y的绘图区间                          |
| label          | 字符串        | 图例标签                              |
| n1             | 正整数        | x方向采样点数                           |
| n2             | 正整数        | y方向采样点数                           |
| surface\_color | 字符串/函数/三元组 | 曲面颜色或颜色映射函数                       |
| colorbar       | bool       | 是否显示颜色条                           |
| opacity        | 0-1浮点数     | 曲面透明度                             |
| wireframe      | bool       | 是否绘制网格线                           |
| cmap           | 字符串        | Matplotlib色图名称                    |
| title          | 字符串        | 图标题                               |
| xlabel         | 字符串        | x轴标签                              |
| ylabel         | 字符串        | y轴标签                              |
| zlabel         | 字符串        | z轴标签                              |
| aspect\_ratio  | 字符串        | 坐标轴比例，'auto'或'equal'              |
| backend        | 字符串        | 绘图后端，'matplotlib'/'plotly'/'k3d'等 |
| show           | bool       | 是否立即显示图形                          |
| legend         | bool       | 是否显示图例                            |

"""

#  画出三维曲面 z = sin(sqrt(x^2+y^2))
# import matplotlib.pyplot as plt
# from sympy.plotting import plot3d
# from sympy.abc import x, y
# from sympy import sin, sqrt
# plt.rc('font', size=16)
# plt.rc('text', usetex=True)
# plot3d(sin(sqrt(x**2 + y**2)), (x, -10, 10), (y, -10, 10), xlabel='$x$', ylabel='$y$')

"""
3.隐函数画图
| 参数          | 类型/取值      | 说明                         |
| ----------- | ---------- | -------------------------- |
| expr        | 表达式/等式/不等式 | 待绘制的隐式关系，如 Eq(x**2+y**2,1) |
| x\_var      | 符号或三元组     | x轴变量或 (x, xmin, xmax)      |
| y\_var      | 符号或三元组     | y轴变量或 (y, ymin, ymax)      |
| adaptive    | bool       | 是否使用自适应网格；默认 True          |
| depth       | 0‒4 整数     | 自适应递归深度；默认 0               |
| n           | 正整数        | 非自适应时的网格点数；默认 300          |
| line\_color | 字符串或RGB    | 曲线颜色；默认 'blue'             |
| title       | 字符串        | 图标题                        |
| xlabel      | 字符串        | x轴标签                       |
| ylabel      | 字符串        | y轴标签                       |
| show        | bool       | 是否立即显示；默认 True             |
| Eq          | 类          | 用于构造等式 Eq(lhs, rhs)        |

"""

# 绘制隐函数(x-1)^2 + (y-2)^3 - 4 = 0 的图形
# import matplotlib.pyplot as plt
# from sympy.abc import x, y
# # 等价于(implicit 含蓄的)
# # from sympy.plotting.plot_implicit import plot_implicit as pt
# # from sympy import Eq
# from sympy import plot_implicit as pt, Eq
# plt.rc('font', size=16)
# plt.rc('text', usetex=True)
# pt(Eq((x-1)**2 + (y-2)**3, 4), (x, -6, 6), (y, -2, 4), xlabel='$x$', ylabel='$y$')

# 使用匿名函数（lambda 函数）
from sympy import plot_implicit as pt
from sympy.abc import x, y


# def implicit(expr1):
#     return pt(expr1)
#
#
# ezplot = (x-1)**2+(y-2)**3-4
# implicit(ezplot)
# 等价与
ezplot = lambda expr: pt(expr)
ezplot((x-1)**2+(y-2)**3-4)
