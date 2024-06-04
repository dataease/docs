## 1 编辑仪表板

!!! Abstract ""
	点击下图所示的位置或者新建仪表板，进入仪表板编辑界面。

![2.0编辑仪表板](../img/dashboard_generation/2.0编辑仪表板.png){ width="900px" }

![2.0新建仪表板2](../img/dashboard_generation/2.0新建仪表板2.png){ width="900px" }

## 2 撤销

!!! Abstract ""
	点击下图按钮，撤销上一步操作。

![2.0撤销](../img/dashboard_generation/2.0撤销.png){ width="900px" }

## 3 恢复

!!! Abstract ""
	**点击下图按钮，可以对组件操作恢复。**

![2.0恢复](../img/dashboard_generation/2.0恢复.png){ width="900px" }

## 4 样式

!!! Abstract ""
	点击【样式】按钮，左侧弹出仪表板样式编辑页面。

![样式](../img/dashboard_generation/2.0仪表板配置.png){ width="900px" }

### 4.1 仪表板主题

!!! Abstract ""
	可在此位置设置仪表板的主题，包括系统主题与自定义主题，如下图所示，点击【保存】，可保存为仪表板主题。
	
![仪表板主题](../img/dashboard_generation/2.0仪表板风格.png){ width="900px" }

### 4.2 仪表板整体配置

!!! Abstract ""
	如下图所示，可调整仪表板主题色、组件间隙，主题色支持浅色与深色切换。  
	**提示：** 设置组件间隙有或无。

![仪表板主题色、组件间隙](../img/dashboard_generation/2.0仪表板整体配置.png){ width="900px" }

!!! Abstract ""
	如下图所示，可设置仪表板的刷新频率，支持到秒级刷新时间。  
	**提示：** 此设置在仪表板编辑页面不生效。

![仪表板刷新时间](../img/dashboard_generation/2.0刷新频率.png){ width="900px" }

!!! Abstract ""
	如下图所示，可调整图表展示结果，选择【仪表板】，则覆盖图表的结果展示数量，取值范围 1~10000。

![仪表板视图结果展示](../img/dashboard_generation/2.0视图结果数量.png){ width="900px" }

### 4.3 仪表板背景
!!! Abstract ""
	如下图所示，点击【仪表板背景】，设置仪表板背景颜色或图片，支持重新上传背景图片。

![仪表板背景](../img/dashboard_generation/2.0仪表板背景.png){ width="900px" }

### 4.4 图表样式

!!! Abstract ""
	仪表板的样式设置支持调整所有组件的共用样式，即将影响整个仪表板已存在的组件，同时在图表层面也可做微调；  
	如下图所示，支持设置组件背景颜色、透明度、边框半径以及背景；

![仪表版_其他样式](../img/dashboard_generation/2.0图表样式.png){ width="900px" }

### 4.5 组件配色

!!! Abstract ""
	如下图所示，支持调整图表的配色方案，支持调整卡片的配色，包括文本卡与指标卡的配色，支持调整表格的配色，包括汇总表、明细表与透视表。

![仪表板_组件配色](../img/dashboard_generation/2.0图表配色.png){ width="900px" }

### 4.6 图表标题

!!! Abstract ""
	如下图所示，支持统一设置标题样式，标题样式首先基于仪表板，各图表可再在组件层面做微调。

![仪表板_图表标题](../img/dashboard_generation/2.0图表标题.png){ width="900px" }

### 4.7 查询组件
	
!!! Abstract ""
	如下图所示，支持设置过滤组件标题样式，包括位置调整与颜色调整，支持输入框样式调整。

![仪表板_过滤组件](../img/dashboard_generation/2.0查询组件样式.png){ width="900px" }

## 5 外部参数设置

!!! Abstract ""
	点击下图按钮，弹出外部参数设置页面，外部参数设置步骤：
	增加一个参数并命名，启用参数，可设置多个参数；配置联动视图与联动视图的字段；

![仪表板_批量操作](../img/dashboard_generation/仪表板外部传参.png){ width="900px" }

!!! Abstract ""
	公共链接参数组装，对传参进行 base64 处理，以下为示例：  
	配置参数名为"省份"，关联了仪表板中【省份】文本下拉过滤组件（也可关联对应的图表字段），组装参数为 {"省份":"北京市"}，使用 base64 加密处理，该示例通过电脑终端进行，其它方式均可。
	```
	echo '{"省份":"北京市"}'|base64
	```
	加密结果为：eyLnnIHku70iOiLljJfkuqzluIIifQo= ，组装规则如下:  
	< 仪表板公共链接 > + < ?attachParams= > + < 加密后的结果 >  
	构建完整的 URL 为：<仪表板公共链接>?attachParams=eyLnnIHku70iOiLljJfkuqzluIIifQo=
	以公共链接的形式访问仪表板，关联的内容被过滤。  

![仪表板_批量操作](../img/dashboard_generation/外部传参示例.png){ width="900px" }

!!! Abstract ""
	公共链接外部参数支持一参多传、多参数传参，可通过数组形式传入多值，对组件进行多选，如下示例，对参数进行处理。   
	提示： 传参处理时，若拼接后的 URL 带特殊符号，需做转换处理，示例如：+ 用 %2B 替代。  
	```
	echo '{"省份":["山东省","四川省","广东省","河南省"]}'|base64
	```
	```
	echo '{"省份":"广东省","年份":"2023"}'|base64
	```
	注意： 在做完 base64 编码后，再做一次 encodeURIComponent 的 URL 编码，以防有些内容编码后存在特殊字符，浏览器无法解析的情况。  
	存在这类字符时，会提示”外部参数解析错误未生效，请按规定编码方式传参“。

## 6 批量操作

!!! Abstract ""
	点击批量操作按钮，选择图表，可批量设置图表样式属性，且根据所选择的图表不同，可修改的属性不同，如下图所示。

![仪表板_批量操作](../img/dashboard_generation/2.0批量操作.png){ width="900px" }

!!! Abstract ""
	**请注意：当勾选多个不同类别的图形时，只能批量修改共性的属性。**

![仪表板_批量操作](../img/dashboard_generation/2.0批量样式调整.png){ width="900px" }

## 7 复用

!!! Abstract ""
	支持复用所有的组件，复用图表支持适配当前仪表板样式。

![仪表板_复用](../img/dashboard_generation/2.0复用.png){ width="900px" }

!!! Abstract ""
	复制上图不一样样式的仪表板中的图表会自动适配当前仪表板下的样式。

![仪表板_复用](../img/dashboard_generation/2.0进行复用.png){ width="900px" }

## 8 保存

!!! Abstract ""
	点击下图所示的保存按钮，保存仪表板。

![仪表板_保存](../img/dashboard_generation/2.0保存.png){ width="900px" }

## 9 返回

!!! Abstract ""
	点击下图所示的返回按钮，关闭仪表板。

![仪表板_关闭](../img/dashboard_generation/2.0返回.png){ width="900px" }


