# ============= 函数 ================

# 函数：内置函数、第三方模块函数和自定义函数，函数通常前后空两行，形参和实参最好不要同名，不然会有弱警告

# 1.自定义函数
# 语法：
"""
def functionName(formalParameters):
    functionBody
"""
# （1）functionName 函数名，可以是任何有效的Python标识符
# （2）formalParameters 形式参数（简称形参），在调用函数时通过给形参赋值来传递调用值
#     形参可以有零个、一个或多个，多个形参时形参之间用逗号（,）分割；小括号必不可少，没有形参时也要有小括号
# （3）functionBody 函数体，是函数被调用时执行的一组语句，可以有一个或多个语句组成，多个语句的函数体一定要！！！注意缩进！！！
#     函数通常用三个单引号 '''...''' 来注释说明函数；函数体内容不可为空，可用 pass 来表示空语句
#     在函数调用时，函数名后面括号中的变量名称成为实际参数（简称实参 actual parameters ）
#       定义函数时主义：
#           A 函数定义必须放在函数调用之前，否则编译器会由于找不到该函数而报错
#           B 返回值不是必须的，如果没有 return 语句，则默认返回 None

# 定义阶乘函数求5！


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# print(factorial(0))


def factorial2(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r
# print(factorial2(0))

# 2.自定义函数的四种参数：位置参数、默认参数、可变参数和关键字参数，四种参数可以混用，但混用时必须按前面说的顺序
# （1）位置参数：实参按位置顺序传递给相应位置的形参，实参数目应与形参数目相同
# （2）默认参数：指在构造函数时已经给某些形参赋予初值，当调用函数时，这样的参数不用传值，默认参数必须指向不变对象
# 例，计算 1 到 n 的 p 次方和


def square_sum(n, p=2):
    result = sum([i**p for i in range(1, n+1)])
    return n, p, result


# # 推荐该版本输出
# n, p, result = square_sum(10)
# print(f"1 到 {n} 的{p} 次方的和为：{result}")
# # 低版本输出
# print("1 到 %d 的 %d 次方和为：%d" % square_sum(10, 3))

# （3）可变参数：如果不确定该给自定义函数传入多少个参数值时，需要使用可变参数,*args(arguments)


def add(a, b):
    return a, b, sum([a, b])


# a1, b1, s1 = add(10, 23)
# print(f"{a1}和{b1}的和为：{s1}")


# args 前加 * ，这样的参数就是可变参数，该参数可以接纳任意多个实参
# 原因：该类型的参数将输入的实参进行了捆绑，并组装到元组中，就是自定义函数print(args)的效果，无法将具体的实参指定给具体的形参
def add1(*args):
    print(args, end='')
    s = sum(args)
    return s


# s1 = add1(10, 12, 6, 8)
# print(f"的和为{s1}")

# （4）关键字参数(kwargs)：可以把带参数名的参数值组装到一个 字典 中，键就是具体的实参名，值就是传入的参数值


# name, age 为位置参数，kw 为关键字参数，关键字参数会将用户任意填写的组装为字典
def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'others:', kwargs)


# person('Michael', 30)
# person('Bob', 35, city='beijing')
# person('Adam', 45, gender='M', job='Engineer')
# person('N', 18, 18, 'doctor') # 转化不了键值对

# 3.参数传递：传值调用和传址调用
# （1）传值（call by value）调用：将自变量的值逐个赋值给形参，在函数中实参的任何改变都不影响原来自变量的值
# （2）传址（pass by reference）调用：在调用函数时，所传递的参数值时变量的内存地址，实参的变动会影响原来自变量的值
# 当传递的数据是不可改变对象（如数值、字符串）时，在传递参数时，会先复制一份再传递
# 当传递的数据是可变对象（如；列表）时，在传递参数值，会直接以内存地质来传递，在函数中修改了，因为是同一个地址，所以自变量也会改变


# 传值调用
def fun(a, b):
    a, b = b, a
    print(f"函数内交换位置后：a = {a}， b = {b}")


# a1, b1 = 10, 15
# print(f"调用函数前的数值：a = {a1}, b = {b1}")
# print("-----------------------------------")
# fun(a1, b1)
# print("-----------------------------------")
# print(f"调用函数后的数值：a = {a1}, b = {b1}")

# 传址调用


def change(data):
    data[0], data[1] = data[1], data[0]
    print(f"函数内交换位置后：", end='')
    for j in range(2):
        print(f"data[{j}] = {data[j]}", end='\t')


# data1 = [16, 25]
# print(f"原始数据为：", end='')
# for j1 in range(2):
#     print(f"data[{j1}] = {data1[j1]}", end='\t')
# print(f"\n--------------------------------------------")
# change(data1)
# print(f"\n--------------------------------------------")
# print(f"排序后的数据为：", end='')
# for j1 in range(2):
#     print(f"data[{j1}] = {data1[j1]}", end='\t')

# (3)参数传递的符合数据解包
# 传递参数时，可以使用列表、元组、集合、字典及其他可迭代对象（range）作为实参，并在实参名称前加一个 * 号，python 解释器会自动解包，然后传递给多个单变量形参
# 若使用字典作为实参，则默认使用字典的键，如果需要将键值对作为参数则需要使用 items() 方法；如果需要将字典的值作为参数则需要调用字典的 values() 方法
# 最后，要保证实参中元素个数与形参个数相等，否则会出现错误


def fun1(a, b, c):
    print(f"the summary of three number:{a+b+c}")


# seq = [1, 2, 3]
# print(fun1(*seq))
# tup = (1, 2, 3)
# print(fun1(*tup))
# dic = {1: 'a', 2: 'b', 3: 'c'}
# print(fun1(*dic))
# # 转换成元组进行“+”运算后变成了一个元组
# print(fun1(*dic.items()))
# # 键值对的值转换成字符串进行“+”运算
# print(fun1(*dic.values()))
# set1 = {1, 2, 3}
# print(fun1(*set1))

"""
4.两个特殊函数：
（1）匿名函数：没有函数名的简单函数，只可以包含一个表达式，不允许包含其他复杂语句，表达式的结果是函数的返回值
（2）递归函数：直接或间接调用函数本身的函数，
A 函数a中又调用函数a本身，则称函数a为直接递归，程序设计常用简介递归
B 如果函数a中先调用函数b，函数b又调用函数a，则称函数a为间接递归
注：递归程序要点：a 找出正确的递归算法(写成函数形式p(n)=...p(n-1)，定义域即递归结束条件)——基础 b 确定结束递归算法的条件，这是决定递归程序能否正常结束的的关键
递归算法的优缺点：
优点：递归算法使程序简介、紧凑，很容易解决一些用非递归算法很难解决的问题；
缺点：牺牲存储空间。每次调用递归都要保存相关的参数和变量；反复调用递归函数会增加时间开销
"""

# f = lambda a, b=2, c=5: a-b+c
# print(f"f = {f(10, 20)}")
# print(f"f = {f(10, 20, 30)}")
# print(f"f = {f(c=20, a=10, b=30)}") # 使用关键字实参（形参名=值）

# 先定义函数 1 到 n 的 m 次幂，然后调用该函数求 s = k（k：1~100）+k^2（k：1~50）+k^-1（k：1~10）
# f1 = lambda n, m: sum([i**m for i in range(1, n+1)])
# s = f1(100,1) + f1(50, 2) + f1(10, -1)
# print(f"s = {s}")

# 输入 n ，求 n！(用递归写)


def fac(n1):
    if n1 < 1:
        return 1
    else:
        return n1*fac(n1-1)


# n2 = int(input("请输入n的值："))
# print(f"{n2}! = {fac(n2)}")


def fun2(x1, n3):
    if n3 == 1:
        return x1
    else:
        return x1*(1-fun2(x1, n3-1))


# x, n = eval(input("请输入参数x和n:"))
# print(f"p({x},{n}) = {fun2(x, n)}")

def f(x):
    return x**2+x+1


def g(x):
    return x**3+2*x+1


def h(x):
    return 1/f(x)
