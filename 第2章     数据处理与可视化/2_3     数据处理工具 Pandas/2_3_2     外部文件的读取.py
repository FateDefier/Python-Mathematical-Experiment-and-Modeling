# ================ 外部文件的读取 ======================

"""
实际大多数情况下是通过 Python 读取外部数据，这些数据可能是文本文件（如 csv，txt 等类型）和 电子表格 Excel 文件等

本小节介绍如何基于 Pandas 库实现文本文件和 Excel 文件的读取
"""

"""
1.文本文件的读取
Pandas 模块中的 read_csv 函数，可以读取 txt 或 csv（逗号分隔的文本文件）文本格式数据

pd.read_csv(
    filepath_or_buffer,        # 文件路径或URL（必选）
    sep=',',                   # 分隔符，默认逗号','
    delimiter=None,            # 同sep，优先使用sep
    header='infer',            # 表头行位置（0表示第一行，None表示无表头）
    names=None,                # 自定义列名（列表）
    index_col=None,            # 指定索引列（列名或索引）
    usecols=None,              # 指定读取的列（列名或索引列表）
    dtype=None,                # 指定列的数据类型（字典形式）
    engine=None,               # 解析引擎：{'c', 'python', 'pyarrow'}
    converters=None,           # 自定义列转换函数（字典形式）
    skiprows=None,             # 跳过的行数（整数或函数）
    nrows=None,                # 读取的行数（用于预览大文件）
    na_values=None,            # 视为NaN的值（列表或字典）
    keep_default_na=True,      # 是否保留默认的NaN识别值
    na_filter=True,            # 是否检测NaN（设置False可提升性能）
    verbose=False,             # 是否输出详细信息
    skip_blank_lines=True,     # 是否跳过空行
    parse_dates=False,         # 是否解析日期列
    date_parser=None,          # 自定义日期解析函数
    iterator=False,            # 是否返回迭代器（用于处理大文件）
    chunksize=None,            # 分块读取时的行数
    compression='infer',       # 压缩格式：{'infer', 'gzip', 'bz2', 'zip', 'xz'}
    thousands=None,            # 千位分隔符（如','或'.'）
    decimal='.',               # 小数点分隔符
    encoding=None,             # 文件编码（如'utf-8', 'gbk'）
    error_bad_lines=None,      # 弃用（改用on_bad_lines）
    warn_bad_lines=None,       # 弃用（改用on_bad_lines）
    on_bad_lines='error',      # 错误行处理方式：{'error', 'warn', 'skip'}
    low_memory=True,           # 是否分块处理大文件
    memory_map=False,          # 是否将文件映射到内存（提升大文件读取速度）
)

其中几个重要参数如下：
(1) filepath_or _buffer ：可以是 URL 和文件，可用 URL 类型包括 http, ftp 等，还支持 s3、gcs 等云存储协议（需安装 fsspec 库）．
(2) sep: 支持正则表达式作为分隔符（如 sep='\s+' 匹配任意空白字符），默认逗号分隔（保留但弃用delimiter）
(4) header: header= None, 指明原始数据文件没有列标题，这样 read_csv 会自动加上列标题 header= 0 表示文件第一行为列标题（索引从 0 开始）．
    header参数可以是一个 list， 例如，［0, 1, 3]，这个 list 表示将文件中的第 1, 2, 4 行作为列标题（意味着每一列有多个标题）， 这些行将被忽略掉．
(5) names：如果原数据集中没有字段，可以通过该参数在数据读取时给数据框添加具体的表头
(6) index_col: 用作行索引的列编号或者列名， 如果给定一个序列则有多个行索引
(7) skiprows: 支持函数过滤：传入函数可动态跳过特定行；支持行索引列表：如 skiprows=[0, 2, 5] 跳过第 1、3、6 行
(8) skipfooter: 数据读取时，指定需要跳过原数据集末尾的行数．
(9) nrows: 指定读取数据的行数．
(10) na_values: 指定原数据集中哪些特征的值作为缺失值．
(11) skip_blankJines: 读取数据时是否需要跳过原数据集中的空白行， 默认为True. 
(12) parse_dates: 结合 infer_datetime_format=True 可加速日期解析
    如果参数值为 True, 则尝试解析数据框的行索引；
    如果参数为列表，则尝试解析对应的日期列， 
    如果参数为嵌套列表， 则将某些列合并为日期列；
    如果参数为字典，则解析对应的列（字典中的值），并生成新的字段名（字典中的键）．
(13) thousands: 指定原始数据集中的千分位符．
"""

# 代码也可见相同名的 ipynb 文件，更好的数据处理和可视化交互界面

# import pandas as pd
# df = pd.read_csv(
#     "data2_3_2.txt",
#     sep=',',
#     parse_dates={'birthday': [0, 1, 2]},
#     skiprows=2,
#     skipfooter=2,
#     comment='#',
#     thousands='&',
#     engine='python'
# )
# print

"""
2.Excel 文件的存取
read_excel() 函数可以读入 Excel 文件的数据

read_excel(
    io(文件名),
    sheet_name=0,（表单名或表单序号）
    header=0,
    names=None,
    index_col=None
    parse_cols=None
    usecols=None
    dtype=None
)

"""

"""
3.数据子集的获取
有时数据读入后并不是对整体数据进行分析，而是分析数据中的部分子集
在 Pandas 库中实现数据框子集的获取可以使用 iloc, loc 两种方法．这两种方法既可以对数据行进行筛选，也可以实现变量的筛选
    语法 [rows_select, cols_select].
iloc(integer location) 只能通过行号和列号进行数据的筛选，该索引方式与数组的索引方式类似，都是从 0 开始，可以间隔取号，对于切片仍然无法取到上限．
loc(location) 可以指定具体的行标签（行名称）和列标签（字段名），而且还可以将 row_select 指定为具体的筛选条件
"""




















