## 环境要求

!!! info "部署服务器要求"
    * 操作系统: CentOS 7.x
    * CPU/内存: 4核8G
    * 磁盘空间: 50G
    * 可访问互联网

## 下载安装包

请自行下载 MeterSphere 最新版本的在线安装包，并复制到目标机器的 /tmp 目录下

!!! tip ""
    安装包下载链接: https://github.com/metersphere/metersphere/releases

## 解压安装包

以 root 用户 ssh 登录到目标机器, 并执行如下命令

```sh
cd /tmp
# 解压安装包
tar zxvf metersphere-release-v1.0.3.tar.gz
```

## 修改安装配置(可选)

在安装包解压后的目录，编辑修改安装参数

```sh
cd metersphere-release-v1.0.3
vim install.conf
```

!!! info "安装配置文件说明, 如果无特殊需求可以不进行修改采用默认参数安装"
    ```vim
    # 基础配置
    ## MeterSphere 安装目录的上级目录, MeterSphere 将安装在 ${base_dir}/metersphere 目录中
    MS_BASE=/opt
    ## MeterSphere 相关组件所使用 Docker 镜像的镜像地址前缀
    MS_PREFIX=''
    ## MeterSphere 相关组件所使用 Docker 镜像的镜像标签
    MS_TAG=dev
    ## 安装模式, 支持的安装模式有 allinone | server | node-controller 三种
    MS_MODE=allinone
    ## MeterSphere Web 服务的监听端口
    MS_PORT=8081
    ## Node controller Web 服务的监听端口
    MS_NODE_CONTROLLER_PORT=8082

    # 数据库配置
    ## 是否使用外部 MySQL 数据库
    MS_EXTERNAL_MYSQL=false
    ## MySQL 数据库地址，仅在使用外部数据库时修改
    MS_MYSQL_HOST=mysql
    ## MySQL 数据库端口，仅在使用外部数据库时修改
    MS_MYSQL_PORT=3306
    ## MySQL 数据库库名, 仅在使用外部数据库时修改
    MS_MYSQL_DB=metersphere
    ## MySQL 数据库用户名
    MS_MYSQL_USER=root
    ## MySQL 数据库密码
    MS_MYSQL_PASSWORD=Password123@mysql

    # Kafka 配置
    ## 是否使用外部 kafka
    MS_EXTERNAL_KAFKA=false
    ## Kafka 地址, 仅在使用外部 Kafka 时修改
    MS_KAFKA_HOST=$(hostname -I|cut -d" " -f 1)
    ## Kafka 端口, 仅在使用外部 Kafka 时修改
    MS_KAFKA_PORT=19092
    ## Kafka Topic
    MS_KAFKA_TOPIC=JMETER_METRICS
    ## Kafka Log Topic
    MS_KAFKA_LOG_TOPIC=JMETER_LOGS
    ## Kafka Test Topic
    MS_KAFKA_TEST_TOPIC=JMETER_TESTS
    ## Kafka 外部访问地址
    MS_KAFKA_EXT_HOST=
    ## Kafka 外部访问端口
    MS_KAFKA_EXT_PORT=19092  

    ```

!!! info "注意"
    如果使用外部数据库进行安装，推荐使用 MySQL 5.7 版本。同时 MeterSphere 对数据库部分配置项有要求，请参考下附的数据库配置，修改环境中的数据库配置文件

    ```
    [mysqld]
    default-storage-engine=INNODB
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
    sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
    skip-name-resolve
    ```

    请参考文档中的建库语句创建 MeterSphere 使用的数据库，metersphere-server 服务启动时会自动在配置的库中创建所需的表结构及初始化数据。
    ```mysql
    CREATE DATABASE `metersphere` /*!40100 DEFAULT CHARACTER SET utf8mb4 */
    ```

安装脚本默认使用 /opt/metersphere 目录作为安装目录，MeterSphere 的配置文件、数据及日志等均存放在该安装目录

!!! info "安装目录目录结构说明"
    ```
    /opt/metersphere/
    ├── bin                                         #-- 安装过程中需要加载到容器中的脚本
    ├── compose_files                               #-- 根据不同的安装模式，保存需要使用到的 compose 文件信息
    ├── conf                                        #-- MeterSphere 各组件及数据库等中间件的配置文件
    ├── data                                        #-- MeterSphere 各组件及数据库等中间件的数据持久化目录
    ├── docker-compose-base.yml                     #-- MeterSphere 基础 Docker Compose 文件，定义了网络等基础信息 
    ├── docker-compose-kafka.yml                    #-- MeterSphere 自带的 Kafka 所需的 Docker Compose 文件
    ├── docker-compose-mysql.yml                    #-- MeterSphere 自带的 MySQL 所需的 Docker Compose 文件
    ├── docker-compose-node-controller.yml          #-- MeterSphere Node-Controller 组件所需的 Docker 文件
    ├── docker-compose-server.yml                   #-- MeterSphere Server 及 Data-Streaming 所需的 Docker Compose 文件
    ├── logs                                        #-- MeterSphere 各组件的日志文件持久化目录
    └── version                                     #-- 安装包对应的 MeterSphere 版本信息
    ```

## 执行安装脚本

```sh
# 进入安装包目录
cd metersphere-release-v1.0.3
# 运行安装脚本
/bin/bash install.sh
# 等待安装脚本执行完成后，查看 MeterSphere 状态
msctl status
```

安装成功后，通过浏览器访问如下页面登录 MeterSphere

```
地址: http://目标服务器IP地址:8081
用户名: admin
密码: metersphere
```

