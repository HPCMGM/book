# 1. 运行

## 1.1 显示调用

```bash
/bin/bash test.sh
sh test.sh
```

## 1.2 隐式调用

在`test.sh`开头插入

```bash
#!/bin/bash
```

赋予文件可执行权限, 执行命令

```bash
chmod +x test.sh
```

调用命令

```bash
./test.sh
```

# 2. 重载

## 2.1 source

```bash
source test.sh
```

## 2.2 .

```bash
. test.sh
```



