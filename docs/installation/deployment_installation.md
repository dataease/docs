!!! Abstract ""
    请使用 DataEase **v3.0.0** 等已发布版本的代码运行。请勿使用 `dev`、`dev-v3` 等分支，开发或测试分支的部分依赖可能未上传到中央仓库，编译时容易出现依赖缺失。

    本文所使用源码为 DataEase **v3.0.0** ，操作系统以 CentOS 7 及以上为例，说明如何以源码形式编译并运行社区版。建议环境不低于 4 核 / 8G。

## 1 项目结构

     ```
     ├── CODE_OF_CONDUCT.md
     ├── CONTRIBUTING.md
     ├── Dockerfile                                # 构建容器镜像使用的 Dockerfile
     ├── LICENSE                                   # License 申明
     ├── README.md
     ├── SECURITY.md
     ├── core                                      # 社区版功能源码
     │   ├── core-backend                          # 后端，产物为 CoreApplication.jar
     │   └── core-frontend                         # 前端
     ├── de-xpack                                  # 企业版功能源码（不开源）
     ├── drivers                                   # 数据源驱动文件
     ├── installer                                 # 安装工程源码
     ├── mapFiles                                  # 地图原始文件
     ├── pom.xml                                   # 整体 Maven 项目使用的 pom 文件
     ├── sdk                                       # DataEase 基础接口工程源码
     └── staticResource                            # 静态资源文件
     ```

## 2 配置环境

### 2.1 安装 JDK 21

!!! Abstract ""
    DataEase v3 使用 JDK 21，可到 [Oracle 官网](https://www.oracle.com/java/technologies/downloads/#java21) 按 CPU 架构下载安装包。以下以 x64 RPM 为例：

    ```
    # 下载 JDK 21 RPM 安装包
    wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.rpm

    # 安装 RPM 安装包
    yum -y install jdk-21_linux-x64_bin.rpm
    ```

!!! Abstract ""
    验证 JDK 已正确安装：

    ```
    java -version
    ```

    输出类似：

    ```
    java version "21.0.10" 2026-01-20 LTS
    Java(TM) SE Runtime Environment (build 21.0.10+7-LTS)
    Java HotSpot(TM) 64-Bit Server VM (build 21.0.10+7-LTS, mixed mode, sharing)
    ```

### 2.2 安装 Git

!!! Abstract ""
    执行命令安装 Git：

    ```
    yum install -y git
    ```

!!! Abstract ""
    验证 Git：

    ```
    git --version
    ```

### 2.3 安装配置 Maven

!!! Abstract ""
    到 [Apache Maven 官网](https://maven.apache.org/download.cgi) 下载 3.9.x 版本。

!!! Abstract ""
    执行命令安装 Maven：

    ```
    wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz
    tar zxvf apache-maven-3.9.6-bin.tar.gz
    mv apache-maven-3.9.6 /opt

    echo "export M2_HOME=/opt/apache-maven-3.9.6" >> ~/.bashrc
    echo "export PATH=\$PATH:\$M2_HOME/bin" >> ~/.bashrc
    source ~/.bashrc
    ```

!!! Abstract ""
    验证 Maven（`Java version` 应为 21）：

    ```
    mvn -v
    ```

### 2.4 安装配置 Node.js

!!! Abstract ""
    使用 Maven 打包前端时，`frontend-maven-plugin` 会自动安装 **Node.js v23.11.0** 与 npm 10.9.2，一般不必再单独安装。前端生产构建脚本会设置 `NODE_OPTIONS=--max_old_space_size=8192`，建议编译机内存不少于 16G，4 核 8G 可能在打包阶段内存不足。

    仅在需要独立执行 `npm run dev` 时，再自行安装与上述版本接近的 Node.js。

## 3 代码运行

### 3.1 源码准备

!!! Abstract ""
    下载源码到本地：

    ```
    cd /opt
    git clone -b v3.0 https://github.com/dataease/dataease.git
    ```

    **注意：前后端工程在下载目录的 `core` 下。** `v3.0` 维护分支版本号仍为 3.0.0，并已在 `sdk/pom.xml` 中声明 Fit2Cloud 公共仓库。直接使用标签 `v3.0.0` 时，`mvn clean install` 可能因无法解析 `dataease-license-sdk`、`calcite-core`（classifier 为 `de`）而失败。

### 3.2 源码编译

!!! Abstract ""
    根目录 `pom.xml` 主要构建 `sdk`，社区版可运行 JAR 需再进入 `core` 使用 `standalone`  profile 打包：

    ```
    cd dataease
    mvn clean install

    cd core
    mvn clean package -Pstandalone -U -Dmaven.test.skip=true
    ```

!!! Abstract ""
    编译完成后，在 `core/core-backend/target` 目录下可以看到 `CoreApplication.jar`。

!!! Abstract ""
    `core-backend` 引用的 `calcite-core`（classifier `de`）以及 `dataease-license-sdk` 属于 DataEase 发布到 Fit2Cloud 公共仓库的依赖，不属于 GitHub 开源仓。仓库地址为 `https://repository.fit2cloud.com/repository/fit2cloud-public/`。该依赖会持续迭代并上传到公共仓库，对社区版编译一般无影响。

### 3.3 配置运行环境

!!! Abstract ""
    **操作系统设置**

    增加系统监听文件数量：

    ```
    echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
    ```

!!! Abstract ""
    **MySQL 配置**

    请使用 MySQL 8.0 及以上。以下为推荐配置（与安装包模板接近）：

!!! Abstract ""
    **说明：** 安装器默认使用内置 MySQL。如需改用外部 MySQL 或其他元数据库（达梦、KingbaseES、Oracle、PostgreSQL、SQL Server、GreatSQL），请参考 [外部数据库部署](multi_database_deployment.md)。

    ```
    [mysqld]
    datadir=/var/lib/mysql

    default-storage-engine=INNODB
    character_set_server=utf8
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
    binlog_expire_logs_seconds=432000
    sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
    skip-name-resolve

    [mysql]
    default-character-set=utf8

    [mysql.server]
    default-character-set=utf8
    ```

    创建 DataEase 运行时使用的数据库，例如 `dataease`：

    ```
    CREATE DATABASE `dataease` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    ```

!!! Abstract ""
    **运行目录设置**

    创建 DataEase 运行目录：

    ```
    mkdir -p /opt/dataease3.0/config \
      /opt/dataease3.0/drivers \
      /opt/dataease3.0/cache \
      /opt/dataease3.0/logs \
      /opt/dataease3.0/data/map-origin \
      /opt/dataease3.0/data/static-resource \
      /opt/dataease3.0/data/driver
    ```

    内置数据源驱动目录为 `/opt/dataease3.0/drivers`；`/opt/dataease3.0/data/driver` 给 Spring Boot `loader.path` 加载额外 JDBC。进入源码目录，将 `drivers` 复制到 `/opt/dataease3.0/drivers`：

    ```
    cp -rp /opt/dataease/drivers/* /opt/dataease3.0/drivers/
    ```

    将源码 `mapFiles` 复制到 `/opt/dataease3.0/data/map-origin`（v3 内置地图目录为 `map-origin`，不再使用 v2 的 `data/map` 作为原始地图目录）：

    ```
    cp -rp /opt/dataease/mapFiles/* /opt/dataease3.0/data/map-origin/
    ```

    将源码 `staticResource` 复制到 `/opt/dataease3.0/data/static-resource`：

    ```
    cp -rp /opt/dataease/staticResource/* /opt/dataease3.0/data/static-resource/
    ```

    进入配置目录：

    ```
    cd /opt/dataease3.0/config
    ```

    创建 `application.yml`，将 `YOUR_IP` / `YOUR_DATABASE` / `YOUR_USER` / `YOUR_PASSWORD` 改为实际数据库信息。v3 默认使用 MariaDB JDBC 驱动连接 MySQL：

    ```
    server:
        tomcat:
            connection-timeout: 70000
    spring:
        servlet:
            multipart:
                max-file-size: 500MB
                max-request-size: 500MB
        datasource:
            driver-class-name: org.mariadb.jdbc.Driver
            url: jdbc:mariadb://YOUR_IP:3306/YOUR_DATABASE?autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false&allowPublicKeyRetrieval=true
            username: YOUR_USER
            password: YOUR_PASSWORD
    dataease:
        path:
            substitule: /opt/dataease3.0/config/substitule.json
        default-pwd: DataEase@123456
    ```

    社区版源码不含 `de-xpack` 登录实现，会使用内置替补登录。请指定 `dataease.path.substitule` 为可写文件，并用 `dataease.default-pwd` 固定管理员密码。若不配置，首次启动会生成随机密码并写入该文件。默认值 `classpath:substitule.json` 不是可靠的磁盘路径，不要使用。

### 3.4 运行 JAR

!!! Abstract ""
    将 `core/core-backend/target/CoreApplication.jar` 复制到运行目录后启动。v3 需指定额外配置目录，并加载外部驱动路径：

    ```
    cp /opt/dataease/core/core-backend/target/CoreApplication.jar /opt/dataease3.0/
    cd /opt/dataease3.0
    java -Dfile.encoding=utf-8 \
      -Dloader.path=/opt/dataease3.0/data/driver/ \
      -Dspring.config.additional-location=/opt/dataease3.0/config/ \
      -jar CoreApplication.jar
    ```

    官方镜像的 `JAVA_OPTIONS` 中 `loader.path` 还包含 `/opt/apps`；源码直接跑 JAR 时使用上面的运行目录即可。配置目录源码运行用 `config`，安装包 / 镜像场景一般为 `conf`（挂载到容器内 `/opt/apps/config`）。

!!! Abstract ""
    登录页会请求 `/de2api/setting/authentication/status`（企业认证方式状态）。社区版源码没有该接口时，浏览器会提示 `Request failed with status code 404`，页面停在「加载中」，无法输入账号。编译前在 `core/core-backend` 增加空实现即可，例如：

    ```
    package io.dataease.community;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    import java.util.Collections;
    import java.util.List;

    @RestController
    @RequestMapping("/setting/authentication")
    public class CommunityAuthenticationController {
        @GetMapping("/status")
        public List<Object> status() {
            return Collections.emptyList();
        }
    }
    ```

    官方安装包已包含对应模块，按安装包部署一般不会出现此问题。

!!! Abstract ""
    启动完成后可通过 `http://服务器IP:8100` 访问：

    ```
    用户名: admin
    密码: DataEase@123456
    ```

    密码与第 3.3 节 `dataease.default-pwd` 保持一致。若启动时 `substitule.json` 里已经有密码，则以文件中的值为准。

## 4 镜像制作

### 4.1 安装 Docker

!!! Abstract ""
    在服务器上安装 Docker。可使用 DataEase 项目组提供的脚本，也可自行安装（需同时具备 docker compose）：

    ```
    curl -fsSL https://resource.fit2cloud.com/get-docker-linux.sh | bash

    # 设置 docker 开机自启，并启动 docker 服务
    systemctl enable docker
    systemctl daemon-reload
    service docker start
    ```

### 4.2 制作镜像

!!! Abstract ""
    先完成第 3.2 节编译，再进入项目根目录执行：

    ```
    cd /opt/dataease
    docker build -t registry.cn-qingdao.aliyuncs.com/dataease/dataease:v3.0.0 .
    ```

!!! Abstract ""
    使用 `docker images` 可查看镜像是否打包成功。

## 5 镜像运行

### 5.1 配置运行环境

!!! Abstract ""
    创建运行目录：

    ```
    mkdir -p /opt/dataease3.0/conf \
      /opt/dataease3.0/logs \
      /opt/dataease3.0/data \
      /opt/dataease3.0/cache
    ```

    在运行目录下创建 `docker-compose.yml`：

    ```
    services:
      dataease:
        image: registry.cn-qingdao.aliyuncs.com/dataease/dataease:v3.0.0
        container_name: dataease
        ports:
          - 8100:8100
        volumes:
          - /opt/dataease3.0/conf:/opt/apps/config
          - /opt/dataease3.0/logs:/opt/dataease3.0/logs
          - /opt/dataease3.0/data:/opt/dataease3.0/data
          - /opt/dataease3.0/cache:/opt/dataease3.0/cache
    ```

    创建配置文件目录及 `application.yml`：

    ```
    mkdir -p /opt/dataease3.0/conf
    ```

    在 `/opt/dataease3.0/conf/application.yml` 中写入第 3.3 节的数据源配置（将 `YOUR_IP` 等替换为实际值）。镜像内通过 `-Dspring.config.additional-location=/opt/apps/config/` 加载该目录。

### 5.2 运行镜像

!!! Abstract ""
    在运行目录下执行：

    ```
    cd /opt/dataease3.0
    docker compose up -d
    # 或者 docker-compose up -d
    ```

!!! Abstract ""
    容器状态正常后，浏览器访问 `http://服务器IP:8100`，默认账号密码与第 3.4 节相同。

!!! Abstract ""
    登录成功后进入工作台，源码启动效果如下：

![源码启动效果](../img/installation/源码启动效果.png){ width="900px" }
