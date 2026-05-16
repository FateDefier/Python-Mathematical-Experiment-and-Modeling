# =============== Matplotlib 基础用法 ==================

"""
Matplotlib 基础用法
"""

"""
Matplotlib 提出了 Object Container （对象容器）的概念，
它有Figure, Axes, Axis, Tick 四种类型的对象容器． 
    Figure 负责图形大小、位置等操作； 
    Axes   负责坐标轴位置绘图等操作； 
    Axis   负责坐标轴的设置等操作． 
    Tick   负责格式化刻度的样式等操作．
四种对象容器之间是层层包含的关系
"""

"""
Matplotlib.pyplot 模块画折线图的 plot() 函数的常用语法和参数含义如下：
（1）plot(x, y, s)
    其中，x 为数据点的 x 坐标，y 为数据点的 y 坐标，s 为指定线条颜色、线条样式和数据点形状

            绘图常见的样式和颜色类型
    符号参数	         类型	                含义
       b	        线条颜色	            Blue, 蓝色
       c	        线条颜色	            Cyan, 青色
       g	        线条颜色	            Green, 绿色
       k	        线条颜色	            Black, 黑色
       m	        线条颜色	            Magenta, 洋红色
       r	        线条颜色	            Red, 红色
       w	        线条颜色	            White, 白色
       y	        线条颜色	            Yellow, 黄色
       -----------------------------------------------  
       -	        线条样式	            实线 (solid line)
       --	        线条样式	            虚线 (dashed line)
       -.	        线条样式	            点画线 (dash-dot line)
       :	        线条样式	            点线 (dotted line)
       ------------------------------------------------
       .	        数据点形状	        点 (point)
       o	        数据点形状	        圆圈 (circle)
       *	        数据点形状	        星形 (star)
       x（小写）	    数据点形状	        十字架 (cross)
       s	        数据点形状	        正方形 (square)
       p	        数据点形状	        五角星 (pentagon)
      D/d	        数据点形状	        钻石 (diamond)/ 小钻石
       h	        数据点形状	        六角形 (hexagon)
       +	        数据点形状	        加号
       |	        数据点形状	        竖直线
    v ^ < >	        数据点形状	        分别是下三角、上三角、左三角、右三角
    1 2 3 4	        数据点形状	        分别是 Tripod（三脚架） 向下、向上、向左、向右

位置参数
x：x 轴数据，可以是列表、数组等可迭代对象如果未提供，默认使用 range(len(y)) 作为 x 轴数据
y：y 轴数据，是必须提供的参数，同样可以是列表、数组等可迭代对象

格式字符串参数（fmt）
fmt是一个可选的字符串参数，用于快速设置线条颜色、样式和数据点标记，它是由颜色、标记和线条样式三个字符按顺序组成的字符串，比如'ro-'表示红色圆圈标记和实线
颜色字符：如'b'（蓝色）、'g'（绿色）、'r'（红色）、'c'（青色）、'm'（洋红色）、'y'（黄色）、'k'（黑色）、'w'（白色）等
标记字符：像'.'（点）、'o'（圆圈）、'*'（星形）、's'（正方形）等
线条样式字符：'-'（实线）、'--'（虚线）、'-.'（点划线）、':'（点线） 

关键字参数
color：设置线条颜色，除了使用颜色字符外，还可以用十六进制颜色码（如'#FF5733'）、RGB 元组（如(0.1, 0.2, 0.3)） 、颜色名称（如'red'、'blue' ）等
linestyle：设置线条样式，可选值有'solid'（实线，等价于'-'）、'dashed'（虚线，等价于'--'）、'dashdot'（点划线，等价于'-.'）、'dotted'（点线，等价于':'）、'None'（无线条） 
linewidth 或 lw：设置线条宽度，值为浮点数，如2.0表示线条宽度为 2 个单位
marker：设置数据点标记，可选值如'o'（圆圈）、's'（正方形）、'^'（上三角）等
markersize 或 ms：设置数据点标记的大小，值为浮点数，比如8表示标记大小为 8 个单位
markeredgecolor 或 mec：设置数据点的边缘颜色，取值方式和color类似
markeredgewidth 或 mew：设置数据点的边缘宽度，值为浮点数
markerfacecolor 或 mfc：设置数据点的填充颜色，取值方式和color类似
alpha：设置图形的透明度，取值范围是 0（完全透明）到 1（完全不透明） ，如0.5表示半透明
label：为线条添加标签，用于图例显示在绘制多个线条并需要添加图例时，通过plt.legend()方法可以显示这些标签对应的图例
zorder：设置绘图的图层顺序，数值越大越在上方显示，用于处理多个图形重叠时的前后顺序问题
dash_capstyle：设置虚线端点的样式，可选值有'butt'（平头）、'round'（圆头）、'projecting'（突出） 
dash_joinstyle：设置虚线连接点的样式，可选值有'miter'（尖角）、'round'（圆角）、'bevel'（斜角） 
antialiased 或 aa：设置是否抗锯齿，取值为True（开启抗锯齿，使线条和标记边缘更平滑）或False（关闭抗锯齿） 
picker：设置是否开启交互式选择功能，可以是布尔值（True开启，False关闭），也可以是指定选择容差的数值 
pickradius：当picker为True或数值时，设置选择半径，即鼠标点击位置与数据点的距离在这个半径范围内就可以选中数据点
clip_on：设置是否裁剪图形，取值为True（裁剪，超出坐标轴范围的部分不显示）或False（不裁剪） 
clip_box：当clip_on为True时，指定裁剪的边界框 
clip_path：当clip_on为True时，指定裁剪的路径 

Matplotlib.pyplot 的其他常用函数：
（2）pie()：绘制饼状图
（3）bar()：绘制柱状图
（4）hist()：绘制二维直方图
（5）scatter()：绘制散点图
"""

"""
plt.scatter(x, y, c='r', marker='H', s=20)
表示绘制散点图，x 坐标数据为 x，y 坐标数据为 y，c='r' 表示颜色为红色，marker='H' 表示数据点为六边形，s=20 表示数据点的尺寸大小为20
"""

"""
Matplotlib 绘图主要步骤
（1）导入 Matplotlib.pyplot 模块
（2）设置绘图的数据及参数
（3）调用 Matplotlib.pyplot 模块的 plot(),pie(),bar(),hist(),scatter()等函数绘图
    注意模块加载的两种方式
    (i).import matplotlib.pyplot as plt 或 from matplotlib import pyplot as plt
    (ii).from matplotlib.pyplot import *
（4）设置绘图的 x 轴、y 轴、标题、网格线、图例等内容
（5）调用 show() 函数显示已绘制的图形

为了将面向对象的绘图库包装成只使用函数的API,pyplot模块的内部保存了当前图形以及当前子图等信息
可以使用 gcf()（Get Current Figure）和 gca()（Get Current Axes）获得这两个对象

gcf() 获得的是表示图形的 Figure 对象
gca() 获得的则是表示子图的 Axes 对象 
例如：
fig = gcf()
axes = gca()
"""

#%%
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# #%% 中文支持
# # rcParams ———— runtime configuration parameters 运行时配置参数
# # font（字体）sans-serif 无衬线体（如黑体，微软雅黑），serif 衬线体（如宋体、楷体）
# # axes(表示坐标轴对象的类)unicode_minus(Unicode Minus Sign,也就是 unicode 编码中的➖)
# # plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
# # plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号，设置为True时使用 Unicode 减号（−）来显示负号
# # 下面是等价简写，还有种写法见 2_4_1.ipynb 文件
# plt.rc('font', family='SimHei')
# plt.rc('axes', unicode_minus=False)
# #%% 画图
# a = pd.read_excel("excel1.xlsx", usecols=range(1, 4))
# c = np.sum(a)  # 默认（axis=0，按列求和），axis=1 时按行求和
# ind = np.array([1, 2, 3])  # 柱状图在 x 轴的位置
# width = 0.2  # 每个柱状图的宽度，占 0.2 个单位
# plt.rc('font', size=6)  # rc（全局配置），font（字体设置）
# plt.bar(ind, c, width)
# plt.xlabel("用户")
# plt.ylabel("消费数据")
# plt.xticks(ind, ['用户A', '用户B', '用户C'], rotation=20)  # ticks（刻度）
# plt.savefig('figure_excel1.png', dpi=500)  # dpi=500：图像分辨率（每英寸点数），值越高越清晰，运行的越慢
# plt.show()

#%% 输出系统字体
# # 查看系统字体，自带的有STXihei（华文细黑）、STSong（华文宋体）、SimHei（黑体）
# import matplotlib.font_manager as fm
#
# # 获取所有可用字体
# fonts = fm.findSystemFonts()
#
# # 打印包含"hei"或"song"等中文字体关键字的字体
# chinese_fonts = [f for f in fonts if 'hei' in f.lower() or 'song' in f.lower() or 'microsoft' in f.lower()]
# for font in chinese_fonts:
#     print(fm.FontProperties(fname=font).get_name())
