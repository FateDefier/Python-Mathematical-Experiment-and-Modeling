# =================== 随机变量及其分布 ====================

"""
NumPy 能生成一定概率分布的随机数，但如果需要更具体的概率密度、分布函数等，就用到了 scipy.stats(statistics)

Python 做简单的统计分析也可以使用 scipy.stats 模块（第四章介绍）

scipy.stats 模块包含了多种概率分布的随机变量，随机变量分为连续型和离散型两种

所有的连续型随机变量都是 rv_continuous（random variable continuous连续型随机变量） 的派生类的对象

所有的离散型随机变量都是 rv_discrete (random variable discrete离散型随机变量)的派生类的对象
"""

"""
1.连续型随机变量及其分布
"""

# ====== 控制台输入以下代码可查看 scipy.stats 模块所有的连续型随机变量（总数：90多个） ===========
# from scipy import stats
# [k for k, v in stats.__dict__.items() if isinstance(v, stats.rv_continuous)]

"""
连续型随机变量对象都有如下方法．
rvs（Random Variates Sample）: 产生随机数样本，可以通过 size 参数指定输出的数组的大小
pdf（Probability Density Function）: 随机变量的概率密度函数．
cdf（Cumulative Distribution Function）:累积分布函数， 随机变量的分布函数．
sf（Survival Function）: 随机变量的生存函数，它的值是 1-cdf.
ppf（Percent-Point Function）:分位点(分位数)函数（CDF 的反函数），分布函数的反函数．
stat（Statistics）: 统计量（返回期望、方差等），计算随机变量的期望和方差
fit（Fit）: 参数拟合（极大似然估计），对一组随机样本利用极大似然估计法，估计总体中的未知参数．

    常用连续型随机变量的概率密度函数
分布名称  | 关键字        | 调用方式
----------|---------------|-----------------------------------------------------------------------
均匀分布  | uniform.pdf   | uniform.pdf(x, a, b)       # [a, b] 区间
指数分布  | expon.pdf     | expon.pdf(x, theta)        # 期望 theta               （exponent 指数）
正态分布  | norm.pdf      | norm.pdf(x, mu, sigma)     # 均值 mu，标准差 sigma
χ² 分布   | chi2.pdf      | chi2.pdf(x, n)             # 自由度 n
t 分布    | t.pdf         | t.pdf(x, n)                # 自由度 n
F 分布    | f.pdf         | f.pdf(x, m, n)             # 自由度 m, n
Gamma 分布| gamma.pdf     | gamma.pdf(x, A, B)         # 形状 A，尺度 B
"""

"""
2.离散性随机变量及其分布
在 scipy.stats 模块中所有描述离散分布的随机变量都从rv_discrete 类继承，也可以直接用 rv_discrete 类自定义离散概率分布．

========== 正态分布（normal distribution） ===========对应的相关函数
功能        | 调用方式
------------|----------------------------------------------------------
概率密度    | norm.pdf(x, mu, sigma)        # 均值 mu，标准差 sigma
分布函数    | norm.cdf(x, mu, sigma)        # 均值 mu，标准差 sigma
分位数      | norm.ppf(alpha, mu, sigma)    # 均值 mu，标准差 sigma 下的 alpha 分位数
随机数      | norm.rvs(mu, sigma, size=N)   # 生成 N 个正态随机数
最大似然估计 | norm.fit(a)                   # 对样本数组 a 估计 mu 与 sigma

| 分布名称 | SciPy 关键字     | 调用方式（概率质量函数）                     | 参数说明                            |
| ---- | ------------- | -------------------------------- | ------------------------------- |
| 二项分布 | `binom.pmf`   | `scipy.stats.binom.pmf(k, n, p)` | `k`：成功次数；`n`：总试验次数；`p`：单次成功概率   |（binomial probability mass function）
| 几何分布 | `geom.pmf`    | `scipy.stats.geom.pmf(k, p)`     | `k`：首次成功所需的试验次数（≥1）；`p`：单次成功概率  |（geometry probability mass function）
| 泊松分布 | `poisson.pmf` | `scipy.stats.poisson.pmf(k, mu)` | `k`：事件次数；`mu`（λ）：单位时间/空间内平均发生次数 |（possion probability mass function）

"""

# # ====== 控制台输入以下代码可查看 scipy.stats 模块所有的离散型随机变量（总数：14个） ===========
# from scipy import stats
# [k for k, v in stats.__dict__.items() if isinstance(v, stats.rv_discrete)]
"""
'binom',
 'bernoulli',
 'betabinom',
 'nbinom',
 'geom',
 'hypergeom',
 'nhypergeom',
 'logser',
 'poisson',
 'planck',
 'boltzmann',
 'randint',
 'zipf',
 'zipfian',
 'dlaplace',
 'skellam',
 'yulesimon',
 'nchypergeom_fisher',
 'nchypergeom_wallenius'
"""
