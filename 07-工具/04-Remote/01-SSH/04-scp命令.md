# 1. scp

## 1.1 参数说明

```bash
scp [选项] [参数]
```

* -r: 对文件夹执行上传/下载操作

## 1.2 示例

### 1.2.1 上传

```bash
scp -r C:/Users/w5659/Desktop/import_img bsodgm@192.168.182.132:/home/bsodgm/Desktop/ 
```

### 1.2.2 下载

```bash
scp -r bsodgm@192.168.182.132:/home/bsodgm/Desktop/ C:/Users/w5659/Desktop/import_img
```

