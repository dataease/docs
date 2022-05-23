## 1 准备工作

### 1.1 服务器准备

!!! Abstract ""
    这里选择 Nginx 实现服务的负载均衡，如有 F5 或其他公有云的 SLB 服务，可略过该部分内容。  
    **此处在 MySQL 集群节点上进行 Nginx 的安装，节点规划：**

    * Nginx-1 节点，IP 为 10.1.11.187
    * Nginx-2 节点，IP 为 10.1.11.189

    其他信息：

    * DataEase-1 节点，IP 为 10.1.11.5
    * DataEase-2 节点，IP 为 10.1.11.84

### 1.2 软件准备

!!! Abstract ""
    可以在 Nginx 官网下载对应的安装包，此处下载的是 nginx-1.21.6.tar.gz。

    ```shell
    # 下载 Nginx 安装包
    wget http://nginx.org/download/nginx-1.21.6.tar.gz
    ```

### 1.3 防火墙

!!! Abstract ""
    Nginx 默认通过 80 端口通信，需要打开防火墙的 80 端口：

    ```shell
    firewall-cmd --zone=public --add-port=80/tcp --permanent
    firewall-cmd --reload
    ```

## 2 Nginx 安装

!!! Abstract ""
	**分别登录到两个节点上，执行以下命令进行 Nginx 的安装：**  
    ```
    # 安装依赖
    yum install -y gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel

    # 解压 Nginx 到 /opt 目录下
    tar zxvf nginx-1.21.6.tar.gz -C /opt

    # 配置安装 Nginx
    cd /opt/nginx-1.21.6
    ./configure --user=nobody --group=nobody --prefix=/usr/local/nginx --with-http_gzip_static_module --with-http_ssl_module --with-stream
    make && make install
    ```

## 3 添加 Nginx 服务

!!! Abstract ""
	**在两个节点上添加 Nginx 系统服务：** 
    ```
    cat <<EOF >> /lib/systemd/system/nginx.service
    [Unit]
    Description=nginx
    After=network.target
    [Service]
    Type=forking
    ExecStart=/usr/local/nginx/sbin/nginx
    ExecReload=/usr/local/nginx/sbin/nginx -s reload
    ExecStop=/usr/local/nginx/sbin/nginx -s quit
    PrivateTmp=true
    [Install]
    WantedBy=multi-user.target
    EOF
    ```


    启动 Nginx 服务，并设置为开机自启动：
    ```shell
    systemctl start nginx
    systemctl enable nginx
    ```

## 4 配置 Nginx

!!! Abstract ""
	**修改 /usr/local/nginx/conf/nginx.conf 文件，加上 include /usr/local/nginx/conf.d/*.conf;**  

![Nginx-配置](../../img/installation/HA/nginx-配置.png){ width="900px" }

!!! Abstract ""
	**创建配置文件目录 /usr/local/nginx/conf.d，并进入到该目录下：**
    ```
    mkdir -p /usr/local/nginx/conf.d && cd $_
    ```

    创建配置文件 de.conf。
    
    **提示：** 以下配置可根据用户环境的实际情况进行调整
    ```shell
    upstream 10.1.11.137{
        ip_hash;
        server 10.1.11.5:80 fail_timeout=100s max_fails=10;
        server 10.1.11.84:80 fail_timeout=100s max_fails=10;
    }
    server {
        listen 80;
        client_max_body_size 50m;
        location / {
            proxy_pass http://10.1.11.137;
            add_header X-Upstream $upstream_addr;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_next_upstream error timeout http_404 http_500 http_502 http_503;
        }
    }
    ```

## 5 重启 Nginx 服务

!!! Abstract ""
	**执行命令重启两个节点上的 Nginx 服务：**

    ```
    systemctl restart nginx
    ```

![Nginx-状态](../../img/installation/HA/nginx-状态.png){ width="900px" }
