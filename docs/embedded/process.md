!!! Abstract ""
    DataEase 支持使用 Iframe 以及 DIV 进行嵌入，两种方法的流程如下。

    **注意：嵌入需要在 DataEase 的配置文件 /opt/dataease2.0/conf/application.yml 里增加 origin-list 配置，并重启服务。详细见常见问题 4.2。**
## 1 DIV 嵌入式流程

!!! Abstract ""
    在 DataEase 中创建嵌入式应用后，首先获取其 APP ID 和 APP Secret，同时获取 DataEase 用户账号。使用这些信息生成 token，并利用生成的 token 进行认证。引入 DataEase 提供的嵌入式 js 文件后，使用指定参数创建 DataEaseBi 对象，并渲染 DIV 容器即可实现嵌入式应用的集成与展示。
![2. DataEase 嵌入式流程.jpg](../img/embedded/2. DataEase 嵌入式流程.jpg){ width="900px" }

## 2 Iframe 嵌入式流程
!!! Abstract ""
    在 DataEase 中创建嵌入式应用后，首先获取其 APP ID 和 APP Secret，同时获取 DataEase 用户账号。使用这些信息生成 token，并利用生成的 token 进行认证。使用 postMessage 通信并传入相应参数，即可实现嵌入式应用的集成与展示。
![2. DataEase 嵌入式流程（2）.jpg](../img/embedded/2. DataEase 嵌入式流程（2）.jpg){ width="900px" }