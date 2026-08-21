
!!! Abstract ""
	按照本文档 [离线安装](offline_INSTL_and_UPG.md) 步骤，下载新版本安装包并上传解压后，重新执行安装命令进行升级。

	```sh
	# 进入项目目录
	cd dataease-offline-installer-v3.x.y
	# 运行安装脚本
	/bin/bash install.sh
	# 查看 DataEase 状态
	dectl status
	```

	**注意：升级前做好数据库的备份工作是一个良好的习惯，可参考[备份还原](backup_faq.md)。**

	**插件兼容性提醒：如果您使用的是企业版并已安装插件，DataEase 升级后请前往[应用商店](https://apps.fit2cloud.com/dataease)下载最新插件，完成插件更新后重启 DataEase。若继续使用旧版插件，涉及该插件的功能可能会报错或无法正常使用。**
