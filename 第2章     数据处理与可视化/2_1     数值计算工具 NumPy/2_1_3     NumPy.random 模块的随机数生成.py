# ============== NumPy.random 模块的随机数生成 ==============

"""
1.python 内置的 random 模块可以生成随机数，但是每次只能随机生成一个，且随机数种类不够丰富
2.NumPy.random 模块可以生成随机向量，且种类丰富，如下：

常见随机数生成函数
seed(n)                                         - 设置随机数种子
beta(a, b, size=None)                           - 生成 Beta 分布随机数
chisquare(df, size=None)                        - 生成自由度为 df 的卡方分布随机数
choice(a, size=None, replace=None, p=None)      - 从 a 中有放回地随机挑选指定数量的样本
exponential(scale=1.0, size=None)               - 生成指数分布随机数
f(dfnum, dfden, size=None)                      - 生成 F 分布随机数
gamma(shape, scale=1.0, size=None)              - 生成伽马分布随机数
geometric(p, size=None)                         - 生成几何分布随机数
hypergeometric(ngood, nbad, nsample, size=None) - 生成超几何分布随机数
laplace(loc=0.0, scale=1.0, size=None)          - 生成 Laplace 分布随机数
logistic(loc=0.0, scale=1.0, size=None)         - 生成 Logistic 分布随机数
lognormal(mean=0.0, sigma=1.0, size=None)       - 生成对数正态分布随机数
negative_binomial(n, p, size=None)              - 生成负二项分布随机数
multinomial(n, pvals, size=None)                - 生成多项分布随机数
multivariate_normal(mean, cov[, size])          - 生成多元正态分布随机数
normal(loc=0.0, scale=1.0, size=None)           - 生成正态分布随机数
pareto(a, size=None)                            - 生成帕累托分布随机数
poisson(lam=1.0, size=None)                     - 生成泊松分布随机数
rand(d0, d1, ..., dn)                           - 生成 n+1 维的 [0, 1) 上均匀分布随机数
randn(d0, d1, ..., dn)                          - 生成 n+1 维的标准正态分布随机数
randint(low, high=None, size=None, dtype='l')   - 生成区间 [low, high) 上的随机整数
random_sample(size=None)                        - 生成 [0, 1) 上的随机数
standard_t(df, size=None)                       - 生成标准的 t 分布随机数
uniform(low=0.0, high=1.0, size=None)           - 生成区间 [low, high) 上均匀分布随机数
wald(mean, scale, size=None)                    - 生成 Wald 分布随机数
weibull(a, size=None)                           - 生成 Weibull 分布随机数

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.gridspec as gridspec
import matplotlib.font_manager as fm


def get_available_font():
    chinese_fonts = ["SimHei", "FangSong", "KaiTi", "Microsoft YaHei"]
    available_fonts = [f for f in chinese_fonts if f in [f.name for f in fm.fontManager.ttflist]]
    return available_fonts[0] if available_fonts else None


plt.rcParams["font.family"] = get_available_font()

# 设置中文字体
plt.rcParams["font.family"] = get_available_font()
plt.rcParams["axes.unicode_minus"] = False  # 确保负号正确显示

# 定义随机数生成函数和参数，修正了指数分布的pdf定义错误
distributions = [
    {"name": "均匀分布", "func": np.random.uniform, "params": {"low": 0, "high": 1},
     "pdf": lambda x: stats.uniform.pdf(x, 0, 1)},
    {"name": "正态分布", "func": np.random.normal, "params": {"loc": 0, "scale": 1},
     "pdf": lambda x: stats.norm.pdf(x, 0, 1)},
    {"name": "指数分布", "func": np.random.exponential, "params": {"scale": 1.0},
     "pdf": lambda x: stats.expon.pdf(x, scale=1.0)},
    {"name": "Beta分布", "func": np.random.beta, "params": {"a": 2, "b": 5}, "pdf": lambda x: stats.beta.pdf(x, 2, 5)},
    {"name": "卡方分布", "func": np.random.chisquare, "params": {"df": 5}, "pdf": lambda x: stats.chi2.pdf(x, 5)},
    {"name": "F分布", "func": np.random.f, "params": {"dfnum": 5, "dfden": 10}, "pdf": lambda x: stats.f.pdf(x, 5, 10)},
    {"name": "伽马分布", "func": np.random.gamma, "params": {"shape": 2, "scale": 1.0},
     "pdf": lambda x: stats.gamma.pdf(x, 2, scale=1.0)},
    {"name": "几何分布", "func": np.random.geometric, "params": {"p": 0.3}, "pdf": lambda x: stats.geom.pmf(x, 0.3),
     "discrete": True},
    {"name": "超几何分布", "func": np.random.hypergeometric, "params": {"ngood": 7, "nbad": 13, "nsample": 8},
     "pdf": lambda x: stats.hypergeom.pmf(x, 20, 7, 8), "discrete": True},
    {"name": "拉普拉斯分布", "func": np.random.laplace, "params": {"loc": 0, "scale": 1.0},
     "pdf": lambda x: stats.laplace.pdf(x, 0, 1.0)},
    {"name": "逻辑分布", "func": np.random.logistic, "params": {"loc": 0, "scale": 1.0},
     "pdf": lambda x: stats.logistic.pdf(x, 0, 1.0)},
    {"name": "对数正态分布", "func": np.random.lognormal, "params": {"mean": 0, "sigma": 1.0},
     "pdf": lambda x: stats.lognorm.pdf(x, 1.0, scale=np.exp(0))},
    {"name": "负二项分布", "func": np.random.negative_binomial, "params": {"n": 5, "p": 0.5},
     "pdf": lambda x: stats.nbinom.pmf(x, 5, 0.5), "discrete": True},
    {"name": "多项分布", "func": np.random.multinomial, "params": {"n": 10, "pvals": [0.2, 0.3, 0.5]}, "discrete": True,
     "special": True},
    {"name": "多元正态分布", "func": np.random.multivariate_normal, "params": {"mean": [0, 0], "cov": [[1, 0], [0, 1]]},
     "special": True},
    {"name": "帕累托分布", "func": np.random.pareto, "params": {"a": 3}, "pdf": lambda x: stats.pareto.pdf(x, 3)},
    {"name": "泊松分布", "func": np.random.poisson, "params": {"lam": 3}, "pdf": lambda x: stats.poisson.pmf(x, 3),
     "discrete": True},
    {"name": "标准t分布", "func": np.random.standard_t, "params": {"df": 3}, "pdf": lambda x: stats.t.pdf(x, 3)},
    {"name": "Wald分布", "func": np.random.wald, "params": {"mean": 1, "scale": 1.0},
     "pdf": lambda x: stats.invgauss.pdf(x, 1 / 1.0, scale=1.0)},
    {"name": "威布尔分布", "func": np.random.weibull, "params": {"a": 2}, "pdf": lambda x: stats.weibull_min.pdf(x, 2)},
]

# 生成随机样本并可视化
sample_size = 10000
plt.figure(figsize=(15, 30))
gs = gridspec.GridSpec(10, 2, hspace=0.6, wspace=0.3)

for i, dist in enumerate(distributions):
    try:
        # 生成随机样本
        if dist.get("special"):
            if dist["name"] == "多项分布":
                # 多项分布特殊处理
                sample = dist["func"](**dist["params"], size=sample_size)
                ax = plt.subplot(gs[i])
                categories = ["类别" + str(j + 1) for j in range(len(dist["params"]["pvals"]))]
                mean_counts = np.mean(sample, axis=0)
                ax.bar(categories, mean_counts)
                ax.set_title(f"{dist['name']} (n={dist['params']['n']})")
                ax.set_xlabel("类别")
                ax.set_ylabel("平均计数")
                continue
            elif dist["name"] == "多元正态分布":
                # 多元正态分布特殊处理
                sample = dist["func"](**dist["params"], size=sample_size)
                ax = plt.subplot(gs[i])
                # 绘制散点图
                ax.scatter(sample[:, 0], sample[:, 1], alpha=0.5, s=5)
                ax.set_title(f"{dist['name']} (μ={dist['params']['mean']})")
                ax.set_xlabel("X轴")
                ax.set_ylabel("Y轴")
                ax.set_aspect('equal')
                continue

        # 普通分布处理
        sample = dist["func"](**dist["params"], size=sample_size)
        ax = plt.subplot(gs[i])

        if dist.get("discrete", False):
            # 离散分布绘制直方图
            bins = np.arange(sample.min(), sample.max() + 2) - 0.5
            counts, _, _ = ax.hist(sample, bins=bins, density=True, alpha=0.6, color='skyblue')
            ax.set_title(f"{dist['name']} (样本)")
            # 绘制理论概率质量函数
            x_range = np.arange(sample.min(), sample.max() + 1)
            ax.plot(x_range, dist["pdf"](x_range), 'ro', ms=4, label='理论分布')
            ax.legend()
        else:
            # 连续分布绘制直方图和理论PDF
            ax.hist(sample, bins=50, density=True, alpha=0.6, color='skyblue')
            x_range = np.linspace(sample.min(), sample.max(), 1000)
            ax.plot(x_range, dist["pdf"](x_range), 'r-', lw=2, label='理论分布')
            ax.set_title(f"{dist['name']} (样本与理论分布)")
            ax.legend()

        ax.set_xlabel("值")
        ax.set_ylabel("密度/概率")

    except Exception as e:
        print(f"无法生成{dist['name']}的可视化: {e}")

plt.suptitle("常见概率分布可视化", fontsize=16, y=0.99)
plt.subplots_adjust(top=0.96)  # 调整布局，为suptitle留出空间
plt.savefig('probability_distributions.png', dpi=300, bbox_inches='tight')
plt.show()
