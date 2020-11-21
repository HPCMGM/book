```bash
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2020/5/21 18:53
import os
import re
import time

import win32gui
import win32process


def get_pids(title):
    """
    利用窗口名称, 获取程序对应的pid
    :param title: 窗体名称
    :return: pids列表
    """
    pids = []

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            text = win32gui.GetWindowText(hwnd)
            # print(text.encode(), title.encode(), text.encode()==title.encode(), end="\n\n")
            if re.findall(title, text):
                pids.append(win32process.GetWindowThreadProcessId(hwnd))

    win32gui.EnumWindows(get_all_hwnd, 0)
    return pids


def kill_process(title):
    """
    结束进程
    :param title: 窗体名称
    :return:
    """
    print("正在结束进程!")
    pids_list = get_pids(title)
    print(pids_list)
    for pids in pids_list:
        for pid in pids:
            os.system("taskkill /F /pid:{}".format(pid))
    time.sleep(1)
    if not get_pids(title):
        print("进程已终止!")
    else:
        print("进程不可终止!")


def start_process(title, cmd):
    """
    启动进程
    :param title: 窗体名称
    :return:
    """
    print("准备启动进程!")
    os.system("start {}".format(cmd))
    time.sleep(2)
    if get_pids(title):
        print("进程已启动!")
    else:
        print("进程启动失败!")


with open(r"E:\cron\config.cfg", "r", encoding="utf-8-sig") as f:
# with open(r"E:\project\code\test\t_win32\config.cfg", "r", encoding="utf-8") as f:
    for content in f.read().split("\n"):
        title, cmd = content.rsplit("###")
        print(title)
        title = title.strip()
        cmd = cmd.strip()
        kill_process(title)
        start_process(title, cmd)
```

