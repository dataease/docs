## 1 准备工作

!!! Abstract ""
    DataEase 本身并不需要 Kettle 组成集群模式，多个独立的 Kettle 节点也可以由 DataEase 内部的调用策略来分配使用。

### 1.1 服务器准备

!!! Abstract ""
    此处搭建三个 Kettle 节点，节点规划如下：

    - kettle-1 节点，IP 为 10.1.11.55
    - kettle-2 节点，IP 为 10.1.11.178
    - kettle-3 节点，IP 为 10.1.11.68

    所有服务器的操作系统均为 CentOS 7，这里使用的是 CentOS 7.7，服务器硬件配置视数据规模而定。

    其他信息：

    - NFS 节点，IP 为 10.1.11.64，用于 Kettle 的挂载路径为 /opt/kettle


### 1.2 软件准备

!!! Abstract ""
    下载 Kettle 安装包，此处使用的是 pdi-ce-8.3.0.0-371.zip。

### 1.3 防火墙

!!! Abstract ""
    此处我们会在 18080 端口运行 Kettle，所以需要保证 18080 端口可被外部访问，可以执行以下命令打开防火墙的 18080 端口：

    ```shell
    firewall-cmd --zone=public --add-port=18080/tcp --permanent
    firewall-cmd --reload
    ```

## 2 安装 NFS

### 2.1 挂载 NFS 目录

!!! Abstract ""
    由于 Kettle 需要使用通过 DataEase 上传的 Excel 文件，此处采用了 NFS 方案。

    ```shell
    # 安装 NFS 相关软件包
    yum install -y nfs-utils

    # 创建要挂载的目录
    mkdir -p /opt/dataease/data/kettle

    # 修改 /etc/fstab 文件
    echo "10.1.11.64:/opt/kettle /opt/dataease/data/kettle nfs defaults 0 0" >> /etc/fstab
    ```

### 2.2 挂载

!!! Abstract ""
    ```
    mount -a
    ```

### 2.3 安装 JDK 1.8

!!! Abstract ""
    执行命令安装 OpenJDK 1.8：

    ```shell
    yum install -y java-1.8.0-openjdk
    ```

## 3 安装 Kettle

### 3.1 解压安装包

!!! Abstract ""
    执行命令将安装包解压到 /opt/kettle 目录下：
    ```shell
    unzip -d /opt/kettle pdi-ce-8.3.0.0-371.zip
    ```
### 3.2 安装驱动

!!! Abstract ""
    Kettle 需要通过数据库驱动程序来连接各类数据源，官方提供的安装包内驱动程序并不齐全，此处需要额外添加几个驱动，可以通过百度网盘进行下载：  
    链接: https://pan.baidu.com/s/1bTpL1MtFnebaOv1wqKhulQ?pwd=ltvj 提取码: ltvj

### 3.3 创建配置文件

!!! Abstract ""
    创建 Kettle 运行时的配置文件，将数据目录指向 NFS 路径：

    ```properties
    mkdir -p /opt/kettle/conf/.kettle

    cat > /opt/kettle/conf/.kettle/repositories.xml <<EOF
    <?xml version="1.0" encoding="UTF-8"?>
    <repositories>
     <repository>
     <id>KettleFileRepository</id>
     <name>repo</name>
     <description>File repository</description>
     <is_default>false</is_default>
     <base_directory>/opt/dataease/data/kettle</base_directory>
     <read_only>N</read_only>
     <hides_hidden_files>N</hides_hidden_files>
     </repository>
    </repositories>
    EOF
    ```

### 3.4 配置环境变量

!!! Abstract ""
    设置环境变量 KETTLE_HOME：
    
    ```conf
    echo "KETTLE_HOME=/opt/kettle/conf" >> /etc/profile
    source /etc/profile
    ```

### 3.5 运行 Kettle

!!! Abstract ""
    执行启动命令：
    ```conf
    nohup /opt/kettle/data-integration/carte.sh 0.0.0.0 18080 &
    ```