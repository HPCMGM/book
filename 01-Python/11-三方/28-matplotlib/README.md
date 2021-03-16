# matplotlib

Python专用的绘图工具, 开源免费.

* 2D绘图
* 渐进式, 交互式

其他常见的工具:

* matlab
* 网页绘图: d3, echarts, javascripts
* seaborn: 基于matplotlib
* pandas: 基于matplotlib



# helloword

```python
import matplotlib.pyplot as plt


plt.figure(figsize=(20, 8), dpi=100)
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("name.png") # 此步骤必须放在show之前, 否则会保存空图片
plt.show()
```

# 安装

```shell
pip install matplotlib
```

## 解决中文显示问题

#### 方法一

指定使用的字体库

```shell
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
```



#### 方法二

1. 下载中文字体包: https://fontzone.net/download/simhei

2. 安装字体

   * linux

     ```shell
     cp ~/SimHei.ttf /usr/share/fonts/SimHei.ttf
     ```

   * windows: 双击安装

3. 删除缓存

   * 方法一

     ```shell
     cd ~/.matplotlib
     rm -rf *
     ```

   * 方法二

     ```shell
     # 运行如下代码
     import matplotlib as mpl
     mpl.get_cachedir()   # 将此路径下的文件删除
     mpl.matplotlib_fname()   # 将此数据添加到步骤4中
     ```

4. 配置文件

   ```shell
   vim ~/.matplotlib/matplotlibrc
   # 添加如下信息
   font.family         : sans-serif
   font.sans-serif     : SimHei
   axes.unicode_minus  : False
   ```

   