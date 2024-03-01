## 1 环境要求

!!! Abstract ""
	**部署服务器要求：**  

    * 操作系统: 可运行 VirtualBox 的 Windows 操作系统
    * CPU/内存: 4核8G
    * 磁盘空间: 200G


## 2 安装部署
### 2.1 在 Windows 系统中安装虚拟机

!!! Abstract ""
	电脑上没有安装虚拟化软件，需要先安装虚拟化软件。市面上主流的桌面虚拟化软件有 VMware Workstation 和 VirtualBox。如果电脑上已经安装了其中一款软件，可以直接跳过这一部分。  
	示例选择了 VirtualBox。因为 VirtualBox 是免费的，有需求的用户可以自行选择安装收费的 VMware Workstation。  
	VirtualBox 下载链接：https://download.virtualbox.org/virtualbox/7.0.14/VirtualBox-7.0.14-161095-Win.exe。

!!! Abstract ""
	下载 VirtualBox 后，双击安装包进行安装，安装完成后默认打开 VirtualBox。

![VirtualBox](../img/installation/ova部署安装VirtualBox1.png){ width="900px" }

![VirtualBox](../img/installation/ova部署安装VirtualBox2.png){ width="900px" }


!!! Abstract ""

	虚拟化软件 VirtualBox 已经安装完成，点击 “完成” 会自动打开 VirtualBox 虚拟机。

### 2.2  虚拟机导入 Ubuntu 系统 OVA 包

!!! Abstract ""
	在虚拟机中安装 Ubuntu 系统，可以下载 DataEase 提供的 Ubuntu OVA 文件，直接导入到 VirtualBox 就可以使用，省去安装系统的过程。  
	通过网盘链接下载 Ubuntu OVA 文件: https://pan.baidu.com/s/1gNM-tvT35YPpineCVauviA?pwd=DeUb 提取码：DeUb 

![社区版下载DataEase](../img/installation/选择对应版本.png){ width="900px" }


!!! Abstract ""
	在 VirtualBox 界面上，点击 ”导入” ，选择下载好的 Ubuntu OVA 文件，点击 “下一步”。

![导入 OVA](../img/installation/导入OVA包1.png){ width="900px" }


!!! Abstract ""
	选择一个可用空间在 50G 以上的磁盘位置，点击 “完成”。
![导入 OVA](../img/installation/选择磁盘空间.png){ width="900px" }

!!! Abstract ""
	等待 DataEase 虚拟机完成导入。

![导入 OVA](../img/installation/等待完成OVA导入.png){ width="900px" }


!!! Abstract ""
	导入完成后，选择导入的虚拟机，点击“启动”按钮。

![启动](../img/installation/虚拟机导入完成.png){ width="900px" }

!!! Abstract ""
	启动后，输入用户名和密码进入系统。注意：此处密码不显示，输入完成按回车。

	* 用户名：root

    * 密码：passwd

![启动](../img/installation/启动虚拟机输入密码.png){ width="900px" }

!!! Abstract ""
	查看虚拟机的 IP，输入命令 ip a。每个环境的 IP 地址都不一样，本次演示环境的虚拟机 IP 地址为 192.168.11.230。

![启动](../img/installation/查看虚拟机IP.png){ width="900px" }

### 2.3  Ubuntu 系统中安装 DataEase

!!! Abstract ""
	成功在虚拟机中安装并启动 Ubuntu 系统，连接 Ubuntu 系统即可进行 DataEase 安装。

	如果没有用于连接 Linux 系统终端的工具，可以选择安装 FinalShell，下载地址：http://www.hostbuf.com/downloads/finalshell_windows_x64.exe。

![登录](../img/installation/安装FinalShell1.png){ width="900px" }
![登录](../img/installation/安装FinalShell2.png){ width="900px" }

!!! Abstract ""
	安装 FinalShell 成功后，按照下图操作创建链接。
![登录](../img/installation/创建SSH连接.jpg){ width="900px" }

!!! Abstract ""
	填写连接配置信息，进行确认。双击创建好的连接，即可连接到虚拟机的 Ubuntu 系统。

	* 主机填写 Ubuntu 系统的 IP 地址；

	* 用户名和密码填写 Ubuntu 系统的用户名和密码。

![登录](../img/installation/输入连接配置.jpg){ width="900px" }
![登录](../img/installation/成功创建连接.jpg){ width="900px" }
![登录](../img/installation/连接主机成功.jpg){ width="900px" }

!!! Abstract ""
	连接 Ubuntu 系统后，按照 [DataEase 离线部署]( https://dataease.io/docs/v1/installation/offline_installation/)步骤进行操作，即可部署 DataEase。
