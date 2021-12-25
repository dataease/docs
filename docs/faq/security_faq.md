## DataEase在安全性方面有没有相关说明，比如不会把数据上传到你们服务器上？

DataEase 源码在 Github 上是开源的，我们没有留任何后门代码。DataEase 可以在完全离线的环境下使用，定时同步模式的数据集会同步数据到 DataEase 本地服务器，并不会向外网传送任何数据。

## 关于"Log4j2远程代码执行漏洞"的修复

DataEase 使用到的 Apache Doris 组件受此漏洞影响，大家可以升级到 v1.5.2 版本，也可以手动修改 Apache Doris 对应的 docker-compose 文件来处理，具体操作如下：

v1.5.0 和 v1.5.1 版本，修改 /opt/dataease/docker-compose-doris.yml 文件；v1.4.1 及以前版本，修改 /opt/dataease/docker-compose-kettle-doris.yml 文件，加入环境变量 FORMAT_MESSAGES_PATTERN_DISABLE_LOOKUPS。(注意 doris-fe 和 doris-be 两处修改)
```yml
  doris-fe:
    image: registry.cn-qingdao.aliyuncs.com/dataease/doris:0.15
    container_name: doris-fe
    environment:
      - DORIS_ROLE=fe-leader
      - FORMAT_MESSAGES_PATTERN_DISABLE_LOOKUPS=true

...

  doris-be:
    image: registry.cn-qingdao.aliyuncs.com/dataease/doris:0.15
    container_name: doris-be
    environment:
      - DORIS_ROLE=be
      - FORMAT_MESSAGES_PATTERN_DISABLE_LOOKUPS=true
```
重启服务即可。