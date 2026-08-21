本仓库保存了 [DataEase](https://github.com/dataease/dataease) 的 [官方文档](https://dataease.cn/docs/v3/)，使用 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建。

当前默认文档版本为 **v3**（分支 `v3`）。导航与页面结构以根目录 `mkdocs.yml` 为准。

## 本地开发

### 克隆本仓库

```bash
git clone https://github.com/dataease/docs.git
cd docs
git checkout v3
```

### 安装依赖

```bash
pip install -r requirements/requirements.txt
```

### 修改文档

- 文档结构：`mkdocs.yml` 的 `nav`
- 正文与图片：`docs/` 目录

### 本地预览

```bash
mkdocs serve
```

浏览器访问提示的本地地址即可预览。

### 构建

```bash
mkdocs build
```
