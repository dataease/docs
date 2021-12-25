## 忘记了登录密码如何处理？
当普通用户忘记密码时可使用管理员账号在页面上的用户管理页面为其重置密码，当系统管理员忘记密码且没有其他系统管理员账号时，需要通过数据库操作重置密码。

DataEase 的用户信息存放在数据库中的 `sys_user` 表中，其中 password 字段为用户密码的 `md5` 值。
```sql
update sys_user set password='40b8893ea9ebc2d631c4bb42bb1e8996' where username='admin';
```

连接到数据库后，执行上面的 SQL 语句可以将用户 `admin` 的密码重置为 `dataease`。
