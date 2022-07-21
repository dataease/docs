## 1 准备工作

### 1.1 服务器准备

!!! Abstract ""
    **此处搭建一个简单的 Apache Doris 集群，集群节点规划：**

    - 1 个 FE 节点，IP 为 10.1.11.39
    - 3 个 BE 节点，IP 分别为 10.1.11.37，10.1.11.27，10.1.11.70

    所有服务器的操作系统均为 CentOS 7，这里使用的是 CentOS 7.7，服务器硬件配置视数据规模而定，可参考[ Apache Doris 官方文档](https://doris.apache.org/zh-CN/docs/install/install-deploy/)。

### 1.2 软件准备

!!! Abstract ""
    从 Apache Doris 官网[下载 Doris 的安装包](https://doris.apache.org/zh-CN/download/) ， 将安装包放在所有 Doris 节点服务器上，这里下载的是 1.0.0 版本的安装包。

    下载了 Doris 安装包后，将安装包解压，放置于自己的运行目录下。这处示例将安装包放置于 /opt/doris 目录下，结构如下所示：
    ```conf
    [root@doris-1 opt]# tree -L 2
    .
    └── doris
        ├── apache_hdfs_broker
        ├── be
        ├── CHANGE-LOG.txt
        ├── DISCLAIMER
        ├── fe
        ├── LICENSE-dist.txt
        ├── licenses
        ├── NOTICE-dist.txt
        ├── README
        └── udf
    
    6 directories, 5 files
    ```

### 1.3 操作系统参数设置

!!! Abstract ""
    **设置系统最大打开文件句柄数，修改 /etc/security/limits.conf**

    ```conf
    echo "* soft nofile 204800" >> /etc/security/limits.conf
    echo "* hard nofile 204800" >> /etc/security/limits.conf
    echo "* soft nproc 204800" >> /etc/security/limits.conf
    echo "* hard nproc 204800 " >> /etc/security/limits.conf
    ```

    修改 /etc/sysctl.conf
    
    ```conf
    echo fs.file-max = 6553560 >> /etc/sysctl.conf
    ```

    设置完参数后，可以重启一下服务器。

### 1.4 防火墙

!!! Abstract ""
    **Doris 各个实例直接通过网络进行通讯，以下表格展示了所有需要的端口：**

| 实例名称 | 端口名称 | 默认端口 | 通讯方向 | 说明                                     |
| --- | --- | --- | --- |----------------------------------------|
| BE | be_port                  | 9060 | FE --> BE | BE 上 thrift server 的端口，用于接收来自 FE 的请求   |
| BE | webserver_port           | 8040 | BE <--> BE | BE 上的 http server 的端口                  |
| BE | heartbeat_service_port   | 9050 | FE --> BE | BE 上心跳服务端口（thrift），用于接收来自 FE 的心跳       |
| BE | brpc_port                | 8060 | FE <--> BE, BE <--> BE | BE 上的 brpc 端口，用于 BE 之间通讯               |
| FE | http_port                | 8030 | FE <--> FE，用户 <--> FE | FE 上的 http server 端口                   |
| FE | rpc_port                 | 9020 | BE --> FE, FE <--> FE | FE 上的 thrift server 端口，每个 fe 的配置需要保持一致 |
| FE | query_port               | 9030 | 用户 <--> FE | FE 上的 mysql server 端口                  |
| FE | edit_log_port            | 9010 | FE <--> FE | FE 上的 bdbje 之间通信用的端口                   |

!!! Abstract ""
    如果简单处理，也可以将防火墙关闭：

    ```shell
    service firewalld stop
    ```

## 2 安装运行 Doris FE

### 2.1 Java 运行环境

!!! Abstract ""
    **Doris FE 是 Java 项目，它的运行需要有 JRE 的环境支持，在 FE 节点上安装 Java 环境：**
    ```conf
    yum install -y java-1.8.0-openjdk

    echo "export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk" >> /etc/profile
    source /etc/profile
    ```

### 2.2 配置 FE

!!! Abstract ""
    **获取 Doris 节点所处的内网网段，此示例的内网网段的 CIDR 是 10.1.11.0/24。**  
    如不清楚，也可执行命令查询：
    ```conf
    [root@Doris-1 ~]# ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
            valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
            valid_lft forever preferred_lft forever
    2: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 00:50:56:bb:75:3e brd ff:ff:ff:ff:ff:ff
        inet 10.1.11.39/24 brd 10.1.11.255 scope global noprefixroute ens192
            valid_lft forever preferred_lft forever
        inet6 fe80::250:56ff:febb:753e/64 scope link noprefixroute
            valid_lft forever preferred_lft forever
    ```

    返回结果中的 10.1.11.39/24，也可作为当前节点的 CIDR 使用。

    将网段信息配置到 /opt/doris/fe/conf/fe.conf 配置文件中：
    ```conf
    echo "priority_networks = 10.1.11.39/24" >> /opt/doris/fe/conf/fe.conf
    ```
    fe.conf 配置文件中很多参数默认是注释状态，可以根据实际情况来调整，例如：
    ```conf
    qe_max_connection = 65535
    max_conn_per_user = 1024
    sys_log_delete_age=1d
    audit_log_delete_age=3d
    exec_mem_limit=8589934592
    tablet_create_timeout_second=30
    catalog_trash_expire_second = 60
    enable_batch_delete_by_default=true
    max_layout_length_per_row=10000000
    ```

### 2.3 启动 FE

!!! Abstract ""
    **执行启动命令：**
    ```shell
    bash /opt/doris/fe/bin/start_fe.sh --daemon
    ```
    可以通过查看 FE 的运行日志来了解 FE 的启动情况：
    ```shell
    tail -f /opt/doris/fe/log/fe.log
    ```

## 3 安装运行 Doris BE

### 3.1 配置 BE

!!! Abstract ""
    **获取 Doris 节点所处的内网网段，此示例的内网网段的 CIDR 是 10.1.11.0/24。**  
    如不清楚，也可参考之前配置 FE 时，通过命令 ip a 获取。
    将网段信息配置到 /opt/doris/be/conf/be.conf 配置文件中：
    ```shell
    echo "priority_networks = 10.1.11.0/24" >> /opt/doris/be/conf/be.conf
    ```
    be.conf 配置文件中很多参数默认是注释状态，可根据实际情况来调整。

### 3.2 启动 BE

!!! Abstract ""
    **执行启动命令：**
    ```shell
    bash /opt/doris/be/bin/start_be.sh --daemon
    ```

    可以通过查看 BE 的运行日志来了解 BE 的启动情况：
    ```shell
    tail -f /opt/doris/be/log/be.INFO
    ```

## 4 配置集群

### 4.1 登录 FE

!!! Abstract ""
    **以 MySQL client 登录 FE，初始时 FE root 用户无密码：**
    ```shell
    mysql -uroot -h10.1.11.39 -P9030
    ```

### 4.2 在 FE 中添加 BE 节点

!!! Abstract ""
    ```conf
    mysql> ALTER SYSTEM ADD BACKEND '10.1.11.37:9050';
    Query OK, 0 rows affected (0.06 sec)
    
    mysql> ALTER SYSTEM ADD BACKEND '10.1.11.27:9050';
    Query OK, 0 rows affected (0.00 sec)
    
    mysql> ALTER SYSTEM ADD BACKEND '10.1.11.70:9050';
    Query OK, 0 rows affected (0.01 sec)
    ```

### 4.3 查询 BE 是否成功添加

!!! Abstract ""
    ```conf
    mysql> show proc '/backends';
    +-----------+-----------------+------------+------------+---------------+--------+----------+----------+---------------------+---------------------+-------+----------------------+-----------------------+-----------+------------------+---------------+---------------+---------+----------------+--------------------------+--------+--------------------+-------------------------------------------------------------------------------------------------------------------------------+
    | BackendId | Cluster         | IP         | HostName   | HeartbeatPort | BePort | HttpPort | BrpcPort | LastStartTime       | LastHeartbeat       | Alive | SystemDecommissioned | ClusterDecommissioned | TabletNum | DataUsedCapacity | AvailCapacity | TotalCapacity | UsedPct | MaxDiskUsedPct | Tag                      | ErrMsg | Version            | Status                                                                                                                        |
    +-----------+-----------------+------------+------------+---------------+--------+----------+----------+---------------------+---------------------+-------+----------------------+-----------------------+-----------+------------------+---------------+---------------+---------+----------------+--------------------------+--------+--------------------+-------------------------------------------------------------------------------------------------------------------------------+
    | 11002     | default_cluster | 10.1.11.27 | 10.1.11.27 | 9050          | 9060   | 8040     | 8060     | 2022-05-13 12:39:38 | 2022-05-13 14:19:22 | true  | false                | false                 | 7         | 2.179 KB         | 93.932 GB     | 96.941 GB     | 3.10 %  | 3.10 %         | {"location" : "default"} |        | 1.0.0-rc03-Unknown | {"lastSuccessReportTabletsTime":"2022-05-13 14:18:34","lastStreamLoadTime":-1,"isQueryDisabled":false,"isLoadDisabled":false} |
    | 11001     | default_cluster | 10.1.11.37 | 10.1.11.37 | 9050          | 9060   | 8040     | 8060     | 2022-05-13 12:46:46 | 2022-05-13 14:19:22 | true  | false                | false                 | 2         | 2.146 KB         | 93.936 GB     | 96.941 GB     | 3.10 %  | 3.10 %         | {"location" : "default"} |        | 1.0.0-rc03-Unknown | {"lastSuccessReportTabletsTime":"2022-05-13 14:19:11","lastStreamLoadTime":-1,"isQueryDisabled":false,"isLoadDisabled":false} |
    | 11003     | default_cluster | 10.1.11.70 | 10.1.11.70 | 9050          | 9060   | 8040     | 8060     | 2022-05-13 12:45:41 | 2022-05-13 14:19:22 | true  | false                | false                 | 3         | 1.063 KB         | 93.932 GB     | 96.941 GB     | 3.10 %  | 3.10 %         | {"location" : "default"} |        | 1.0.0-rc03-Unknown | {"lastSuccessReportTabletsTime":"2022-05-13 14:18:23","lastStreamLoadTime":-1,"isQueryDisabled":false,"isLoadDisabled":false} |
    +-----------+-----------------+------------+------------+---------------+--------+----------+----------+---------------------+---------------------+-------+----------------------+-----------------------+-----------+------------------+---------------+---------------+---------+----------------+--------------------------+--------+--------------------+-------------------------------------------------------------------------------------------------------------------------------+
    3 rows in set (0.35 sec)
    ```
    查询结果中 Alive 字段为 true 则表示添加成功。

### 4.4 创建 DataEase 库及初始化 FE 密码
    
!!! Abstract ""
    ```conf
    mysql> CREATE DATABASE dataease;
    Query OK, 0 rows affected (0.02 sec)

    mysql> SET PASSWORD FOR 'root' = PASSWORD('Password123@doris');
    Query OK, 0 rows affected (0.00 sec)
    ```