## 1 备份

!!! Abstract ""
    DataEase 集群中各节点是通过 NFS 共享节点的数据，所以只需要备份 DataEase 集群环境中的 NFS 服务器的目录文件即可。
    ```sh
    #登录到 NFS 服务器操作：
    #新建 dataease-bak 目录，将持久化文件复制到该目录
    mkdir /opt/dataease-bak
    cp -r /opt/kettle /opt/plugins/ /opt/static-resource /opt/custom-drivers /opt/custom /opt/business /opt/dataease-bak
    # /opt/dataease-bak 目录则是备份文件，恢复时可将该目录中的文件复制到 NFS 服务器的原目录 /opt 即可。
    ```

!!! Abstract ""
    MySQL 数据库是单独部署的，所以需要备份 MySQL 中的数据。
    ```sh
    #登录 MySQL 服务器，执行备份命令
    mysqldump -uroot -pPassword123@mysql dataease >>  /opt/mysql-dataease.bak.sql
    mysqldump -uroot -pPassword123@mysql -ntd -R dataease > /opt/mysql-function.bak.sql
    ```

## 2 还原

!!! Abstract ""
    DataEase 集群环境的恢复数据操作，只要恢复 NFS 目录文件和 MySQL 备份即可。
    ```sh
    #登录 NFS 服务器，将备份的 dataease-bak 恢复至原目录 /opt
    cp -r dataease-bak/* /opt/
    # 覆盖原文件
 
    #登录 MySQL 服务器，将备份的 SQL 导入
    mysql -uroot -pPassowrd123@mysql
    use dataease
    source /opt/mysql-dataease.bak.sql;
    source /opt/mysql-function.bak.sql;  
 
    #如果 dataease 库删除了，需要先创建 dataese 库
    CREATE DATABASE `dataease` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
 
    #登录 DataEase 每个节点加载 dataease 服务
    dectl reload
    ```