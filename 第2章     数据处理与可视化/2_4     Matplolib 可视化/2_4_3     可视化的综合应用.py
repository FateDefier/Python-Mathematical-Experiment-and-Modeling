# ================= 可视化的综合应用 ====================

"""
实际应用中往往会根据业务需要，将绘制的多个子图组合到一个图形界面内，
前面已经使用过subplot 函数
"""

"""
多种图形组合，可以使用 Matplotlib.pyplot 模块的 subplot 函数和 subplot2grid 函数
构成的组合图形可以是 m x n 的风格，也可以是跨行或跨列的分块风格

（1）plt.subplot(nrows, ncols, index, **kwargs)
nrows：网格的总行数
ncols：网格的总列数
index：当前子图的位置（从左到右、从上到下编号，从 1 开始）
**kwargs：其他可选参数，如 projection='3d'（创建三维坐标轴）
（2）plt.subplot2grid(shape, loc, rowspan=1, colspan=1, **kwargs) - 灵活网格布局
shape：网格的总行数和总列数（元组 (nrows, ncols)）
loc：当前子图的起始位置（元组 (row, col)），从 0 开始计数
rowspan：子图跨越的行数（默认 1）
colspan：子图跨越的列数（默认 1）
**kwargs：其他可选参数，如 projection='3d'

参数	    subplot()	        subplot2grid()
布局方式	均匀网格	            可跨越行 / 列的灵活网格
编号方式	从 1 开始的线性索引	从 0 开始的行列坐标
跨行跨列	不支持	            支持 rowspan 和 colspan
典型场景	简单的 N×M 网格布局	复杂的非均匀布局（如子图大小不同）
"""
