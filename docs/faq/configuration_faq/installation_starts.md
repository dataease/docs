## 1 一键安装时，提示语法错误

!!! Abstract ""
    一键安装脚本会与 Github 进行连接，从 Github 上获取 DataEase 最新的版本信息以及最新的安装包。由于国内网络与 github 连接存在不稳定，所以有可能会导致无法获取安装所需的相关信息。 遇到这种情况的话，可以多尝试执行几次安装脚本，或者也可以到 https://github.com/dataease/dataease/releases 上下载 DataEase 的离线安装包安装。

![安装报错](../../img/faq/install-error.png){ width="900px" }

## 2 安装时提示 "Pool overlaps with other one on this address space"

!!! Abstract ""
    可以参考[如何修改 DataEase 运行的 docker 网段？](../configuration/#7-docker)
![网段冲突](../../img/faq/address-space.png){ width="900px" }


## 3 无法通过一键安装脚本在线安装 docker 和 docker-compose

!!! Abstract ""
    **注意：** 在线安装脚本使用的下载源为境外源，可能会存在网络不稳定，或者网速慢的情况。  
    可以在百度网盘上下载 docker 离线安装包进行安装，链接: https://pan.baidu.com/s/1WUbObtcPgPqpaNK6TGCOrA 提取码: gbut  
    解压后执行安装包里的安装脚本即可： bash install-docker.sh

## 4 服务无法完全启动，查看 dataease 日志，发现 docker 访问出现 Permission denied。

!!! Abstract ""
    **这种情况一般是由于 selinux 导致的，可以临时关闭 selinux 试试：**
    ```shell
    setenforce 0
    ```
    然后重启 DataEase 服务：
    ```shell
    service dataease restart
    ```

## 5 DataEase 启动过程中，提示 doris-fe unhealthy

!!! Abstract ""
    **DataEase 启动过程中，提示 doris-fe unhealthy。执行 dectl status 无法查看到 doris-fe 容器，解决方法如下，执行：**
    ```shell
    dectl reload
    ```
    重载容器。受限于服务器性能的原因，doris-be 启动比较慢，doris-fe 依赖 doris-be ，在检测时间内未成功启动完成，doris-fe 便不会再启动。

## 6 Doris-fe 启动失败，日志提示 UNKNOWN 

!!! Abstract ""
    **查询 Doris-fe 日志报事务错误 20 问题，状态为 UNKNOWN。**
    ```shell
    Problem closing transaction 20. The current state is:UNKNOWN.
    ```
    此为磁盘空间不足导致，清理磁盘空间后再重启 Doris-fe 即可，具体可参考知识库。

    - [磁盘空间不足导致 Doris-fe 显示 unhealthy 状态的解决方案](https://kb.fit2cloud.com/?p=93)  
    - [排查DataEase服务器磁盘空间占用情况并清理](https://kb.fit2cloud.com/?p=159)  
    - [清理 DataEase 服务器磁盘空间](https://kb.fit2cloud.com/?p=52)  