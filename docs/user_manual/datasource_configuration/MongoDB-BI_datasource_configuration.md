## 1 前提条件

!!! Abstract ""
    链接 MongoDB-BI 之前，请提前安装部署 MongoDB BI Connector，可参考此篇[知识库](https://kb.fit2cloud.com/?p=143)，并收集以下信息：

    - 数据库服务器的 IP 地址和端口号
    - 数据库名称
    - 数据库用户名和密码

## 2 配置数据源链接步骤

!!! Abstract ""
    步骤一：登入 DataEase 系统。

!!! Abstract ""
    步骤二：按照以下步骤，选择 MongoDB-BI 图标。

![MongoDB](../../img/datasource_configuration/选择Mongodb-BI.png){ width="900" }

!!! Abstract ""
    步骤三：填入收集的 IP 、端口、数据库等相关的信息。

![MongoDB](../../img/datasource_configuration/Mongodb链接信息.png){ width="900" }

!!! Abstract ""
    详细说明信息如下：

| 基础属性             | 说明                 |
|:-----------------|:-------------------|
| 显示名称             | 数据源界面左侧列表中的显示名称    |   
| 描述               | 填写与此数据源相关的一些附属说明信息 |
| 驱动               | /                  |
| 主机名/IP 地址        | 填写数据库所在服务器的 IP 地址  |
| 端口               | 填写正确的端口            |
| 数据库名称            | 连接的数据库的名称          |
| 用户名              | 数据库对应的用户名          |
| 密码               | 数据库对应的密码           |
| 查询超时           | 请根据实际情况填写          |
| 额外的 JDBC 链接字符集   | 填写连接数据库的 JDBC 字符集  |



!!! Abstract ""
    步骤四：数据源检验，校验成功后如下图所示，点击保存即可。

![MongoDB](../../img/datasource_configuration/Mongodb校验成功.png){ width="900" }