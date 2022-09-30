## 1 DataEase Service

!!! Abstract ""
    DataEase 在安装的时候默认向系统中添加了相应的 dataease Service，支持的 Service 命令有：

    - start : 启动 DataEase 服务
    - stop : 停止 DataEase 服务，并删除相关的运行容器、docker 网络等资源
    - restart : 停止后启动 DataEase 服务，相当于先执行 stop，再执行 start 命令
    - status : 查看 DataEase 服务当前各容器运行状态

## 2 dectl

!!! Abstract ""
    DataEase 默认内置了命令行运维工具 - dectl，通过执行 dectl help 命令，可以查看相关的帮助文档。

    ```
    Usage:
      ./dectl [COMMAND] [ARGS...]
      ./dectl --help
    
    Commands:
      status       查看 DATAEASE 服务运行状态
      start        启动 DATAEASE 服务
      stop         停止 DATAEASE 服务
      restart      重启 DATAEASE 服务
      reload       重新加载 DATAEASE 服务
      uninstall    卸载 DATAEASE 服务
      upgrade      升级 DATAEASE 服务
      version      查看 DATAEASE 版本信息
      clear-images 清理 DATAEASE 旧版本的相关镜像
      clear-logs   清理 DATAEASE 历史日志以及 Doris 临时日志
    ```