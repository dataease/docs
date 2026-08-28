## 1 环境要求

!!! Abstract ""
    **部署服务器要求：**

| 项目 | 要求 |
| --- | --- |
| 操作系统及配置 | CentOS/RHEL 7 及以上 64 位系统 |
| 配置 | 4 核 / 8G 内存 / 200G 硬盘 |
| 其他 | 可访问互联网 |

## 2 下载在线安装包

!!! Abstract ""
    请自行下载 DataEase 最新版本的在线安装包，并复制到目标机器的 `/tmp` 目录下。

    安装包下载链接：https://github.com/dataease/dataease/releases

## 3 端口要求

!!! Abstract ""
    部署 DataEase 服务需要开通的访问端口说明如下：

| 端口 | 作用 | 说明 |
| --- | --- | --- |
| 22 | SSH | 安装、升级及管理使用 |
| 8100 | Web 服务端口 | 默认端口，可根据需要更改 |

## 4 安装部署

### 4.1 解压安装包

!!! Abstract ""
    以 root 用户 SSH 登录到目标机器，并执行如下命令：

    ```
    cd /tmp
    # 解压安装包（dataease-online-installer-v3.0.0.tar.gz 为示例名称，请替换为实际包名）
    tar zxvf dataease-online-installer-v3.0.0.tar.gz
    ```

    安装脚本默认使用 `/opt/dataease3.0` 目录作为安装目录，DataEase 相关安装文件均存放在该目录。

### 4.2 设置安装参数（可选）

!!! Abstract ""
    DataEase 支持以配置文件设置安装参数（安装目录、服务端口、数据库等）。也可在执行 `install.sh` 时按交互提示选择数据库类型等选项；数据库相关的 JPA / Profile 配置由安装脚本自动完成，无需在文档中手工配置方言文件。

    具体参数请参见安装包中的 `install.conf` 文件：

    ```
    # 基础配置
    ## 安装目录
    DE_BASE=/opt
    ## Service 端口
    DE_PORT=8100
    ## 登录超时时间，单位 min。如果不设置则默认 16 小时，也就是 960
    DE_LOGIN_TIMEOUT=960
    ## 安装模式
    DE_INSTALL_MODE=community
    ## 动态路径
    DE_CONTEXT_PATH=

    # 数据库配置
    ## 是否使用外部数据库
    DE_EXTERNAL_DB=false
    ## 默认运行数据库类型: MySQL、SQLServer、DM、Oracle、Kingbase、GreatSQL、PostgreSQL
    DE_DB_TYPE=mysql
    ## 数据库地址
    DE_DB_HOST=mysql-de
    ## 数据库端口（仅使用外部数据库时才生效）
    DE_DB_PORT=3306
    ## DataEase 数据库库名
    DE_DB_DATABASE=dataease
    ## DataEase schema
    DE_DB_SCHEMA=
    ## 数据库用户名
    DE_DB_USER=root
    ## 数据库密码，密码如包含特殊字符，请用双引号引起来，例如 DE_DB_PASSWORD="Test@4&^%*^"
    DE_DB_PASSWORD=Password123@mysql
    ## 数据库参数，下面是各个数据库的推荐参数
    DE_DB_PARAMS="autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false&allowPublicKeyRetrieval=true"

    # 定时报告镜像配置
    ## 是否使用外部 Playwright，若使用外部 Playwright，则限制参数无效
    DE_EXTERNAL_PLAYWRIGHT=false
    DE_PLAYWRIGHT_SERVER=http://de-playwright-api:3000/screenshot
    DE_PLAYWRIGHT_CONCURRENCY=4
    DE_PLAYWRIGHT_SHM_SIZE=2gb

    # APISIX 配置
    ## 是否使用外部 APISIX
    DE_EXTERNAL_APISIX=false
    ## 使用外部 APISIX，则下列参数无效
    ## APISIX 端口
    DE_APISIX_PORT=9080

    # 同步模块配置
    ## 是否使用外部同步模块
    DE_EXTERNAL_SYNC_TASK=false

    # 其他配置
    DE_EXPORT_VIEWS_LIMIT=100000
    DE_EXPORT_DATASET_LIMIT=100000
    DE_ORIGIN_LIST="http://localhost:8000"
    ## DataEase 节点列表，用于多节点部署，节点以逗号分隔，如 192.168.1.101,192.168.1.102
    DE_SERVERS=dataease
    ## application.yml 文件中可引入的其他配置文件
    DE_SPRING_PROFILE=mysql
    ```

!!! Abstract ""
    使用外部数据库时，请先完成建库，并在 `install.conf` 中设置 `DE_EXTERNAL_DB=true` 以及 `DE_DB_TYPE`、`DE_DB_HOST` 等连接信息；也可在运行 `install.sh` 时按提示选择。详见 [外部数据库部署](multi_database_deployment.md)。服务启动时会自动创建所需表结构及初始化数据。

### 4.3 执行安装脚本

!!! Abstract ""

    ```
    # 进入安装包目录（请替换为实际解压目录名称）
    cd dataease-online-installer-v3.0.0

    # 运行安装脚本
    /bin/bash install.sh
    ```

!!! Abstract ""
    安装成功后，通过浏览器访问如下页面登录：

    ```
    地址: http://目标服务器IP地址:服务运行端口
    用户名: admin
    密码: DataEase123456
    ```

## 5 升级步骤

!!! Abstract ""
    在可连接互联网的情况下，执行以下命令即可完成在线升级：

    ```
    # 升级至最新版本
    dectl upgrade
    ```

    建议升级前自行备份重要数据与配置。
