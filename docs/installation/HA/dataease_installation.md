## 1 准备工作

!!! Abstract ""
    **DataEase 环境的搭建需要准备以下服务器：**

    * 节点 A： 10.1.11.174
    * 节点 B： 10.1.11.175

## 2 环境要求

!!! Abstract ""
    **部署 DataEase 服务器要求：**

    * 操作系统：CentOS 7.x
    * CPU/内存：4 核 8G
    * 磁盘空间：500G
    
## 3 配置文件

!!! Abstract ""
    **注意：**
    
     1. 在安装前需要离线下载 DataEase 最新安装包并传输至服务器内，且需要对 DataEase 运行时所需的一些配置文件进行修改；       
     2. 修改 install.conf 文件，将 DE_ENGINE_MODE 设置为 cluster，将 VIP 地址和映射的 MySQL 服务端口等信息填入对应的 MySQL 相关配置信息中，且 DE_EXTERNAL_MYSQL 设置为 true。

!!! Abstract ""	
	**修改 dataease.properties 文件，加入 Redis 相关设置。根据实际 Redis 的配置放开对应的参数，并填入对应的信息即可。**
    ```
    spring.cache.type=redis
    
    #redis 公共配置
    spring.redis.timeout=10000
    spring.redis.lettuce.pool.max-active=8
    spring.redis.lettuce.pool.max-wait=-1
    spring.redis.lettuce.pool.max-idle=8
    
    #单机模式 redis 配置
    #spring.redis.database=0
    #spring.redis.host=10.1.11.197
    #spring.redis.port=6379
    #spring.redis.password=admin123456
    
    #哨兵模式 redis 配置
    #spring.redis.sentinel.master=mymaster
    #spring.redis.sentinel.nodes=10.1.11.197:6379,10.1.11.197:6380,10.1.11.197:6381
    #spring.redis.sentinel.password=admin123456
    
    #cluster模式 redis 配置
    #spring.redis.cluster.nodes=10.1.11.197:6379,10.1.11.197:6380,10.1.11.197:6381,10.1.11.197:6382,10.1.11.197:6383,10.1.11.197:6384
    #spring.redis.cluster.max-redirects=3
    #spring.redis.password=admin123456
    ```

## 4 准备 Excel 文件目录

!!! Abstract ""
	**默认目录路径为：**
    ```
    /opt/dataease/data/kettle
    ```
   
    安装 NFS 服务的软件包：
    ```
    yum install -y nfs-utils
    ```

    创建挂载目录：
    ```
    mkdir -p /opt/dataease/data/kettle
    ```

    挂载：
    ```
    echo "10.1.11.205:/nfs-share /opt/dataease/data/kettle nfs defaults 0 0" >> /etc/fstab
    mount -a
    ```

## 5 部署服务

!!! Abstract ""
    **执行安装包下的安装文件进行服务的部署：**
    ```
    bash install.sh
    ```


