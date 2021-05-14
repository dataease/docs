## 重启安装服务器后，如何启动 MeterSphere 相关组件？

MeterSphere 在安装过程中没有配置 docker 及其相关容器的自启动。当用户重新启动部署服务器之后，需要手动启动 docker 服务及 MeterSphere 相关容器。

```bash
service docker start
msctl start
msctl status
```

## 如何修改应用的默认端口？

修改 /opt/metersphere/.env 文件中的对应配置后，执行 `msctl reload` 命令重新加载应用。

> 配置文件说明请参考 [修改安装配置(可选)](/installation/online_installation/#_4)

