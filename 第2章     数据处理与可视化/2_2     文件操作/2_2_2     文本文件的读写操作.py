# ================ 文本文件的读写操作 =====================

"""
示例演示
"""

# 统计 Pdata2_2_2_2_1.txt 中元音字母出现的次数
# f = open("Pdata2_2_2_1.txt", "r")
# s = f.read()
# print(s)
# n = 0
# for c in s:
#     if c in "aeiouAEIOU":
#         n += 1
# print(f"Pdata2_2_2_1.txt元音字母个数为：{n}")

# 向文本文件中写入数据
# f1 = open("Pdata2_2_2_1.txt", "w")
# str1 = ['Hello', ' ', 'world!']
# str2 = ['Hello', 'world!']
# f1.writelines(str1)
# f1.write('\n')
# f1.writelines(str2)
# f1.close()
# f2 = open('Pdata2_2_2_1.txt')
# a = f2.read()
# f2.close()
# print(a)

# 读取文本文件2_2_2.txt中的前 6 行前 8 列数据、第 9 列的数值数据、最后一行数据
# import numpy as np
# a = []
# b = []
# c = []
# """
# 用 with 语句打开数据文件并把它绑定到对象 file，不必在担心操作完资源后去关闭数据文件
# """
# with open('2_2_2.txt') as file:
#     # line 为字符串类型
#     for (i, line) in enumerate(file):
#         elements = line.strip().split()  # 先去掉左右空格，然后将字符串切割（返回列表，元素为字符串），传递给elements
#         print(elements)
#         if i < 6:
#             a.append(list(map(int, elements[:8])))  # 6行，每行8个，没 map() 前是字符串，map() 后是map对象，用 list 转换成列表
#             b.append(int(elements[-1].rstrip('kg')))  # 索引为-1，elements最后一列，没 float() 前是字符串
#         else:
#             c.append([int(j) for j in elements[:8]])
# a = np.array(a)
# b = np.array(b)
# c = np.array(c)
# print()
# print(a, '\n')
# print(b, '\n')
# print(c, '\n')
