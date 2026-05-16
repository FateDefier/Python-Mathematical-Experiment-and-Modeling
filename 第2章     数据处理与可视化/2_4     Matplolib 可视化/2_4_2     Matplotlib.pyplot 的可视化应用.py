# =================== Matplotlib.pyplot 的可视化应用 =======================

import numpy as np
import matplotlib.pyplot as plt
"""
Matplotlib 工具库依赖于 NumPy 等工具库，可以绘制多种格式的图形，是计算机结果可视化的重要工具
"""

"""
1.散点图
plt.scatter(x, y, 
            s=None, 
            c=None, 
            marker=None, 
            cmap=None, 
            norm=None,
            vmin=None, 
            vmax=None, 
            alpha=None, 
            linewidths=None,
            edgecolors=None, 
            plotnonfinite=False, 
            data=None, 
            **kwargs)
            
 参数	      功能	            默认值	                        示例值
x, y	    点的坐标	            必须提供	                [1, 2, 3], np.array([4, 5, 6])
s	        点大小	    rcParams["scatter.s"]	            50, [10, 50, 100]
c	        点颜色	            None	            'red', [0.1, 0.5, 0.8]（需配合 cmap）
marker	    点形状	            'o'	                 's'（正方形）、'^'（三角形）、'*'（星形）
cmap	    颜色映射	    rcParams["image.cmap"]	        'viridis', 'plasma', plt.cm.Reds
alpha	    透明度	            None	                          0.5
edgecolors	边缘颜色	            'face'	                      'black', 'none'
linewidths	边缘线宽	        rcParams["lines.linewidth"]	      1, [0.5, 1, 2]
"""

"""
2.饼图
plt.pie(x, explode=None, labels=None, colors=None, autopct=None,
        pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0,
        radius=1, counterclock=True, wedgeprops=None, textprops=None,
        center=(0, 0), frame=False, rotatelabels=False, *, data=None)
    参数	            功能	                默认值	        示例值
    x	        每个扇形的数值	            必须提供	    [35, 25, 25, 15]
    labels	       扇形标签	            None	    ['A', 'B', 'C', 'D']
    colors	       扇形颜色	            None	['red', 'blue', 'green', 'yellow']
    autopct	    显示百分比的格式	        None	   '%1.1f%%'（显示一位小数）
    explode	扇形与圆心的距离（突出显示）	    None	[0, 0.1, 0, 0]（第二个扇形突出）
    shadow	      是否添加阴影	        False	         True
    startangle	起始角度（0=3 点钟方向）	0	       90（从 12 点钟方向开始）
    radius	        饼图半径	            1	                1.2
"""

"""
3.柱状图
plt.bar(x, height, width=0.8, bottom=None, align='center',
        color=None, edgecolor=None, linewidth=None, tick_label=None,
        xerr=None, yerr=None, ecolor=None, capsize=None, error_kw=None,
        log=False, orientation='vertical', **kwargs)
    参数	           功能	         默认值	        示例值
    x	        柱子的位置	    必须提供	    [1, 2, 3, 4]
    height	    柱子的高度	    必须提供	    [10, 20, 15, 25]
    width	    柱子的宽度	     0.8	          0.5
    color	    柱子颜色	        None	    'blue', ['r', 'g', 'b', 'y']
    edgecolor	柱子边缘颜色	    None	        'black'
    align	    柱子对齐方式	    'center'	'edge'（左边缘对齐）
    bottom	    柱子底部位置	    None	    [5, 5, 5, 5]（从 y=5 开始）
    yerr	    误差线数值	    None	    [1, 2, 1, 3]（每个柱子的误差范围）
    ecolor	    误差线颜色	    None	            'red'
"""

"""
4.二维直方图
plt.hist(x, bins=None, range=None, density=False, weights=None,
         cumulative=False, bottom=None, histtype='bar', align='mid',
         orientation='vertical', rwidth=None, log=False, color=None,
         label=None, stacked=False, *, data=None, **kwargs)
    参数	          功能	           默认值	            示例值
    x	        输入数据	          必须提供	np.random.randn(1000)（正态分布数据）
    bins	  分箱数量或边界	        10	    20（20 个箱），[0, 10, 20, 30]（自定义箱边界）
    range	    数据范围	           None	    (0, 100)（只考虑 0-100 之间的数据）
    density	是否归一化（面积 = 1）	   False	            True
    histtype	直方图类型	       'bar'	'step'（只显示轮廓），'barstacked'（堆叠）
    color	      颜色	           None	                'green'
    alpha	     透明度	           None	                 0.5
    cumulative	是否累积	           False	        True（累积分布）

5.箱线图：boxplot 
常用参数
x：指定用于分组的列名，用于在不同的子图中绘制箱线图。
y：指定要绘制箱线图的列名。
data：指定要使用的 DataFrame。
notch：布尔值，默认为 False，如果设置为 True，则绘制带缺口的箱线图，缺口位置为中位数的置信区间。
sym：指定异常值的标记符号，默认为 +。
vert：布尔值，默认为 True，表示箱线图垂直绘制；如果为 False，则水平绘制。
positions：指定箱线图的位置。
widths：指定箱线图的宽度。
"""

# 散点图（刀具的磨损速度）
# x = np.arange((8))
# y = '27.0 26.8 26.5 26.3 26.1 25.7 25.3 24.8'
# y = ",".join(y.split())
# y = np.array(eval(y))
# plt.scatter(x, y)
# plt.savefig('fig1.png', dpi=1000)
# plt.show()

"""
2.多个图形显示在一个页面（一个图多条线）
"""

# # 在同一个图形界面上分别画出 y = sin(x), y = cos（x^2）， X在[0,2pi]之间的图形
# x = np.linspace(0, 2*np.pi, 200)
# y1 = np.sin(x)
# y2 = np.cos(pow(x, 2))
# plt.rc('font', size=16)
# plt.rc('text', usetex=True)  # 调用tex字库
# plt.plot(x, y1, 'r', label='$sin(x)$', linewidth=2)
# plt.plot(x, y2, 'b--', label='$cos(x^2)$', linewidth=2)
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.savefig('fig2.png', dpi=1000)
# plt.legend()
# plt.show()

"""
3.多个图形单独显示（一个窗口，多张图）
(1)plt.subplot(nrow, ncolumn, index)  index 从 1 开始，第一行 ~ 第二行
(2)plt.rc('对象', 参数)（一次只能设一个），如 plt.rc('font', family=['SimHei'])
(3)plt.legend()
    参数	                        说明
    loc	           图例位置（如'best', 'upper right'）
bbox_to_anchor	        自定义位置（x, y 坐标或宽高）
    title	                    图例标题
    frameon	            是否显示边框（True/False）
    framealpha	            边框透明度（0-1）
    fontsize	        字体大小（如'small', 12）
    ncol	                    图例列数（多列显示）
    markerscale	            标记大小缩放因子
    handlelength	        图例标记的长度
    borderpad	            文本与边框的间距

对于 loc 参数
0	最佳位置（自动选择，默认值）
1	右上角（upper right）
2	左上角（upper left）
3	左下角（lower left）
4	右下角（lower right）
5	右侧（right）
6	左侧居中（center left）
7	右侧居中（center right）
8	底部居中（lower center）
9	顶部居中（upper center）
10	正中心（center）
"""

"""
4.三维空间的曲线
mpl_toolkits.mplot3d（ mpl 即matplotlib，toolkit 工具包，mplot3D matplotlib.3D） 是 Matplotlib 库的一个扩展模块
专门用于创建三维可视化图形，包括三维散点图、曲面图、线框图、柱状图等。
"""

"""
5.三维曲面图形
（1）cmap='viridis'：使用 viridis 颜色映射（从蓝到黄）
（2）surface(表面)，绘制三维曲面图
（3）wireframe(wire导线，frame框架)绘制三维线框图（仅显示网格线）
（4）meshgrid(x, y)  # 将一维数组 x 和 y 转换为二维网格矩阵 X 和 Y，广播机制重复，X 和 Y 仍是二维数组，但是被广播
gcdata.txt 中：
x 和 y 的间隔相等（grid data 的关键）

x = [0, 100, ..., 1400]（15 个点，列坐标）
y = [1200, 1100, ..., 0]（13 个点，行坐标）
z 是 13 行 ×15 列的二维数组，每个元素是对应 (x,y) 的高程值。

网格数据的核心是 “规则排列”—— 相邻点的 x、y 间隔固定（如你的数据中 x 间隔 100，y 间隔 100），这也是它能直接用于绘制等高线、曲面图的原因。
"""

"""
6.等高线图
已知平面区域 0 ~ X ~ 1400, 0 ~ y ~ 1200 步长间隔为 100 的网格节点高程数据

plt.contour(x, y, z)  绘制等高线（画的平面图），返回一个 QuadContourSet 对象
x 为列，y 为行，需与 z 的形状匹配，二维数组（形状为 (len(y), len(x))），表示网格上每个点的数值（如高程）
绘制二维数据 z 的等高线图,将三维曲面（如地形、温度场）投影到二维平面上，用曲线表示相同高度（或数值）的点

plt.clabel( QuadContourSet 对象)  添加等高线标签

"""

"""
7.向量图
plt.quiver(X, Y, U, V)
在二维平面上绘制箭头（向量），每个箭头的位置由 (X, Y) 确定，方向和长度由 (U, V) 确定
参数
X, Y：
二维数组，指定每个箭头的起点坐标（网格点位置）。
U, V：
二维数组，指定每个箭头在 x 和 y 方向的分量（决定箭头的方向和长度）
箭头方向：由 (v1, v2) 的比值决定（如 v1=1, v2=1 表示箭头指向东北方向）
箭头长度：与 sqrt(v1² + v2²) 成正比
其他可选参数：
color：箭头颜色。
scale：缩放因子，值越大箭头越短。
angles：箭头角度计算方式（如 'uv' 表示直接使用 U,V 作为方向）。
width：箭头宽度。
cmap：颜色映射（用于根据向量长度着色）。
"""

