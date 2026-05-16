# =================== 流程控制 =======================

# 流程控制：if,for,while（后面都有冒号）

# if 语句：
# if 条件1：缩进+执行语句1
# elif 条件2：缩进+执行语句2（可多个）
# else：缩进+执行语句3

# a, b = eval(input("请输入两个数："))
# if a>b:
#     print(f"最大数为：{a}")
# else:
#     print(f"最大数为：{b}")

# for 语句：
# for 变量 in 迭代对象：缩进+执行语句1，迭代对象包括列表（list），元组（tuple），字符串（str），范围（range）等，集合（set），字典（dict）非序列但可迭代
# for 循环变量 in range(开始（可省略，默认为0）, 结束, 步长（可省略，默认为1）)：缩进+执行语句2，左闭右开区间
# else：（通常不加入该指令）

# # 计算1+2+...+n（从小到大输出）
# n = eval(input("please input integer:"));sum = 0
# print("从小到大输出：")
# for i in range(1,n+1):
#     sum += i
#     print(i,end=" ")
#     if i<n:
#         print("+",end=" ")
#     else:
#         print("=",end=" ")
# print(sum)
# # 计算1+2+...+n（从大到小输出）
# n = eval(input("please input integer:"));sum = 0
# print("从大到小输出：")
# for i in range(n,0,-1):
#     sum += i
#     print(i,end=" ")
#     if i>1:
#         print("+",end=" ")
#     else:
#         print("=",end=" ")
# print(sum)

# while 语句：通常使用True无限循环，使用条件判断+break退出循环
# while 循环条件：缩进+执行语句1
# else:(通常不加入该指令)

# 级数展开计算sin(x)
# math库内置sum函数，不能直接使用sum作为变量名，导入库通常置顶，不然有弱警告
# from math import *
# angle = float(input("请输入角度："))
# n = 0
# x = radians(angle)
# s = item = x
# while True:
#     item *= -x * x / (2 * n + 3) / (2 * n + 2)
#     s += item
#     n += 1
#     if abs(item) < 1e-6:
#         break
# print(f"弧度为{x}\nsin(x) = {s}")
