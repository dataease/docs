## 1 环境要求

!!! Abstract ""
    **部署服务器要求：**

    * 操作系统: Ubuntu 22.04 / CentOS 7.6 64 位系统
    * CPU/内存: 4核8G
    * 磁盘空间: 200G
    * **可访问互联网**

    **提示：支持云平台部署，安装成功后请检查公有云端口开通情况。Docker 版本太老可能会导致安装失败，建议使用安装包内的 Docker。**

## 2 端口要求

!!! Abstract ""
    部署 DataEase 服务需要开通的访问端口说明如下：

| 端口   |    作用    |       说明        |
|------|:--------:|:---------------:|
| 22   |   SSH    |   安装、升级及管理使用    |
| 8100 | Web 服务端口 | 默认端口，根据用户需要可以更改 |

## 3 安装部署

!!! Abstract ""
    GitHub release 链接: https://github.com/dataease/dataease/releases

    v3 一键在线安装脚本尚未正式发布。当前请优先使用 [离线安装包](offline_INSTL_and_UPG.md) 完成部署；若官方后续发布 v3 在线安装脚本，再按发布说明执行。

!!! Abstract ""
    如果使用外部数据库进行安装，请参考 [外部数据库部署](multi_database_deployment.md)。外部 MySQL 推荐 8.X，部分配置项要求如下。

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
	sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
	skip-name-resolve

	[mysql]
	default-character-set=utf8

	[mysql.server]
	default-character-set=utf8
    ```

!!! Abstract ""
    特别注意以下几个参数的设置：

    ```
    character_set_server=utf8
    lower_case_table_names=1
    group_concat_max_len=1024000
    ```

    建库语句示例：

    ```mysql
    CREATE DATABASE `dataease` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
    ```

!!! Abstract ""
    安装成功后，默认运行目录为 `/opt/dataease3.0`。通过浏览器访问登录：

    ```
    地址: http://目标服务器IP地址:服务运行端口
    用户名: admin
    密码: DataEase@123456
    ```
