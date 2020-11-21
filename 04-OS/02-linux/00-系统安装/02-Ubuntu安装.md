# 1. Ubuntu16.04

官方镜像: [下载](http://releases.ubuntu.com/16.04/?_ga=2.143620662.2070533326.1552030904-83798525.1552030904)

## 1.1 独显宿主机安装

1. 在安装前， 黑窗口ubuntu中按e在“quiet splash”后添加： 空格 + nomodeset f10 进入安装
2. 安装完成后， 重启进入系统
3. 修改： sudo vim /etc/default/grub 修改为： GRUB_CMDLINE_LINUX_DEFAULT = “quiet_splash nomodeset”
4. 添加镜像源： sudo add-apt-repository ppa:nilarimogard/webupd8
5. 刷新镜像列表： sudo apt-get update
6. 安装双显卡切换指示器： sudo apt-get install prime-indicator
7. 屏蔽默认显卡： sudo chmod 666 /etc/modprobe.d/blacklist.conf # 追加权限 sudo gedit /etc/modprobe.d/blacklist.conf 在文章最后添加： blacklist nouveau
8. 打开系统设置--》软件--》附加驱动： 记住编号-384 不要更新
9. 安装更新： ctrl + alt + f1 进入命令行 sudo service lightdm stop # 关闭图形化界面 sudo apt-get install nvidia-384 # 安装官方驱动 注意填写刚才的那个版本 sudo service lightdm start # 开启界面化
10. 重启到窗口中将关闭的图形化界面修改回来： queit splash nomodeset 删除并修改为acpi_osi=linux f10 启动
11. 到窗口中继续修改： sudo vi /etc/default/grub 替换nomodest 为 acpi_osi=linux sudo update-grub 完成

## 1.2 安装 vm-tools

到vm中找到设置-->CD/DVD-->使用IOS影响文件选择ubuntu自带镜像确定-->重启-->状态栏上有个VMware tool镜像打开(computer/media/用户名/VMware Tools)-->把VMwareToolsxx.gz转移到桌面-->在home文件夹下创建一个目录放进去 双击打开解压-->进入文件 进入终端-->sudo ./vmware-install.pl 授权安装 遇到提示直接回车-->重启

## 1.3 汉化

SystemSetting---> LanguageSupport--->按照指引不要动 提供权限--->完成后Install/RemoveLanguages..---> 选择中文(Chinese(simplifled))--->Apply继续等--->列表最下面有个汉语 拖到最上面 确定--->重启--->不要询问-->不要修改

## 1.4 输入法

<1> atrl+alr+t 打开终端 输入"im-config" 确定 --> 确定 --> 选择小企鹅输入法-->确定重启

此时想安装搜狗, 双击即可安装成功