## 1 安装 Git 和 jdk 11

!!! Abstract ""
	**本文以 CentOS 8.3 为例，举例说明如何以源码的形式编译 DataEase 工程，并进行前后端分离部署。**  
	本文所有操作均在阿里云（新加坡区）4C8G 环境中执行。
	```shell
	yum install -y git java-1.8.0-openjdk*
	```

## 2 安装配置 Maven

!!! Abstract ""
	```shell
	# 下载并安装 Maven
	wget https://dlcdn.apache.org/maven/maven-3/3.8.4/binaries/apache-maven-3.8.4-bin.tar.gz
	
	tar zxvf apache-maven-3.8.4-bin.tar.gz
	
	mv apache-maven-3.8.4 /opt
	
	echo "export M2_HOME=/opt/apache-maven-3.8.4" >> ~/.bashrc
	
	echo "export PATH=\$PATH:\$M2_HOME/bin" >> ~/.bashrc
	
	source ~/.bashrc
	```
    默认安装 Maven 后，在 Maven 安装目录中有配置文件 settings.xml，**该文件中默认开启了 mirror，可以将该 mirror 设置注释掉：**
	```xml
		<mirror>
		  <id>maven-default-http-blocker</id>
		  <mirrorOf>external:http:*</mirrorOf>
		  <name>Pseudo repository to mirror external repositories initially using HTTP.</name>
		  <url>http://0.0.0.0/</url>
		  <blocked>true</blocked>
		</mirror>
	```

## 3 安装配置 nodejs

!!! Abstract ""
	```shell
	wget https://nodejs.org/dist/v16.13.0/node-v16.13.0-linux-x64.tar.xz
	
	tar xvf node-v16.13.0-linux-x64.tar.xz
	
	mv node-v16.13.0-linux-x64 /opt
	
	echo "export PATH=\$PATH:/opt/node-v16.13.0-linux-x64/bin" >> ~/.bashrc
	
	source ~/.bashrc
	```
