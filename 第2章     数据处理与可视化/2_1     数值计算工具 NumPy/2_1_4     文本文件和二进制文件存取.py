# ================ 文本文件和二进制文件存取 ===================

"""
（1）Numpy 提供多种文件操作函数以便用户存取数组内容
（2）文件存取格式：二进制文件 和 文本文件
（3）二进制文件：NumPy 专用的格式化二进制类型和无格式类型
"""

"""
1.文本文件的存取
（1）savetxt() 和 loadtxt() 存取文本文件:fmt 和 dtype 应相同，否则报错

    A savetxt()：将 1 维和 2 维数组保存到文本文件中
    np.savetxt(
    fname='data.txt',        # 文件名或文件对象
    X=data,                  # 要保存的数组
    fmt='%.18e',             # 格式化字符串（默认科学计数法），fmt：指定数据格式，如'%d'（整数）、'%.2f'（两位小数）
    delimiter=' ',           # 分隔符（默认空格），delimiter定界符：列分隔符，如','用于 CSV 格式
    newline='\n',            # 行分隔符
    header='',               # 文件头（字符串），header：添加文件头注释
    footer='',               # 文件尾（字符串），footer：添加文件尾注释
    comments='# ',           # 注释前缀
    encoding='latin1'        # 编码方式
    ) 
    
    B loadtxt()：将文本文件中的数据加载到 1 维和 2 维数组
    loaded_data = np.loadtxt(
    fname='data.txt',        # 文件名或文件对象
    dtype=float,             # 数据类型（默认float），dtype：指定读取的数据类型
    comments='#',            # 注释符号
    delimiter=' ',           # 分隔符
    converters=None,         # 自定义转换器
    skiprows=0,              # 跳过的行数，skiprows：跳过文件前几行（常用于跳过标题）
    usecols=None,            # 使用的列索引，usecols：指定读取哪些列（索引从 0 开始）
    unpack=False,            # 是否转置，unpack：若为True，则转置结果（适用于读取多列数据）
    ndmin=0,                 # 返回数组的最小维度
    encoding='latin1',       # 编码方式
    max_rows=None            # 最大读取行数
    )
（2）genfromtxt：处理缺失数据
    data = np.genfromtxt(
    fname,                   # 文件名、URL 或文件对象
    dtype=float,             # dtype：float（默认）：所有列转为浮点数；None：自动推断每列类型。如果元数据有字符型数据，必须指定数据类型为“str”
    comments='#',            # 注释符号（如'#'），会忽略该行
    delimiter=None,          # 分隔符（默认空格）
    skip_header=0,           # 跳过的标题行数，默认不跳过
    skip_footer=0,           # 跳过的页脚行数，默认不跳过
    converters=None,         # 将指定列的数据转换成其他数值
    missing_values=None,     # missing_values：缺失值标记（如'nan'、'?'）
    filling_values=None,     # filling_values：填充缺失值（如0、np.nan）
    usecols=None,            # usecols：指定使用的列（如(0, 2)表示第 1 和第 3 列）
    names=None,              # 为读入的列设置列名，True：使用第一行作为列名；['col1', 'col2']：自定义列名；
    excludelist=None,        # 需排除的列名
    deletechars=None,        # 列名中需删除的字符
    replace_space='_',       # 列名中空格的替换字符
    autostrip=False,         # 是否自动去除空白
    case_sensitive=True,     # 列名是否区分大小写
    defaultfmt='f%i',        # 默认列名格式
    unpack=False,            # 是否转置结果
    usemask=False,           # 是否返回掩码数组
    loose=True,              # 是否宽松解析
    invalid_raise=True,      # 无效值是否引发错误
    max_rows=None,           # 最大读取行数
    encoding='bytes'         # 编码方式（如'utf-8'、'latin1'），默认为'bytes'
)   
    dtype=None + names=True：自动创建结构化数组。
"""

# import numpy as np
# a = np.arange(0, 3, 0.5).reshape(2, 3)
# np.savetxt("Pdata2_4_1.txt", a)  # 默认".18e"格式保存（科学计数法），默认空格分隔
# b = np.loadtxt("Pdata2_4_1.txt")
# print(f"b = {b}")  # 返回浮点型数据（默认）
# np.savetxt("Pdata2_4_1.txt", a, fmt="%d", delimiter=",")  # 中文逗号，分隔符要与txt文件一致，txt文件无法正常显示
# c = np.loadtxt("Pdata2_4_1.txt", dtype=int, delimiter=",")  # 读入时也要指定逗号分隔
# print(f"c = {c}")

# import numpy as np
# a = np.loadtxt("Pdata2_4_2.txt")  # 返回值 a 为浮点型数据
# print(f"a = {a}")
# b = a[0:2, 1:4]
# print(f"b = {b}")

# import numpy as np
# a = np.loadtxt("Pdata2_4_3.txt", dtype=str, delimiter='，', encoding='utf-8')
# b = a[1:, 1:].astype(float)
# print(f"b = {b}")

# import numpy as np
# a = np.loadtxt("sh_data.csv", dtype=str, delimiter=',', usecols=1, encoding='utf-8')
# print(a)

# import numpy as np
# a = np.genfromtxt("Pdata2_4_4.txt", max_rows=6, usecols=range(8))  # 读取文件的前 6 行中的前 8 列
# b = np.genfromtxt("Pdata2_4_4.txt", dtype=str, max_rows=6, usecols=[8])  # 读取含字符串数据必须指定dtype=str
# b = [float(v.rstrip('kg')) for v in b]  # == b = [float(v.rstrip('kg')) for (i, v) in enumerate(b)]
# c = np.genfromtxt("Pdata2_4_4.txt", skip_header=6)  # 跳过前 6 行，从第 7 行开始读取
# print(a, '\n\n', b, '\n\n', c)

"""
2.二进制格式文件存取
（1）tofile() 和 fromfile() 存取二进制格式文件
A tofile() 方法可以将数组中的数据以二进制格式写进文件，tofile() 输出的数据不保存数组形状和元素类型等信息
B 因此用 fromfile() 函数读回数据时需要用户指定元素类型，并对数组的形状进行适当的修改
（2）load(), save() 和 savez() 存取 NUmPy 专用的二进制格式文件
A load() 和 save() 用 NumPy 专用的二进制格式存储数据，它们会自动处理元素类型和形状等信息
B savez(file_name, arr1, arr2, ...)：将多个数组保存到一个二进制文件，输出的是一个扩展名为 npz 的压缩文件
    用解压软件打开 “Pdata2_4_7.npz" 文件， 会发现其中有两个文件： 
    “arr_O.npy", “arr_1.npy" ，分别保存着数组 c,d 的内容． 
    load(）自动识别 npz 文件， 并且返回一个类似于字典的对象， 可以通过数组名作为键获取数组的内容
"""

# import numpy as np
# a = np.arange(6).reshape(2, 3)
# a.tofile('Pdata2_4_5.bin')
# b = np.fromfile('Pdata2_4_5.bin', dtype=int).reshape(2, 3)
# print(a, '\n\n', b)

import numpy as np
a = np.arange(6).reshape(2,3)
np.save("Pdata2_4_6.npy", a)
b = np.load("Pdata2_4_6.npy")
c = np.arange(6, 12).reshape(2, 3)
d = np.sin(c)
np.savez("Pdata2_4_7.npz", c, d)
e = np.load("Pdata2_4_7.npz")
f1 = e["arr_0"]  # 利用“键”arr_0（文件名）提取第一个数组的数据
f2 = e["arr_1"]  # 利用“键”arr_1（文件名）提取第二个数组的数据
print(f1, '\n\n', f2)
