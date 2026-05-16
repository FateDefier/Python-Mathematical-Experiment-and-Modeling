# ================== 序言 ====================

"""
Matplotlib 是 Python 强大的数据可视化工具库，类似与 MATLAB 语言。
Matplotlib 提供了一整套与 MATLAB 相似的命令 API，十分适合进行交互式制图，
而且也可以方便地将它作为绘图控件，嵌入 GUI 应用程序中．

Matplotlib 是神经生物学家 John D. Hunter 千 2007 年创建的，其函数设计参
考了 MATLAB
"""

# 以下是 pandas，polars，matplotlib，seaborn，plotly 常见用法
"""
================= pandas 和 polars ===================================================
1. 核心差异：设计理念
Pandas：基于单线程设计，依赖 NumPy 数组存储数据，灵活性高，但处理大规模数据时容易遇到性能瓶颈（尤其是超过内存的数据集）。
Polars：基于 Rust 开发，默认支持多线程和向量化操作，数据存储采用列式格式，更适合处理大数据（可高效处理比内存大的数据集），且语法更严格（减少隐式拷贝和错误）。
2. 性能对比
小数据：两者速度接近，Pandas 可能因生态成熟更顺手。
大数据：Polars 优势明显，多线程 + 列式存储让过滤、聚合等操作速度比 Pandas 快数倍甚至数十倍（尤其数据量超过 100 万行时）。
内存效率：Polars 内存占用更低，支持 “零拷贝” 操作，适合处理超内存数据（可分块读取）。
3. 常用操作对比
操作	            Pandas 代码	                        Polars 代码	                                                说明
读取 CSV	pd.read_csv("data.csv")	            pl.read_csv("data.csv")	                                语法类似，Polars 支持多线程读取
选择列	df[["col1", "col2"]]	            df.select(["col1", "col2"])	                            Polars 更强调显式操作
过滤行	df[df["col1"] > 10]	                df.filter(pl.col("col1") > 10)	                        Polars 用 filter 方法
分组聚合	df.groupby("col1")["col2"].mean()	df.groupby("col1").agg(pl.col("col2").mean())	        Polars 聚合语法更统一
新增列	df["new_col"] = df["col1"] * 2	    df.with_column((pl.col("col1") * 2).alias("new_col"))	Polars 不修改原数据（ immutable）
排序	df.sort_values("col1")	                    df.sort("col1")	语法类似
4. 适用场景
选 Pandas：
处理小数据，需要丰富的第三方库支持（如 Matplotlib 绘图、Scikit-learn 联动）。
依赖 Pandas 独有的功能（如 apply 自定义函数的灵活性，尽管性能差）。
选 Polars：
处理大数据（百万级以上行），追求高性能和低内存占用。
需要并行计算加速，或处理超内存数据集。
偏好严格的语法（减少隐式错误）。
"""

"""
===================== matplotlib ======================
一、基础绘图函数
1. plt.plot()
功能：绘制折线图，常用于函数曲线（如一次函数、三角函数、微分方程解曲线等）。
核心参数：
x, y：x 轴、y 轴数据（数组或列表）。
label：曲线标签（用于图例说明）。
color：线条颜色（如'r'红色、'b'蓝色，或十六进制'#FF0000'）。
linestyle：线条样式（'-'实线、'--'虚线、':'点线等）。
linewidth：线条粗细（数值，如2）。
marker：数据点标记（如'o'圆点、's'正方形，用于离散点标注）。
示例：绘制 y = sin(x) 曲线
python
运行
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-', linewidth=1.5)

2. plt.scatter()
功能：绘制散点图，用于展示离散数据（如样本点、实验数据）。
核心参数：
x, y：散点的 x、y 坐标。
s：散点大小（单个数值或数组，控制每个点的尺寸）。
c：散点颜色（可与cmap配合使用，实现颜色映射，如按数值大小着色）。
cmap：颜色映射方案（如'viridis'、'coolwarm'，用于体现数据梯度）。
marker：散点形状（同plt.plot()的marker）。
示例：绘制随机样本点
python
运行
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, s=50, c=y, cmap='viridis', label='样本点')

3. plt.bar() / plt.barh()
功能：绘制柱状图（bar垂直，barh水平），用于对比离散类别数据（如不同模型的误差、各参数的影响权重）。
核心参数：
x：类别标签（数组，如[1,2,3]或['A','B','C']）。
height（bar）/ width（barh）：柱形高度（或宽度），即数据值。
width（bar）/ height（barh）：柱形宽度（或高度），控制粗细。
color：柱形颜色（单个颜色或数组，为每个柱分配颜色）。
示例：对比 3 个模型的准确率
python
运行
models = ['模型1', '模型2', '模型3']
acc = [0.85, 0.92, 0.78]
plt.bar(models, acc, color=['red', 'green', 'blue'])

二、坐标轴与图例设置
1. plt.xlabel() / plt.ylabel()
功能：设置 x 轴、y 轴标签（注明变量含义，如 “时间（s）”“误差值”）。
参数：xlabel/ylabel（标签文本）、fontsize（字体大小，如12）。
2. plt.xlim() / plt.ylim()
功能：设置 x 轴、y 轴的显示范围（避免图像被截断或留白过多）。
参数：(min, max)，如plt.xlim(0, 10)限制 x 轴为 0 到 10。
3. plt.legend()
功能：显示图例（标注不同曲线 / 数据的含义）。
参数：loc（图例位置，如'upper right'右上角、'best'自动选最优位置）、fontsize（字体大小）。
4. plt.title()
功能：设置图表标题（说明图像主题，如 “微分方程数值解曲线”）。
参数：label（标题文本）、fontsize、pad（标题与图表的间距）。
三、子图与多图布局
plt.subplot()
功能：在一个画布上创建多个子图（同时展示多组数据或对比不同条件下的结果）。
参数：nrows, ncols, index（行数、列数、当前子图索引，如subplot(2,1,1)表示 2 行 1 列的第 1 个子图）。
示例：上下排列两个子图，分别展示sin(x)和cos(x)
python
运行
x = np.linspace(0, 2*np.pi, 100)
plt.subplot(2,1,1)  # 第1个子图
plt.plot(x, np.sin(x), color='r')
plt.title('sin(x)')

plt.subplot(2,1,2)  # 第2个子图
plt.plot(x, np.cos(x), color='b')
plt.title('cos(x)')
plt.tight_layout()  # 自动调整子图间距

四、网格与注释
1. plt.grid()
功能：添加网格线（便于读取数据点的大致数值）。
参数：True/False（是否显示）、linestyle（网格线样式，如'--'虚线）、alpha（透明度，0~1 之间）。
2. plt.annotate()
功能：添加注释文本（标注关键数据点，如极值点、转折点）。
核心参数：
text：注释文本（如'最大值'）。
xy：被注释点的坐标（(x,y)）。
xytext：注释文本的位置坐标。
arrowprops：箭头样式（如{'arrowstyle': '->'}添加指向被注释点的箭头）。
示例：标注sin(x)的最大值点
python
运行
max_x = np.pi/2
max_y = 1
plt.annotate('最大值', xy=(max_x, max_y), xytext=(max_x+1, max_y+0.2),
             arrowprops={'arrowstyle': '->'})


五、保存图像
plt.savefig()
功能：保存绘制的图像（用于论文、报告插入）。
参数：filename（保存路径及文件名，如'result.png'）、dpi（分辨率，如300保证清晰度）、bbox_inches='tight'（去除多余空白）。
"""


"""
========================== seaborn =======================================
这些函数的参数排列都遵循 “数据集优先，核心变量紧随，样式 / 分组参数在后” 的逻辑，和数学建模中 “先明确数据和变量，再细化分析维度” 的思路一致

1. 散点图（用于变量关系分析）：seaborn.scatterplot()
函数参数排列（核心）：
sns.scatterplot(data=None, x=None, y=None, hue=None, style=None, size=None, ...)
关键参数说明：
data：数据集（如 DataFrame，优先传入，后续参数可直接用列名）。
x, y：x 轴、y 轴数据（必填，通常是建模中的自变量和因变量）。
hue：按某列数据给点上色（用于区分类别，如不同组别、标签）。
style：按某列数据设置点的样式（如圆形、方形，辅助区分类别）。
size：按某列数据设置点的大小（体现第三维度的数值差异）。

示例：

python
运行
sns.scatterplot(data=df, x="feature1", y="target", hue="category", style="category")

2. 线图（用于趋势分析，如拟合曲线、时间序列）：seaborn.lineplot()
函数参数排列（核心）：
sns.lineplot(data=None, x=None, y=None, hue=None, style=None, ci="ci", ...)
关键参数说明：
data, x, y, hue, style：与scatterplot一致。
ci：置信区间显示方式（默认 "ci=95" 显示 95% 置信区间，设为 "sd" 显示标准差，设为 None 不显示）。
marker：是否显示数据点（如marker="o"显示圆点）。

示例：

python
运行
sns.lineplot(data=df, x="epoch", y="accuracy", hue="model", ci=None)  # 对比不同模型的精度趋势

3. 直方图 / 核密度图（用于数据分布分析）：seaborn.histplot()、seaborn.kdeplot()
histplot()（直方图）
参数排列：sns.histplot(data=None, x=None, y=None, hue=None, bins=None, kde=False, ...)
bins：直方图的分箱数（控制 bins 宽度，影响分布颗粒度）。
kde：是否叠加核密度曲线（kde=True时同时显示分布趋势）。
kdeplot()（核密度图）
参数排列：sns.kdeplot(data=None, x=None, y=None, hue=None, fill=False, bw_adjust=1, ...)
fill：是否填充曲线下方区域（fill=True更直观）。
bw_adjust：带宽调整（值越大曲线越平滑，越小越贴合数据）。

示例：

python
运行
sns.histplot(data=df, x="error", bins=20, kde=True)  # 查看误差项的分布
sns.kdeplot(data=df, x="feature2", hue="category", fill=True)  # 对比不同类别的特征分布

4. 箱线图（用于异常值检测、组间差异）：seaborn.boxplot()
函数参数排列（核心）：
sns.boxplot(data=None, x=None, y=None, hue=None, order=None, ...)
关键参数说明：
x, y：通常 x 为类别变量（如不同算法），y 为数值变量（如性能指标）。
order：指定 x 轴类别的显示顺序（如order=["A", "B", "C"]）。
箱线图默认显示四分位数、中位数和异常值（超出 1.5 倍四分位距的点）。

示例：

python
运行
sns.boxplot(data=df, x="algorithm", y="mse", order=["LR", "SVM", "RF"])  # 对比不同算法的均方误差

5. 热图（用于相关性分析）：seaborn.heatmap()
函数参数排列（核心）：
sns.heatmap(data, annot=False, cmap="viridis", fmt=".2f", linewidths=0, ...)
关键参数说明：
data：必须是二维数组（如相关系数矩阵df.corr()）。
annot：是否在单元格中显示数值（annot=True用于明确相关性大小）。
cmap：颜色映射（如"coolwarm"适合正负相关对比）。
fmt：数值显示格式（如fmt=".2f"保留两位小数）。

示例：

python
运行
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")  # 显示特征间的相关系数

6. 回归曲线（用于线性 / 非线性关系建模初探）：seaborn.regplot()
函数参数排列（核心）：
sns.regplot(data=None, x=None, y=None, order=1, ci=95, scatter=True, ...)
关键参数说明：
order：回归阶数（order=1为线性回归，order=2为二次曲线回归）。
ci：置信区间（同lineplot，设为 None 不显示）。
scatter：是否显示原始数据点（scatter=False只显示回归线）。

示例：

python
运行
sns.regplot(data=df, x="feature", y="target", order=2, ci=95)  # 拟合二次曲线并显示置信区间

"""

"""
=================================== plotly =====================================
1. plotly.express.line()（线图，展示趋势）
功能：绘制折线图，适合表现变量随时间或连续参数的变化趋势（如模型预测值与真实值对比）。
参数排列及说明：

data_frame：数据源（DataFrame 类型，必传）。
x：x 轴数据列名（字符串，必传，如模型的 “参数值”）。
y：y 轴数据列名（字符串，必传，如模型的 “输出结果”）。
color（可选）：按某列分组着色（如不同模型的结果用不同颜色区分）。
title（可选）：图表标题（字符串）。
labels（可选）：字典，自定义轴标签（如 {"x": "迭代次数", "y": "误差值"}）。

示例：

python
运行
import plotly.express as px
px.line(df, x="epoch", y="loss", color="model_type", title="模型训练损失趋势", labels={"epoch": "迭代轮次", "loss": "损失值"})

2. plotly.express.scatter()（散点图，分析相关性）
功能：展示两个变量的分布及相关性（如模型输入与输出的关系、特征间关联）。
参数排列及说明：

data_frame：数据源（DataFrame，必传）。
x：x 轴数据列名（必传）。
y：y 轴数据列名（必传）。
color（可选）：分组着色（如按 “类别标签” 区分点的颜色）。
size（可选）：按某列值定义点的大小（如用 “样本权重” 控制点的尺寸）。
trendline（可选）：添加趋势线（如 trendline="ols" 表示添加线性回归趋势线，辅助分析相关性）。

示例：

python
运行
px.scatter(df, x="feature1", y="target", color="category", size="weight", trendline="ols", title="特征与目标值相关性")

3. plotly.graph_objects.Figure.add_trace()（自定义轨迹，灵活绘图）
功能：通过 graph_objects 模块手动添加轨迹（如在同一图中叠加模型预测曲线与置信区间），比 express 更灵活。
常用轨迹及参数（以 Scatter 为例）：

轨迹类型：go.Scatter()
参数排列：
x：x 轴数据（数组，必传）。
y：y 轴数据（数组，必传）。
mode：点 / 线显示模式（字符串，如 "lines+markers" 表示线加标记）。
name：轨迹名称（图例中显示）。
line/marker（可选）：字典，设置线 / 点的样式（如 line=dict(color="red", width=2)）。

示例：

python
运行
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y=df["pred"], mode="lines", name="预测值", line=dict(color="blue")))
fig.add_trace(go.Scatter(x=df["x"], y=df["true"], mode="markers", name="真实值", marker=dict(color="red")))

4. plotly.express.bar()（柱状图，比较离散数据）
功能：对比不同类别或组别的数值（如不同模型的评估指标、不同参数组合的结果）。
参数排列及说明：

data_frame：数据源（DataFrame，必传）。
x：x 轴类别列名（必传，如 “模型名称”）。
y：y 轴数值列名（必传，如 “准确率”）。
color（可选）：按子类别着色（如同一模型在不同数据集上的结果）。
barmode（可选）：柱状图模式（"group" 分组并列，"stack" 堆叠，默认 group）。

示例：

python
运行
px.bar(df, x="model", y="accuracy", color="dataset", barmode="group", title="不同模型在数据集上的准确率")

5. update_layout()（更新图表布局）
功能：统一设置图表的标题、轴标签、尺寸等布局属性（通常在绘图后调用）。
常用参数排列：

title：标题（字典，如 title=dict(text="模型性能分析", font=dict(size=20))）。
xaxis/yaxis：x/y 轴设置（字典，如 xaxis=dict(title="参数λ", range=[0, 10])）。
width/height：图表宽 / 高（整数，如 width=800）。

示例：

python
运行
fig = px.line(df, x="x", y="y")
fig.update_layout(
    title=dict(text="模型输出曲线", font=dict(size=18)),
    xaxis=dict(title="输入变量", showgrid=False),
    yaxis=dict(title="输出结果"),
    width=900, height=500
)

"""