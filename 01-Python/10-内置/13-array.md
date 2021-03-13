```python
2. array(数组):
    2.1 优点:
        <1> 限制类型, 执行效率高, 利于储存
    2.2 类型使用:
        'b'         signed integer     1
        'B'         unsigned integer   1
        'u'         Unicode character  2 (see note)
        'h'         signed integer     2
        'H'         unsigned integer   2
        'i'         signed integer     2
        'I'         unsigned integer   2
        'l'         signed integer     4
        'L'         unsigned integer   4
        'q'         signed integer     8 (see note)
        'Q'         unsigned integer   8 (see note)
        'f'         floating point     4
        'd'         floating point     8
    2.3 使用(用法和list相似):
        int_arr = array.array("i")
        int_arr.append(1)
        int_arr.append(2)
        print(int_arr)
```

