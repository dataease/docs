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

    注意：当前支持的平台有：
    
    - [Windows(x86)](https://community.fit2cloud.com/download/de-desktop/latest?arch=win_amd64)
    - [Linux(x86)](https://community.fit2cloud.com/download/de-desktop/latest?arch=linux_amd64)
    - [MacOS(arm64)](https://community.fit2cloud.com/download/de-desktop/latest?arch=mac_arm64)
    
    其他平台暂不支持。

### 2.2 安装步骤

!!! Abstract ""
    **Windows 系统**：

    安装包解压后，进入解压后的文件夹，双击 DataEase.exe 启动程序。如果弹出安全提示或者访问网络安全等，一律信任。

!!! Abstract ""
    **MacOS 系统**：

    启动前需赋予 /opt 目录写权限：sudo chmod -R 777 /opt，双击解压文件后，点击应用图标启动程序。如有安全提示，一律信任。  
    注意：若提示“已损坏无法打开”问题，可进行以下尝试： 

    - 在终端执行命令 sudo spctl --master-disable，并且在系统偏好设置 – 安全性与隐私 – 通用 ，选择“任何来源”选项
    - 在终端中输入 xattr -cr (这里要注意后面有个空格，不进行回车)，再将提示已损坏无法打开的程序图标拖到命令栏中，然后回车再次打开程序即可正常运行。
    - 如 M1 等 arm 架构的设备提示文件损坏，可参考：https://kb.fit2cloud.com/?p=2b3dcedd-bec9-47dd-863f-ef8e1571fc51。


!!! Abstract ""
    **Linux 系统**：  
    以 Ubuntu 系统为例的安装步骤： 

    - 安装命令：sudo dpkg -i [package]，例如：sudo dpkg -i dataease_1.0.0_amd64.deb。  
    - 启动前需赋予 /opt 目录和 /usr/lib/dataease 目录的写权限，如 sudo chmod -R a+w /opt /usr/lib/dataease。
    - 在启动台找到 DataEase 图标，点击启动。    

    注意：Ubuntu、Debian、openSUSE 等系统时，请勿使用 root 用户，需使用普通用户安装。卸载使用 sudo dpkg -P dataease。


### 2.3 升级操作

!!! Abstract ""
    下载最新版对离线安装包：[**DataEase 桌面版官方网站**](https://www.dataease.cn/)。
    
    - Windows 系统和 MacOS 系统在原存储位置进行解压，解压完成即可完成升级。
    - Linux 系统利用命令行安装后完成升级，

### 2.4 备份还原

!!! Abstract ""
    DataEase 桌面版安装后，相关文件和运行数据存储在 /opt/dataease2.0 路径下。包括 DataEase 运行时所需的配置文件及运行时产生的数据，包括日志文件等。   
    具体存放位置根据系统有所区别：   

     Windows 系统：

    - 如果将桌面版解压至 C 盘，运行后会在 C 盘下生成 `opt/dataease2.0` 文件夹。 
    - 若再解压至 D 盘 并运行 D 盘下的可执行文件（exe），则会在 D 盘下创建 `opt/dataease2.0` 文件夹，相当于生成了一个全新运行环境。

     MacOS 系统和 Linux 系统：

    - 数据固定存放在 /opt/dataease2.0 目录。

    **备份 DataEase 将 /opt/dataease2.0 目录进行备份压缩即可。还原 DataEase 则把原环境里的运行目录 /opt/dataease2.0 ，整个目录覆盖掉新环境里的 /opt/dataease2.0 目录。**



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

    详细功能请参考本文档 [**快速入门**](../quick_start/) 和 [**功能手册**](../user_manual/general/) 。
