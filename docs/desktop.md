## 1 桌面版介绍
!!! Abstract ""
    [**DataEase 桌面版**](https://www.dataease.cn/)是一款永久免费的 BI 工具。更符合国人使用习惯，提供简单易用的数据可视化分析功能。

    - 常用的数据源支持：支持 OLTP、OLAP、数据仓库、数据湖、数据文件和 API 接口等多种数据源。
    - 多样的图表支持：支持指标图、表格、线/面图、柱/条图、分布图、地图、关系图、双轴图等各种图表类型。
    - 丰富的业务场景模板：提供 200+ 高质量大屏模板，覆盖制造、零售电商、银行金融、医药健康、交通物流等各行各业。

![桌面版介绍](newimg/桌面版效果.gif){ width="900px" }


## 2 安装指南
### 2.1 安装准备
!!! Abstract ""

    - 端口检查：DataEase 的访问端口为 8100，请确保本机的 8100 端口未被占用，以避免端口冲突。
    - 版本检查：请确认本机未安装其他版本的 DataEase（如社区版、企业版等），以防止配置冲突。
    - 离线安装包下载：[**访问 DataEase 桌面版官方网站**](https://www.dataease.cn/)，点击 【立即下载】 按钮，系统将根据您的操作系统自动下载对应版本的安装包。

    **注意：当前支持的系统和版本（其他平台暂不支持）**：
    
    - Windows 系统 - [Windows(x86)](https://community.fit2cloud.com/download/de-desktop/latest?arch=win_amd64) ：支持 Windows 10 或更高版本。
    - MacOS 系统 - MacOS ([x86](https://community.fit2cloud.com/download/de-desktop/latest?arch=mac_amd64) & [arm64](https://community.fit2cloud.com/download/de-desktop/latest?arch=mac_arm64))：支持 MacOS 11（Big Sur）或更高版本。
    - Linux 系统 - [Linux(x86)](https://community.fit2cloud.com/download/de-desktop/latest?arch=linux_amd64)：只支持 64 位 Linux，不支持 32 位 Linux。


### 2.2 安装步骤

!!! Abstract ""
    **Windows 系统**：

    安装包解压后，进入解压后的文件夹，双击 DataEase.exe 启动程序。如果弹出安全提示或者访问网络安全等，一律信任。

!!! Abstract ""
    **MacOS 系统**：

    双击解压文件后，点击应用图标启动程序。如有安全提示，一律信任。 

    注意：如 M1 等 arm 架构的设备提示文件损坏，可参考：https://kb.fit2cloud.com/?p=2b3dcedd-bec9-47dd-863f-ef8e1571fc51。


!!! Abstract ""
    **Linux 系统**：  
    以 Ubuntu 系统为例的安装步骤： 

    - 安装命令：sudo dpkg -i [package]，例如：sudo dpkg -i dataease_1.0.0_amd64.deb。
    - 在启动台找到 DataEase 图标，点击启动。    

    注意：Ubuntu、Debian、openSUSE 等系统时，请勿使用 root 用户，需使用普通用户安装。卸载使用 sudo dpkg -P dataease。卸载使用 sudo dpkg -P dataease。



### 2.3 升级操作

!!! Abstract ""
    下载最新版对离线安装包：[**DataEase 桌面版官方网站**](https://www.dataease.cn/)。
    
    - Windows 系统和 MacOS 系统在原存储位置进行解压，解压完成即可完成升级。
    - Linux 系统利用命令行安装后完成升级，

### 2.4 备份还原

!!! Abstract ""
    DataEase 静态资源目录为用户主目录，具体存放位置根据系统有所区别：   

    - Windows：<系统盘>:/Users/<用户名>
    - Mac：/Users/<用户名>
    - Linux：/home/<用户名>


    **注意：桌面版不支持回退操作，如果要运行新版本，建议先数据备份。备份 DataEase 将数据目录进行备份压缩即可。还原 DataEase 则把原环境里的运行目录进行覆盖。**

!!! Abstract ""
    如果曾使用过公测版的 DataEase 桌面版，在切换到正式版后，需要手动调整引擎设置中的 URL，将其修改为用户主目录路径。例如：

    - 公测版 URL：jdbc:h2:/opt/...  
    - 正式版 URL：jdbc:h2:/Users/<your_username>/opt/...


## 3 注意事项
### 3.1 桌面版与服务器版差异
!!! Abstract ""
    桌面版因架构不同，无法支持以下服务器版的部分功能：

    - 分享链接：不支持创建公共连接，无法分享仪表板或数据大屏链接。
    - 消息中心：不支持消息通知功能，无法接收系统推送的通知。
    - 帮助功能：无法访问帮助、论坛、博客以及企业版试用功能。
    - 系统设置：不支持系统设置中的“新页面打开方式”选项。
    - 字体管理：不支持自定义字体的添加与管理功能。
    - 移动端支持：仅限桌面环境运行，不支持移动设备访问。
    - **X-Pack 功能：不支持升级为企业版，无法使用如平台对接等功能。**

    详细功能请参考本文档 [**快速入门**](../quick_start/) 和 [**功能手册**](../user_manual/general/) 。
