# NetworkX

networkx库主要用于绘制复杂拓扑图, 注意需要和matplotlib联合使用

**官网教程**: https://www.osgeo.cn/networkx/tutorial.html

#### helloworld

```python
import networkx as nx
import matplotlib.pyplot as plt

nodes = (
    "A",
    "B",
    "C"
)

g = nx.DiGraph()
[g.add_node(node) for node in nodes]

edges = (
    ("A", "B"),
    ("A", "C"),
    ("C", "B")
)

g.add_edges_from(edges)
```

输出

![image-20210320191533187](image/README/image-20210320191533187.png)