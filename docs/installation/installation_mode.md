## 1 安装模式介绍

!!! Abstract ""
    v1.9.0 及以后版本安装模式模式分为本地模式（local）、精简模式（simple）、集群模式（cluster），v1.9.0 以前版本不涉及该内容，等同于安装的本地模式。  
    安装模式对应 DataEase 中的配置参数为 DE_ENGINE_MODE，在不做修改的情况下，系统默认安装精简模式。  
    

### 1.1 本地模式

!!! Abstract ""
    **DE_ENGINE_MODE=local**  
    使用本地模式安装，DataEase 会自带 Doris 与 Kettle 组件，无需再做额外配置，但各组件均为单点，不具备高可用特性。  
    在此模式下，Excel 数据集，API 数据集以及定时同步的数据默认保存在自带的 Doris 组件中。

### 1.2 精简模式

!!! Abstract ""
    **DE_ENGINE_MODE=simple**  
    使用精简模式安装,系统不会额外安装 Doris 与 Kettle 组件,提供用户轻量级的应用系统,尤其是对接数据量较小的情况。  
    在此模式下，若用户需要使用 Excel 数据集或 API 数据集可在系统管理界面配置数据引擎（目前仅支持 MySQL 类型），相关数据会存储到该数据引擎中。若只需使用数据库直连则无需做此配置。
    

### 1.3 集群模式

!!! Abstract ""
    **DE_ENGINE_MODE=cluster**  
    使用集群模式安装，系统不会额外安装 Doris 与 Kettle 组件，但会在系统管理模块提供 Doris 与 Kettle 的链接配置界面（请参考【系统管理】的【系统参数】说明），用户可独立安装 Doris 集群及 Kettle 并配置在 DataEase 中。集群模式下 Excel 数据集，API 数据集以及定时同步的数据通过 Kettle 抽取到 Doris 集群中。  
    Doris 安装部署可参考：http://doris.incubator.apache.org/zh-CN/  
    Kettle 安装部署可参考：http://www.kettle.org.cn/   

## 2 切换安装模式

!!! Abstract ""
    若需切换安装模式，修改 /opt/dataease/.env 文件中 DE_ENGINE_MODE 参数，在 DataEase 安装包解压目录下，重新执行安装脚本即可。
    ```shell
    bash install.sh
    ```