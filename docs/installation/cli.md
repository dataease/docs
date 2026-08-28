## 1 DataEase Service

!!! Abstract ""
    DataEase 在安装时默认向系统添加了 dataease Service，支持的命令有：

    - `start`：启动 DataEase 服务
    - `stop`：停止 DataEase 服务，并删除相关运行容器、docker 网络等资源
    - `restart`：停止后启动 DataEase 服务（先 stop 再 start）
    - `status`：查看 DataEase 服务当前各容器运行状态

## 2 dectl

!!! Abstract ""
    DataEase 默认内置命令行运维工具 `dectl`，执行 `dectl help` 可查看帮助。常用命令如下：

    ```
    DATAEASE 控制脚本

    Usage:
      ./dectl [COMMAND] [ARGS...]
      ./dectl --help

    Commands:
      status         查看 DATAEASE 服务运行状态
      start          启动 DATAEASE 服务
      stop           停止 DATAEASE 服务
      restart        重启 DATAEASE 服务
      reload         重新加载 DATAEASE 服务
      upgrade        升级 DATAEASE 服务
      clear-images   清理 DATAEASE 旧版本的相关镜像
      clear-logs     清理 DATAEASE 历史日志
      version        查看 DATAEASE 版本
    ```

!!! Abstract ""
    DataEase 的日志目录一般为：`/opt/dataease3.0/logs`（以实际安装目录为准）。
