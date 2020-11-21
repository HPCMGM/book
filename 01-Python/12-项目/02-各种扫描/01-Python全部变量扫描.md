```python
# coding=utf-8
import os

def search_params(base_dir, import_module):
    """获取所有根目录下的某个模块中的所有的变量"""
    from sys import path
    path.append(base_dir)  # 写入路径到系统
    list_file = os.listdir(path=base_dir)
    param_list = []
    for file in list_file:
        a = base_dir + "/" + file
        # 获取子文件夹
        if os.path.isdir(a):

            # 获取子文件中存在views.py视图函数模块
            if import_module + ".py" in os.listdir(path=a):
                list_main = set(dir())
                print(file + "." + import_module)
                try:
                    views = __import__(file + "." + import_module, globals(), locals(), [import_module])
                except Exception as error:
                    raise Exception(error)
                list_all = set(dir(views))
                # 排除本模块中的参数影响
                list_view = [param for param in list_all.difference(list_main) if
                             param[:1] != "_" and param != "list_main"]

                # print(list_view)
                for view in list_view:
                    view_path = file + "." + import_module
                    view = getattr(views, view)
                    path = view.__module__
                    # 获取变量所在模块, 必须在file下的views中
                    # print(path, view_path)
                    if path == view_path:
                        param_list.append(view.__name__)
    return param_list


if __name__ == '__main__':
    # print(search_params(os.path))
    base_dir = os.path.dirname(os.getcwd())
    print(base_dir)
    print(search_params(base_dir, "resupper"))
```

