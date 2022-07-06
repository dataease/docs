## 1 下载代码

!!! Abstract ""
	**此处以 v1.8 分支举例：**
	```shell
	git clone -b v1.8 https://github.com/dataease/dataease.git
	```

## 2 地图库准备

!!! Abstract ""
	**DataEase 从 1.2 版本开始支持地图组件。在 DataEase 源码工程的目录下有一个地图文件目录 mapFiles/full，需要将该目录下的文件放置到 /opt/dataease/data/feature/full 目录下：**
	```shell
	mkdir -p /opt/dataease/data/feature
	cd dataease
	cp -r mapFiles/full /opt/dataease/data/feature/full
	```

## 3 驱动库准备

!!! Abstract ""
	**DataEase 从 1.4 版本开始将数据源连接用的驱动库独立在 drivers 目录中。 在 DataEase 源码工程的目录下有一个驱动文件目录 drivers，需要将该目录放置到 /opt/dataease/drivers 下：**
	```shell
	mkdir -p /opt/dataease/drivers
	cp -rp drivers/* /opt/dataease/drivers/
	```

## 4 插件库准备

!!! Abstract ""
	**DataEase 从 1.9 版本开始支持以插件的形式导入组件与数据源，下载 dataease-extensions 工程源码：**
	```shell
	git clone https://github.com/dataease/dataease-extensions.git
	```
	切换到插件工程 dev 分支下，找到 build.sh 和 plugin.json，然后在各个插件目录下执行：

	```shell
	bash build.sh
	```
	进行插件的编译打包，最终生成 xxx.zip，可在系统管理的【插件管理】界面进行上传安装。

