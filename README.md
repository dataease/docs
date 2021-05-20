本仓库保存了 [DataEase 项目]() 的 [官方文档](https://dataease.io/docs/)，该文档使用 [MkDocs]() 文档框架下的 [Material for MkDocs]() 主题进行构建。

## 本地开发

### 克隆本仓库
```bash
git clone https://github.com/dataease/docs.git
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
    - 系统架构: system_arch.md
    - 安装部署: 
        - 在线安装: installation/online_installation.md
        - 离线安装: installation/offline_installation.md
        - 在线升级: installation/online_upgrade.md
        - 离线升级: installation/offline_upgrade.md
    - 用户手册:
        - 通用功能: user_manual/general.md
        - 数据源: user_manual/datasource_configuration.md
        - 数据集: user_manual/dataset_configuration.md
        - 视图: user_manual/view_generation.md
        - 仪表盘: user_manual/dashboard_generation.md
        - 系统管理:
            - 用户管理: user_manual/system_management/user.md
            - 菜单管理: user_manual/system_management/menu.md
            - 组织管理: user_manual/system_management/organization.md
            - 角色管理: user_manual/system_management/role.md
            - 模版管理: user_manual/system_management/module.md
            - 权限管理: user_manual/system_management/permission.md
    - 使用教程:
        - 使用 DataEase 进行销售仪表盘制作: manual_demo/sales_dashboard.md
    - 常见问题:
        - 系统管理: faq/system_management.md
    - 开发文档: dev_manual.md
    - 关于:
        - 更新说明: about/changelog.md
        - 联系我们: about/contact.md
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