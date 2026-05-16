# ============= 序列实用操作 ===============

# 序列包括string 字符串、list 列表、tuple 元组

# 1.string 字符串的实用操作
# （1）内置函数 str() :将数值数据转化为字符串
# 要接多个字符串，用“ + ”连接
# print('大学''论语''中庸''孟子')

# （2）len()函数 ：获取字符串的长度
# print(len('happy'))

# （3）count()函数：找出该字符串出现的次数,str.count()
# str = "Good morning"
# print(str.count('o'))

# （4）eval()函数：把字符串作为对应的python语句执行，也可用于将字符串转换为数值数据
# x = '12+23'
# print(eval(x))

# （5）find()函数：从字符串中从左到右查找子字符串，返回值为子字符串所在位置的最左端索引，没有找到返回-1,str.find()
#     rfind()方法：从右向左茶盏,str.rfind()
# str = 'abcdefghijk'
# ind = str.find('def')
# print(ind) # 3
# print(str.rfind('def')) # 3

"""
（6）split()函数：将字符串分割成序列，返回分割后的字符串列表，默认分隔符为空格，str.split('分隔符（字母、符号等）')
"""

str1 = "I am a student"
List1 = str1.split()
print(List1)
# str2 = "1,2,3,4"
# List2 = str2.split(',') # 逗号“,”作为分隔符
# print(List2)

"""
（7）strip()函数：去除字符串开头和结尾的空白字符（空格、换行符 \n、制表符 \t、回车符 \r 等），str.strip(),同时strip([chars])可去除指定字符，返回列表
    lstrip()函数：去除字符串左边所有空格(lstrip-left strip)，rstrip()函数：去除字符串右边所有空格(rstrip-right strip)
"""

# str1 = "     I am a student      "
# print(str1.strip())
# print(str1.lstrip())
# print(str1.rstrip())

# join()函数：通过某个字符连接序列中的字符串元素，返回拼接好的字符串（连接的字符也在新的字符串内），split()的逆用法，'分隔符'.join(列表等)
# List = ['I', 'am', 'a', 'student']
# print(List)
# print('a'.join(List))



# 2.几个序列操作函数

# 匿名函数：Python支持单行定义函数，成为 lambda 函数（匿名函数）
# lambda 函数设计一个可以接受任意多个参数并返回单个表达式值的函数
# 函数 f(x,y) = |x| + y^3
# f = lambda x,y: abs(x) + y**3
# print(f"f(-3,2) = {f(-3,2)}")

# （1）map()函数：map(func, iterable, ...)（即map(func,*iteranle)），iterables 可被迭代的对象，... 表示可以有多个可迭代对象（当函数 func 接受多个参数时）
# map()函数接受一个函数 func 和一个列表，把 func 依次作用在列表的每个元素上，得到一个新列表

# pow(x,y)表示x^y,range(6)表示 [0, 1, 2, 3, 4, 5]（不是列表），[2 for b in range (6)]（列表推导式）表示[2, 2, 2, 2, 2, 2],最后表示对range（6）中的每个数平方
# map 函数返回一个 map 对象，这是一个惰性求值的可迭代对象。如果要查看实际的计算结果，可以将其转换为列表
# a = map(pow, range(6),[2 for b in range (6)])
# print(a)
# print(list(a))

# （2）reduce()函数：reduce(function, sequence[, initial]),累加累乘常用
# 其中 function 是有两个参数的函数，sequence(序列) 是元组、列表、字典和字符串等可迭代对象，initial是可选的初始值
# reduce工作过程：在迭代 sequence 的过程中，首先将前两个元素传给函数参数，函数加工后，然后把得到的结果和第三个元素作为两个参数传给函数参数，以此类推
# 如果传入了 initial 初值，首先传的则为 initial 值和第一个元素，累计计算后合并序列最终会得到一个单一的返回值

# 计算5！
# from functools import reduce
# print(reduce(lambda x, y: x*y, range(1, 6)))
# # 计算1+2+……+6
# print(reduce(lambda x, y: x + y, range(7)))
# print(reduce(lambda x, y: x + y, range(6), 6))

# （3）filter 函数：filter(function or None, iterable),filter(过滤器)
# 通过 function 对 iterable 中的元素进行过滤，并返回一个迭代器（iterator），其中是 function 返回 True 的元素
# 如果 function 传入None，则返回所有本身可以判断为 True 的元素
# iterator 对象也无法显示（map也是），输出是用list进行转换

# 筛选并输出 20 以内能被 3 整除的数
# print(filter(lambda x: x%3 == 0, range(1,20)))
# print(list(filter(lambda x: x%3 == 0, range(1,20))))
# print(list(filter(None, range(6))))

# （4）zip()函数：zip(list1, list2, ......)，zip（拉链，压缩）
# 将多个列表对应位置的元素组合为元组(小括号)，并返回包含这些元组的 zip 对象，也需要转换为列表查看

# a = range(1, 5)
# b = range(5, 9)
# c = zip(a, b)
# print(c)
# print(list(c))

# （5）enumerate（）函数：enumerate(a),返回元组（带下标）
# 枚举列表、元组或其他可迭代对象的元素，返回枚举对象，枚举对象中的每个元素是包含下标和元素值的元组。对字符串、字典同样有效

# a = [(1, 5), (2, 6), (3, 7)]
# for b in enumerate(a):
#     print(b)
# # enumerate 用于列表推导式，value接收返回的元组，ind接收返回的索引
# print([value[0] for (ind,value) in enumerate(a)])
# print([value[1] for (ind,value) in enumerate(a)])
# print([value for (ind,value) in enumerate(a)])



# 3.列表推导式和元组生成器推导式
# （1）列表推导式：在一个序列的值上应用一个任意表达式，将其结果收集到一个新的列表中并返回
# 基本形式：[返回值+for+返回值+in+iterable+条件+循环]（可多层嵌套），iterable为可迭代对象

# [0] 是一个列表，[0]*6--列表重复，得到[0, 0, 0, 0, 0, 0]
# B = [[0]*6 for i in range(4)]
# print(B)

# A 使用列表推导式实现嵌套列表的平铺
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # 二位列表遍历两次，第一次遍历 a ，得到 c （依次为3个一维列表），第二次对每个 c 遍历得到 d （a 中的每个元素）

# b = [d for c in a for d in c]
# print(b)

# B 过滤不符合条件的元素
# a = [-1, -2, 6, 8, -10, 3]
# b = [i for i in a if i > 2]
# print(b)

# C 在列表推导式中使用多个循环，实现多序列元素的任意组合，还可结合条件语句过滤特定元素
# c = [(x, y) for x in range(5) if x%2 == 0 for y in range(5) if y%2 ==1]
# print(c)

# (2)元组生成器推导式
# 与列表推导式类似，但元组生成器推导式使用小括号，且其元组生成器推导式结果是生成器对象，需转化为元组,生成器对象智能转化为元组

# g1 = (t(i+1)**2 for i in range(6))
# print(tuple(g1))
# print(list(g1)) # 生成器对象不能转化为列表
# print(set(g1))
