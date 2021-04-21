1. 安装scrapyd

   ```shell
   pip install scrapyd scrapyd-client
   ```

2. 配置文件

   ```shell
   vim /usr/local/lib/python2.7/site-packages(dist-packages)/scrapyd/default_scrapyd.conf
   ```

   修改如下字段

   ```shell
   bind_address: 0.0.0.0
   ```

3. 启动服务

   ```shell
   scrapyd   # 默认端口为6800
   ```

4. 配置scrapy settings文件

   ```python
   [deploy: scrapyd_tencent]     # 部署名字
   url = "http://localhost:6800" # 部署网站
   project = Tencent             # 项目名称
   ```

5. 开始部署

   ```shell
   scrapyd-deploy scrapyd_tencent -p Tencent  # 如果代码修改, 需要重新部署
   ```

6. 执行爬虫

   ```shell
   curl http://localhost:6800/schedule.json -d project=Tencent -d spider=tencent_crawl
   curl http://localhost:6800/cancel.json -d project=Tencent -d job=SHA1值
   ```

   

