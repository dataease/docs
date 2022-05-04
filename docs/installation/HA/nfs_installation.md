## 1 准备工作

!!! Abstract ""
    **NFS 服务器信息：**

    * IP： 10.1.11.205

## 2 环境要求

!!! Abstract ""
    **部署 NFS 服务器要求：**

    * 操作系统：CentOS 7.x
    * CPU/内存：4 核 8G
    * 磁盘空间：500G

## 3 NFS 服务器端安装与配置

!!! Abstract "" 
    **安装 NFS 服务的软件包：**
    ```
    yum install -y nfs-utils
    ```

    创建 NSF 目录：
    ```
    mkdir -p /nfs-share
    chmod 666 /nfs-share
    ```

    编辑 exports 文件：命令中的 “10.1.11.0/24” 替换为各自具体的网段：
    ```
    echo "/nfs-share 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports
    ```

    rpcbind 和 NFS 做开机启动：
    
    **提示：** 必须先启动 rpcbind 服务。
    ```
    systemctl enable rpcbind.service
    systemctl enable nfs-server.service
    ```
 
    分别启动 rpcbind 和 NFS 服务：
    ```
    systemctl start rpcbind.service
    systemctl start nfs-server.service
    ```

    设置 exports 配置生效：
    ```
    exportfs -r
    ```

    检查 exports 是否生效：
    ```
    exportfs
    # 10.1.11.205 为 nfs 服务器地址，即当前机器地址
    showmount -e 10.1.11.205
    ```
![check_nfs](../../img/installation/HA/check_nfs.png){ width="900px" }

## 4 NFS 客户端安装与配置

!!! Abstract ""  
    **安装 NFS 服务的软件包：**
    ```
    yum install -y nfs-utils
    ```

    创建挂载目录：
    ```
    mkdir -p /opt/kettle/data
    ```

    挂载：
    ```
    echo "10.1.11.205:/nfs-share /opt/kettle/data nfs defaults 0 0" >> /etc/fstab
    mount -a
    ```
