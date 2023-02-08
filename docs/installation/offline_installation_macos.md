## 1 环境要求

!!! Abstract ""
	**部署服务器要求：**  

    * 操作系统: 可运行 Docker 的 macOS 操作系统
    * CPU/内存: 4核8G
    * 磁盘空间: 200G

## 2 安装部署

### 2.1 安装 Docker

!!! Abstract ""
	下载地址： https://docs.docker.com/desktop/mac/install/

### 2.2 下载并解压 DataEase 安装包

!!! Abstract ""
	[下载 DataEase 最新版安装包](https://community.fit2cloud.com/#/products/dataease/downloads)  
	**注意：** 下载时需根据 MacBook 的芯片选择安装包  

	* Inter 芯片：选择 “DataEase v1.18.2 AMD64” 安装包；  
	* Apple 芯片：选择 “DataEase v1.18.2 ARM64” 安装包。  

### 2.3 解压安装包

!!! Abstract ""

	```powershell
	tar -zxvf dataease-v1.18.2-offline.tar.gz
	```

### 2.4 下载 dataease-mac.git 部署文件

!!! Abstract ""
	手动复制 dataease-mac 中的 install.sh 到解压目录 dataease-v1.18.2-offline 中，替换原有的 install.sh	
	**下载地址：** https://github.com/mfanoffice/dataease-mac

### 2.5 编辑 install.conf

!!! Abstract ""

	```powershell
	DE_BASE=/Users/User_Dir  #更换为自己的用户目录
	```
### 2.6 执行安装

!!! Abstract ""
	进入到解压目录，执行 

	```powershell
	sudo chmod +x install.sh && sudo ./install.sh
	```

### 2.7 访问服务

!!! Abstract ""
	在浏览器访问 http://localhost