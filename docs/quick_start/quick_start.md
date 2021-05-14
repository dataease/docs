我们为用户准备了可以快速部署 MeterSphere 所有组件及所需的中间件的在线安装脚本, 你可以通过该脚本部署并体验 MeterSphere 所提供的功能

!!! warning "注意"
    快速安装脚本所部署的环境仅适用于测试体验目的, 生产环境请参考本文档[「在线安装」](../installation/online_installation.md)章节内容进行部署

## 部署服务器要求

!!! info "部署服务器要求"
    * 操作系统: 任何支持 Docker 的 Linux x64
    * CPU/内存: 4核8G
    * 磁盘空间: 20G
    * 可访问互联网

## 安装步骤

### 执行快速安装脚本

以 root 用户 ssh 登录目标服务器, 执行如下命令

```sh
curl -sSL https://github.com/metersphere/metersphere/releases/latest/download/quick_start.sh | sh
```

安装脚本默认使用 /opt/metersphere 目录作为安装目录，MeterSphere 的配置文件、数据及日志等均存放在该安装目录

## 登录并使用

### 登录

安装成功后，通过浏览器访问如下页面登录 MeterSphere

```
地址: http://目标服务器IP地址:8081
用户名: admin
密码: metersphere
```

### 界面说明

![!界面说明](../img/layout.png)

