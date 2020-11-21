```python
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/1/30 13:06
#
import zipfile
import os
import re
import shutil
import xlrd
import xlwt

base_dir = os.path.dirname(os.path.abspath(__file__))
name = "{}.docx".format(input("请输入word文件名:\n"))
reco_path = "word\document.xml"
excel_path = input("请输入excel文件名:\n")+".xls"


def get_path(name):
    return os.path.join(base_dir, name)


def rename(name):
    path = get_path(name)
    os.rename(path, path + ".zip")

def unzip(name):
    path = get_path(name + ".zip")
    f = zipfile.ZipFile(path, "r")
    for file in f.namelist():
        f.extract(file, "")
    f.close()


def replace_content(addr, username):
    with open(reco_path, "r", encoding="utf-8") as f:
        content = f.read()
        content = re.sub(r"一一", addr[0], content, re.S)
        content = re.sub(r"壹壹", username[0], content, re.S)

        content = re.sub(r"二二", addr[1], content, re.S)
        content = re.sub(r"贰贰", username[1], content, re.S)

        content = re.sub(r"三三", addr[2], content, re.S)
        content = re.sub(r"叁叁", username[2], content, re.S)

        content = re.sub(r"四四", addr[3], content, re.S)
        content = re.sub(r"肆", username[3], content, re.S)

        content = re.sub(r"五五", addr[4], content, re.S)
        content = re.sub(r"伍伍", username[4], content, re.S)

        content = re.sub(r"六六", addr[5], content, re.S)
        content = re.sub(r"陆陆", username[5], content, re.S)

        content = re.sub(r"七七", addr[6], content, re.S)
        content = re.sub(r"柒柒", username[6], content, re.S)

        content = re.sub(r"八八", addr[7], content, re.S)
        content = re.sub(r"捌捌", username[7], content, re.S)
    with open(reco_path, "w", encoding="utf-8") as f:
        f.write(content)
    addr.clear()
    username.clear()


def zip_file(name):
    f = zipfile.ZipFile(get_path(name), 'w', zipfile.ZIP_DEFLATED)
    for i in os.listdir(get_path("_rels")):
        f.write("_rels\\" + i)
    for i in os.listdir(get_path("customXml")):
        if os.path.isdir("customXml\\" + i):
            for a in os.listdir(get_path("customXml\\{}".format(i))):
                f.write("customXml\\{}\\".format(i) + a)
        else:
            f.write("customXml\\" + i)
    for i in os.listdir(get_path("docProps")):
        f.write("docProps\\" + i)
    for i in os.listdir(get_path("word")):
        if os.path.isdir("word\\" + i):
            for a in os.listdir(get_path("word\\{}".format(i))):
                f.write("word\\{}\\".format(i) + a)
        else:
            f.write("word\\" + i)
    f.write("[Content_Types].xml")
    f.close()
    shutil.rmtree("_rels")
    shutil.rmtree("customXml")
    shutil.rmtree("docProps")
    shutil.rmtree("word")
    os.remove("[Content_Types].xml")


def read_excel(exc_path):
    workbook = xlrd.open_workbook(exc_path)
    sheet = workbook.sheet_by_index(1)
    addrs = []
    usernames = []
    a = 1
    is_stop = False
    for i in range(1, sheet.nrows):
        addr, username = sheet.row_values(i)[1:]
        if not any([addr, username]):
            if is_stop is True:
                break
            is_stop = True
        addrs.append(addr)
        usernames.append(username)
        if len(addrs) == 8:
            print(addrs, usernames)
            unzip(name)
            replace_content(addrs, usernames)
            new_file = name.split(".")[0] + str(a) + ".docx"
            zip_file(new_file)
            a += 1
    if addrs:
        addrs += [""] * (8 - len(addrs))
        usernames += [""] * (8 - len(usernames))
        unzip(name)
        replace_content(addrs, usernames)
        new_file = name.split(".")[0] + str(a) + ".docx"
        zip_file(new_file)


rename(name)
read_excel(excel_path)
os.rename(name + ".zip", name)
# os.remove(name + ".zip")
```

