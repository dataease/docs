!!! Abstract ""
    DIV 嵌入支持嵌入单个数据大屏、仪表板，图表资源。也支持数据集、数据源，仪表板，数据大屏等模块嵌入，提供一个模块的完整能力，可根据实际需要进行选择。

    DIV 嵌入需引入 DataEase 嵌入式 JS。

    DIV 嵌入的初始化图表不依赖监听触发，DIV 嵌入需要定义好容器的大小 。

    **注意：嵌入需要在 DataEase 的配置文件 /opt/dataease2.0/conf/application.yml 里增加 origin-list 配置，并重启服务。详细见常见问题 4.2。**

## 1 仪表板嵌入
!!! Abstract ""
    仪表板嵌入支持嵌入单个仪表板，并可浏览嵌入的仪表板。仪表板嵌入还支持外部参数设置。

    ```
    #
    1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
    2、定义一个 DIV 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、获取仪表板 ID。
    5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。

    双向传参应用场景：
    一、第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。
      1、初始化看板时，由第三方系统向 DataEase 传参过滤数据。
       a) 前端传参
       b) 后端传参
      2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
    二、DataEase 向第三方系统传参
      1、查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容。
    #
    <template>
        <div class="card content-box">
         <div style="width: 100%; height: 100%" id="div-dashboard-view"></div>
        </div>
    </template>
    <script setup lang="ts" name="dashboard">

    import {getToken} from "@/api/common";
    # 仪表板 ID
    let dvId = "";
    # DataEase 企业版访问地址
    let baseUrl = "";

    getToken().then(result => {
        # Dashboard：仪表板数据大屏嵌入固定写法。
        const dataease = new DataEaseBi("Dashboard", {
    
        baseUrl: baseUrl,
        #  token: JWT token 认证。
        token: result,
        dvId: dvId,
        # 固定写法：dashboard 仪表板、dataV 数据大屏
        busiFlag: "dashboard"
    });

        dataease.initialize({container: "#div-dashboard-view"});

    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```

### 1.1 仪表板双向参数传递

!!! Abstract ""
    使用仪表板、数据大屏、图表嵌入，可以通过嵌入式外部参数进行系统的数据交互，具体使用如下，代码采用 [Vue3 代码](https://github.com/dataease/embedded-demo/tree/isv-embedded-demo) ，仪表板、数据大屏、图表双向参数传递等场景参考示例代码中相应部分。

    使用外部参数，需要在仪表板或者数据大屏设置好外部参数，具体见外部参数设置。
双向传参应用场景：</br>

!!! Abstract ""
    第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。

    1.初始化看板时，由第三方系统向 DataEase 传参过滤数据。

    a) 前端传参
    在仪表板嵌入的基础上，加入外部参数即可。
    ```

    #
    1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
    2、定义一个 DIV 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、获取仪表板 ID。
    5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #
    <script setup lang="ts" name="dashboard">
    
    import {getToken} from "@/api/common";
    
    # 外部参数
    const initParams = {
      attachParams: {
        参数名1: ["参数值1","参数值2"],
        参数名2: "参数值"
      }
    }
    
    # 仪表板 ID
    let dvId = "";
    //DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
    
      const dataease = new DataEaseBi("Dashboard", {
        baseUrl: baseUrl,
        token: result,
        dvId: dvId,
        # 默认写法
        busiFlag: "dashboard",
        # 外部参数
        outerParams: JSON.stringify(initParams)
      });
    
      dataease.initialize({container: "#div-dashboard-view"});
    
    })
    </script>
    ```

    b) 后端传参
    DataEase 支持后端 token 加密传参。
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
            #设置令牌生成时间，
            builder.withIssuedAt(new Date());
            # 返回 token
            return builder.sign(algorithm);
        }
    }
    ```
    2. 查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
    ```
    <template>
      <div class="card content-box">
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
        <div style="width: 100%; height: 100%" id="div-dashboard-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    
    import {getToken} from "@/api/common";
    
    const changeUser = function (command: String) {
    postMsg(command);
    }
    
    ## 仪表板 ID
    let dvId = "";
    ## DataEase 访问地址
    let baseUrl = "";
    
    const postMsg = function (user: String) {
        const param = {
            type: "attachParams",
            targetSourceId: dvId,
            params: {
              参数名: 参数值
            }
        }
        window.postMessage( JSON.parse(JSON.stringify(param)) , "*" );
    }
    
    getToken().then(result => {
        const dataease = new DataEaseBi("Dashboard", {
            baseUrl: baseUrl,
            token: result,
            dvId: dvId,
            busiFlag: "dashboard"
        });
        dataease.initialize({container: "#div-dashboard-view"});
    })
    </script>
    ```
!!! Abstract ""
    DataEase 向第三方系统传参

    1.查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容，具体内容可通过解析传递的 message，获取相应的信息。

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
    1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
    2、定义一个 DIV 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、获取仪表板 ID。
    5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #

    <script setup lang="ts" name="dashboard">
    
    import {getToken} from "@/api/common";
    import { onMounted , onUnmounted } from "vue";
    import { Base64 } from "js-base64";
    
    onMounted(() => {
      window.addEventListener("message" , onMessage , false);
    })
    
    onUnmounted( () => {
      window.removeEventListener("message" , onMessage , false);
    })
    
    const initParams = {
      attachParams: {
        user: "参数值"
      },
      # DataEase 向外部传惨开关
      callBackFlag: "yes"
    }
    
    # 仪表板 ID
    let dvId = "";
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
      const dataease = new DataEaseBi("Dashboard", {
        baseUrl: baseUrl,
        token: result,
        dvId: dvId,
        busiFlag: "dashboard",
        outerParams: JSON.stringify(initParams)
      });
    
      dataease.initialize({container: "#div-dashboard-view"});
    
    })
    # 解析传递消息，若为 de_inner_params，则获取对应信息，并解析 message，base64 编码
    const onMessage = function (event: any) {
      if (event.data?.eventName === "de_inner_params") {
        const dvId = event.data.args.sourceDvId;
        const viewId = event.data.args.sourceViewId;
        const message = event.data.args.message;
        const messageDecode = Base64.decode(message);
        alert("仪表板ID : "+ dvId + " ; 图表ID : " + viewId + " ; 点击详情 : " + messageDecode);
      }
    }
    
    </script>
    ```
## 2 仪表板设计器嵌入
!!! Abstract ""
    仪表板编辑嵌入，嵌入整个仪表板设计器界面，可浏览嵌入仪表板也可编辑该仪表板。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取仪表板 ID。
       5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-dashboard-designer-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="dashboardDesigner">
    
    import {getToken} from "@/api/common";
    # 仪表板 ID
    let dvId = "";
    # DataEase 企业版访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        # DashboardEditor：仪表板设计器嵌入固定写法。
      const dataease = new DataEaseBi("DashboardEditor", {
         baseUrl: baseUrl,
         token: result,
         resourceId: dvId,
         # 固定写法
         opt: "create"
        });
    
        dataease.initialize({container: "#div-dashboard-designer-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```
## 3 数据大屏嵌入
!!! Abstract ""
    数据大屏嵌入支持嵌入单个数据大屏，并可浏览嵌入的数据大屏。数据大屏嵌入还支持外部参数设置。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取数据大屏 ID。
       5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    
       双向传参应用场景：
       一、第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。
         1、初始化看板时，由第三方系统向 DataEase 传参过滤数据。
          a) 前端传参
          b) 后端传参
         2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
       二、DataEase 向第三方系统传参
         1、查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容。
    #
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-dataV-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="dashboard">
    
    import {getToken} from "@/api/common";
    # 数据大屏 ID
    let dvId = "";
    # DataEase 企业版访问地址
    let baseUrl = "";
    getToken().then(result => {
        # Dashboard：仪表板数据大屏嵌入固定写法。
        const dataease = new DataEaseBi("Dashboard", {
            baseUrl: baseUrl,
            # token: JWT token 认证。
            token: result,
            dvId: dvId,
            # 固定写法：dashboard 仪表板、dataV 数据大屏
            busiFlag: "dataV"
        });
    
        dataease.initialize({container: "#div-dataV-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```
### 3.1 数据大屏双向参数传递
!!! Abstract ""
    参考 DIV 仪表板双向参数传递以及 DIV 数据大屏嵌入，将相应 busiFlag 修改对应。

## 4 数据大屏设计器嵌入
!!! Abstract ""
    数据大屏设计器嵌入，嵌入整个数据大屏设计器界面，可浏览嵌入数据大屏也可编辑该数据大屏。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取数据大屏 ID。
       5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-dataV-editor-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="dataVEditor">
    
    import {getToken} from "@/api/common";
    # 数据大屏 ID
    let dvId = "";
    # DataEase 企业版访问地址
    let baseUrl = "";
    
    getToken().then(result => {
    # VisualizationEditor：仪表板设计器嵌入固定写法。
        const dataease = new DataEaseBi("VisualizationEditor", {
            baseUrl: baseUrl,
            token: result,
            dvId: dvId,
            # 固定写法
            opt: "create"
        });
    
        dataease.initialize({container: "#div-dataV-editor-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```
## 5 图表嵌入
!!! Abstract ""
    图表嵌入支持嵌入单个图表，并可浏览嵌入的图表。图表嵌入还支持外部参数设置。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、获取仪表板/数据大屏 ID以及图表 ID。
       5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    
       双向传参应用场景：
       一、第三方系统向 DataEase 传参，依赖于 DataEase 仪表板/数据大屏外部参数实现。
         1、初始化看板时，由第三方系统向 DataEase 传参过滤数据。
          a) 前端传参
          b) 后端传参
         2、查看看板时，可点击第三方系统的查询组件等，过滤 DataEase 的看板数据。
       二、DataEase 向第三方系统传参
         1、查看看板时，可点击 DataEase 里的各个组件，向第三方系统传递当前点击的内容。
    #
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="view">
    
    import {getToken} from "@/api/common";
    # 仪表板 ID / 数据大屏 ID
    let dvId = "";
    # 图表 ID
    let chartId = "";
    # DataEase 企业版访问地址
    let baseUrl = "";
    
    
    getToken().then(result => {
        # Dashboard：仪表板数据大屏嵌入固定写法。
        const dataease = new DataEaseBi("ViewWrapper", {
            baseUrl: baseUrl,
            # token: JWT token 认证。
            token: result,
            dvId: dvId,
            chartId: chartId,
            # 固定写法：dashboard 仪表板、dataV 数据大屏
            busiFlag: "dashboard"
        });
    
        dataease.initialize({container: "#div-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```
### 5.1 图表双向参数传递
!!! Abstract ""
    参考 DIV 仪表板双向参数传递以及 DIV 图表嵌入。

## 6 我的填报嵌入
!!! Abstract ""
    支持我的填报的嵌入，查看填报信息。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       5、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-datafillinghandler-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="datafillinghandler">
    
    import {getToken} from "@/api/common";
    
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        const dataease = new DataEaseBi("DataFillingHandler", {
            baseUrl: baseUrl,
            token: result
        });
    
        dataease.initialize({container: "#div-datafillinghandler-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```

## 7 模块嵌入
!!! Abstract ""
    DataEase 现有模块，数据源、数据集、数据大屏、仪表板等模块均可实现嵌入式。

### 7.1 仪表板模块
!!! Abstract ""
    嵌入整个仪表板模块，嵌入后可实现仪表板模块的整体使用，包括新建仪表板，编辑仪表板、删除仪表板。

    ```
    <template>
        <div class="card content-box">
            <div style="width: 100%; height: 100%" id="div-dashboard-module-view"></div>
        </div>
    </template>
    <script setup lang="ts" name="dashboardModule">
    
    import {getToken} from "@/api/common";
    
    # DataEase 企业版访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        # DashboardPanel：仪表板模块嵌入固定写法。
            const dataease = new DataEaseBi("DashboardPanel", {
                # baseUrl：DataEase 企业版访问地址。
                baseUrl: baseUrl,
                # token: JWT token 认证。
                token: result
            });
        
            dataease.initialize({container: "#div-dashboard-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```

### 7.2 数据大屏模块
!!! Abstract ""
    嵌入整个数据大屏模块，嵌入后可实现数据大屏模块的整体使用，包括新建数据大屏，编辑数据大屏，删除数大屏。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #
    <template>
        <div class="card content-box">
            <div style="width: 100%; height: 100%" id="div-dataV-module-view"></div>
        </div>
    </template>
    <script setup lang="ts" name="dataVModule">
    
    import {getToken} from "@/api/common";
    
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        # ScreenPanel：数据大屏模块嵌入固定写法。
        const dataease = new DataEaseBi("ScreenPanel", {
            baseUrl: baseUrl,
            # token: JWT token 认证
            token: result
        });
    
        dataease.initialize({container: "#div-dataV-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    ```
###  7.3 数据集模块
!!! Abstract ""
    嵌入整个数据集模块，嵌入后可实现数据集模块的整体使用，包括新建数据集，编辑数据集，删除数集。

    ```
    #
       1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
       2、定义一个 DIV 容器，并且设置好宽高。
       3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
       4、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #

    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-dataset-module-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="datasetModule">
    
    import {getToken} from "@/api/common";
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        # Dataset：数据集模块嵌入固定写法。
            const dataease = new DataEaseBi("Dataset", {
                baseUrl: baseUrl,
                # token: JWT token 认证
                token: result
            });
    
        dataease.initialize({container: "#div-dataset-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```

###  7.4 数据源模块
!!! Abstract ""
    嵌入整个数据源，嵌入后可实现数据源模块的整体使用，包括新建数据源，编辑数据源，删除数源。

    ```
    #
    1、DIV 嵌入需要引用嵌入式 JS，一般可以在 index.html 里进行引用.
    2、定义一个 DIV 容器，并且设置好宽高。
    3、调用嵌入式 Token 生成接口，获取嵌入式 Token。
    4、创建 DataEaseBi 对象，传入相应参数，渲染 DIV 容器，完成嵌入。
    #

    <template>
        <div class="card content-box">
            <div style="width: 100%; height: 100%" id="div-datasource-module-view"></div>
        </div>
    </template>
    <script setup lang="ts" name="datasourceModule">
    
    import {getToken} from "@/api/common";
    
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        # Datasource：数据源模块嵌入固定写法。
        const dataease = new DataEaseBi("Datasource", {
            baseUrl: baseUrl,
            # token: JWT token 认证
            token: result
        });
        
        dataease.initialize({container: "#div-datasource-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```
###  7.5 数据填报模块
!!! Abstract ""
    嵌入整个数据源，嵌入后可实现数据源模块的整体使用，包括新建数据源，编辑数据源，删除数源。

    ```
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-datafilling-module-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="datafillingModule">
    
    import {getToken} from "@/api/common";
    
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
    # DataFilling：数据填报模块嵌入固定写法。
        const dataease = new DataEaseBi("DataFilling", {
            baseUrl: baseUrl,
            # token: JWT token 认证
            token: result
        });
        
        dataease.initialize({container: "#div-datafilling-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```

###  7.6 Copilot 模块
!!! Abstract ""
    嵌入 Copilot 模块。

    ```
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-copilot-module-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="copilotmodule">
    
    import {getToken} from "@/api/common";
    
    # DataEase 访问地址
    let baseUrl = "";
    
    getToken().then(result => {
        # Copilot： Copilot 模块嵌入固定写法。
        const dataease = new DataEaseBi("Copilot", {
            baseUrl: baseUrl,
            // token: JWT token 认证
            token: result
        });
    
        dataease.initialize({container: "#div-copilot-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```
###  7.7 模版管理模块
!!! Abstract ""

    ```
    <template>
      <div class="card content-box">
        <div style="width: 100%; height: 100%" id="div-templatemanage-module-view"></div>
      </div>
    </template>
    <script setup lang="ts" name="templatemanage">
    
    import {getToken} from "@/api/common";
    
    # DataEase 访问地址
    let baseUrl = "";
    let opt = "create"
    getToken().then(result => {
        # TemplateManage：模版管理模块嵌入固定写法。
        const dataease = new DataEaseBi("TemplateManage", {
            baseUrl: baseUrl,
            #  token: JWT token 认证
            token: result
            opt: opt
        });
    
        dataease.initialize({container: "#div-templatemanage-module-view"});
    
    })
    </script>
    <style scoped lang="scss">
    @import "index";
    </style>
    @/api/hook
    ```