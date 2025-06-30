# 产品介绍

??? warning "重要通知 | DataEase 漏洞通知及修复方案（DE-2025.06）"
    **2025年 5 月和 6 月，有用户反馈发现 DataEase 开源 BI 工具存在安全漏洞，并向 DataEase 开源项目组进行上报。**

    **漏洞信息：** 
    <br> [DataEase H2数据源存在远程代码执行漏洞，CVE编号为CVE-2025-49003。](https://github.com/dataease/dataease/security/advisories/GHSA-x97w-69ff-r55q)
    <br> [DataEase Redshift数据源JDBC参数存在绕过漏洞，CVE编号为CVE-2025-53004。](https://github.com/dataease/dataease/security/advisories/GHSA-mfg2-qr5c-99pp)
    <br> [DataEase PostgreSQL数据源JDBC参数存在绕过漏洞，CVE编号为CVE-2025-53005。](https://github.com/dataease/dataease/security/advisories/GHSA-99c4-h4fq-r23v)
    <br> [DataEase PostgreSQL和Redshift数据源JDBC参数存在绕过漏洞，CVE编号为CVE-2025-53006。](https://github.com/dataease/dataease/security/advisories/GHSA-q726-5pr9-x7gm)

    **以上漏洞影响版本为：** <br> DataEase v2.10.11 之前的版本

    **安全版本为：** <br> DataEase版本 >= v2.10.11 版本
    <br> 注：DataEase v2.10.11 版本已经于 2025 年 6 月 26 日 发布。

    **修复方案：**
    <br>升级 DataEase 软件至上述安全版本。

    **特别鸣谢：** <br> 感谢Java-Chains Team和以下社区用户向 DataEase 开源社区及时反馈上述漏洞。
    <br> CVE-2025-49003：[@Fushuling](https://github.com/Fushuling) [@Lych1e1](https://github.com/Lych1e1)
    <br> CVE-2025-53004：[@Le1a](https://github.com/Le1a) [@for-A1kaid](https://github.com/for-A1kaid)
    <br> CVE-2025-53005：[@Le1a](https://github.com/Le1a) [@for-A1kaid](https://github.com/for-A1kaid) [@Z1Tanuki](https://github.com/Z1Tanuki)
    <br> CVE-2025-53006：[@unam4](https://github.com/unam4)


!!! Abstract ""
    DataEase 是开源的数据可视化分析工具，帮助用户快速分析数据并洞察业务趋势，从而实现业务的改进与优化。  
    DataEase 支持丰富的数据源连接，能够通过拖拉拽方式快速制作图表，并可以方便地与他人分享。

![功能架构图](./newimg/product_acceptance/功能架构图.jpg){ width="1024px" }

## 1 界面展示

![界面展示图](./newimg/product_acceptance/界面介绍.gif){ width="1024px" }

## 2 模板市场

!!! Abstract ""
    模板市场链接地址：https://templates.dataease.cn 。

![模板市场图](./newimg/product_acceptance/模板市场.png){ width="1024px" }

## 3 产品优势

!!! Abstract ""

    - 开源开放：零门槛，线上快速获取和安装；快速获取用户反馈、按月发布新版本；
    - 简单易用：极易上手，通过鼠标点击和拖拽即可完成分析；
    - 全场景支持：多平台安装和多样化嵌入支持；
    - 安全分享：支持多种数据分享方式，确保数据安全。

## 4 主要功能

!!! Abstract ""

    - 图表展示: 支持 PC 端、移动端及大屏展示；
    - 图表制作: 支持丰富的图表类型、支持拖拉拽方式快速制作仪表板或数据大屏；
    - 数据查询：支持基于 Calcite 的跨源数据查询；
    - 数据连接: 支持关系型数据库、数据文件、数据仓库、API 等各种数据源。

## 5 版本对比

![版本对比图](./newimg/product_acceptance/版本对比.jpg){ width="1024px" }

## 6 了解更多 

!!! Abstract ""

    - **如何向团队介绍 DataEase？：** [人人可用的开源 BI 工具](https://dataease.io/download/introduce-dataease_202501.pdf)
    - **获取新一代数据可视化分析平台应用指南：** [新一代数据可视化分析工具应用指南](https://fit2cloud-support.oss-cn-beijing.aliyuncs.com/%E3%80%8A%E6%96%B0%E4%B8%80%E4%BB%A3%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E5%BA%94%E7%94%A8%E6%8C%87%E5%8D%97%E3%80%8B%EF%BC%88DataEase%E7%BC%96%E8%91%97%EF%BC%89.pdf)
    - **DataEase 知识库：** https://kb.fit2cloud.com/categories/dataease
    - **飞致云培训认证中心：** https://edu.fit2cloud.com/index 
