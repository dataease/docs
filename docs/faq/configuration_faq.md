## 80 端口被占用了，如何修改为其他端口？

>可以登录到 DataEase 服务器上，在 /opt/dataease 目录下，找到 docker-compose.yml 文件，把 dataease 的运行端口 80 端口改为其他端口（注意，后端容器运行端口8081不能修改），然后执行 dectl reload 即可。

## 执行一键安装脚本时报错，提示脚本错误。
>
![安装报错](../img/faq/install-error.png)

>一键安装脚本会与 Github 进行连接，从 Github 上获取 DataEase 最新的版本信息以及最新的安装包。由于国内网络与 github 连接存在不稳定，所以有可能会导致无法获取安装所需的相关信息。
遇到这种情况的话，可以多尝试执行几次安装脚本，或者也可以到 https://github.com/dataease/dataease/releases 上下载 DataEase 的离线安装包安装。


## 如何修改 DataEase 运行的 docker 网段？

>DataEase 暂时还不支持修改 docker 运行网段。


## 如何与 MeterSphere 安装在同一台服务器上？
>DataEase 与 MeterSphere 安装在同一台服务器上时，有可能会发生以下冲突：
>
- docker 网段冲突
- mysql 容器名冲突

!!! tips ""
由于 MeterSphere 在运行时并没有指定运行网段，所以不一定会产生 docker 网段冲突，如没有网段冲突，则可以直接跳到第三步执行。

1. 修改 MeterSphere 的网段
> 修改 /opt/metersphere/docker-compose-base.yml，网络部分定义如下：
```yml
networks:
  ms-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.20.0.0/16
          gateway: 172.20.0.1
```

2. 重启 MeterSphere 服务
>
```shell
# uninstall 可以在停止 MeterSphere 服务的同时，删除其对应的 docker network
msctl uninstall
# reload 会重新启动 MeterSphere 服务，并按照第一步的设置创建新的 docker network
msctl reload
```

3. 修改 DataEase MySQL 容器相关配置
> 修改 /opt/dataease/docker-compose.yml，将 dataease 的 depends_on 里的 mysql 改为 mysql-de，例如：
```yml
  dataease:
    image: registry.cn-qingdao.aliyuncs.com/dataease/dataease:v1.0.0
    container_name: dataease
    ports:
      - 80:8081
    mem_limit: 4096m
    volumes:
      - dataease-conf:/opt/dataease/conf
      - dataease-logs:/opt/dataease/logs
      - dataease-plugins:/opt/dataease/plugins/thirdpart
      - dataease-kettle-data:/opt/dataease/data/kettle
    depends_on:
      mysql-de:
        condition: service_healthy
```
> 修改 /opt/dataease/docker-compose-mysql.yml，将 mysql 相关的容器名改为 mysql-de，例如：
```yml
  mysql-de:
    image: registry.cn-qingdao.aliyuncs.com/dataease/mysql:5.7.25
    container_name: mysql-de
```
> 修改 /opt/dataease/conf/dataease.properties，将数据库 URL 信息改为如下：
```properties
spring.datasource.url=jdbc:mysql://mysql-de:3306/dataease?autoReconnect=false&useUnicode=true&characterEncoding=UTF-8&characterSetResults=UTF-8&zeroDateTimeBehavior=convertToNull&useSSL=false
```

4. 修改 DataEase 服务启动端口（可选）
> 修改 /opt/dataease/docker-compose.yml，将 dataease 的运行端口改为如8088（注意，后端容器运行端口8081不能修改)：
```yml
  dataease:
    image: registry.cn-qingdao.aliyuncs.com/dataease/dataease:v1.0.0
    container_name: dataease
    ports:
      - 8088:8081
```

5. 启动 DataEase 服务
>
```shell
dectl reload
```