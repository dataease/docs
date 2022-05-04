## 1 基础设置

!!! Abstract ""
    如下图所示，可设置请求超时时间，消息保留时间，以及是否显示首页。  
    **提示：默认请求超时时间为 10 秒，如遇网络不通畅，报超时错误，可通过此项参数调整，当前最大值支持 100 秒。**

![基础设置](../../img/system_management/基础设置.png){ width="900" }

## 2 邮件设置

!!! Abstract ""
    用户可通过配置邮件的基本信息，来接收仪表板分享、数据集同步或数据源失效的信息。

![邮件设置](../../img/system_management/邮件设置.png){ width="900" }

## 3 引擎设置

### 3.1 精简模式

!!! Abstract ""
    精简模式下需配置数据引擎用以存储 Excel 及 API 数据集数据，目前该引擎只支持 MySQL 类型；  
    DataEase v1.10.0 之前版本中引擎的参数都为空，用户不知道需要配置的情况下上传 Excel 会报错，提示用户“未配置数据引擎”；  
    DataEase v1.10.0 系统会检查是否设置了引擎参数，若无设置，则读取 dataease.properties 配置文件中 MySQL 连接信息，自动填入其中；  
    参考以下示例图，也可使用外部 MySQL 。

![MySQL设置](../../img/system_management/MySQL设置.png){ width="900" }

### 3.2 集群模式

!!! Abstract ""
    集群模式下需要手动配置 Doris 组件的参数，用以存储 Excel 数据集，API 数据集数据和定时同步模式下数据集的数据。

![Doris设置](../../img/system_management/Doris设置.png){ width="900" }

## 4 Kettle 设置

!!! Abstract ""
    集群模式下需配置 Kettle 组件用以做数据抽取，可手动配置 Kettle 的基本信息，并可添加多个 Kettle 组件，多个 Kettle 存在时，任务将随机分配。

![Kettle设置](../../img/system_management/Kettle设置.png){ width="900" }  
![Kettle设置_编辑](../../img/system_management/Kettle设置_编辑.png){ width="900" }

    