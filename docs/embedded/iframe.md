!!! Abstract ""
    Iframe 嵌入支持嵌入单个数据大屏、仪表板，图表资源。也支持数据集、数据源，仪表板，数据大屏等模块嵌入，提供一个模块的完整能力，可根据实际需要进行选择。

    使用 postMessage 方式实现 DataEase 和嵌入系统的页面信息交互。

    （postMessage 是挂载在 window下的一个方法，用于不同域名下的两个页面的信息交互，父子页面通过  postMessage（）发送消息，再通过监听 message 事件接收信息。）Iframe 嵌入必须在监听触发后，再初始化图表。

    **注意：嵌入需要在 DataEase 的配置文件 /opt/dataease2.0/conf/application.yml 里增加 origin-list 配置，并重启服务。详细见常见问题 4.2。**

##  1 仪表板嵌入
!!! Abstract ""
    仪表板嵌入支持嵌入单个仪表板，并可浏览嵌入的仪表板。仪表板嵌入还支持外部参数设置。

    ```
    #
       一、公共链接嵌入（数据不敏感或内网环境可用，使用 ticket 的方式会较为安全）。
       1、获取仪表板公共链接
       2、定义一个 iframe 容器，并且设置好宽高。
       3、设置 iframe 容器的 src 为仪表板公共链接。
    
       二、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取仪表板 ID。
       5、构建初始化参数。
       6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    
       双向传参应用场景：
       一、第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。
         1、初始化看板时，由第三方系统向 DataEase 传参过滤数据。
          a) 公共链接拼接 attachParams 过滤数据。
          b) 公共链接使用 ticket 设置参数过滤数据。
          b) DataEase 推荐的 iframe 嵌入方式前端传参过滤数据。
          b) DataEase 推荐的 iframe 嵌入方式后端传参过滤数据。
         2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
       二、DataEase 向第三方系统传参
         1、查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 仪表板 ID
    let dvId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法：dashboard 仪表板、dataV 数据大屏
        busiFlag: "dashboard",
        dvId: dvId,
        # 固定写法
        type: "Dashboard",
        #  JWT token 认证。
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
### 1.1 仪表板双向参数传递
!!! Abstract ""
    使用仪表板、数据大屏、图表嵌入，可以通过嵌入式外部参数进行系统的数据交互，具体使用如下，代码采用 [Vue3 代码](https://github.com/dataease/embedded-demo/tree/isv-embedded-demo) ，仪表板、数据大屏、图表双向参数传递等场景参考示例代码中相应部分。

    使用外部参数，需要在仪表板或者数据大屏设置好外部参数，具体见外部参数设置。

双向传参应用场景： </br>
!!! Abstract ""
    第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。

    1.初始化看板时，由第三方系统向 DataEase 传参过滤数据。
    a) 公共链接拼接 attachParams 过滤数据。

    ```
    #
    一、公共链接嵌入（数据不敏感或内网环境可用，使用 ticket 的方式会较为安全）。
    1、获取仪表板公共链接
    2、定义一个 iframe 容器，并且设置好宽高。
    3、设置 iframe 容器的 src 为仪表板公共链接。
    #

    <script setup lang="ts" name="dashboard">
    import {Base64} from "js-base64";
    import {nextTick} from "vue";
    
    nextTick(()=>{
    
      const params = {
        参数名1: ["参数值1" , "参数值2"],
        参数名2: "参数值2"
      }
    # 公共链接拼接 attachParams
      let url = "https://embedded-bi-inner.dataease.cn/#/de-link/uY6HGgCD?attachParams="+Base64.encodeURL(JSON.stringify(params));
    
      document.getElementById("iframe-dashboard-view").src = url;
    })
    
    </script>
    ```
    b) 公共链接使用 ticket 设置参数过滤数据。
    ```
    # 
    一、公共链接嵌入（数据不敏感或内网环境可用，使用 ticket 的方式会较为安全）。
    1、获取仪表板公共链接
    2、定义一个 iframe 容器，并且设置好宽高。
    3、设置 iframe 容器的 src 为仪表板公共链接。
    # 
    <script setup lang="ts" name="dashboard">
    import {Base64} from "js-base64";
    import {nextTick} from "vue";
    
    nextTick(()=>{
    
      const params = {
        参数名1: ["参数值1" , "参数值2"],
        参数名2: "参数值2"
      }
    
    # 公共链接使用 ticket 设置参数
     let url = "https://embedded-bi-inner.dataease.cn/#/de-link/uY6HGgCD?ticket=rGD7gNBN"
      document.getElementById("iframe-dashboard-view").src = url;
    })
    
    </script>
    ```
    c) DataEase 推荐的 iframe 嵌入方式前端传参过滤数据。
    ```
    #
    二、DataEase 嵌入式推荐的 iframe 嵌入
    1、iframe 嵌入需要先在 application.yml 里添加 origin-list
    2、定义一个 iframe 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、获取仪表板 ID。
    5、构建初始化参数。
    6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #
    
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 仪表板 ID
    let dvId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    # 外部参数
    const initParams = {
      attachParams: {
        "参数名":"参数值"
      }
    }
    
    # 嵌入式参数
    const params = {
      busiFlag: "dashboard",
      dvId: dvId,
      type: "Dashboard",
      embeddedToken: "",
      "de-embedded": true,
      outerParams: JSON.stringify(initParams)
    }

    let iframe = null;
    
    onUnmounted(()=>{
      window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
      iframe = document.getElementById("iframe-dashboard-view");
    
      getToken().then(result => {
        params.embeddedToken = result;
        iframe.src = url;
    
        window.addEventListener("message" , onMessage , false);
      })
    })
    
    const onMessage = function (event: any){
      if (event.data?.msgOrigin === "de-fit2cloud") {
        const contentWindow = iframe.contentWindow;
        contentWindow.postMessage(params , "*")
      }
    }
    ```
    d) DataEase 推荐的 iframe 嵌入方式后端传参过滤数据。
    ```
    @RestController
    public class TokenApi {
    #
    ## 获取 DataEase 嵌入式 Token
    ## DataEase 嵌入式 Token 使用的是 JWT 认证，由 appId、appSecret 以及 DataEase 用户名生成。
    ## Java 程序可直接引用 java-jwt (https://mvnrepository.com/artifact/com.auth0/java-jwt) 依赖，其它后端语言可自行百度加密代码。
    ## 注意，嵌入式 Token 的过期时间默认为 480 分钟，可通过修改 application.yml 进行调整
    ## 配置参数名称为 dataease.embedded-exp
    #

        @GetMapping("/token/{account}")
        public String generate(@PathVariable("account") String account) throws JsonProcessingException {
            SettingVO vo = SettingUtils.read();
            # vo.getAppSecret() 实际为创建的嵌入式应用的 APP Secret 。
            Algorithm algorithm = Algorithm.HMAC256(vo.getAppSecret());
            JWTCreator.Builder builder = JWT.create();
            List<String> ipList = new ArrayList<>();
            ipList.add("192.168.1.10");
            ipList.add("192.168.1.20");
            ObjectMapper objectMapper = new ObjectMapper();
            String json = objectMapper.writeValueAsString(ipList);
            # vo.getAppId(): 实际为创建的嵌入式应用的 APP ID。account 用户账号。
            # arg 参数，参数值多个使用 json 格式
            builder.withClaim("account", account).withClaim("appId", vo.getAppId()).withClaim("arg1", "参数值1").withClaim("arg2", json);
            # 设置令牌生成时间，
            builder.withIssuedAt(new Date());
            # 返回 token
            return builder.sign(algorithm);
        }
    }
    ```
    2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
    ```
    #
    二、DataEase 嵌入式推荐的 iframe 嵌入
    1、iframe 嵌入需要先在 application.yml 里添加 origin-list
    2、定义一个 iframe 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、获取仪表板 ID。
    5、构建初始化参数。
    6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #
    
    <template>
      <div class="card-iframe content-box">
        <div style="float: right; cursor: pointer; margin-top: 0.5vh">
          <el-dropdown trigger="click" @command="changeUser">
                <span class="el-dropdown-link">
                  点我切换参数
                </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="参数1">参数1</el-dropdown-item>
                <el-dropdown-item command="参数2">参数2</el-dropdown-item>
                <el-dropdown-item command="参数3">参数3</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 仪表板 ID
    let dvId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        busiFlag: "dashboard",
        dvId: dvId,
        type: "Dashboard",
        embeddedToken: "",
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
         window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    const changeUser = function (command: String) {
        postMsg(command);
    }
    
    const postMsg = function (user: String) {
        const param = {
            type: "attachParams",
            targetSourceId: dvId,
            params: {
            参数名: 参数值
            }
        }
        const contentWindow = iframe.contentWindow;
        contentWindow.postMessage( JSON.parse(JSON.stringify(param)) , "*" );
    }
    
    </script>
    ```
!!! Abstract ""
    DataEase 向第三方系统传参 </br>

    查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容，具体内容可通过解析传递的 message，获取相应的信息。

    以下为 DataEase 传递内部消息的解析后得到的参数例子，这些参数均可以在 DataEase 获取数据大屏的接口详情里得到。

    ```
    1.完整 data json 如下。
    {
        "msgOrigin": "de-fit2cloud",
        "type": "dataease-embedded-interactive",
        "eventName": "de_inner_params",
        "args": {
                "sourceDvId": "1029081671057674240",
                "sourceViewId": "7237349581229395968",
                "message":               
    "eyJvcHRpb24iOiJwb2ludENsaWNrIiwibmFtZSI6IjE3MTQwOTczMjY2OTQiLCJ2aWV3SWQiOiI3MjM3MzQ5NTgxMjI5Mzk1OTY4IiwiZGltZW5zaW9uTGlzdCI6W3siaWQiOiIxNzE0MDk3MzI2NjkzIiwidmFsdWUiOjB9LHsiaWQiOiIxNzE0MDk3MzI2Njk0IiwidmFsdWUiOiJCb2IifV0sInF1b3RhTGlzdCI6W119"
                }
    }
    
    2.message base64解码 json 如下。
    {
        "option": "pointClick",
        "name": "1714097326694",
        "viewId": "7237349581229395968",
        "dimensionList": [
            {
                "id": "1714097326693",
                "value": 0
            },
            {
                "id": "1714097326694",
                "value": "Bob"}
        ],
        "quotaList": [ ]}
    ```

    ```
    #
    二、DataEase 嵌入式推荐的 iframe 嵌入
    1、iframe 嵌入需要先在 application.yml 里添加 origin-list
    2、定义一个 iframe 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、获取仪表板 ID。
    5、构建初始化参数。
    6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #
    
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    import {Base64} from "js-base64";
    
    # 仪表板 ID
    let dvId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const initParams = {
      callBackFlag: "yes"
    }
    
    const params = {
      busiFlag: "dashboard",
      dvId: dvId,
      type: "Dashboard",
      embeddedToken: "",
      "de-embedded": true,
      outerParams: JSON.stringify(initParams)
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
      window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
      iframe = document.getElementById("iframe-dashboard-view");
    
      getToken().then(result => {
        params.embeddedToken = result;
        iframe.src = url;
    
        window.addEventListener("message" , onMessage , false);
      })
    })
    
    const onMessage = function (event: any){
      if (event.data?.eventName === "de_inner_params") {
        const dvId = event.data.args.sourceDvId;
        const viewId = event.data.args.sourceViewId;
        const message = event.data.args.message;
        const messageDecode = Base64.decode(message);
        alert("仪表板ID : "+ dvId + " ; 图表ID : " + viewId + " ; 点击详情 : " + messageDecode);
      }
      if (event.data?.msgOrigin === "de-fit2cloud") {
        const contentWindow = iframe.contentWindow;
        contentWindow.postMessage(params , "*")
      }
    }
    
    </script>
    ```
##  2 仪表板设计器嵌入
!!! Abstract ""
    仪表板编辑嵌入支持嵌入整个仪表板设计器界面，用户不仅可以浏览嵌入的仪表板，还可以对其进行编辑：

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取仪表板 ID。
       5、构建初始化参数。
       6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 仪表板 ID
    let dvId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法：dashboard 仪表板、dataV 数据大屏
        busiFlag: "dashboard",
        resourceId: dvId,
        # 固定写法
        type: "DashboardEditor",
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
            window.addEventListener("message" , onMessage , false);
     })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    ```

##  3 数据大屏嵌入
!!! Abstract ""
    数据大屏嵌入支持嵌入整个数据大屏，用户可以浏览嵌入的数据大屏，数据大屏嵌入还支持外部参数设置。

    ```
    #
       一、公共链接嵌入（数据不敏感或内网环境可用，使用 ticket 的方式会较为安全）。
       1、获取数据大屏公共链接
       2、定义一个 iframe 容器，并且设置好宽高。
       3、设置 iframe 容器的 src 为数据大屏公共链接。
    
       二、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取数据大屏 ID。
       5、构建初始化参数。
       6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    
       双向传参应用场景：
       一、第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。
         1、初始化看板时，由第三方系统向 DataEase 传参过滤数据。
          a) 公共链接拼接 attachParams 过滤数据。
          b) 公共链接使用 ticket 设置参数过滤数据。
          b) DataEase 推荐的 iframe 嵌入方式前端传参过滤数据。
          b) DataEase 推荐的 iframe 嵌入方式后端传参过滤数据。
         2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
       二、DataEase 向第三方系统传参
         1、查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 数据大屏 ID
    let dvId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法：dashboard 仪表板、dataV 数据大屏
        busiFlag: "dataV",
        dvId: dvId,
        # 固定写法
        type: "Dashboard",
        #  JWT token 认证。
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
### 3.1 数据大屏双向参数传递
!!! Abstract ""
    参考 Ifram 仪表板双向参数传递以及 Iframe 数据大屏嵌入，将相应 busiFlag 修改对应。

##  4 数据大屏设计器嵌入
!!! Abstract ""
    数据大屏设计器嵌入支持嵌入整个数据大屏设计器界面，用户不仅可以浏览嵌入的数据大屏，还可以对其进行编辑：

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取仪表板 ID。
       5、构建初始化参数。
       6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    let dvId = "967564651451781120";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "https://embedded-bi-inner.dataease.cn/#/chart-view";
    
    const params = {
        # 固定写法：dashboard 仪表板、dataV 数据大屏
        busiFlag: "dataV",
        dvId: dvId,
        # 固定写法
        type: "VisualizationEditor",
        #  JWT token 认证。
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
    if (event.data?.msgOrigin === "de-fit2cloud") {
    const contentWindow = iframe.contentWindow;
    contentWindow.postMessage(params , "*")
    }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```

## 5 图表嵌入
!!! Abstract ""
    图表嵌入支持嵌入单个图表，并可浏览嵌入的图表。图表嵌入还支持外部参数设置。

    ```
    #
       一、、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取仪表板/数据大屏 ID 以及图表 ID。
       5、构建初始化参数。
       6、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    
       双向传参应用场景：
       一、第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。
         1、初始化看板时，由第三方系统向 DataEase 传参过滤数据。
          a) DataEase 推荐的 iframe 嵌入方式前端传参过滤数据。
          b) DataEase 推荐的 iframe 嵌入方式后端传参过滤数据。
         2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
       二、DataEase 向第三方系统传参
         1、查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 仪表板 ID / 数据大屏 ID
    let dvId = "";
    # 图表 ID
    let chartId = "";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    #
    ## 仪表板图表 busiFlag：dashboard
    ## 数据大屏图表 busiFlag：dataV

      const params = {
        # 固定写法：dashboard 仪表板、dataV 数据大屏
        busiFlag: "dashboard",
        dvId: dvId,
        chartId: chartId,
        #  JWT token 认证
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
      }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })

    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
### 5.1 图表双向参数传递
!!! Abstract ""
    参考 Iframe 仪表板双向参数传递以及 iframe 图表嵌入。

## 6 我的填报嵌入
!!! Abstract ""
    支持我的填报嵌入，填报模块信息。

    ```
    #
       DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-datafillinghandler-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="datafillinghandler">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        type: "DataFillingHandler",
        embeddedToken: "",
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-datafillinghandler-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
             window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud" && event.data?.type !== 'dataease-embedded-interactive') {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```

## 7 模块嵌入

### 7.1 仪表板模块
!!! Abstract ""
    嵌入整个仪表板模块后，可以实现对仪表板模块的整体使用，包括新建、编辑和删除仪表板：

    ```
    #
       DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
          <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-datafillinghandler-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="datafillinghandler">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        type: "DataFillingHandler",
        embeddedToken: "",
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-datafillinghandler-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud" && event.data?.type !== 'dataease-embedded-interactive') {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
### 7.2 数据大屏模块
!!! Abstract ""
    嵌入整个数据大屏模块后，可以实现对数据大屏模块的整体使用，包括新建、编辑和删除数据大屏。

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
        <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/char-view
    let url = "";
    
    const params = {
        # 固定写法 ScreenPanel 数据大屏模块。
        type: "ScreenPanel",
        #  JWT token 认证
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
### 7.3 数据集模块
!!! Abstract ""
    嵌入整个数据集模块，嵌入后可实现数据集模块的整体使用，包括新建数据集，编辑数据集，删除数集。

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
        <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法 Dataset 数据集模块。
        type: "Dataset",
        #  JWT token 认证
        embeddedToken: "",
        #固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
    
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
    
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```

### 7.4 数据源模块
!!! Abstract ""
    嵌入整个数据源，嵌入后可实现数据源模块的整体使用，包括新建数据源，编辑数据源，删除数源。

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
        <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-dashboard-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法 Datasource 数据集模块。
        type: "Datasource",
        # JWT token 认证
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```

### 7.5 数据填报模块
!!! Abstract ""
    嵌入整个数据填报，嵌入后可实现数据填报模块的整体使用。

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
        <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-datafilling-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="dataFilling">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法 DataFilling 数据填报模块。
        type: "DataFilling",
        //JWT token 认证
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-datafilling-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```


### 7.6 Copilot 模块
!!! Abstract ""
    嵌入 Copilot 模块。

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
        <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-copilot-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="copilot">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法 Copilot 模块。
        type: "Copilot",
        # JWT token 认证
        embeddedToken: "",
        # 固定写法
        "de-embedded": true
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-dashboard-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```

### 7.7 模版管理模块
!!! Abstract ""

    ```
    #
       一、DataEase 嵌入式推荐的 iframe 嵌入
       1、iframe 嵌入需要先在 application.yml 里添加 origin-list
       2、定义一个 iframe 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、构建初始化参数。
       5、监听来自 DataEase 事件的 msgOrigin ，如果 msgOrigin 为 de-fit2cloud ，则通过 postMessage 发送初始化参数，渲染看板。
    #

    <template>
      <div class="card-iframe content-box">
        <iframe style="height: 100%; width: 100%; border: 0" src=""  id="iframe-templatemanage-view" ></iframe>
      </div>
    </template>
    <script setup lang="ts" name="templatemanage">
    import {getToken} from "@/api/common";
    import {nextTick , onUnmounted} from "vue";
    
    # 固定写法，如 https://embedded-bi-inner.dataease.cn/#/chart-view
    let url = "";
    
    const params = {
        # 固定写法 模版管理 模块。
        type: "TemplateManage",
        # JWT token 认证
        embeddedToken: "",
        # 固定写法
        "de-embedded": true,
        busiFlag: "dataV"
    }
    
    let iframe = null;
    
    onUnmounted(()=>{
        window.removeEventListener("message",onMessage,false);
    })
    
    nextTick(()=>{
        iframe = document.getElementById("iframe-templatemanage-view");
        
        getToken().then(result => {
            params.embeddedToken = result;
            iframe.src = url;
        
            window.addEventListener("message" , onMessage , false);
        })
    })
    
    const onMessage = function (event: any){
        if (event.data?.msgOrigin === "de-fit2cloud") {
            const contentWindow = iframe.contentWindow;
            contentWindow.postMessage(params , "*")
        }
    }
    
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
