## 1 整体部署规划

!!! Abstract ""

    **HA 部署的大体方案如下：**  
    **可视具体情况在某些节点上部署多个服务，以下 IP 地址是测试高可用部署的服务器，相关配置信息如下，仅供参考。** 

    **VIP 1 个：**

    * IP 为 10.1.11.137

    **DataEase 运行节点 2 个：**

    * DataEase-1 节点，IP 为 10.1.11.5，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    * DataEase-2 节点，IP 为 10.1.11.84，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像

    **MySQL 运行节点 2 个，互为主主，Nginx 和 Keepalived 与 MySQL 共用节点：**

    * MySQL-1 节点，IP 为 10.1.11.187，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    * MySQL-2 节点，IP 为 10.1.11.189，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    
    **NFS 运行节点 1 个：**

    * NFS 节点，IP 为 10.1.11.64，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
   
    **Kettle 运行节点 3 个：**

    * Kettle-1 节点，IP 为 10.1.11.55，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    * Kettle-2 节点，IP 为 10.1.11.178，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    * Kettle-3 节点，IP 为 10.1.11.68，配置 4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像

    **Redis 运行节点 1 个，模拟单节点运行 cluster 集群：**

    * Redis 节点，IP 为 10.1.11.10，配置：4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    
    **Doris 运行节点 4 个，1 FE 3 BE：**
    
    * Doris-FE 节点，IP 为 10.1.11.39，配置：4C 16G、500G 存储，预装 CentOS 7.7 的官方镜像
    * Doris-BE-1 节点，IP 为 10.1.11.37，配置：4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    * Doris-BE-2 节点，IP 为 10.1.11.27，配置：4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像
    * Doris-BE-3 节点，IP 为 10.1.11.70，配置：4C 8G、500G 存储，预装 CentOS 7.7 的官方镜像

## 2 部署顺序

!!! Abstract ""
    1. 安装部署 NFS 服务
    2. 安装部署 MySQL 集群
    3. 安装部署 Nginx 集群
    4. 安装部署 Keepalived 及配置 VIP
    5. 安装部署 Redis 集群
    6. 安装部署 Apache Doris 集群
    7. 安装部署 Kettle 集群
    8. 安装部署 DataEase 集群
