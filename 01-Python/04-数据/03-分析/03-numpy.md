## 安装本单元需要的库

1. 准备`requirements.txt`

   ```shell
   matplotlib==2.2.2
   numpy==1.14.2
   pandas==0.20.3
   tables==3.4.2
   jupyter==1.0.0
   ```

2. 安装`Ta-Lib`依赖

   ```shell
   wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
   tar -zxf ta-lib-0.4.0-src.tar.gz
   cd ta-lib
   ./configure
   make -j 4
   make install
   pip install TA-Lib==0.4.16
   ```

3. 安装依赖库

   ```shell
   pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
   ```

4. 若安装完成后Ipython无法正常使用, 则重新安装即可

