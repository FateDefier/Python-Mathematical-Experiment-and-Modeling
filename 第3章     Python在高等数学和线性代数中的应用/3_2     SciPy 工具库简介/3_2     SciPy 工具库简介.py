# =============== SciPy 工具库简介 ==================

"""
SciPy 是对 Num.Py 的功能扩展， 它提供了许多高级数学函数，
例如， 微分、积分、微分方程、优化算法、数值分析、高级统计函数、方程求解等．

SciPy 是在NumPy 数组框架的基础上实现的，它对 NumPy数组和基本的数组运算进行扩展，满足科学家和工程师解决问题时需要用到的大部分数学计算功能．

SciPy 支持的功能包括文件处理、积分、数值分析、优化方法、统计学、信号与图像处理、聚类分析和空间分析等下面简要介绍部分功能模块．
"""

"""
1.微积分模块（scipy.integrate）
（1）给定函数的数值积分（边界函数 = 把积分下限/上限写成“关于外层变量的函数”，降维思想）
| 函数                                                  | 常用参数（简版）                                                    | 说明      |
| --------------------------------------------------- | --------------------------------------------------------            | ------- |
| `quad(func, a, b, **kw)`                            | `func` 被积函数；`a,b` 积分限；`args=()` 额外参数；`epsabs, epsrel` 容差 | 一重积分    |
| `dblquad(func, a, b, gfun, hfun, **kw)`             | `gfun,hfun` y 的边界函数（或常数）；其余同上                            | 二重积分    |
| `tplquad(func, a, b, gfun, hfun, qfun, rfun, **kw)` | `qfun,rfun` z 的边界函数；其余同上                                    | 三重积分    |
| `nquad(func, ranges, **kw)`                         | `ranges=[(x0_l,x0_u), ...]` 每维上下限列表                         | N 重通用积分 |
| `fixed_quad(func, a, b, n=5)`                       | `n` 固定高斯节点数                                                 | 固定阶高斯求积 |
| `quadrature(func, a, b, **kw)`                      | `tol, rtol` 误差限；`maxiter` 最大迭代                              | 自适应高斯求积 |
（2）给定离散点的数值积分
| 函数                                     | 常用参数（简版）                                              |            说明              |
| -------------------------------------- | --------------------------------------------                 | ---------------------------- |
| `cumtrapz(y, x=None, dx=1.0, axis=-1)` | `y` 被积函数值数组；`x` 自变量坐标（可选）；`dx` 步长；`axis` 积分轴 | 梯形法求累积积分（返回与 `y` 同形状的累积积分数组） |（cumulative trapezoid）
| `simps(y, x=None, dx=1.0, axis=-1)`    | 同上                                                       | 辛普森法求一次积分值                   |
| `romb(y, dx=1.0, axis=-1)`             | `y` 必须为**2^k + 1**个均匀离散点；`dx` 步长；`axis` 积分轴      | Romberg 法求一次积分值（要求均匀采样）      |
（3）微分方程的数值解
| 函数               | 常用参数（简版）                                                           | 含义/示例                                                                         |
| ---------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **odeint**       | `odeint(func, y0, t, args=(), rtol=1e-6, atol=1e-9)`               | `func` 计算导数；`y0` 初值向量；`t` 时间序列；`args` 额外常参；`rtol/atol` 相对/绝对容差                |
| **ode**          | `ode.set_integrator('vode', rtol=1e-6, atol=1e-9)`                 | 先用 `ode(func)` 创建对象，再调用 `set_integrator` 选方法（`vode`, `lsoda`, `dopri5` 等）并设容差 |
| **complex\_ode** | `complex_ode(func).set_integrator('dop853', rtol=1e-6, atol=1e-9)` | 与 `ode` 完全一致，只是支持复数初值与复微分方程                                                   |

"""

# 查看函数的用法（如 romberg）（控制台输入）
# from scipy.integrate import romberg
# help(romberg)

"""
2.线性代数模块
与 numpy.linalg 相比， scipy.linalg 函数有更高级的特征
| 函数                   | 典型调用                                     | 一句话功能                            | 高级特性（相对 np.linalg）      |   
| -------------------- | ---------------------------------------- | -------------------------------- | -------------------------------------- | 
| `linalg.solve(A, b)` | `x = solve(A, b)`                        | **解线性方程组** Ax = b                | 自动选 LU / Cholesky / Bunch-Kaufman，更快更稳 |   
| `linalg.inv(A)`      | `Ainv = inv(A)`                          | **求矩阵逆** A⁻¹                     | 支持 `overwrite_a=True` 省内存              |   
| `linalg.det(A)`      | `det(A)`                                 | **算行列式**                         | 大矩阵可选 `overwrite_a=True` 省 RAM     |   | |
| `linalg.eig(A[,B])`  | `vals, vecs = eig(A)`                    | **求特征值/向量**；可选广义特征值              | 支持广义特征值 `eig(A, B)`          |   
| `linalg.svd(A)`      | `U, s, Vh = svd(A, full_matrices=False)` | **奇异值分解** A = U Σ Vᴴ             | 可选 `lapack_driver`；支持截断 SVD        |   
| `linalg.cholesky(A)` | `L = cholesky(A, lower=True)`            | **Cholesky 分解** A = L Lᵀ（正定矩阵专用） | 支持选主元，稳定性更好                   |   

"""

"""
3.优化模块（scipy.optimize）
 SciPy 的优化模块提供了解决单变量和多变量的目标函数最小值问题的功能．
它通过大量的算法解决最小化问题．优化模块支持线性回归、搜索函数的最大值与最小值、方程求根、线性规划、拟合等功能
| 功能            | 典型函数                                                                     | 常用参数速记                                                           | 适用数据/场景    |
| ------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------- | ---------- |
| **单变量最小值**    | `minimize_scalar(fun, bounds=None, method='brent')`                      | `fun` 标量函数；`bounds` 搜索区间；`method='brent'`/`'golden'`/`'bounded'` | 一元函数极值、调参  |
| **多变量最小值**    | `minimize(fun, x0, method='BFGS', bounds=None, constraints=())`          | `fun` 多元函数；`x0` 初值；`bounds` 元组列表；`constraints` dict 或 list       | 多元无/有约束优化  |
| **线性规划**      | `linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)`                             | `c` 目标系数；`A_ub/b_ub` 不等式；`A_eq/b_eq` 等式；`bounds` 变量上下界           | 资源分配、运输问题  |
| **非线性最小二乘拟合** | `least_squares(fun, x0, bounds=(-np.inf, np.inf))`                       | `fun` 残差函数；`x0` 初值；`bounds` 同 minimize                           | 曲线/曲面拟合    |
| **方程求根**      | `root(fun, x0, method='hybr')`                                           | `fun(x)=0` 方程组；`x0` 初值；`method` 选算法                              | 非线性方程组     |
| **全局优化**      | `differential_evolution(func, bounds, strategy='best1bin')`              | `func` 目标；`bounds` 列表/Bounds 对象                                  | 多峰、非凸、黑箱函数 |
| **带约束非线性规划**  | `minimize(..., constraints={'type':'eq/ineq', 'fun':g}, method='SLSQP')` | 同 2，但加 `constraints`                                             | 设计优化、工艺约束  |

"""

"""
4.插值模块（scipy.interpolate）
插值模块支持一维和多维插值，例如，泰勒 (Taylor) 多项式插值，一维和多维样条插值
| 功能              | 典型函数                                            | 常用参数                                                                | 适用场景          |
| --------------- | ----------------------------------------------- | ------------------------------------------------------------------- | ------------- |
| **一维泰勒多项式**     | `TaylorPolynomial(f, x0, n)`（需自行实现）             | 无官方实现                                                               | 教学演示          |
| **一维线性插值**      | `interp1d(x, y, kind='linear')`                 | `x, y` 数据；`kind` 选 'linear'/'nearest'/'slinear'/'quadratic'/'cubic' | 快速曲线补点        |
| **一维样条**        | `UnivariateSpline(x, y, s=0)`                   | `x, y` 数据；`s` 平滑因子；`k` 阶数（默认 3）                                     | 平滑曲线、信号拟合     |
| **一维 B-Spline** | `make_interp_spline(x, y, k=3)`                 | `k` 阶数；`bc_type` 边界条件                                               | 精确通过所有点且光滑    |
| **多维线性插值**      | `griddata(points, values, xi, method='linear')` | `points` (N×D)；`values` (N,)；`xi` 查询网格                              | 散乱 2D/3D 数据补洞 |
| **多维样条**        | `RectBivariateSpline(x, y, Z, kx=3, ky=3)`      | `x, y, Z` 网格数据；`kx, ky` 阶数                                          | 规则网格 2D 曲面    |
| **多维平滑样条**      | `SmoothBivariateSpline(x, y, z, s=None)`        | 同上，但可带平滑因子 `s`                                                      | 含噪声 2D 数据平滑   |
| **任意维样条**       | `Rbf(*args, function='multiquadric')`           | `function` 选核函数                                                     | 任意维散乱点插值      |

"""

"""
5.统计学模块（scipy.stats）
统计模块提供了各种随机变量的分布、统计量的计算、分布拟合、参数检验等功能
| 功能        | 典型子模块 / 函数                                            | 常用参数                                                              | 适用场景            |
| --------- | ----------------------------------------------------- | ----------------------------------------------------------------- | --------------- |
| **连续分布**  | `stats.norm(loc, scale)` 等 100+ 分布                    | `loc` 均值，`scale` 标准差，`rvs(size)` 随机样本，`pdf(x)` 概率密度，`cdf(x)` 累积概率 | 正态、指数、伽玛、贝塔等    |
| **离散分布**  | `stats.poisson(mu)` / `stats.binom(n, p)`             | `mu`, `n`, `p`；`pmf(k)` 概率质量函数，`rvs(size)` 随机整数                   | 泊松、二项、几何、超几何等   |
| **随机数**   | `rvs(size=1000)`                                      | 任意分布对象的 `.rvs()` 方法                                               | 蒙特卡洛模拟          |
| **统计量**   | `stats.describe(a)` / `stats.mode(a)`                 | 数组或列表                                                             | 均值、方差、偏度、峰度、众数  |
| **分位数**   | `stats.scoreatpercentile(a, 50)` 或 `np.percentile`    | 任意分位点                                                             | 中位数、四分位距        |
| **分布拟合**  | `dist.fit(data)`                                      | 任意分布对象的 `.fit()`                                                  | 参数估计（MLE）       |
| **假设检验**  | `stats.ttest_ind(a, b)` / `stats.kstest(sample, cdf)` | 两组样本或样本与 CDF                                                      | t 检验、KS 检验、卡方检验 |
| **核密度估计** | `stats.gaussian_kde(data)`                            | 一维或多维数组                                                           | 非参数概率密度估计       |
| **回归诊断**  | `stats.linregress(x, y)`                              | 两列数据                                                              | 线性回归斜率、截距、R²    |

"""

"""
6.傅里叶变换模块（scipy.fftpack）
离散傅里叶变换和离散傅里叶逆变换可以分别用 fft 和 ifft 函数来计算．
| 功能          | 典型函数                                      | 常用参数                         | 适用场景     |
| ----------- | ----------------------------------------- | ---------------------------- | -------- |
| **一维 FFT**  | `scipy.fft.fft(x, n=None, axis=-1)`       | `x` 输入序列；`n` 补零长度；`axis` 变换轴 | 频谱分析、滤波  |
| **一维 IFFT** | `scipy.fft.ifft(x, n=None, axis=-1)`      | 同上                           | 信号还原、逆变换 |
| **二维 FFT**  | `scipy.fft.fft2(x, s=None, axes=(-2,-1))` | `s` 补零尺寸；`axes` 变换轴对         | 图像频域处理   |
| **二维 IFFT** | `scipy.fft.ifft2(...)`                    | 同上                           | 图像还原     |
| **多维 FFT**  | `scipy.fft.fftn(x, s=None, axes=None)`    | 任意维                          | 高维频域分析   |
| **多维 IFFT** | `scipy.fft.ifftn(...)`                    | 同上                           | 高维逆变换    |
| **实数 FFT**  | `scipy.fft.rfft(x, n=None, axis=-1)`      | 仅返回正频率部分                     | 实序列省内存   |
| **实数 IFFT** | `scipy.fft.irfft(...)`                    | 同上                           | 从实频谱还原   |

"""

"""
7.信号处理模块(scipy.signal)
信号处理模块包含一系列滤波函数、滤波器设计函数，以及对一维和二维数据进行B样条插值的函数这个模块包含的函数可以进行以下操作：
卷积、 B－样条、滤波、滤波器设计、 MATLAB 式的 IIR 滤波器设计、连续时间的线性系统、离散时间的线性系统、线性时不变系统、信号波形、窗函数、小波分析和光谱分析等．
| 功能            | 典型函数                                  | 常用参数                        | 一句话用法示例                                       |
| ------------- | ------------------------------------- | --------------------------- | --------------------------------------------- |
| **卷积**        | `convolve(in1, in2, mode='full')`     | `mode='same'/'valid'`       | `convolve(x, h, mode='same')` 一维卷积            |
| **B-样条**      | `bspline(x, n)`                       | `n` 阶数                      | `bspline(np.arange(10), 3)` 三次 B-样条基          |
| **滤波**        | `lfilter(b, a, x)`                    | `b, a` 滤波器系数；`x` 信号         | `lfilter([1, -1], [1], x)` 一阶差分               |
| **IIR 滤波器设计** | `butter(N, Wn, btype='low')`          | `N` 阶；`Wn` 归一化截止；`btype` 类型 | `butter(4, 0.2, 'high')` 高通巴特沃斯               |
| **FIR 滤波器设计** | `firwin(numtaps, cutoff)`             | `numtaps` 长度；`cutoff` 截止    | `firwin(51, 0.3)` 51 点低通 FIR                  |
| **连续 LTI 系统** | `TransferFunction(num, den)`          | `num, den` 分子/分母多项式         | `sys = TransferFunction([1], [1, 2, 1])`      |
| **离散 LTI 系统** | `dlti(num, den, dt=0.1)`              | `dt` 采样周期                   | `dlti([1], [1, -0.5], dt=0.01)`               |
| **冲激/阶跃响应**   | `impulse(sys) / step(sys)`            | `sys` 为 LTI 对象              | `t, y = impulse(sys)`                         |
| **窗函数**       | `hamming(M)` / `hann(M)`              | `M` 长度                      | `win = hamming(256)`                          |
| **频谱分析**      | `welch(x, fs=1.0)`                    | `fs` 采样率；返回频率、功率谱           | `f, Pxx = welch(sig, fs=1000)`                |
| **小波**        | `cwt(data, scales, wavelet='morlet')` | `scales` 尺度序列               | `coefs = cwt(sig, np.arange(1,31), 'morlet')` |

"""

"""
8.多维图像处理模块（scipy.ndimage）
通常图像处理可以看作对二维数组的操作．这个模块提供了图像处理的各种函数，例如，图像几何变换、图像滤波等
| 功能           | 典型函数                                              | 常用参数                           | 示例（灰度图 `img` 为 2-D ndarray）                       |
| ------------ | ------------------------------------------------- | ------------------------------ | ------------------------------------------------- |
| **几何变换**     | `rotate(img, angle)`                              | `angle` 旋转角（度）；`reshape=False` | `rotate(img, 45)` 逆时针旋转 45°                       |
| **缩放**       | `zoom(img, zoom)`                                 | `zoom` 缩放因子（>1 放大）             | `zoom(img, 0.5)` 缩小一半                             |
| **平移**       | `shift(img, offset)`                              | `offset=(dy, dx)` 像素偏移         | `shift(img, (10, -5))` 下移 10 右移 5                 |
| **高斯滤波**     | `gaussian_filter(img, sigma)`                     | `sigma` 标准差                    | `gaussian_filter(img, 2)` 平滑去噪                    |
| **中值滤波**     | `median_filter(img, size)`                        | `size=3` 邻域窗口                  | `median_filter(img, 3)` 去椒盐噪                      |
| **Sobel 边缘** | `sobel(img, axis=-1)`                             | `axis=0/1` 沿行/列求导              | `sobel(img, axis=1)` 水平边缘                         |
| **拉普拉斯**     | `laplace(img)`                                    | 无                              | `laplace(img)` 二阶边缘检测                             |
| **通用卷积**     | `convolve(img, kernel)`                           | `kernel` 任意核数组                 | `convolve(img, [[1,1,1],[1,1,1],[1,1,1]])/9` 均值模糊 |
| **形态学**      | `binary_erosion/ dilation(binary_img, structure)` | `structure` 结构元素               | `binary_erosion(mask, ones((3,3)))` 腐蚀            |
| **统计滤波**     | `generic_filter(img, func, size)`                 | `func=np.std` `size=5`         | `generic_filter(img, np.std, 3)` 局部标准差            |

"""

"""
9.空间分析模块（scipy.spatial）
空间分析是一系列用于分析空间数据的算法．空间数据是指和地理空间或垂直空间相关的数据对象．这种数据包括点、线、多边形、其他几何和地理特征信息．
该模块支持 Delaunay 三角剖分、 Voronoi 图、 N 维凸包等功能， 支待 KD 树(scipy.spatial.kdtree) 实现快速近邻查找算法，还可以对初始向量集合进行距离矩阵的计算
| 功能                | 典型函数                                         | 常用参数                        | 一句话示例                                                   |
| ----------------- | -------------------------------------------- | --------------------------- | ------------------------------------------------------- |
| **Delaunay 三角剖分** | `Delaunay(points)`                           | `points` 二维或 N 维坐标数组        | `tri = Delaunay(xy)` 生成三角形网格                            |
| **Voronoi 图**     | `Voronoi(points)`                            | `points` 同上                 | `vor = Voronoi(xy)` 生成泰森多边形                             |
| **凸包计算**          | `ConvexHull(points)`                         | `points` 同上                 | `hull = ConvexHull(xy)` 得最小凸多边形                         |
| **KD-树近邻搜索**      | `KDTree(data)`                               | `data` 坐标数组；`leafsize` 节点大小 | `tree = KDTree(xy); idx = tree.query_ball_point(pt, r)` |
| **距离矩阵**          | `distance.cdist(XA, XB, metric='euclidean')` | `metric` 可选欧氏、曼哈顿、切比雪夫等     | `D = cdist(A, B)` 得两两距离矩阵                               |
| **绘图辅助**          | `delaunay_plot_2d(tri)`                      | `tri` Delaunay 对象           | `delaunay_plot_2d(tri)` 一键画三角网                          |


"""

"""
10.聚类模块
聚类是将一个大的集合分成多个组的过程． SciPy 聚类模块包括两个子模块：
向量量化 (vector quantization, VQ)(scipy.cluster.vq) 和层次聚类 (scipy.cluster. hierarchy). 
VQ 模块支持 K 均值聚类和向量量化， 层次聚类模块支持分层聚类和聚合聚类
| 功能         | 子模块                       | 典型函数                                             | 常用参数                                            | 一句话示例                                           |
| ---------- | ------------------------- | ------------------------------------------------ | ----------------------------------------------- | ----------------------------------------------- |
| **K-均值聚类** | `scipy.cluster.vq`        | `vq.kmeans2(data, k)`                            | `data` 样本矩阵；`k` 簇数；`minit='++'` 初始化             | `centroids, labels = kmeans2(X, 3)`             |
| **向量量化**   | `scipy.cluster.vq`        | `vq.vq(obs, code_book)`                          | `obs` 观测；`code_book` 质心                         | `codes, dist = vq(X, centroids)`                |
| **层次聚类**   | `scipy.cluster.hierarchy` | `hierarchy.linkage(y, method='ward')`            | `y` 距离向量或矩阵；`method='ward'/'single'/'complete'` | `Z = linkage(pdist(X), 'ward')`                 |
| **绘制树状图**  | `scipy.cluster.hierarchy` | `hierarchy.dendrogram(Z)`                        | `Z` 上一步的 linkage 结果                             | `dendrogram(Z)` 一键可视化                           |
| **切分树**    | `scipy.cluster.hierarchy` | `hierarchy.fcluster(Z, t, criterion='maxclust')` | `t` 簇数或距离阈值                                     | `labels = fcluster(Z, 4, criterion='maxclust')` |

"""

"""
11.文件输入/输出模块（scipy.io）
该模块支待一系列格式文件的读和写这些格式文件包括： MATLAB 文件、ALD 文件、Matrix Market 文件、无格式的 FORTRAN 文件、 WAV 声音文件、ARFF文件和 NetCDF 文件
SciPy 可以使用 MATLAB 的 ".mat" 文件格式读取和写入数据，函数为 load-mat 和 savemat. 
| 功能                  | 典型函数                                    | 常用参数                           | 一句话示例                                                          |
| ------------------- | --------------------------------------- | ------------------------------ | -------------------------------------------------------------- |
| **读写 MATLAB .mat**  | `loadmat(file)` / `savemat(file, dict)` | `file` 路径；`dict` 变量字典          | `data = loadmat('data.mat')`                                   |
| **读 Matrix Market** | `mmread(file)`                          | `file` .mtx 路径                 | `A = mmread('A.mtx')` 稀疏/密集矩阵                                  |
| **写 Matrix Market** | `mmwrite(file, matrix)`                 | `file` 输出路径；`matrix` 任意数组      | `mmwrite('out.mtx', A)`                                        |
| **读 WAV 音频**        | `wavfile.read(file)`                    | `file` .wav 路径                 | `rate, data = wavfile.read('sound.wav')`                       |
| **写 WAV 音频**        | `wavfile.write(file, rate, data)`       | `rate` 采样率；`data` 一维/二维数组      | `wavfile.write('new.wav', 44100, y)`                           |
| **读 NetCDF**        | `netcdf_file(file, mode='r')`           | `file` 路径；返回类字典对象              | `nc = netcdf_file('data.nc'); t = nc['time'][:]`               |
| **读 ARFF**          | `arff.loadarff(file)`                   | `file` .arff 路径                | `data, meta = arff.loadarff('dataset.arff')`                   |
| **读写无格式 FORTRAN**   | `FortranFile(file, mode='r')`           | `file` 路径；`read_record(dtype)` | `with FortranFile('data.bin') as f: rec = f.read_record('f4')` |

"""

# 加载数据
import scipy.io
# 返回 data 是一个字典，盖子点包含了与“.mat”文件相关的变量名对应的键，对应值为NumPy数组格式
# data = scipy.io.loadmat('nasty_duplicate_fieldnames.mat')
# print(data)

# 保存数据到".mat"文件要创建一个包含要储存的所有变量的字典（变量名和值），函数为 savemat
# 下面是保存数组 x 和 y
# data = {}
# x = ([1, 2, 3], [4, 5, 6])
# y = ([9], [8], [7])
# data['x'] = x
# data['y'] = y
# scipy.io.savemat('datafile.mat', data)

"""
还有其他一些模块：如附件模块 (scipy.misc)，实现图形读写操作功能；稀疏矩阵及
其相关算法模块 (scipy.sparse)；特殊函数模块 (scipy. special) 等．
"""
