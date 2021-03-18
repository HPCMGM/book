# numpy

基于C语言编写, 解除了GIL锁, 效率远高于CPython, 此模块主要用于:

* numpy支持量化运算
* 多维数组处理, 比原生list要快, list是使用引用, numpy使用的是内存块

```python
import numpy as np
a = list(range(100))
b = np.array(list(range(100)))
%timeit sum(a)
%timeit sum(b)
```

输出

```shell
212 ns ± 1.78 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
2.99 µs ± 44.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```



