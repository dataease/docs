## 环境要求

!!! info "部署服务器要求"
    * 操作系统: CentOS 7.x
    * CPU/内存: 4核8G
    * 磁盘空间: 50G
    * 可访问互联网

## 下载安装包

请自行下载 DataEase 最新版本的在线安装包，并复制到目标机器的 /tmp 目录下

!!! tip "以下地址暂未开放"
    安装包下载链接: https://github.com/dataease/dataease/releases

## 解压安装包

以 root 用户 ssh 登录到目标机器, 并执行如下命令

```sh
cd /tmp
# 解压安装包
tar zxvf dataease-release-v1.0.0.tar.gz
```

## 执行安装脚本

```sh
# 进入安装包目录
cd dataease-release-v1.0.0
# 运行安装脚本
/bin/bash install.sh
```

在安装的过程中，安装程序会提供几个安装选项，如"是否进行精简模式安装"、"是否使用内建 MySQL"等。安装程序默认进行精简安装，且使用内建 MySQL。

- 使用精简模式安装，仅仅会安装和运行 DataEase 基础服务，精简模式下的 DataEase 仅支持直连模式的数据库连接方式。
- 使用非精简模式安装，将安装和运行如 kettle、 doris 等组件，支持定时同步模式的数据库连接方式。

!!! info "注意"
    如果使用外部数据库进行安装，推荐使用 MySQL 5.7 版本。同时 DataEase 对数据库部分配置项有要求，请参考下附的数据库配置，修改环境中的数据库配置文件

    ```
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

	[mysql]
	default-character-set=utf8

	[mysql.server]
	default-character-set=utf8
    ```

    请参考文档中的建库语句创建 DataEase 使用的数据库，DataEase 服务启动时会自动在配置的库中创建所需的表结构及初始化数据。
    ```mysql
    CREATE DATABASE `dataease` /*!40100 DEFAULT CHARACTER SET utf8mb4 */
    ```

安装脚本默认使用 /opt/dataease 使用的数据库，DataEase 的配置文件、数据及日志等均存放在该安装目录

!!! info "安装目录目录结构说明"
    ```
    /opt/dataease/
	├── bin                                         #-- 安装过程中需要加载到容器中的脚本
	├── conf                                        #-- DataEase 各组件及数据库等中间件的配置文件
	├── data                                        #-- DataEase 各组件及数据库等中间件的数据持久化目录
	├── docker-compose-kettle-doris.yml             #-- DataEase 内建的 kettle 和 doris 所需的 Docker Compose 文件 
	├── docker-compose-mysql.yml                    #-- DataEase 内建的 MySQl 所需的 Docker Compose 文件 
	├── docker-compose.yml                          #-- DataEase 基础 Docker Compose 文件，定义了网络等基础信息 
	├── logs                                        #-- DataEase 各组件的日志文件持久化目录
	└── templates                                   #-- DataEase 各组件及数据库等中间件的配置文件的原始文件
    ```



安装成功后，通过浏览器访问如下页面登录 DataEase

```
地址: http://目标服务器IP地址:80
用户名: admin
密码: dataease
```

