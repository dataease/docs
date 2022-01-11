### 如何备份还原 DataEase？

!!! Abstract ""
    DataEase安装后，相关文件的分布路径如下：

    - /opt/dataease - 默认运行路径，在安装时可设置。主要存放 DataEase 运行时所需的配置文件及运行时产生的数据，包括日志文件等
    - /usr/bin - 默认 docker 及 docker-compose 的运行程序被放置在此目录下
    - /usr/local/bin/dectl - DataEase 的命令行工具
    - /var/lib/docker - 默认 docker 镜像加载在此

!!! Abstract ""
    综上所述，备份 DataEase 主要需要备份运行路径，如 /opt/dataease 目录即可。
    还原步骤如下：

    - **为了镜像版本一致，请在新环境里安装同一个版本的 DataEase，安装时请选择相同的配置参数**
    - 停止两个环境里的 DataEase 服务，执行命令： service dataease stop
    - 把原环境里的运行目录 /opt/dataease 整个目录覆盖掉新环境里的 /opt/dataease 目录
    - 启动新环境里的 DataEase 服务： service dataease start

