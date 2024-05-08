## 1 查看

!!! Abstract ""
	切换到仪表板模块时，系统会自动展示位于第一个的默认仪表板，用户可根据需要设定最关注的仪表板为默认的第一个仪表板；  
	默认仪表板栏支持置顶功能，进入仪表板页面后，若默认的仪表板栏存在仪表板，则显示第一个默认的仪表板；
	用户可通过置顶的功能调整默认显示的仪表板。

![仪表盘_查看默认仪表板](../img/dashboard_generation/仪表板_查看默认仪表板.png){ width="900px" }

!!! Abstract ""
	点击下图中所示位置，查看仪表板。

![仪表盘_查看](../img/dashboard_generation/仪表板_查看.png){ width="900px" }

## 2 分享

!!! Abstract ""
	点击下图中所示位置，点击【分享】。

![仪表板_分享](../img/dashboard_generation/仪表板_分享.png){ width="900px" }

!!! Abstract ""
	可在下图所示的位置，选择分享的组织、角色或用户。

![仪表板_分享给](../img/dashboard_generation/仪表板_分享给.png){ width="900px" }

!!! Abstract ""
	可在下图所示位置：

	1.查看其它组织或用户分享给自己的仪表板；  
	2.我分享给其他组织、角色、用户的仪表板，并支持编辑（添加、删除）分享对象、甚至一键取消分享。

![仪表板_被分享](../img/dashboard_generation/仪表板_被分享.png){ width="900px" }

## 3 公共链接

### 3.1 创建公共链接

!!! Abstract ""
	点击下图中所示位置，创建公共链接。

![仪表板_创建公共链接](../img/dashboard_generation/仪表板_创建公共链接.png){ width="900px" }

!!! Abstract ""
	打开下图中所示链接分享的按钮，链接自动生成，点击【复制链接】，可把链接分享给任何组织或个人。  
	**分享链接可设置有效期及密码保护。**

![仪表板_创建公共链接_复制链接](../img/dashboard_generation/仪表板_创建公共链接_复制链接.png){ width="900px" }

!!! Abstract ""
	公共链接功能现已集成 Ticket 机制，增强了链接的安全性和灵活性。每个 Ticket 均可独立设定有效期。此外，相较于之前版本需要对外部参数进行 base64 编码处理，现在的公共链接外部参数可以直接在 Ticket 参数中简易设置。  
	具体操作如下： 一个仪表板的公共链接为 https://example.dataease.com/link/bcg48L2W；

![name](../img/release_notes/1.9%20公共链接增加%20Ticket%20机制1.png){ width="500px" }

!!! Abstract ""
	对其进行 Ticket 设置，设置参数为 {"name":"Tony","age":10}，获取到该条 Ticket 的 ticket 为“VMv5FH2o” ；
![name](../img/release_notes/1.9%20公共链接增加%20Ticket%20机制3.png){ width="500px" }

![name](../img/release_notes/1.9%20公共链接增加%20Ticket%20机制4.png){ width="500px" }

!!! Abstract ""
	使用 Ticket 的公共链接格式为 https://example.dataease.com/link/bcg48L2W?ticket=VMv5FH2o。 
	在此情况下，无需传递 Ticket 参数，DataEase 将从数据库自动获取 Ticket 相关参数。    
	当启用 Ticket “必选”选项时，只有在 URL 中附带 ticket 参数的情况下，公共链接才能被成功访问。
![name](../img/release_notes/1.9%20公共链接增加%20Ticket机制5.png){ width="500px" }

!!! Abstract ""
	公共链接查看仪表板时支持切换全屏预览。
![name](../img/release_notes/v1-18-14-13.png){ width="900px" }

### 3.2 公共链接传参

!!! Abstract ""
	公共连接支持第三方系统参数，具体设置可参考【仪表板基础功能】的【外部参数设置】说明。

![仪表板_创建公共链接_外部参数](../img/dashboard_generation/仪表板_创建公共链接_外部参数.png){ width="900px" }

### 3.3 公共链接返回

!!! Abstract ""
	公共链接跳转后支持返回；  
	访问公共链接后，在页面的右上角的区域有一个较小的功能菜单区，当鼠标移动到右上角时，会出现功能菜单，包括返回上一级、清除所有联动（有联动的时候）、下载；  
	可以通过点击“返回上一级”以回到点击公共链接前的页面；  
	应用场景：使用公共链接做嵌入式，访问后需要返回原系统。

![仪表板_创建公共链接_返回](../img/dashboard_generation/仪表板_创建公共链接_返回.png){ width="900px" }

### 3.4 公共链接导出 PDF 

!!! Abstract ""
	公共链接支持导出 PDF；  
	访问公共链接后，在页面的右上角的区域有一个较小的功能菜单区，当鼠标移动到右上角时，会出现功能菜单，包括返回上一级、清除所有联动（有联动的时候）、下载；  
	点击“下载”，则可在公共链接访问仪表板时导出该仪表板的 PDF。

![仪表板_创建公共链接_导出PDF](../img/dashboard_generation/仪表板_创建公共链接_导出PDF.png){ width="900px" }

## 4 仪表板发布

!!! Abstract ""
	支持仪表板发布功能，仪表板在未发布的状态下，名称及图标呈现灰色，点击在预览界面的【发布】按钮，点击后未发布的仪表板即发布，同时按钮会变为【取消发布】。

	处于发布状态的仪表板，以下情况可以访问：

	- 被分享的用户
	- 仪表板公共链接
	- 有该仪表板使用及更多权限的用户

	处于取消发布状态的仪表板，以下情况可以访问：

	- 有该仪表板管理及更多权限的用户

![仪表板_取消发布](../img/dashboard_generation/仪表板_取消发布.png){ width="900px" }

!!! Abstract ""
	点击【取消发布】则仪表板恢复到未发布状态，取消发布后的仪表板，没有访问权限的用户会看到仪表板显示为【已下架】。

![仪表板_发布](../img/dashboard_generation/仪表板_发布.png){ width="900px" }

![仪表板_已下架](../img/dashboard_generation/仪表板_已下架.png){ width="900px" }

## 5 保存为模板

!!! Abstract ""
	点击下图中所示位置，保存为模板，在创建仪表板时使用。

![仪表板_保存为模版](../img/dashboard_generation/仪表板_保存为模版.png){ width="900px" }

## 6 仪表板导出 
### 6.1 导出为模板

!!! Abstract ""
	点击下图中所示位置，导出模板到本地，可在本地的下载目录中查看，亦可用此模板创建仪表板。

![仪表板_导出为模版](../img/dashboard_generation/仪表板_导出为模版.png){ width="900px" }

### 6.2 导出为 PDF

!!! Abstract ""
	点击下图中所示位置，点击可弹出 PDF 的预览窗口。

![仪表板_导出pdf](../img/dashboard_generation/仪表板_导出pdf入口.png){ width="900px" }

!!! Abstract ""
	预览导出的 PDF 样式，另外还支持带参数下载，比如：仪表板名称、导出时间、导出人等，点击【导出为 PDF 】，下载 PDF 文件至本地，点击【取消】，取消下载 PDF 文件。

![仪表板_导出pdf](../img/dashboard_generation/仪表板_导出pdf预览.png){ width="900px" }

### 6.3 导出为图片

!!! Abstract ""
	仪表板支持导出图片，点击下图所示的位置，可导出图片。

![仪表板_导出图片](../img/dashboard_generation/仪表板_导出图片.png){ width="900px" }

### 6.4 导出为应用

!!! Abstract ""
	支持将仪表板【导出为应用】，可将仪表板及其用到的数据集、数据源关联关系一并导出成一个应用文件，文件名称为：XXX-APP.DEAPP。

![仪表板_导出应用](../img/dashboard_generation/仪表板_导出应用.png){ width="900px" }

## 7 预览

!!! Abstract ""
	支持两种预览方式，第一种：新打开页面预览，第二种：全屏预览仪表盘。

![仪表板_预览](../img/dashboard_generation/仪表板_预览.png){ width="900px" }

## 8 查看明细与放大

### 8.1 导出视图 Excel

!!! Abstract ""
	预览模式下，视图放大页面支持导出视图图片，查看视图明细页面支持导出视图图表数据。

![仪表板_预览](../img/dashboard_generation/仪表板_放大.png){ width="900px" }

!!! Abstract ""
	视图侧支持导出原始明细数据，根据用户权限+视图的过滤条件+仪表板过滤组件+外部传参过滤数据，然后导出该视图所使用的数据集数据，包含数据集所有字段。  
	**注意：公共链接无导出原始明细数据的功能。**

![name](../img/release_notes/1.4 支持在视图侧导出视图原始明细数据.png){ width="900px" }
 
![明细导出结果](../img/dashboard_generation/明细导出结果.png){ width="900px" }

### 8.2 导出视图图片

!!! Abstract ""
	在视图放大效果下，支持导出视图图片。  
	**注意：** 表格类视图不支持，因为该视图本身形式就是表格，按 Excel 导出即可。

![仪表板_导出图片](../img/dashboard_generation/仪表板_导出视图图片.png){ width="900px" }

## 9 收藏 

!!! Abstract ""
	点击下图中所示位置，收藏仪表板。

![仪表板_收藏](../img/dashboard_generation/仪表板_收藏.png){ width="900px" }

!!! Abstract ""
	收藏后，可在下图所示位置查看收藏列表。

![仪表板_收藏列表](../img/dashboard_generation/仪表板_收藏列表.png){ width="900px" }

## 10 刷新

!!! Abstract ""
	仪表板刷新提供手动与自动两种方式，其中自动刷新配置如下，支持开关控制，可开启固定刷新功能，实时刷新数据，若当前仪表板一般长时间无数据更新，不需要固定刷新功能则可关闭此功能，完成配置后需保存仪表板进入预览界面查看效果。

![仪表板_刷新](../img/dashboard_generation/仪表板_自动刷新配置.png){ width="900px" }

!!! Abstract ""
	同时，仪表板提供手动刷新按钮，用户需要时可自行点击进行刷新。

![仪表板_刷新](../img/dashboard_generation/仪表板_手动刷新按钮.png){ width="900px" }


