## 1 操作系统参数设置

!!! Abstract ""
	**增加系统监听文件数量：**
	```shell
	echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
	```

## 2 MySQL 配置

!!! Abstract ""
	**以下是推荐的 MySQL 配置：** 
	```inf
	[mysqld]
	datadir=/var/lib/mysql
	default-storage-engine=INNODB
	character_set_server=utf8
	lower_case_table_names=1
	table_open_cache=128
	max_connections=2000
	max_connect_errors=6000
	innodb_file_per_table=1
	innodb_buffer_pool_size=1G
	max_allowed_packet=64M
	transaction_isolation=READ-COMMITTED
	innodb_flush_method=O_DIRECT
	innodb_lock_wait_timeout=1800
	innodb_flush_log_at_trx_commit=0
	sync_binlog=0
	group_concat_max_len=1024000
	sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
	skip-name-resolve
	```

	**特别注意以下几个参数的设置：**
	```
	character_set_server=utf8
	lower_case_table_names=1
	group_concat_max_len=1024000
	```

## 3 创建 MySQL 数据库

!!! Abstract ""
	**登录要连接的 MySQL 服务器，创建 DataEase 运行时使用的数据库，此处示例数据库名为 dataease-wei：**

	```mysql
	CREATE DATABASE `dataease-wei` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
	```

## 4 创建 DataEase 配置文件及日志相关

!!! Abstract ""
	```shell
	mkdir -p /opt/dataease/conf
	mkdir -p /opt/dataease/logs
	
	# 添加 DataEase 运行配置文件，除了 MySQL 连接信息必须正确外，Kettle 和 Doris 如不用的话，相关信息可不修改
	cat <<EOF>> /opt/dataease/conf/dataease.properties
	# 数据库配置
	spring.datasource.url=jdbc:mysql://192.168.1.100:3306/dataease-wei?autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false
	spring.datasource.username=root
	spring.datasource.password=Password123@mysql
	
	carte.host=kettle
	carte.port=18080
	carte.user=cluster
	carte.passwd=cluster
	
	doris.db=dataease
	doris.user=root
	doris.password=Password123@doris
	doris.host=doris-fe
	doris.port=9030
	doris.httpPort=8030
	
	#新建用户初始密码
	dataease.init_password=DataEase123456
	#登录超时时间单位min  如果不设置 默认8小时也就是480
	dataease.login_timeout=480
	
	logger.level=INFO
	EOF
	```
