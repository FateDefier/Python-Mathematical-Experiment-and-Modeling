# ================== 高等数学问题的符号解（通解） ===================

"""
SymPy 包括许多功能，从基本的符号算术到多项式、微积分、求解方程、离散数学和统计等
它主要处理三种类型的数据：整型数据、实数和有理数．
有理数包括两个部分：分子和分母， 可以用 Ration(定额) 类定义有理数．
本节通过示例程序来理解 SymPy 的概念及应用．
"""

"""
1.求极限
limit(表达式, x, 极限)
"""

# 求 lim(x-0)sin(x)/x, lim(x-正无穷)(1+1/x)**x
# from sympy import *
# x = symbols('x')
# print(limit(sin(x)/x, x, 0))
# print(limit(pow(1+1/x, x), x, oo))  # 两个“ o ”表示正无穷

"""
2.求导数
diff(函数, 求导的自变量, 求导的阶数)
"""

# z = sin(x) + x**2*e**y，求 z 对 x 的二阶偏导、z 对 y 的一阶偏导
# from sympy import *
# x, y = symbols('x y')  # 定义两个符号变量
# z = sin(x) + x**2*exp(y)  # 构造符号表达式
# print(f"z 关于 x 的二阶偏导数为：{diff(z, x, 2)}")
# print(f"z 关于 y 的一阶偏导数为：{diff(z, y, 1)}")

"""
3.级数求和
summation(表达式, (变量, start, step))
factor(符号表达式)  因式分解
"""

# sum(k:1-n)k**2=n*(n+1)*(2n-1)/6, sum(k:1-oo)1/k**2= pi**2/6
# from sympy import *
# k, n = symbols('k n')
# print(summation(k**2, (k, 1, n)))
# print(factor(summation(k**2, (k, 1, n))))  # 把计算结果因式分解
# print(summation(1/k**2, (k, 1, oo)))

"""
4.泰勒展开
expr.series(x, 0, k) ==
series(表达式y, 自变量x, 展开点0, k)(展开到包含 x**(k-1) 的一项，与高数中展开到 k 阶一致)
默认返回的展开结果里带有 大写 O 余项（例如 O(x**3)），表示高阶无穷小
.removeO() 是 SymPy 表达式对象的一个方法，专门用来“把泰勒展开结果里的大 O 余项删除掉”，返回一个 纯多项式表达式
.removeO() 只影响 Order 对象
"""

# sin(x)在 0 点处的 3，5，7 阶泰勒展开，并在同意图形界面上画出 sin(x) 及它的 3，5，7阶泰勒展开式在区间[0, 2]上的图形
# import matplotlib.pyplot as plt
# from sympy import *
# from sympy.plotting import *
# plt.rc('font', size=16)
# plt.rc('text', usetex=True)
# x = symbols('x')
# y = sin(x)
# for k in range(3, 8, 2):
#     print(y.series(x, 0, k))  # 等价于print(series(y, x, 0, k))
# # removeO() O 是大写的 o
# plot(y, series(y, x, 0, 3).removeO(), series(y, x, 0, 5).removeO(),
#      series(y, x, 0, 7).removeO(), (x, 0, 2), xlabel='$x$', ylabel='$y$')

"""
5.不定积分和定积分
integrate(expr, (x, 积分下限, 积分上限))
"""

# 验证 sin(2x) 在 0-pi 上的定积分=0， sin(x)/x 在 0-oo 的定积分=pi/2
# from sympy import integrate, symbols, sin, pi, oo
# x = symbols('x')
# print(integrate(sin(2*x), (x, 0, pi)))
# print(integrate(sin(x)/x, (x, 0, oo)))
#
# # 求不定积分 4*x**3+3*x**2+2*x+1
# print(integrate(4*x**3+3*x**2+2*x+1, (x, 0, x)))

"""
6.求解代数方程（方程组）的符号解（通解）
将代数方程化简到等号（=）右边为0，左边表达式为expr
# 解单个方程
    solve(expr, 符号变量x)
    roots(expr, 符号变量x)  可以得到根的数量信息（包括根）
# 解方程组
    solve([expr1, expr2, ...], [符号变量x, 符号变量y, ...])
    可能返回多组解
# 求驻点
    solve(diff(expr, x), x)
expr.subs(x, 1)  # 带入 x=1 求解
expr.subs({x: 3, y: 4})  # 带入两个值求解 
"""

# 求 x**3 = 1, (x-2)**2*(x-3)**3 = 0
# from sympy import *
# x = symbols('x')
# print(solve(x**3-1, x))
# print(solve((x-2)**2*(x-3)**3))
# print(roots((x-2)**2*(x-3)**3, x))

# 求解如下方程组
# x^2 + y^2 = 1
# x - y =0
# from sympy import *
# x, y = symbols('x, y')
# s = solve([x**2+y**2-1, x-y], [x, y])
# print(f"方程组的解为：", s)

# 求函数 f(x) = 2*x**3-5*x**2+x 的驻点，并求函数在 [0, 1] 上的最大值
# from sympy import *
# x = symbols('x')
# y = 2*x**3-5*x**2+x
# x0 = solve(diff(y, x), x)  # 求驻点
# print(f"驻点的精确解为：{x0}")
# # 多个阶使用列表推导式取出，使用 n() 将精确解转换为浮点数
# print(f"驻点的浮点数表示为：{[x0[i].n() for i in range(len(x0))]}")
# # 带入区间左右端点和驻点值，比较可得出最大最小值，可以发现
# # 当 x=5/6 - sqrt(19)/6(0.106850176076554)时,y_max=-sqrt(19)/6 - 5*(5/6 - sqrt(19)/6)**2 + 2*(5/6 - sqrt(19)/6)**3 + 5/6(0.0522051838383851)
# y0 = [y.subs(x, 0), y.subs(x, 1), y.subs(x, x0[0]), y.subs(x, x0[1].n())]
# print(f"三个点的函数值分别为：{y0}")

"""
7.求微分方程（方程组）的符号解（通解）
SymPy 库提供了 dsolve 函数求常微分方程的符号解．
在声明时，可以使用 Function() 函数
>>>y•Function('y') 
或者
>>>y=symbols ('y', cls=Function) 
将符号变量声明为函数类型
（1）求通解：在 y 为函数类型后
diff(y(x), x, n)表示 y 的 n 阶导，用于构造表达式expr（等号右边变形为 0 ）
后使用 dsolve(expr, y(x))求解（通解）
（2）初值问题（ics:initial conditions初始条件）
dsolve(expr, y(x), ics={y(x0): 0, diff(y(x), x).subs(x, x0): 1})
"""

# 求下列微分方程的解
# 齐次方程：y''-5y'+6y = 0
# 非齐次方程：y''-5y'+6y = xe^2x
# from sympy import *
# x = symbols('x')
# y = Function('y')  # 或 y = symbols('y', cls=Function)
# eq1 = diff(y(x), x, 2) - 5*diff(y(x), x, 1) + 6*y(x)
# eq2 = diff(y(x), x, 2) - 5*diff(y(x), x, 1) + 6*y(x) - x*exp(2*x)
# aw1 = dsolve(eq1, y(x))
# aw2 = dsolve(eq2, y(x))
# print(f"齐次方程组的解为：{aw1}")
# print(f"非齐次方程组的解为：{aw2}")

# 初值问题
# （1）y''-5y'+6y = 0, y(0)=1,y'(0)=0
# （2）y''-5y'+6y = xe^2x, y(0)=1,y(2)=0
# from sympy import *
# x = symbols('x')
# y = symbols('y', cls=Function)
# eq1 = diff(y(x), x, 2) - 5*diff(y(x), x, 1) + 6*y(x)
# eq2 = diff(y(x), x, 2) - 5*diff(y(x), x, 1) + 6*y(x) - x*exp(2*x)
# aw1 = dsolve(eq1, y(x), ics={y(0): 1, diff(y(x), x).subs(x, 0): 0})
# aw2 = dsolve(eq2, y(x), ics={y(0): 1,y(2): 0})
# print(f"初值问题的解为：{aw1}")
# print(f"边值问题的解为：{aw2}")
