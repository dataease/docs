## 1 NFS 服务器端安装与配置

### 1.1 环境信息

!!! Abstract ""
    **注意：** NFS 在集群中起到存储 Excel、插件包等文件的作用。  
    **NFS 服务器信息如下：**

    - IP 为 10.1.11.64

### 1.2 防火墙

!!! Abstract ""
    **为了避免 NFS 服务的通信问题，可以先将防火墙关闭，或者打开对应的端口。**
    ```shell
    systemctl stop firewalld
    ```

### 1.3 安装 NFS 服务器所需的软件包

!!! Abstract ""
    ```shell
    yum install -y nfs-utils
    ```

### 1.4 创建 NFS 目录

!!! Abstract ""
    ```shell
    mkdir -p /opt/kettle /opt/plugins/thirdpart /opt/static-resource /opt/custom-drivers /opt/custom /opt/business
    chmod 666 -R /opt/kettle /opt/plugins/thirdpart /opt/static-resource /opt/custom-drivers /opt/custom /opt/business
    ```

### 1.5 编辑 exports 文件

!!! Abstract ""
    **以下命令中的 “10.1.11.0/24” 请替换为各自具体的网段。**

    ```shell
    echo "/opt/kettle 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports
    
    echo "/opt/static-resource 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports
    
    echo "/opt/plugins/thirdpart 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports

    echo "/opt/custom-drivers 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports

    echo "/opt/custom 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports

    echo "/opt/business 10.1.11.0/24(rw,no_root_squash,no_all_squash,sync)" >> /etc/exports

    mount -a
    ```  

    文件夹存放文件介绍：  
    ```shell
    - kettle：Excel、CSV 文件；  
    - static-resource：图片等静态文件；  
    - thirdpart：外部插件包；  
    - custom-drivers：数据库驱动包；    
    - custom：地图文件；  
    - business：第三方平台定时报告附件。
    ```

### 1.6 rpcbind 和 NFS 做开机启动

!!! Abstract ""
    **NFS 服务器使用 rpcbind 来实现端口映射工作，必须先启动 rpcbind 服务。**

    ```shell
    systemctl enable rpcbind.service
    systemctl enable nfs-server.service
    ```

### 1.7 分别启动 rpcbind 和 NFS 服务

!!! Abstract ""
    ```shell
    systemctl start rpcbind.service
    systemctl start nfs-server.service
    ```

### 1.8 让 exports 配置生效

!!! Abstract ""
    ```shell
    exportfs -r
    ```

### 1.9 检查 exports 是否生效

!!! Abstract ""
    ```conf
    exportfs
    # 10.1.11.64 为 NFS 服务器地址，即当前机器地址
    showmount -e 10.1.11.64
    ```