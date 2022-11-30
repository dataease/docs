## 1 编辑

!!! Abstract ""
	DataEase v1.9.0 版本，原视图的【数据】、【样式】统一挪动到仪表板内，减少界面来回跳动的动作；   
	创建一个新的视图后，仪表板右侧会默认展开该视图的配置界面，点击【收回】也可将右侧视图编辑区隐藏。  
	**提示：** 鼠标切换其他视图，右侧配置项也会跟随变动为新视图的内容。

![组建编辑_基础功能](../img/dashboard_generation/组件编辑_基础功能.png){ width="900px" }

## 2 复制

!!! Abstract ""
	点击下图中所示的位置，复制组件。

![组件复制_基础功能](../img/dashboard_generation/组件复制_基础功能.png){ width="900px" }


## 3 删除

!!! Abstract ""
	点击下图所示的位置，删除组件。

![组件删除_基础功能](../img/dashboard_generation/组件删除_基础功能.png){ width="900px" }

## 4 层级设置

!!! Abstract ""
	悬浮模式下的组件，支持图层设置。

### 4.1 图层置顶

!!! Abstract ""
	点击下图所示的位置，组件图层置顶。

![组件置顶_基础功能](../img/dashboard_generation/组件置顶_基础功能.png){ width="900px" }

### 4.2 图层置底

!!! Abstract ""
	点击下图所示的位置，组件图层置底。

![组件置底_基础功能](../img/dashboard_generation/组件置底_基础功能.png){ width="900px" }

### 4.3 图层上移

!!! Abstract ""
	点击下图所示的位置，组件图层上移一层。

![组件上移_基础功能](../img/dashboard_generation/组件上移_基础功能.png){ width="900px" }

### 4.4 图层下移

!!! Abstract ""
	点击下图所示的位置，组件图层下移一层。

![组件下移_基础功能](../img/dashboard_generation/组件下移_基础功能.png){ width="900px" }

## 5 分布方式调整

!!! Abstract ""
	点击下图所示的位置，切换组件在仪表板中的分布方式，可切换为悬浮或矩阵。

![切换组件分布方式_基础功能](../img/dashboard_generation/切换组件分布方式_基础功能.png){ width="900px" }

## 6 组件位置及大小调整

!!! Abstract ""
	悬浮模式下组件支持精确位置及大小设置。

	- 支持设置组件相对于上方和左方的间距；
	- 支持设置组件的高度和宽度值。

![组件位置及大小](../img/dashboard_generation/组件位置及大小调整.png){ width="900px" }

## 7 联动设置

!!! Abstract ""
	如下图，点击展开功能菜单，开始【联动设置】。  
	**提示：** 文本卡、指标卡、仪表盘、水波图、词云图、富文本视图不支持联动设置。

![联动设置](../img/dashboard_generation/联动设置入口.png){ width="900px" }

!!! Abstract ""
	如下图，当设置两个视图联动时，设置相对应的数据集的联动字段，设置完成后，点击【确定】，联动设置完成。

![设置联动字段](../img/dashboard_generation/联动设置_字段关联.png){ width="900px" }

!!! Abstract ""
	第一步，点击【浙江省】，并选择【联动】。
!!! Abstract ""
	如果视图同时设置了联动和钻取，那么当点击时由用户选择执行联动或者钻取，当只设置了联动时，默认执行联动；当只设置了钻取时，默认执行钻取。

![联动展示](../img/dashboard_generation/联动选择.png){ width="900px" }

!!! Abstract ""
	第二步，联动结果展示，如下图，设置了联动的视图，只展示浙江省的数据，视图联动时，支持联动部分高亮显示。

![联动展示](../img/dashboard_generation/联动结果.png){ width="900px" }

!!! Abstract ""
	第三步，可点击下图所示位置，清除局部联动和所有联动。

![地图联动](../img/dashboard_generation/联动清除.png){ width="900px" }

## 8 跳转设置

!!! Abstract ""
	如下图，点击展开功能菜单，开始【跳转设置】。  
	**提示：** 文本卡、指标卡、仪表盘、水波图、词云图、富文本视图不支持跳转。

![跳转设置入口](../img/dashboard_generation/跳转设置入口.png){ width="900px" }

!!! Abstract ""
	**第一种，仪表板间跳转，如下图所示，设置原视图与目标仪表板的跳转：**  
	第一步：设置启用字段；  
	第二步：择仪表板链接类型；  
	第三步：选定跳转的仪表板（系统默认会追加一个字段选择）；  
	第四步：选择关联视图和联动字段；  
	第五步：点击【确定】，完成跳转设置。  
	**注意：** 当前用户至少拥有目标仪表板的查看权限，跳转时，若启用字段是指标字段，则提示”未获取跳转信息“。

![跳转设置](../img/dashboard_generation/跳转设置_仪表板间.png){ width="900px" }

!!! Abstract ""
	**第二种，外部链接跳转，支持将视图的点击值作为参数传递给第三方公共链接，作为第三方链接的参数：**  
	第一步：设置启用字段；  
	第二步：选择外部链接链接类型；  
	第三步：填写外部链接地址，同时支持点击字段用来拼接 URL 或者参数（AntV 图库，若为折线图、柱状图等图形，不能出现叠加维度的情况）；  
	第四步：点击【确定】，完成跳转设置。  
	**注意：** 跳转时，若启用字段是指标字段，则提示”未获取跳转信息“。 

![跳转设置](../img/dashboard_generation/跳转设置_外部链接.png){ width="900px" }

!!! Abstract ""
	点击视图中的维度字段，即可触发跳转。

![跳转展示](../img/dashboard_generation/跳转结果入口.png){ width="900px" }

!!! Abstract ""
	如果选择的是仪表板跳转，那么跳转至目标仪表板，并联动目标仪表板的视图，如果不需要，可点击右上角清除联动。

![跳转设置](../img/dashboard_generation/跳转结果_仪表板间.png){ width="900px" }

!!! Abstract ""
	如果选择的是外部链接跳转，那么跳转至第三方平台，同时点击值传递给第三方链接。

![跳转设置](../img/dashboard_generation/跳转结果_外部链接.png){ width="900px" }

## 9 组件样式

!!! Abstract ""
	如下图，点击展开功能菜单，开始【组件样式】设置。

![组件样式入口](../img/dashboard_generation/组件样式入口.png){ width="900px" }

!!! Abstract ""
	支持设置组件的内边距，边框半径与组件背景，背景支持颜色类背景、图片类背景与边框类背景；  
	以下图为示例，勾选【背景】，背景选择【边框 1】，点击【确定】，完成背景设置。

![组件背景设置](../img/dashboard_generation/组件背景设置.png){ width="900px" }

!!! Abstract ""
	过滤组件支持边框、文字、背景色设置，如下图所示。

![组件样式](../img/dashboard_generation/组件样式.png){ width="900" }

!!! Abstract ""
	所有过滤组件样式边框支持自定义颜色，系统内置边框图片文件为 SVG 图片，系统支持边框色设置，可替换 SVG 图片的颜色。

![组件样式](../img/dashboard_generation/组件样式边框.png){ width="900" }

## 10 超链接

!!! Abstract ""
	如下图所示，点击展开功能菜单，开始【超链接】设置。  
	**提示：** 视图及组件均支持超链接的设置。

![超链接入口](../img/view_generation/超链接入口.png){ width="900px" }  
![超链接启用](../img/view_generation/超链接启用.png){ width="900px" }  
![超链接跳转](../img/view_generation/超链接跳转.png){ width="900" }