## 1 DataEase 升级

!!! Abstract ""
	按照本文档 [离线安装](offline_installation.md) 步骤，下载新版本安装包并上传解压后，重新执行安装命令进行升级。  
	**注意：** 请在集群中每个 DataEase 节点依次操作。

	```sh
	# 进入项目目录
	cd dataease-release-v1.x.y-offline
	# 运行安装脚本
	/bin/bash install.sh
	# 查看 DataEase 状态
	dectl status
	```

	**注意：升级前做好数据库的备份工作是一个良好的习惯，可参考[备份还原](https://dataease.io/docs/v1/faq/backup_faq/)。**

## 2 其他组件升级

!!! Abstract ""
	在 DataEase 集群环境中，Doris、Kettle、Redis、Nginx 组件是独立部署的，可按需升级，建议与官方使用版本保持一致。