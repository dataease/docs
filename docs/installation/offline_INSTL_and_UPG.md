## 1 环境要求

!!! Abstract ""
    **部署服务器要求：**

    * 操作系统: Ubuntu 22.04 / CentOS 7.6 64 位系统
    * CPU/内存: 4核8G
    * 磁盘空间: 200G

    **提示：Docker 版本太老可能会导致安装失败，建议使用安装包内的 Docker，或者使用 v23.0.5 版本及以上的 Docker。**

    安装脚本会检查运行目录所在磁盘剩余空间，不足 20G 时给出警告。

!!! Abstract ""
    安装器默认使用内置 **MySQL 8.4.5** 容器作为元数据库。如需改用外部 MySQL，或达梦、KingbaseES、Oracle、PostgreSQL、SQL Server、GreatSQL，请参考 [外部数据库部署](multi_database_deployment.md)。

## 2 下载离线安装包

!!! Abstract ""
    请自行下载 DataEase 最新版本的离线安装包，并复制到目标机器的 /tmp 目录下。  
    安装包下载链接: https://community.fit2cloud.com/#/products/dataease/downloads

## 3 端口要求

!!! Abstract ""
    部署 DataEase 离线服务需要开通的访问端口说明如下：

| 端口   |    作用    |       说明        |
|------|:--------:|:---------------:|
| 22   |   SSH    |   安装、升级及管理使用    |
| 8100 | Web 服务端口 | 社区版默认访问端口，对应 `DE_PORT`，可按需修改 |
| 9080 | APISIX 网关端口 | 企业版默认访问端口，对应 `DE_APISIX_PORT` |

!!! Abstract ""
    企业版安装完成后，安装脚本提示的访问地址使用 **9080**（APISIX）。社区版使用 **8100**。内置 MySQL 容器默认不对外映射 3306 端口。

## 4 安装部署

### 4.1  解压安装包

!!! Abstract ""
    以 root 用户 ssh 登录到目标机器, 并执行如下命令：

    ```
    cd /tmp
    # 解压安装包（dataease-offline-installer-v3.0.0-ce.tar.gz 为示例名称，请替换为实际包名）
    tar zxvf dataease-offline-installer-v3.0.0-ce.tar.gz
    ```

### 4.2  设置安装参数（可选）

!!! Abstract ""
    DataEase 支持以配置文件的形式来设置安装参数，如安装目录、服务运行端口、数据库配置参数等，具体参数请参见安装包中的 `install.conf` 文件：

    ```
    # 基础配置
    ## 安装目录
    DE_BASE=/opt
    ## Service 端口
    DE_PORT=8100
    ## 登录超时时间，单位 min。不设置则默认 16 小时，也就是 960
    DE_LOGIN_TIMEOUT=960
    ## 安装模式，community | enterprise（以安装包为准）
    DE_INSTALL_MODE=community
    ## 动态路径
    DE_CONTEXT_PATH=

    # 数据库配置
    ## 是否使用外部数据库
    DE_EXTERNAL_MYSQL=false
    ## 数据库地址
    DE_MYSQL_HOST=mysql-de
    ## 数据库端口（仅使用外部数据库时才生效）
    DE_MYSQL_PORT=3306
    ## DataEase 数据库库名
    DE_MYSQL_DB=dataease
    ## 数据库用户名
    DE_MYSQL_USER=root
    ## 数据库密码，密码如包含特殊字符，请用双引号引起来
    DE_MYSQL_PASSWORD=Password123@mysql
    ## 数据库参数
    DE_MYSQL_PARAMS="autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false&allowPublicKeyRetrieval=true"

    # 定时报告镜像配置
    ## 是否使用外部 Playwright，若使用外部 Playwright，则限制参数无效
    DE_EXTERNAL_PLAYWRIGHT=false
    DE_PLAYWRIGHT_SERVER=http://de-playwright-api:3000/screenshot
    DE_PLAYWRIGHT_CONCURRENCY=4
    DE_PLAYWRIGHT_SHM_SIZE=2gb

    # APISIX 配置
    ## 是否使用外部 APISIX
    DE_EXTERNAL_APISIX=false
    ## APISIX 端口
    DE_APISIX_PORT=9080

    # 同步模块配置
    ## 是否使用外部同步模块
    DE_EXTERNAL_SYNC_TASK=false

    # 其他配置
    DE_EXPORT_VIEWS_LIMIT=100000
    DE_EXPORT_DATASET_LIMIT=100000
    DE_ORIGIN_LIST="http://localhost:8000"
    ## DataEase 节点列表，用于多节点部署，节点以逗号分隔
    DE_SERVERS=dataease
    ## application.yml 可引入的其他配置文件。外部 MySQL 可留空；达梦 / 金仓 / Oracle / PG / SQL Server 等请填写对应 profile，见 [外部数据库部署](multi_database_deployment.md)
    DE_SPRING_PROFILE=
    ```

### 4.3  执行安装脚本

!!! Abstract ""

	```
    # 进入安装包目录（请替换为实际解压目录名称）
    cd dataease-offline-installer-v3.0.0-ce

    # 运行安装脚本
    /bin/bash install.sh
	```

!!! Abstract ""
    使用外部数据库时，请先完成建库，并参考 [外部数据库部署](multi_database_deployment.md) 修改 `install.conf`。DataEase 服务启动时会自动在配置的库中创建所需的表结构及初始化数据。

!!! Abstract ""
    安装脚本使用 `/opt/dataease3.0` 作为默认安装目录（`DE_BASE` + `dataease3.0`）。DataEase 的配置文件、数据及日志等均存放在该目录。

    安装目录结构说明：

    ```
    /opt/dataease3.0/
    ├── apisix                                      #-- APISIX 配置与日志（企业版）
    ├── bin                                         #-- 安装过程中加载到容器的脚本
    ├── cache                                       #-- 缓存文件
    ├── conf                                        #-- 运行配置（application.yml、my.cnf、mysql.env 等）
    ├── data                                        #-- 数据持久化目录
    ├── docker-compose-apisix.yml                   #-- 内建 APISIX / etcd（企业版）
    ├── docker-compose-mysql.yml                    #-- 内建 MySQL
    ├── docker-compose-playwright.yml               #-- 定时报告 Playwright（企业版）
    ├── docker-compose-task.yml                     #-- 同步任务组件（企业版）
    ├── docker-compose.yml                          #-- DataEase 主服务
    ├── logs                                        #-- 日志
    ├── task                                        #-- 同步任务日志目录
    └── templates                                   #-- 配置模板
    ```

## 5  登录访问

!!! Abstract ""
    安装成功后，通过浏览器访问如下页面登录：  
    - **访问地址** : http://目标服务器IP地址:服务运行端口（社区版默认 8100，企业版默认 9080）  
    - **登录用户名**: admin  
    - **登录密码**: DataEase@123456  
