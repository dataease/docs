# 多数据库部署

## 1 功能概述

!!! Abstract ""
    DataEase v3.0.0 起，系统元数据库支持部署到以下 7 种数据库：

| 部署数据库 | 配置文件 | 驱动类 | 说明 |
|---|---|---|---|
| MySQL | application-standalone_mysql.yml | com.mysql.cj.jdbc.Driver | 默认部署数据库 |
| GreatSQL | application-standalone-GreatSQL.yml | org.mariadb.jdbc.Driver | 兼容 MySQL 协议 |
| 达梦 DM | application-standalone-dm.yml | dm.jdbc.driver.DmDriver | 国产数据库 |
| KingbaseES | application-standalone-kingbase.yml | com.kingbase8.Driver | 国产数据库 |
| Oracle | application-standalone-oracle.yml | oracle.jdbc.driver.OracleDriver | — |
| PostgreSQL | application-standalone-pg.yml | org.postgresql.Driver | — |
| SQL Server | application-standalone-sqlserver.yml | com.microsoft.sqlserver.jdbc.SQLServerDriver | — |

## 2 部署方式

!!! Abstract ""
    v3.0.0 采用源码部署或 Docker 镜像部署时，通过选择不同的配置文件即可切换元数据库。系统根据所选数据库自动适配对应的 Hibernate 方言，无需额外配置 SQL 方言差异。

!!! Abstract ""
    以 KingbaseES 为例，配置文件关键内容如下：

```yaml
spring:
  datasource:
    driver-class-name: com.kingbase8.Driver
    url: jdbc:kingbase8://host:port/db?currentSchema=schema
    username: user
    password: password
  jpa:
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
```

## 3 注意事项

!!! Abstract ""
    - 部署前请先在目标数据库中创建好对应的数据库实例与账号，并授予读写权限；
    - 达梦数据库使用自定义方言 `io.dataease.config.CustomDMDialect`，请勿修改；
    - 切换部署数据库需在全新环境执行初始化，不支持直接迁移存量元数据；
    - 定时任务（Quartz）基于 JDBC JobStore 持久化，随元数据库一同部署。
