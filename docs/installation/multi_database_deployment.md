# 外部数据库部署

!!! Abstract ""

    v3 后端通过 Spring Profile 切换 Hibernate 方言，元数据库除默认 MySQL 外，还新增了 GreatSQL、达梦、KingbaseES、Oracle、PostgreSQL、SQL Server 的支持。

## 1 支持哪些元数据库

!!! Abstract ""
    安装器默认拉起内置 **MySQL 8.4.5** 容器。改用外部库时，在 `install.conf` 里设置 `DE_SPRING_PROFILE`，应用会加载 jar 内对应的 `application-standalone-*.yml`。
| 元数据库 | `DE_SPRING_PROFILE` | JDBC 驱动 | 连接串示例 | Hibernate 方言 |
| --- | --- | --- | --- | --- |
| MySQL 8（默认） | 留空，或 `standalone_mysql` | `org.mariadb.jdbc.Driver` | `jdbc:mariadb://主机:3306/库名?...` | `MySQL8Dialect` |
| GreatSQL | `standalone-GreatSQL` | 同上 | 同上 | `MySQL8Dialect` |
| 达梦 | `standalone-dm` | `dm.jdbc.driver.DmDriver` | `jdbc:dm://主机:5236` | `io.dataease.config.CustomDMDialect` |
| KingbaseES | `standalone-kingbase` | `com.kingbase8.Driver` | `jdbc:kingbase8://主机:端口/库?currentSchema=模式` | `PostgreSQLDialect` |
| Oracle | `standalone-oracle` | `oracle.jdbc.OracleDriver` | `jdbc:oracle:thin:@主机:1521/服务名` | `io.dataease.config.DataEaseOracle11gDialect` |
| PostgreSQL | `standalone-pg` | `org.postgresql.Driver` | `jdbc:postgresql://主机:5432/库?currentSchema=模式` | `PostgreSQLDialect` |
| SQL Server | `standalone-sqlserver` | `com.microsoft.sqlserver.jdbc.SQLServerDriver` | `jdbc:sqlserver://主机:1433;DatabaseName=库名;encrypt=false` | `io.dataease.config.CustomSQLServerDialect` |

!!! Abstract ""
    桌面版另有 H2（`application-desktop.yml`），不走安装器。当前桌面版仍为 v2，v3 桌面版近期推出，此处不展开。

    切换靠两件事：

    1. **`DE_SPRING_PROFILE`** ：写入 `conf/application.yml` 的 `spring.profiles.include`，用来加载对应方言、驱动和 Quartz 配置。
    2. **连接信息** ：jar 里的 profile 文件只有占位符（如 `hostname`），必须在 `conf/` 里写成真实地址。

    `DE_EXTERNAL_MYSQL=true` 这个名字带 MySQL，实际含义是 **不要启动内置 MySQL 容器** 。用任何外部元数据库时都要设为 `true`。

## 2 外部 MySQL / GreatSQL

!!! Abstract ""
    MySQL 协议的库最简单：继续用 `DE_MYSQL_*`，不必改方言。GreatSQL 与 MySQL 兼容，也可走这条路径；若要显式加载 GreatSQL profile，把 `DE_SPRING_PROFILE` 设为 `standalone-GreatSQL`。

### 2.1 安装时指定

!!! Abstract ""
    1. 在外部库中建库、建账号，并授予建表和读写权限：

    ```sql
    CREATE DATABASE `dataease` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
    ```

    2. 解压安装包，编辑 `install.conf`：

    ```
    DE_EXTERNAL_MYSQL=true
    DE_MYSQL_HOST=外部数据库地址
    DE_MYSQL_PORT=3306
    DE_MYSQL_DB=dataease
    DE_MYSQL_USER=用户名
    DE_MYSQL_PASSWORD=密码
    ```

    密码含特殊字符时请加双引号，例如 `DE_MYSQL_PASSWORD="Test@4&^%*^"`。

    3. 执行 `install.sh`。安装器会：
        - 不启动内置 MySQL 容器；
        - 把上述信息写入 `/opt/dataease3.0/conf/application.yml`；
        - 从 `docker-compose.yml` 中去掉对内置 MySQL 的依赖。

    服务启动后会自动在该库中建表并写入初始数据（`ddl-auto: update`）。

### 2.2 已经装好了，再改成外部 MySQL

!!! Abstract ""
    默认安装目录以 `/opt/dataease3.0` 为例。需要改 **3 处** ，然后重启。

    **1. 修改 `application.yml`（必改）**

    文件：`/opt/dataease3.0/conf/application.yml`

    把 `spring.datasource` 改成外部库地址（安装时已经做过 env 替换，之后改 `.env` **不会** 自动更新这个文件）：

    ```
    spring:
      datasource:
        driver-class-name: org.mariadb.jdbc.Driver
        url: jdbc:mariadb://外部IP:3306/dataease?autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false&allowPublicKeyRetrieval=true
        username: 用户名
        password: 密码
    ```

    **2. 修改 `.env`（必改）**

    文件：`/opt/dataease3.0/.env`

    ```
    DE_EXTERNAL_MYSQL=true
    DE_MYSQL_HOST=外部IP
    DE_MYSQL_PORT=3306
    DE_MYSQL_DB=dataease
    DE_MYSQL_USER=用户名
    DE_MYSQL_PASSWORD=密码
    ```

    **3. 修改 `docker-compose.yml`（按需）**

    文件：`/opt/dataease3.0/docker-compose.yml`

    如果 `dataease` 服务下还有类似内容，请删掉，否则会等待已经不再启动的内置 MySQL：

    ```
    depends_on:
      mysql-de:
        condition: service_healthy
    ```

    **不用改** compose 里的镜像、端口、数据卷。数据库地址只写在 `application.yml` 中。

### 2.3 外部 MySQL 建议参数

!!! Abstract ""
    与安装包 `templates/my.cnf` 一致，供外部实例参考：

    ```
    [mysqld]
    default-storage-engine=INNODB
    character_set_server=utf8
    table_open_cache=128
    max_connections=2000
    max_connect_errors=6000
    innodb_file_per_table=1
    innodb_buffer_pool_size=1G
    max_allowed_packet=64M
    transaction_isolation=READ-COMMITTED
    innodb_lock_wait_timeout=1800
    sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
    skip-name-resolve
    ```

    建库请使用 `utf8mb4` / `utf8mb4_0900_ai_ci`（MySQL 8）。

## 3 达梦 / KingbaseES / Oracle / PostgreSQL / SQL Server

!!! Abstract ""
    这几类库不能只改 `DE_MYSQL_*`，必须加载对应的 Spring Profile，并单独写真实 JDBC 连接。容器会把 `/opt/dataease3.0/conf` 挂到 `/opt/apps/config`，同名的 `application-standalone-*.yml` 会覆盖 jar 里的占位配置。

    下文以 **PostgreSQL** 为例完整走一遍；达梦、KingbaseES、Oracle、SQL Server 只换第 1 节表格中的 profile、连接串、驱动类和方言即可。

### 3.1 安装前准备 (pgsql 举例)

!!! Abstract ""
    1. 在目标库中准备空库（或 Schema）和账号，授予建表、读写权限。
    2. 编辑安装包里的 `install.conf`：

    ```
    DE_EXTERNAL_MYSQL=true
    DE_SPRING_PROFILE=standalone-pg
    ```

    把 `standalone-pg` 换成上表中的 profile 名，例如 `standalone-dm`、`standalone-kingbase`。

    3. 执行 `install.sh`。安装完成后、首次访问前，先按下一节写好连接文件、按需补齐 JDBC 驱动，再启动（或改完后 `dectl restart`）。

### 3.2 写入真实连接（必做）

!!! Abstract ""
    在 `/opt/dataease3.0/conf/` 新建与 profile 同名的文件，只改主机、端口、库名、账号、密码。下面以 PostgreSQL 为例（文件名 `application-standalone-pg.yml`）：

    ```
    spring:
      datasource:
        url: jdbc:postgresql://192.168.1.10:5432/dataease?currentSchema=public
        username: 用户名
        password: 你的密码
        driver-class-name: org.postgresql.Driver
      jpa:
        properties:
          hibernate:
            dialect: org.hibernate.dialect.PostgreSQLDialect
            jdbc:
              batch_size: 1000
              lob:
                non_contextual_creation: true
              order_inserts: true
              order_updates: true
              temp:
                use_jdbc_metadata_defaults: false
        hibernate:
          naming:
            physical-strategy: io.dataease.config.DynamicCaseNamingStrategy
          ddl-auto: update
          show-sql: false

    quartz:
      enabled: true
      scheduler-name: deSyncJob
      properties.org.quartz.jobStore.driverDelegateClass: org.quartz.impl.jdbcjobstore.PostgreSQLDelegate
    ```

    同时确认 `conf/application.yml` 中有：

    ```
    spring:
      profiles:
        include: standalone-pg
    ```

    建议主配置里**不要**再保留旧的 `jdbc:mariadb://` 数据源段，避免与 profile 冲突。其他库按同样方式放置文件，连接串和方言用第 1 节表格。拷贝 jar 内 profile 到 `conf/` 时，请一并保留 Quartz 的 `driverDelegateClass`：

    - PostgreSQL / KingbaseES：`org.quartz.impl.jdbcjobstore.PostgreSQLDelegate`
    - SQL Server：`org.quartz.impl.jdbcjobstore.MSSQLDelegate`

    Oracle 示例中请把 `connection-init-sql` 的 Schema 改成实际用户：

    ```
    hikari:
      connection-init-sql: ALTER SESSION SET CURRENT_SCHEMA = 你的Schema
    ```

    KingbaseES 若走官方驱动，使用 `standalone-kingbase` 与 `jdbc:kingbase8://...`；若实例开启 PostgreSQL 兼容协议，也可按本节使用 `standalone-pg` 与 `jdbc:postgresql://...`（仍需准备对应 JDBC 驱动，见下一节）。

### 3.3 补充 JDBC 驱动（按需）

!!! Abstract ""
    元数据库走非默认 MySQL 时，启动日志若出现 `Cannot load driver class: org.postgresql.Driver`（或达梦 / 金仓 / Oracle / SQL Server 对应驱动类），说明当前镜像主 classpath 中没有该驱动，需要手动放入驱动目录。

    **驱动目录（宿主机与容器同路径）：**

    ```
    /opt/dataease3.0/data/driver/
    ```

    官方镜像的 `JAVA_OPTIONS` 已包含 `-Dloader.path=/opt/apps,/opt/dataease3.0/data/driver/`，把 jar 放进该目录即可被 PropertiesLauncher 加载，**一般不必**再改 `docker-compose` 或额外设置 `LOADER_PATH`。

    操作步骤：

    1. 准备对应驱动包，例如 PostgreSQL 可从 [Maven Central](https://repo1.maven.org/maven2/org/postgresql/postgresql/) 获取 `postgresql-42.7.4.jar`（版本可按环境调整）。达梦、KingbaseES、Oracle、SQL Server 请使用厂商提供的 JDBC jar。
    2. 拷贝到驱动目录：

    ```
    mkdir -p /opt/dataease3.0/data/driver
    cp postgresql-42.7.4.jar /opt/dataease3.0/data/driver/
    ls -l /opt/dataease3.0/data/driver/
    ```

    3. 重启 DataEase 使驱动生效：

    ```
    dectl stop
    docker rm -f dataease 2>/dev/null
    dectl start
    ```

    成功时日志中应出现 `Started CoreApplication`，且不再报 `Cannot load driver class`。

    说明：

    - 该目录同时可供业务「数据源」模块使用；元数据库 Hikari 连接也依赖同一 `loader.path`。
    - 不要放到未挂载的路径（例如自行新建的 `/opt/dataease3.0/drivers/`），否则容器内读不到。
    - KingbaseES 业务数据源或官方元库驱动，建议使用金仓安装包 `Interface/jdbc` 中的 `kingbase8-*.jar`，同样放入本目录后重启。

### 3.4 已安装环境切换

!!! Abstract ""
    1. `.env` 中设置 `DE_EXTERNAL_MYSQL=true`，并设置 `DE_SPRING_PROFILE=standalone-xxx`（PostgreSQL 为 `standalone-pg`）。
    2. `conf/application.yml` 的 `spring.profiles.include` 改成同一值；去掉冲突的旧 `jdbc:mariadb://` 配置。
    3. 在 `conf/` 放入对应的 `application-standalone-xxx.yml`，填写真实连接。
    4. 按 3.3 节确认驱动 jar 已在 `/opt/dataease3.0/data/driver/`。
    5. 从 `docker-compose.yml` 去掉对内置 MySQL 的 `depends_on`（同第 2.2 节）。
    6. `dectl restart`。

    请使用空库初始化。不要把未适配的旧库直接当新环境元数据库。

## 4 重启服务

!!! Abstract ""
    改完配置或驱动后必须重启。推荐：

    ```
    dectl restart
    ```

    也等价于：

    ```
    service dataease restart
    ```

    `dectl restart` 会先 `stop` 再 `start`。可用下面命令确认容器已起来、且没有再启动内置 MySQL：

    ```
    dectl status
    ```

    若容器反复退出，可查看：

    ```
    docker logs dataease 2>&1 | tail -n 100
    ```

## 5 注意事项

!!! Abstract ""
    - 只改 `.env` 不改 `conf/` 下的 yml，服务仍会连原来的库；安装时 envsubst 之后，再改 `.env` **不会** 自动更新 `application.yml`。
    - 设置了 `DE_SPRING_PROFILE` 却不在 `conf/` 里覆盖连接信息，会连上 jar 里的占位地址（如 `hostname`），服务无法启动。
    - 内置 MySQL 容器默认不把 3306 映射到宿主机。
    - 启动报 `Cannot load driver class: ...` 时，将对应 JDBC jar 放入 `/opt/dataease3.0/data/driver/` 后重启，详见第 3.3 节。
    - 元数据库与「数据源」模块里的业务库相互独立：业务库类型不影响元数据库选型。
