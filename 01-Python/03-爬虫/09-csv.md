```python
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def json_to_csv():
    json_file = open("lagou.json", "r")
    csv_file = open("lagou.csv", "w")

    try:
        item_list = json.load(json_file)
        # 随便取出一组key当做表头
        head_data = item_list[0].keys()
        # 将value取出
        value_data = [item.values() for item in item_list]
        # 获取写入文件的文件对象
        csv_writer = csv.writer(csv_file)
        # 写入表头
        csv_writer.writerow(head_data)
        # 写入正文, 由于正文中的value有可能为unicode, 需要转化成转化成str, 但是在列表中没有方法直接转码, 那就直接修改当前环境中的编码方式
        # 将ascii码修改为utf-8
        csv_writer.writerows(value_data)
    finally:
        json_file.close()
        csv_file.close()

if __name__ == "__main__":
    json_to_csv()
```

