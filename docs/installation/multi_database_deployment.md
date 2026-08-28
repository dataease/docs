# 外部数据库部署

!!! Abstract ""
    v3 元数据库除默认内置 MySQL 外，还支持 GreatSQL、达梦（DM）、KingbaseES、Oracle、PostgreSQL、SQL Server 等。

    **数据库类型与 JPA / Hibernate 方言等配置已集成到安装脚本中。** 安装时按提示选择数据库类型即可。

## 1 支持的元数据库

!!! Abstract ""
    安装器默认拉起内置 MySQL 容器。改用外部库时，可在运行 `install.sh` 时交互选择，或预先编辑 `install.conf`：

| `DE_DB_TYPE` | 说明 |
| --- | --- |
| `mysql` | MySQL（默认，含内置容器场景） |
| `GreatSQL` | GreatSQL |
| `DM` | 达梦 |
| `Kingbase` | KingbaseES |
| `Oracle` | Oracle |
| `PostgreSQL` | PostgreSQL |
| `SQLServer` | SQL Server |


## 2 安装时选用外部数据库

!!! Abstract ""
    1. 在外部库中建库（或 Schema）、建账号，并授予建表与读写权限。以 MySQL 为例：

    ```sql
    CREATE DATABASE `dataease` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    ```

    2. 解压安装包后，任选其一：

    - **交互安装**：直接执行 `install.sh`，按提示选择是否使用外部数据库、数据库类型，并填写连接信息。
    - **预配置**：编辑 `install.conf`，例如：

    ```
    DE_EXTERNAL_DB=true
    DE_DB_TYPE=mysql
    DE_DB_HOST=外部数据库地址
    DE_DB_PORT=3306
    DE_DB_DATABASE=dataease
    DE_DB_SCHEMA=
    DE_DB_USER=用户名
    DE_DB_PASSWORD=密码
    ```

    密码含特殊字符时请加双引号，例如 `DE_DB_PASSWORD="Test@4&^%*^"`。其他库类型将 `DE_DB_TYPE` 改为上表对应值，并填写正确的主机、端口、库名 / Schema。

    3. 执行 `/bin/bash install.sh`。安装器会：
        - 不启动内置 MySQL 容器（在 `DE_EXTERNAL_DB=true` 时）；
        - 按所选数据库类型自动写入所需配置（含 JPA 相关设置）；
        - 在目标库中自动建表并写入初始数据。

## 3 外部 MySQL 建议参数

!!! Abstract ""
    若外部库为 MySQL，可参考如下参数（与安装包模板接近）：

    ```
    [mysqld]
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
    innodb_lock_wait_timeout=1800
    group_concat_max_len=1024000
    sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
    skip-name-resolve
    ```

    请特别关注：`character_set_server`、`lower_case_table_names`、`group_concat_max_len`。建库建议使用 `utf8mb4`。

## 4 非 MySQL 驱动说明

!!! Abstract ""
    使用达梦、KingbaseES、Oracle、PostgreSQL、SQL Server 等外部库时，若启动日志出现 `Cannot load driver class: ...`，请将对应 JDBC 驱动 jar 放到：

    ```
    /opt/dataease3.0/data/driver/
    ```

    然后执行：

    ```
    dectl restart
    ```

    官方镜像已通过 `loader.path` 加载该目录，一般无需再改 compose。

## 5 注意事项

!!! Abstract ""
    - 优先通过 **安装脚本交互选择** 或 **`install.conf` 中的 `DE_DB_*` / `DE_EXTERNAL_DB`** 完成外部库配置；安装脚本会处理 JPA 等细节。
    - 内置 MySQL 容器默认不把 3306 映射到宿主机。
    - 元数据库与「数据源」模块中的业务库相互独立。
    - 请使用空库初始化；不要将未适配的旧库直接作为新环境元数据库。
    - 改完配置或驱动后请执行 `dectl restart`（或 `service dataease restart`），并用 `dectl status` 确认状态。
