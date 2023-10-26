## 1 环境要求

!!! Abstract ""
    **部署服务器要求：**

    * 操作系统: CentOS/RHELjia 7 及以上 64 位系统
    * CPU/内存: 4核8G
    * 磁盘空间: 200G
    * **可访问互联网**

## 2 下载离线安装包

!!! Abstract ""
    请自行下载 DataEase 最新版本的基础安装包，并复制到目标机器的 /tmp 目录下。

## 3 端口要求

!!! Abstract ""
    部署 DataEase 离线服务需要开通的访问端口说明如下：

| 端口   |    作用    |       说明        |
|------|:--------:|:---------------:|
| 22   |   SSH    |   安装、升级及管理使用    |
| 8100 | Web 服务端口 | 默认端口，根据用户需要可以更改 |

## 4 安装部署



### 4.1  解压安装包

!!! Abstract ""
    以 root 用户 ssh 登录到目标机器, 并执行如下命令：

    ``` 
    cd /tmp
    # 解压安装包（dataease-online-installer-v2.0.0.tar.gz 为示例安装包名称，操作时可根据实际安装包名称替换）
    tar zxvf dataease-online-installer-v2.0.0.tar.gz
    ```

### 4.2  设置安装参数（可选）

!!! Abstract ""
    DataEase 支持以配置文件的形式来设置安装参数，如安装目录、服务运行端口、数据库配置参数等，具体参数请参见安装包中的 install.conf 文件：

    ```
    # 基础配置
    ## 安装目录
    DE_BASE=/opt
    ## Service 端口
    DE_PORT=8100
    ## 登录超时时间，单位min。如果不设置则默认8小时，也就是480
    DE_LOGIN_TIMEOUT=480
    ## 安装模式，community | enterprise
    DE_INSTALL_MODE=community

    # 数据库配置
    ## 是否使用外部数据库
    DE_EXTERNAL_MYSQL=false
    ## 数据库地址
    DE_MYSQL_HOST=mysql-de
    ## DataEase 数据库库名
    DE_MYSQL_DB=dataease
    ## 数据库用户名
    DE_MYSQL_USER=root
    ## 数据库密码
    DE_MYSQL_PASSWORD=Password123@mysql
    ## 数据库参数
    DE_MYSQL_PARAMS="autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false&allowPublicKeyRetrieval=true"
    ```

### 4.3  执行安装脚本

!!! Abstract ""

	```
    # 进入安装包目录（dataease-online-installer-v2.0.0 为示例安装包目录名称，操作时可根据实际安装包名称替换）
    cd dataease-online-installer-v2.0.0

    # 运行安装脚本
    /bin/bash install.sh
	```

!!! Abstract ""
    如果使用外部数据库进行安装，只能使用 MySQL 8.X 版本。同时 DataEase 对数据库部分配置项有要求，请参考下附的数据库配置，修改环境中的数据库配置文件  

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
    特别注意以下几个参数的设置：
    ```
    character_set_server=utf8
    lower_case_table_names=1
    group_concat_max_len=1024000
    ```
    请参考文档中的建库语句创建 DataEase 使用的数据库，DataEase 服务启动时会自动在配置的库中创建所需的表结构及初始化数据。
    ```mysql
    CREATE DATABASE `dataease` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    ```

!!! Abstract ""
    安装脚本使用 /opt/dataease2.0 作为默认安装目录，DataEase 的配置文件、数据及日志等均存放在该安装目录
    安装目录目录结构说明：

    ```
    /opt/dataease2.0/
    ├── apisix                                      #-- 存放 APISIX 组件的配置文件以及其日志文件持久化目录
    ├── bin                                         #-- 安装过程中需要加载到容器中的脚本
    ├── cache                                       #-- 存放 Ehcache 的缓存文件，主要缓存的是权限相关的数据
    ├── conf                                        #-- DataEase 各组件及数据库等中间件的配置文件
    ├── data                                        #-- DataEase 各组件及数据库等中间件的数据持久化目录
    ├── docker-compose-apisix.yml                   #-- DataEase 内建的 APISIX 所需的 Docker Compose 文件
    ├── docker-compose-mysql.yml                    #-- DataEase 内建的 MySQl 所需的 Docker Compose 文件
    ├── docker-compose.yml                          #-- DataEase 基础 Docker Compose 文件，定义了网络等基础信息
    ├── logs                                        #-- DataEase 各组件的日志文件持久化目录
    └── templates                                   #-- DataEase 各组件及数据库等中间件的配置文件的原始文件
    ```

!!! Abstract ""
    安装成功后，通过浏览器访问如下页面登录：
    
    ```
    地址: http://目标服务器IP地址:服务运行端口 
    用户名: admin
    密码: DataEase@123456
    ```

## 5 升级步骤
!!! Abstract ""
    在可连接互联网的情况下，执行以下命令即可完成在线升级步骤（升级前备份是个良好的习惯哦，备份参考见： [备份还原](./backup_faq.md) ）：  

    ```
    # 升级至最新版本 
    dectl upgrade
    ```