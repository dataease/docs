## 1 安装模式介绍

!!! Abstract ""
    v1.9.0 及以后版本安装模式分为本地模式（local）、精简模式（simple）、集群模式（cluster），v1.9.0 以前版本不涉及该内容，等同于安装的本地模式。  
    安装模式对应 DataEase 中的配置参数为 DE_ENGINE_MODE，**在不做修改的情况下，系统默认安装精简模式**。  
    

### 1.1 本地模式

!!! Abstract ""
    **DE_ENGINE_MODE=local**  
    使用本地模式安装，DataEase 会自带 Doris 与 Kettle 组件，无需再做额外配置，但各组件均为单点，不具备高可用特性。  
    在此模式下，Excel 数据集、API 数据集以及定时同步的数据默认保存在自带的 Doris 组件中。

### 1.2 精简模式

!!! Abstract ""
    **DE_ENGINE_MODE=simple**  
    使用精简模式安装，系统不会额外安装 Doris 与 Kettle 组件，提供用户轻量级的应用系统，尤其是对接数据量较小的情况。  
    在此模式下，Excel 数据集或 API 数据集的相关数据存储在数据引擎中（默认配置自带的 MySQL 组件，用户可在系统管理界面配置数据引擎，数据引擎目前仅支持 MySQL 类型）。  
    **注意：由于精简模式未配置 Kettle 与 Doris，故精简模式不提供定时同步模式。**
    

### 1.3 集群模式

!!! Abstract ""
    **DE_ENGINE_MODE=cluster**  
    使用集群模式安装，系统不会额外安装 Doris 与 Kettle 组件，但会在系统管理模块提供 Doris 与 Kettle 的链接配置界面（请参考【系统管理】的【系统参数】说明），用户可独立安装 Doris 集群及 Kettle 并配置在 DataEase 中。集群模式下 Excel 数据集，API 数据集以及定时同步的数据通过 Kettle 抽取到 Doris 集群中。  
    Doris 安装部署可参考：http://doris.incubator.apache.org/zh-CN/  
    Kettle 安装部署可参考：http://www.kettle.org.cn/   

## 2 切换安装模式

!!! Abstract ""
    **安装包部署方式下，若需切换安装模式，请执行以下操作。**  
    步骤一：修改 /opt/dataease/.env 文件（注意 .env 是隐藏文件）中 DE_ENGINE_MODE 参数，比如将 local 改成 simple。

![env](../img/dev_manual/env.png){ width="900px" }

!!! Abstract ""
    步骤二：若是离线安装方式，在 DataEase 离线安装包解压目录（以 v1.12.0 版本为示例，离线包上传到 /tmp 目录下解压，则在 /tmp/dataease-v1.12.0-offline 下），重新执行安装脚本即可。
    ```shell
    bash install.sh
    ```
    若是在线安装方式，在执行一键安装命令的在线安装包解压目录（以 v1.12.0 版本为示例，在 /home 目录下执行命令，则在 /home/dataease-v1.12.0-online 下），重新执行 bash install.sh，也可重新执行在线安装脚本。
    ```
    curl -sSL https://dataease.oss-cn-hangzhou.aliyuncs.com/quick_start.sh | sh
    ```
    **注意：由于精简模式的 Excel 与 API 数据集是保存在配置的数据引擎中的，切换为其它模式会导致这两部分的数据丢失，反之亦然（Excel 与 API 数据集保存位置变更），直连数据库的相关数据集不受影响。**  