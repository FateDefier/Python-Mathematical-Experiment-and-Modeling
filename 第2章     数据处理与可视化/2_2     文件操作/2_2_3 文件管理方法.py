# =============== 文件管理方法 =================

"""
Python 的 os 模块提供了类似于操作系统级的文件管理系统
如显示当前目录下的文件和目录列表、文件重命名、文件删除、目录管理等
先导入 os 模块，再调用方法
"""

"""
1.文件和目录列表
listdir() 方法返回指定目录下的文件和目录列表（list directory path）
os.listdir("目录名")
"""

# import os
# a = os.listdir("c:\\")  # 显示 C 根目录下的文件和目录列表，'$RECYCLE.BIN'————存放回收站内容的系统文件夹
# print(a)
# print("-----------------------------------")
# b = os.listdir(".")  # 显示当前工作目录下的文件和目录列表
# print(b)

"""
2.文件重命名
rename() 方法实现重命名
os.rename("当前文件名", "新文件名")
"""

# import os
# os.rename("data2_2_2.txt", "2_2_2.txt")

"""
3.Python 中的目录操作
所有的文件都在不同的目录中，os 模块有以下几种方法，可以帮助创建、更改和删除目录
（1）mkdir() 方法：在当前目录创建目录（make directory）
    os.mkdir("新目录名")
（2）chdir() 方法：改变当前目录（change directory）
    os.chdir("要成为当前目录的目录名")
    os.chdir() 只是改变 Python 脚本运行时的当前工作目录，它不会移动或复制物理文件，也不会改变 PyCharm 项目中文件的存储位置。
（3）getcwd() 方法：显示当前的工作目录（get current working directory）
    os.getcwd
（4）redir() 方法：删除空目录（空目录）(remove directory)
    os.rmdir("待删除目录名")
"""

# import os
# 在当前目录创建“test目录”
# os.mkdir("test")
#
# os.rmdir("test")

import os

# 查看当前工作目录
print("当前工作目录:", os.getcwd())

try:
    # 更改工作目录
    os.chdir("D:\\Pycharm\\python_modeling\\第2章     数据处理与可视化\\2_2     文件操作")

    # 确认更改后的工作目录
    print("成功将工作目录更改为:", os.getcwd())
except FileNotFoundError:
    print("错误：指定的目录不存在")
except NotADirectoryError:
    print("错误：指定的路径不是一个目录")
except PermissionError:
    print("错误：没有权限访问该目录")
except Exception as e:
    print(f"发生未知错误: {e}")
print("修改后的工作目录:", os.getcwd())
