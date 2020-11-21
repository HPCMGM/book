```python
# coding=utf-8
import os
import time
from datetime import datetime

import psutil

base_dir = os.path.dirname(os.path.abspath(__file__))


class SystemInfo(object):
    """获取当前主机的信息"""

    def __init__(self):
        self.cpu_file = "cpu"
        self.mem_file = "mem"

    @staticmethod
    def cpu(fp, c_t):
        """获取cpu信息"""
        content = "{}-->{}\n".format(c_t.strftime("%Y-%m-%d %H:%M:%S"), psutil.cpu_percent(1))
        print("cpu", content, end="")
        fp.write(content)
        fp.flush()

    @staticmethod
    def mem(fp, c_t):
        """获取内存信息"""
        content = "{}-->{}\n".format(c_t.strftime("%Y-%m-%d %H:%M:%S"), psutil.virtual_memory().percent)
        print("mem", content, end="")
        fp.write(content)
        fp.flush()

    @staticmethod
    def get_file_name(current_time, name):
        """获取文件名称"""
        base_save_path = os.path.join(base_dir, current_time.strftime("%Y-%m-%d"))
        if os.path.exists(base_save_path) is False:
            os.makedirs(base_save_path)
        return os.path.join(base_save_path, "{}_{}.txt".format(name, current_time.strftime("%Y%m%d%H")))

    def write_file(self, current_time, count, name):
        """写入文件"""
        file_name = self.get_file_name(current_time, name)
        content = "{}-->{}\n".format(current_time.strftime("%Y-%m-%d %H:%M"), count)
        print("[INFO] {}".format(content))
        with open(file_name, "a+") as f:
            f.write(content)
            f.flush()

    def loop_write(self):
        """循环写入"""
        f1 = f2 = None
        try:
            while True:
                c_t = datetime.now()
                cpu_file = self.get_file_name(c_t, "cpu")
                mem_file = self.get_file_name(c_t, "mem")
                if f1 is None:
                    f1 = open(cpu_file, "a+")
                    f2 = open(mem_file, "a+")
                elif os.path.exists(cpu_file) is False:
                    self.file_close(f1, f2)
                    f1 = open(cpu_file, "a+")
                    f2 = open(mem_file, "a+")
                self.cpu(f1, c_t)
                self.mem(f2, c_t)
                time.sleep(5)
        finally:
            self.file_close(f1, f2)

    @staticmethod
    def file_close(f1, f2):
        """文件强制关闭"""
        try:
            f1.close()
            f2.close()
        except AttributeError:
            pass

    def start(self):
        """启动器"""
        self.loop_write()


if __name__ == '__main__':
    SystemInfo().start()

```

