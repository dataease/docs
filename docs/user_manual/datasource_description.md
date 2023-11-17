## 1 功能概述

!!! Abstract ""
    【数据源】用来管理各类数据连接信息，是后续数据分析操作中数据的来源；  
    点击【数据源】，进入数据源管理功能模块，该页面包括数据连接的新增（序号 1）、搜索（序号 2）、编辑（序号 3）、复制（序号 4）、删除（序号 5）等功能。

![数据源管理页面](../img/datasource_configuration/数据源管理页面.png){ width="900" }

## 2 支持的数据源类型

!!! Abstract ""
    - **数据仓库/数据湖：** Apache Hive、AWS RedShift、MaxCompute、Apache Kylin
    - **OLTP 型数据库：** MySQL、MongoDB、SQL Server、Oracle、PostgreSQL、MariaDB、Db2、TiDB、达梦（DM）
    - **OLAP 型数据库：** Elasticsearch、ClickHouse、Apache Doris、Apache Impala、StarRocks、Presto、KingBase
    - **数据文件：** Excel、CSV
    - **API 数据源**

![支持的数据源类型](../img/datasource_configuration/支持的数据源类型.png){ width="900" }

!!! Abstract ""
    以下版本为 DataEase 对接调试版，可供参考，其它版本您也可正常对接，若不满足可尝试通过在驱动管理处添加相应版本驱动解决。

    - SQL Server - 2019
    - Elasticsearch - 7.10.1、8.1.1
    - Oracle - 12.2.0.1
    - MongoDB - 4.4.13、5.0.6
    - Db2 - 10.5、11.5.7.0
    - TiDB - 5.3.1
    - PostgreSQL - 12.10、14.2
    - ClickHouse - 22.1.4.30
    - Hive - 2.3.2
    - Kylin - 4.0.0
    - MariaDB - 10.7.8
    - 达梦 - DM8
    - MySQL - 5.7.36
    - Impala - 4.0.0
    - Doris - 0.15、1.0.0、1.1.0
    - Presto - 0.272
    - KingBase8 - 8.6.0

## 3 数据源驱动管理

!!! Abstract ""
    支持手动上传数据源驱动程序，通常无需自行上传新的驱动，若数据源无法正常链接，则可通过上传与用户数据库匹配的驱动版本使用，下图以添加 MySQL 驱动为示例。

![数据源驱动管理入口](../img/datasource_configuration/数据源驱动管理入口.png){ width="900" }

!!! Abstract ""
    填写驱动名称，选择驱动类型 "MySQL"，并填入驱动类名 "com.mysql.jdbc.Driver"，上传驱动文件，保存即可。

![数据源管理_添加驱动](../img/datasource_configuration/数据源管理_添加驱动.png){ width="900" }

![上传驱动](../img/datasource_configuration/上传驱动.png){ width="900" }

!!! Abstract ""
    在数据源配置界面手动选择上一步创建的驱动名称。

![选择上传的驱动](../img/datasource_configuration/选择上传的驱动.png){ width="900" }