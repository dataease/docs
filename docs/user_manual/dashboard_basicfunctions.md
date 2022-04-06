## 1 清空画布

!!! Abstract ""
	点击下图的按钮，清空画布，可以重新添加组件。

![清空画布](../img/dashboard_generation/清空画布.png){ width="900px" }

## 2 重做

!!! Abstract ""
	点击下图按钮，可以对组件重做。

![重做](../img/dashboard_generation/重做.png){ width="900px" }

## 3 撤销

!!! Abstract ""
	点击下图按钮，撤销上一步操作。

![撤销](../img/dashboard_generation/撤销.png){ width="900px" }

## 4 样式

!!! Abstract ""
	点击【样式】按钮，左侧弹出仪表板样式编辑页面。

![样式](../img/dashboard_generation/样式.png){ width="900px" }

### 4.1 仪表板主题

!!! Abstract ""
	可在此位置设置仪表板的主题，包括系统主题与自定义主题，如下图所示，点击【保存】，保存仪表板主题。
	
![仪表板主题](../img/dashboard_generation/仪表板主题.png){ width="900px" }

### 4.2 仪表板属性

!!! Abstract ""
	如下图所示，点击【背景】，设置仪表板背景颜色或图片。

![仪表板背景](../img/dashboard_generation/仪表板背景.png){ width="900px" }

!!! Abstract ""
	如下图所示，点击【组件间隙】，设置组件间隙有或无，适用于"矩阵"模式。

![仪表版组件间隙](../img/dashboard_generation/仪表版组件间隙.png){ width="900px" }

!!! Abstract ""
	如下图所示，点击【刷新时间】，设置仪表板的刷新时间，支持秒级刷新时间。  
	**提示：** 此设置在仪表板编辑页面不生效。

![仪表板刷新时间](../img/dashboard_generation/仪表板刷新时间.png){ width="900px" }

!!! Abstract ""
	如下图所示，点击【视图展示结果】，选择【仪表板】，则覆盖视图的结果展示数量。

![仪表板视图结果展示](../img/dashboard_generation/仪表板视图结果展示.png){ width="900px" }

### 4.3 其他属性

!!! Abstract ""
	如下图所示，此处可以设置组件样式（背景），图形属性（颜色）和表格属性（颜色）。  
	**提示：** 此处设置需要将视图样式设置为 [「样式优先级」](../view_module/view_design/#3) 跟随仪表板才会生效。

![仪表版_其他样式](../img/dashboard_generation/仪表版_其他样式.png){ width="900px" }

## 5 元素移入分布方式

!!! Abstract ""
	可设置元素移入仪表板后的分布方式为"矩阵"或"悬浮"：

    - 矩阵：元素可自动对齐，具有相同的间隔距离，用户放置时元素会自动挤压分布，不可多层叠加；
    - 悬浮：元素可完全按照用户移动位置放置，可多个元素叠加，不受其它组件挤压。  

    **提示：新移入仪表板的元素受该设置影响，已存在仪表板的元素不受其修改的影响，可单独修改元素的属性。**

![当前元素移入分布方式](../img/dashboard_generation/当前元素移入分布方式.png){ width="900px" }  
![元素为矩阵或悬浮](../img/dashboard_generation/元素为矩阵或悬浮-单独修改元素.png){ width="900px" }

## 6 外部参数设置

!!! Abstract ""
	点击下图按钮，弹出外部参数设置页面，外部参数设置步骤：

	- 【序号 1】：启用外部参数；
	- 【序号 2】：增加一个参数并命名，启用参数，可设置多个参数；
	- 【序号 3】：配置联动视图与联动视图的字段；
	- 【序号 4】：点击【确定】保存。

![外部参数设置入口](../img/dashboard_generation/外部参数设置入口.png){ width="900px" }  
![外部参数设置](../img/dashboard_generation/外部参数设置.png){ width="900" }

!!! Abstract ""
	**公共链接参数组装，对传参进行 base64 处理，以下为示例：**  
	配置参数名为"省份"，关联了 “2021 年全国 GDP 数据” 仪表板中“今年上半年 GDP” 和 “GDP 前十强城市” 的 province 字段，组装参数为 {"省份":"北京市"}，使用 base64 加密处理，该示例通过电脑终端进行，其它方式均可。
	```shell
	echo '{"省份":"北京市"}'|base64
	```
	加密结果为：eyLnnIHku70iOiLljJfkuqzluIIifQo=  
	在仪表板的公共链接后加上  ?attachParams=加密后的内容，构建完整的 URL：公共链接?attachParams=eyLnnIHku70iOiLljJfkuqzluIIifQo=  
	以公共链接的形式访问仪表板，关联的内容被过滤：

![](../img/dashboard_generation/外部参数设置_效果预览.png){ width="900px" }