## 1 前提条件

!!! Abstract ""
    链接 Presto 数据库之前，请收集以下信息：

    - 数据库服务器的 IP 地址和端口号
    - 数据库名称
    - Schema
    - 数据库用户名和密码

## 2 配置数据源链接步骤

!!! Abstract ""
    步骤一：登入 DataEase 系统。

!!! Abstract ""
    步骤二：按照以下步骤，选择 Presto 图标。

![Presto](../../img/datasource_configuration/Presto1.png){ width="900" }

!!! Abstract ""
    步骤三：填入收集的 IP 、端口、数据库、Schema 等相关的信息。

![Presto](../../img/datasource_configuration/Presto2.png){ width="900" }

!!! Abstract ""
    详细说明信息如下：

| 基础属性   | 说明                 |
|:-------|:-------------------|
| 显示名称   | 数据源界面左侧列表中的显示名称    |   
| 描述     | 填写与此数据源相关的一些附属说明信息 |
| 主机名    | 填写数据库所在服务器的 IP 地址  |
| 端口     | 填写正确的端口，默认为 8080   |
| 数据库    | 连接的数据库的名称          |
| Schema | 选择对象的集合            |
| 用户名    | 数据库对应的用户名          |
| 密码     | 数据库对应的密码           |
| 查询超时   | 请根据实际情况填写          |


!!! Abstract ""
    步骤四：数据源检验，校验成功后如下图所示，点击保存即可。

![Presto](../../img/datasource_configuration/Presto3.png){ width="900" }