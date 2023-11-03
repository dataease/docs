## 1 DataEase 升级

!!! Abstract ""
	如果您的服务器可以访问互联网，可以通过以下命令直接升级 DataEase 至最新版本。  
	**注意：** 请在集群中每个 DataEase 节点依次操作。
	```sh
	# 升级至最新版本
	dectl upgrade
	# 查看 DataEase 状态
	dectl status
	```

	**注意：升级前做好数据库的备份工作是一个良好的习惯，可参考[备份还原](https://dataease.io/docs/v1/faq/backup_faq/)。**

## 2 其他组件升级

!!! Abstract ""
	在 DataEase 集群环境中，Doris、Kettle、Redis、Nginx 组件是独立部署的，可按需升级，建议与官方使用版本保持一致。