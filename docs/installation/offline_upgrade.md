
按照本文档 [离线安装](./offline_installation.md) 步骤, 下载新版本安装包并上传解压后, 重新执行安装命令进行升级

```sh
# 进入项目目录
cd metersphere-release-v1.x.y-offline
# 运行安装脚本
/bin/bash install.sh
# 查看 MeterSphere 状态
msctl status
```

!!! warning "注意"
    如果在旧版本安装过程中有修改安装目录(默认为 /opt 目录), 在执行升级脚本前需要修改 install.conf 文件并配置安装目录为旧版本的安装目录 