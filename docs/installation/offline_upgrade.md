
!!! Abstract ""
	按照本文档 [离线安装](offline_INSTL_and_UPG.md) 步骤，下载新版本安装包并上传解压后，重新执行安装命令进行升级。

	```sh
	# 进入项目目录
	cd dataease-release-v2.x.y-offline
	# 运行安装脚本
	/bin/bash install.sh
	# 查看 DataEase 状态
	dectl status
	```

	**注意：升级前做好数据库的备份工作是一个良好的习惯，可参考[备份还原](https://dataease.io/docs/v2/installation/backup_faq/)。**