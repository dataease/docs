## 1 富文本

!!! Abstract ""
	双击富文本组件，可定义样式，并支持在编辑区引用维度与指标中字段。
	注意： 引用维度与指标字段时，富文本只选取第一条结果值。

![仪表板_富文本组件入口](../../img/dashboard_generation/2.0富文本组件点击.png){ width="900px" }

![富文本组件_功能](../../img/dashboard_generation/2.0富文本组件.png){ width="900px" }

!!! Abstract ""
	双击输入文字，可单独调整某文字样式。

![富文本组件_调整样式](../../img/dashboard_generation/2.0富文本样式调整.png){ width="900px" }

!!! Abstract ""
	点击插入超链接按钮，可配置超链接，下示例图以插入”百度网页“链接为例。

![富文本组件_超链接](../../img/dashboard_generation/2.0超链接设置.png){ width="900px" }

!!! Abstract ""
	添加表格，输入文字，并可对表格单元格、行、列等做调整，如下图所示。

![富文本组件_表格](../../img/dashboard_generation/2.0富文本表格.png){ width="900px" }


![富文本组件_表格](../../img/dashboard_generation/2.0富文本表格属性设置.png){ width="900px" }

!!! Abstract ""
	还支持插入图片。

![富文本组件_图片](../../img/dashboard_generation/2.0富文本插入图片或者媒体.png){ width="900px" }

![富文本组件_媒体](../../img/dashboard_generation/2.0富文本插入媒体.png){ width="900px" }


## 2 媒体
### 2.1 图片

!!! Abstract ""
	辅助类图片组件，如可作为组件的背景等。

![仪表盘编辑_其他组件](../../img/dashboard_generation/仪表板图片组件.png){ width="900px" }

![仪表盘编辑_其他组件](../../img/dashboard_generation/2.0点击上传图片.png){ width="900px" }


!!! Abstract ""
	图片组件支持不同的适应方式:

    - 适应组件：长宽均跟随组件变化而变化；
    - 原始尺寸：图片原始大小，不跟随组件大小改变而改变；
    - 等比适应：跟随组件大小改变而改变，但是图片原始比例不跟随改变。

![更新1](../../newimg/图片组件支持不同的适应方式.png){ width="900px" }

### 2.2 视频

!!! Abstract ""
	不能上传本地视频，需要填写视频链接信息。如果需要搭建视频服务器可参考知识库：https://kb.fit2cloud.com/?p=0e763f1d-a175-49e0-ac69-af8d39fb789b、https://kb.fit2cloud.com/?p=15 。

![仪表盘编辑_其他组件](../../img/dashboard_generation/仪表板视频组件.png){ width="900px" }

![更新1](../../newimg/新增视频组件.png){ width="900px" }

### 2.3 流媒体

!!! Abstract ""
	流媒体只支持 flv 格式，如果需要使用 rtsp 格式，可参考知识库文章：https://kb.fit2cloud.com/?p=182 。

![仪表盘编辑_其他组件](../../img/dashboard_generation/仪表板流媒体组件.png){ width="900px" }

![更新1](../../newimg/1.15 新增流媒体组件.png){ width="900px" }

### 2.4 图片组
!!! Abstract ""
	支持简单的图片上传和轮播功能。
![更新1](../../newimg/新增图片组组件1.png){ width="900px" }

!!! Abstract ""
	图片组还支持与指定数据集关联设置条件样式，根据数据集的变化展示不同的图片。

![更新1](../../newimg/新增图片组组件2.png){ width="900px" }
![更新1](../../newimg/新增图片组件.gif){ width="900px" }


## 3 Tab 组件

!!! Abstract ""
	用户在制作仪表板时，可通过选项卡展示多个视图，并通过点击切换查看；  
	Tab 组件支持放置视图、媒体等组件，配置方式与单独使用该组件一致，即 Tab 组件支持多组件移入移出自由布局。

![仪表盘编辑_其他组件](../../img/dashboard_generation/2.0Tab组件.png){ width="900px" }

![Tab页展示视图](../../img/dashboard_generation/2.0选择tab1.png){ width="900px" }

!!! Abstract ""
	**背景**

	- 支持组件整体背景设置，包括内边距、圆角、背景颜色、背景图片等。

![更新1](../../img/dashboard_generation/Tab 组件的标题支持背景设置.png){ width="900px" }

!!! Abstract ""
  	**标题背景**

	- 支持开启/关闭标题背景。
	- 可分别设置【激活标题背景】与【非激活标题背景】（颜色、图片、内边距、圆角等）。
	- 支持勾选【复用激活标题背景】，使非激活态直接复用激活态背景样式。

![更新1](../../img/dashboard_generation/Tab 组件的标题背景设置.png){ width="900px" }

!!! Abstract ""
	**Tab 标签**

	- 支持显示/隐藏 Tab 标签区域；关闭后仅展示内容区。
	- 支持设置标签字号、激活字号，以及头部字体颜色、激活字体颜色。
	- 支持加粗、斜体、下划线，以及标签水平位置：【居左】、【居中】、【居右】。
	- 支持对各个 Tab 进行拖拽排序；可双击修改标题，并支持复制、显示/隐藏、删除。

![更新1](../../img/dashboard_generation/Tab 组件的标题背景设置1.png){ width="900px" }

!!! Abstract ""
  	**轮播**

	- 支持开启 Tab 自动轮播，并可设置轮播时间（单位：秒，范围 1～3600）。
	- 轮播在退出编辑模式后开始生效。

![更新1](../../img/dashboard_generation/Tab 组件的标题背景设置3.png){ width="900px" }

!!! Abstract ""
  	**其他操作（编辑态）**

	- 支持新增 Tab；也可在标签下拉菜单中编辑标题、复制或删除当前 Tab（至少保留一个）。


## 4 网页组件

!!! Abstract ""
	点击【更多】->【网页】即可引入网页组件。在配置网站地址时请注意：部分网站可能设置不允许嵌入而无法显示。

![更新1](../../newimg/1.16 新增网页组件0.png){ width="900px" }

![更新1](../../newimg/1.16 新增网页组件.png){ width="900px" }


## 5 分页组件
!!! Abstract ""
用户在制作仪表板时，可通过选项卡展示多个分页，并通过点击切换查看；  
分页组件支持放置仪表板进行展示。

	- 分页组件内支持放置仪表板或数据大屏；
	- 分页组件支持轮播设置；
	- 支持对标签，背景进行样式调整；

![更新1](../../newimg/新增分页组件.png){ width="900px" }
![更新1](../../newimg/新增分页组件1.png){ width="900px" }
![更新1](../../newimg/新增分页组件2.png){ width="900px" }
