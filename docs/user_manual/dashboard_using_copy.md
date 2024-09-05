## 1 分享公共链接

!!! Abstract ""
	点击下图中所示位置，创建公共链接进行仪表板分享。

![更新1](../../newimg/仪表板开启公共链接分享.png){ width="900px" }

![仪表板_创建公共链接](../img/dashboard_generation/创建公共链接.png){ width="900px" }

!!! Abstract ""
	打开下图中所示链接分享的按钮，链接自动生成，点击【复制链接】进行分享。  
	**分享链接可设置有效期及密码保护。**

![仪表板_创建公共链接_复制链接](../img/dashboard_generation/设置公共链接.png){ width="900px" }

!!! Abstract ""
	支持自定义公共链接后缀。
![更新1](../../newimg/1.21 支持自定义公共链接后缀1.png){ width="400px" }![更新1](../../newimg/1.21 支持自定义公共链接后缀2.png){ width="400px" }
!!! Abstract ""
	支持自定义公共链接密码。
![更新1](../../newimg/1.22 公共链接支持自定义密码.png){ width="500px" }

!!! Abstract ""
	公共链接功能现已集成 Ticket 机制，公共链接外部参数可以直接在 Ticket 参数中简易设置，增强外部传参的安全性和灵活性。    
	**注意：设置 Ticket 的同时，需要开启 [设置仪表板外部参数](https://dataease.io/docs/v2/user_manual/dashboard_basicfunctions/#5)。**     
	打开 Ticket 设置，并单独配置其有效期与参数，每个 Ticket 均可独立设定有效期，例如配置有效期为 30 天，参数为 {"name":"Tony","age":10}：  
![更新1](../../newimg/1.2%20公共链接分享支持%20Ticket%20方式2.PNG){ width="500px" }

!!! Abstract ""
	复制 Ticket 链接，那么，使用 Ticket 的公共链接格式为 https://example.dataease.com/link/bcg48L2W?ticket=xk59xiHJ。在此情况下，无需传递 Ticket 参数，DataEase 将从数据库自动获取 Ticket 相关参数。

![更新1](../../newimg/1.2%20公共链接分享支持%20Ticket%20方式3.PNG){ width="500px" }

!!! Abstract ""
	当启用 Ticket “必选”选项时，只有在 URL 中附带 ticket 参数的情况下，公共链接才能被成功访问。

![更新1](../../newimg/1.2%20公共链接分享支持%20Ticket%20方式4.PNG){ width="500px" }



## 2 仪表板导出

!!! Abstract ""
	点击下图中所示位置，导出仪表板的模板、应用、PDF、图片到本地，可在本地的下载目录中查看。

![仪表板_导出为模版](../img/dashboard_generation/仪表板导出.png){ width="900px" }

## 3 仪表板预览

!!! Abstract ""
	支持两种预览方式，第一种：新打开页面预览，第二种：全屏预览仪表盘。

![仪表板_预览](../img/dashboard_generation/仪表板预览.png){ width="900px" }

## 4 查看明细与放大

### 4.1 导出视图 Excel

!!! Abstract ""
	预览模式下，视图放大页面支持导出视图图片，查看视图明细页面支持导出视图图表数据。

![仪表板_预览](../img/dashboard_generation/查看明细和放大.png){ width="900px" }  

!!! Abstract ""
	明细表中的图片，鼠标点击单元格图片，图片会放大展示。

![更新1](../../newimg/1.7%20明细表支持显示图片5.png){ width="900px" }

!!! Abstract ""
	视图明细效果，支持对视图进行 Excel 导出。

![仪表板_预览](../img/dashboard_generation/查看明细.png){ width="900px" }

![明细导出结果](../img/dashboard_generation/视图导出.png){ width="900px" }

!!! Abstract ""
 	支持原始明细数据导出

![更新1](../../newimg/1.3%20支持原始明细数据导出.PNG){ width="900px" }

### 4.2 导出视图图片

!!! Abstract ""
	在视图放大效果下，支持导出视图图片,导出图片时支持选择尺寸。

![仪表板_导出图片](../img/dashboard_generation/进行放大.png){ width="900px" }

![更新1](../../newimg/1.4 导出图片时支持选择尺寸.png){ width="900px" }



## 5 仪表板刷新

!!! Abstract ""
	仪表板刷新提供手动与自动两种方式，其中自动刷新配置如下，支持开关控制，可开启固定刷新功能，实时刷新数据，若当前仪表板一般长时间无数据更新，不需要固定刷新功能则可关闭此功能，完成配置后需保存仪表板进入预览界面查看效果。

![仪表板_刷新](../img/dashboard_generation/仪表板刷新频率.png){ width="900px" }

!!! Abstract ""
	同时，仪表板提供手动刷新按钮，用户需要时可自行点击进行刷新。

![仪表板_刷新](../img/dashboard_generation/进行刷新.png){ width="900px" }


## 6 仪表板全屏

!!! Abstract ""
	仪表板新支持一键全屏预览

![仪表板_刷新](../img/dashboard_generation/仪表板全屏.png){ width="900px" }


