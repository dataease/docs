## 1 忘记了登录密码如何处理？

!!! Abstract ""
    **当普通用户忘记密码时可使用管理员账号在页面上的用户管理页面为其重置密码，当系统管理员忘记密码且没有其他系统管理员账号时，需要通过数据库操作重置密码：**  
    DataEase 的用户信息存放在数据库中的 `sys_user` 表中，其中 password 字段为用户密码的 `md5` 值。
    ```sql
    update sys_user set password='40b8893ea9ebc2d631c4bb42bb1e8996' where username='admin';
    ```
    连接到数据库后，执行上面的 SQL 语句可以将用户 `admin` 的密码重置为 `dataease`。

## 2 遇到系统超时如何处理？

!!! Abstract ""
    **如遇网络不通畅，系统报 ”timeout of xxx exceeded“ 错误，则可在【系统管理】【系统参数】的基础设置增大超时时间，同时支持在数据源的【高级设置】修改查询超时时间。**

![调整超时时间](../img/system_management/调整超时时间.png){ width="900" }

![超时时间](../img/datasource_configuration/超时时间.png){ width="900" }