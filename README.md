本仓库保存了 [MeterSphere 项目]() 的 [官方文档](https://metersphere.io/docs/)，该文档使用 [MkDocs]() 文档框架下的 [Material for MkDocs]() 主题进行构建。

## 本地开发

### 克隆本仓库
```bash
git clone https://github.com/metersphere/docs.git
```

### 安装依赖
```bash
cd docs
pip install -r requirements/requirements.txt
```

### 修改文档内容
本文档的文档结构定义在 `mkdocs.yml` 文件中，文档的具体内容均在 `docs` 目录中。
```yaml
..........
nav:
    - 项目介绍: index.md
    - 快速开始: 
        - 一键部署: quick_start/quick_start.md
        - 创建项目: quick_start/create_project.md
        - 使用测试跟踪: quick_start/test_track.md
        - 使用接口测试: quick_start/api_test.md
        - 使用性能测试: quick_start/load_test.md
    - 系统架构: system_arch.md
    - 安装部署: 
        - 在线安装: installation/online_installation.md
        - 离线安装: installation/offline_installation.md
        - 在线升级: installation/online_upgrade.md
        - 离线升级: installation/offline_upgrade.md
    - 用户手册: 
        - 通用功能: user_manual/general.md
        - 系统设置: user_manual/system_management.md
        - 测试跟踪: user_manual/test_track.md
        # - 系统设置: 
        #     - 模块说明: user_manual/system_management/intro.md
        #     - 系统管理: user_manual/system_management/system.md
        #     - 组织管理: user_manual/system_management/organization.md
        #     - 工作空间管理: user_manual/system_management/workspace.md
        #     - 项目管理: user_manual/system_management/project.md
        #     - 个人信息管理: user_manual/system_management/personal.md
        # - 测试跟踪: 
        #     - 模块说明: user_manual/test_track/intro.md
        #     - 首页: user_manual/test_track/home.md
        #     - 测试用例: user_manual/test_track/test_case.md
        #     - 用例评审: user_manual/test_track/test_case_review.md
        #     - 测试计划: user_manual/test_track/test_plan.md
        #     - 报告: user_manual/test_track/test_report.md
        - 接口测试: 
            - 模块说明: user_manual/api_test/intro.md
            - 首页: user_manual/api_test/home.md
            - 接口定义: user_manual/api_test/api_definition.md
            - 接口自动化: user_manual/api_test/api_automation.md
            - 测试报告: user_manual/api_test/test_report.md
            - 用例步骤说明: user_manual/api_test/api_step.md
            # - 接口详情说明: user_manual/api_test/api_detail.md
            - 内置函数: user_manual/api_test/functions.md
        - 接口测试（旧版）: user_manual/api_test.md
        - 性能测试: user_manual/performance_test.md
        # - 性能测试:
        #     - 模块说明: user_manual/load_test/intro.md
        #     - 首页: user_manual/load_test/home.md
        #     - 性能测试: user_manual/load_test/api_definition.md
        #     - 测试报告: user_manual/load_test/test_report.md
    - 使用教程:
        - 使用 MeterSphere 进行 Dubbo 接口测试: tutorial/dubbo.md
        - 使用 MeterSphere 进行场景化接口测试: tutorial/api_testing.md
        - 使用预执行脚本功能生成接口认证签名: tutorial/pre_processor.md
        - 【视频】MeterSphere 如何与 TAPD和 Jira 对接: https://www.bilibili.com/video/BV1jr4y1c7Lg/
        - 【视频】MeterSphere 如何对接邮件、钉钉、企业微信: https://www.bilibili.com/video/BV1dp4y167ch/
        - 【视频】如何在 MeterSphere 中做场景化的接口测试: https://www.bilibili.com/video/BV1vy4y1q7f7/
        - 【视频】如何在 MeterSphere 中导入 Postman 脚本做接口测试: https://www.bilibili.com/video/BV1W54y1C7uY
        - 【视频】如何在 MeterSphere 中导入 Swagger UI 脚本做接口测试: https://www.bilibili.com/video/BV1YK411A7E8/
    - 常见问题: faq.md
    - 开发文档: dev_manual.md
    - 用户案例: 
        - 88完美邮箱全面提升产品质量的落地指南: case_studies/88com.md
        - 蔚澜环保基于MeterSphere的自动化测试实践: case_studies/weilanep.md
        - 易盛信息MeterSphere接口测试使用经验: case_studies/esunny.md
    - 关于:
        - 更新说明: about/changelog.md
        - 联系我们: about/contact.md
    - JMeter 资源合集: awesome-jmeter.md
    - 企业版试用: enterprise.md
..........
```

文档内容使用 markdown 语法编写，若要添加新的文档，需要先在 `mkdocs.yml` 文件中的 `nav` 部分增加对应章节导航。

### 本地调试文档
```bash
mkdocs serve
```
执行上述命令后，可通过 `http://127.0.0.1:8000` 地址查看生成的文档内容，当修改文档后，页面内容会自动更新。

### 构建文档
```bash
mkdocs build
```

执行上述命令后，会在 `site` 目录下生成文档站点的静态文件，将目录中的内容复制到任意 HTTP 服务器上即可完成文档的部署。

## 帮助完善文档

### Fork 文档仓库
点击仓库右上角的 `fork` 按钮，复制本仓库到自己的 github 账号。

### 克隆 fork 后的仓库
```bash
git clone https://github.com/your-github-account/docs.git
```

### 本地修改并调试

### Push 修改内容到 GitHub 仓库

### 提交 Pull Request 到本仓库