## 1 环境要求

!!! Abstract ""
    **部署服务器要求：**

| 项目 | 要求 |
| --- | --- |
| 操作系统及配置 | CentOS/RHEL 7 及以上 64 位系统 |
| 配置 | 4 核 / 8G 内存 / 200G 硬盘 |
| 其他 | 无（无需访问互联网） |

!!! Abstract ""
    **提示：Docker 版本过旧可能导致安装失败，建议使用安装包内的 Docker，或使用 v23.0.5 及以上版本。**

## 2 下载离线安装包

!!! Abstract ""
    请自行下载 DataEase 最新版本的基础安装包，并复制到目标机器的 `/tmp` 目录下。

## 3 端口要求

!!! Abstract ""
    部署 DataEase 离线服务需要开通的访问端口说明如下：

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
    # 解压安装包（dataease-offline-installer-v3.0.0.tar.gz 为示例名称，请替换为实际包名）
    tar zxvf dataease-offline-installer-v3.0.0.tar.gz
    ```

    安装脚本默认使用 `/opt/dataease3.0` 目录作为安装目录，DataEase 相关安装文件均存放在该目录。

### 4.2 设置安装参数（可选）

!!! Abstract ""
    DataEase 支持以配置文件设置安装参数（安装目录、服务端口、数据库等）。也可在执行 `install.sh` 时按交互提示选择数据库类型等选项；数据库相关的 JPA / Profile 配置由安装脚本自动完成，无需手工编写方言配置。

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
    cd dataease-offline-installer-v3.0.0

    # 运行安装脚本
    /bin/bash install.sh
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
    与安装步骤相同：下载新版本离线安装包并上传解压后，重新执行安装命令进行升级。

    ```
    # 进入安装包目录
    cd dataease-offline-installer-v3.0.0

    # 运行安装脚本
    /bin/bash install.sh
    ```

    建议升级前自行备份重要数据与配置。

## 6 常用管理命令及日志

### 6.1 DataEase Service

!!! Abstract ""
    DataEase 在安装时默认向系统添加了 dataease Service，支持的命令有：

    - `start`：启动 DataEase 服务
    - `stop`：停止 DataEase 服务，并删除相关运行容器、docker 网络等资源
    - `restart`：停止后启动 DataEase 服务（先 stop 再 start）
    - `status`：查看 DataEase 服务当前各容器运行状态

### 6.2 dectl

!!! Abstract ""
    DataEase 默认内置命令行运维工具 `dectl`，执行 `dectl help` 可查看帮助：

    ```
    DATAEASE 控制脚本

    Usage:
      ./dectl [COMMAND] [ARGS...]
      ./dectl --help

    Commands:
      status         查看 DATAEASE 服务运行状态
      start          启动 DATAEASE 服务
      stop           停止 DATAEASE 服务
      restart        重启 DATAEASE 服务
      reload         重新加载 DATAEASE 服务
      upgrade        升级 DATAEASE 服务
      clear-images   清理 DATAEASE 旧版本的相关镜像
      clear-logs     清理 DATAEASE 历史日志
      version        查看 DATAEASE 版本
    ```

    DataEase 的日志目录为：`/opt/dataease/logs`（具体路径以实际安装目录为准，默认安装目录下一般为 `/opt/dataease3.0/logs`）。

    更完整的说明见 [命令行工具使用指南](cli.md)。
