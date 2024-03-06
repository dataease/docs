!!! Abstract ""
    以源码方式运行 DataEase ，请使用 v2.3、v2.2 等已发布分支的代码，请勿使用 dev 等分支。dev 等分支代码均处于开发或测试阶段，用到的依赖并没有上传到中央仓库，在编译时会出现依赖缺失的情况。
    本文所使用源码为 DataEase v2.3 分支。
## 1 项目结构

    ```
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile                                # 构建容器镜像使用的 Dockerfile
    ├── LICENSE                                   # License 申明
    ├── README.md
    ├── SECURITY.md
    ├── core                                      # 社区版功能源码
    ├── de-xpack                                  # 企业版功能源码（不开源）
    ├── drivers                                   # 数据源驱动文件
    ├── installer                                 # 安装工程源码
    ├── mapFiles                                  # 地图文件
    ├── pom.xml                                   # 整体 maven 项目使用的 pom 文件
    ├── sdk                                       # DataEase 基础接口工程源码
    └── staticResource                            # 静态资源文件
    ```

## 2 配置环境

!!! Abstract ""
    本文以 CentOS 7.9 为例，举例说明如何以源码的形式编译 DataEase 工程。所有操作均在阿里云（新加坡区） 4核8G 环境中执行。

### 2.1 安装 JDK 17
!!! Abstract ""
    DataEase v2 使用 JDK17， [Oracle 官网下载 JDK17 安装包](https://www.oracle.com/java/technologies/downloads/#java17),根据 CPU 架构，选择对应安装包。本文档所用测试服务器 CPU 架构为 x64，下载的 x64 架构的 rpm 安装包。

    ```
    # 下载 JDK17 RPM 安装包
    wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.rpm

    # 安装 RPM 安装包
    yum -y install jdk-17_linux-x64_bin.rpm
    ```
!!! Abstract ""
    验证 JDK 正确安装。
    ```
    [root@iZt4n8oa58aqukyv8sf1ciZ ~]# java -version
    java version "17.0.10" 2024-01-16 LTS
    Java(TM) SE Runtime Environment (build 17.0.10+11-LTS-240)
    Java HotSpot(TM) 64-Bit Server VM (build 17.0.10+11-LTS-240, mixed mode, sharing)
    ```
### 2.2 安装 Git
!!! Abstract ""
    执行命令安装 Git。

    ```
    yum install -y git
    ```
!!! Abstract ""
    验证 Git。
    ```
    [root@iZt4n8oa58aqukyv8sf1ciZ ~]# git --version
    git version 1.8.3.1
    ```

### 2.3 安装配置 Maven
!!! Abstract ""
    到 Apache Maven 官网下载最新版本的 Maven，官网地址如下：https://maven.apache.org/download.cgi 。
!!! Abstract ""
    执行命令安装 Maven。

    ```
    # 下载并安装 Maven
    wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz
    tar zxvf apache-maven-3.9.6-bin.tar.gz
    mv apache-maven-3.9.6 /opt

    echo "export M2_HOME=/opt/apache-maven-3.9.6" >> ~/.bashrc
    echo "export PATH=\$PATH:\$M2_HOME/bin" >> ~/.bashrc

    source ~/.bashrc
    ```
!!! Abstract ""
    验证 Maven。

    ```
    [root@iZt4n8oa58aqukyv8sf1ciZ ~]# mvn -v
    Apache Maven 3.9.6 (bc0240f3c744dd6b6ec2920b3cd08dcc295161ae)
    Maven home: /opt/apache-maven-3.9.6
    Java version: 17.0.10, vendor: Oracle Corporation, runtime: /usr/lib/jvm/jdk-17-oracle-x64
    Default locale: zh_CN, platform encoding: UTF-8
    OS name: "linux", version: "3.10.0-1160.105.1.el7.x86_64", arch: "amd64", family: "unix"
    ```
