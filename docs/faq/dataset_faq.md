## 1 添加 Excel 数据集时出现 java.sql.SQLSyntaxErrorException: errCode = 2, detailMessage = The size of a row (1048587) exceed the maximal row size: 1000000

!!! Abstract ""
    1. 修改配置文件: /opt/dataease/conf/fe.conf，将参数改为：max_layout_length_per_row=10000000；
    2. 重启 doris-fe: docker restart doris-fe。

## 2 创建 Excel 数据集或定时同步类型的数据集时，提示 "Access denied for user 'root'(using password:YES)

![doris错误](../img/faq/doris-invalid.png){ width="900px" }

!!! Abstract ""
    **上图的错误是由于 Doris 的配置导致的，一般有两种可能：  
    1. /opt/dataease/conf/dataease.properties 配置文件中，Doris 的连接信息配置错误；  
    2. Doris 初始化时初始密码设置出错。**

    第一种情况，只要把 dataease.properties 配置文件中相关配置信息修改正确后，service dataease restart 即可。  
    第二种情况可以通过以下步骤来判断：  
    连接 doris-fe，以内置 MySQL 举例：  
    ```shell
    # 进入内置 MySQL 容器内
    docker exec -it mysql sh
    # 连接 doris-fe，如果能访问，则不是登录信息问题；如果不能访问，而删除命令中密码部分可直接访问的话，则确定是第二种情况
    mysql -uroot -h doris-fe -P 9030 -pPassword123@doris
    ```
    第二种情况的话，可以先通过下面的步骤来修复：
    ```shell
    # 停止 DataEase 服务
    service dataease stop
    # 删除错误的 doris 配置信息
    rm -rf /opt/dataease/data/fe/*
    rm -rf /opt/dataease/data/be/*
    # 启动 DataEase 服务
    service dataease start
    ```
    如果上述修复方案未生效的话，可以手动初始化一下 Doris。  
    1. 进入 doris-fe  
    可以用任意 MySQL Client 连接 doris-fe，以下以 DataEase 内置的 MySQL 举例：  
    ```shell
    # 进入内置 MySQL 容器内
    docker exec -it mysql sh
    # 进入 MySQL 容器后，连接 doris-fe
    mysql -uroot -h doris-fe -P 9030
    ```
    2. 初始化 Doris  
    连接上 doris-fe 后，执行下面的语句：  
    ```mysql
    ALTER SYSTEM ADD BACKEND "172.19.0.199:9050";
    SET PASSWORD FOR 'root' = PASSWORD('Password123@doris');
    CREATE DATABASE dataease;
    ```
    执行成功后，可以新建 Excel 数据集 或 定时同步类型数据集试试。

## 3 DataEasee 定时同步报错 body exceed max size, max_body_bytes=10737418240 的解决方法

!!! Abstract ""
1.报错日志  
![报错日志](../img/faq/报错日志.png){ width="900px" }

    2.原因  
    由于 Doris 一次默认最大导入的数据量是 10GB,一旦超过就会报错 body exceed max size, max_body_bytes=10737418240。  
    ```
    streaming_load_max_mb​
    类型：int64
    描述：用于限制数据格式为 csv 的一次 Stream load 导入中，允许的最大数据量。单位 MB。
    默认值： 10240
    可动态修改：是
    ```  
    
    3.解决方法  
    BE 启动后，通过下面命令动态设置配置项 streaming_load_max_mb:  
    ```shell
    curl -X POST http://{be_ip}:{be_http_port}/api/update_config?streaming_load_max_mb=1024
    ```  
    返回值如下，则说明设置成功。  
    ```js
    {
        "status": "OK",
        "msg": ""
    }
    ```  
    BE 重启后该配置将失效。如果想持久化修改结果，使用如下命令：  
    ```shell
    curl -X POST http://{be_ip}:{be_http_port}/api/update_config?streaming_load_max_mb=1024\&persist=true
    ```