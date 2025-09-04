
!!! Abstract ""
    单点协议支持目前支持 OIDC、CAS ，使用方式如下：

## 1 OIDC
!!! Abstract ""
    DataEase 企业版支持 OIDC 协议，【系统设置】-> 【认证设置】-> 【OIDC】中进行设置。

    点击 OIDC 编辑。即可设置 OIDC，填写完相关信息后，测试连接显示成功，即配置成功。
![5.1 单点登录（1）.png](../img/embedded/5.1 单点登录（1）.png){ width="900px" }

!!! Abstract ""
    - Client ID：客户端 id。
    - Client Secret：客户端密码。
    - Discovery：OIDC 发现服务。
    - Realm：用于身份验证的领域，此处可自定义。
    - Scope：返回的有关经过身份验证的用户的信息，也称为[声明](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)，可通过发现服务获取，多个参数使用英文逗号分开。
    - Use Pkce：访问令牌。设置为 true 时，在请求标头中设置访问令牌。
    - Redirect Uri：重定向回的 URL。
![5.1 单点登录（2）.png](../img/embedded/5.1 单点登录（2）.png){ width="900px" }

## 2 CAS
!!! Abstract ""
    DataEase 企业版支持 CAS 协议，【系统设置】-> 【认证设置】-> 【CAS】中进行设置。

    点击 CAS 编辑。即可设置 CAS，填写完相关信息后，测试连接显示成功，即配置成功。
![5.1 单点登录（3）.png](../img/embedded/5.1 单点登录（3）.png){ width="900px" }

!!! Abstract ""
    - IdpUri：IdP 的 URI。
    - 回调域名：登录或注销后，回调的重定向 uri。
![5.1 单点登录（4）.png](../img/embedded/5.1 单点登录（4）.png){ width="900px" }

## 3 LDAP
!!! Abstract ""
    DataEase 企业版支持 LDAP 协议，【系统设置】-> 【认证设置】-> 【LDAP】中进行设置。

    点击 LDAP 编辑，即可设置 LDAP，填写完相关信息后，测试连接显示成功，即配置成功。
![5.1 单点登录（5）.png](../img/embedded/5.1 单点登录（5）.png){ width="900px" }

!!! Abstract ""
    - DAP地址： LDAP 服务器的地址。
    - 绑定DN：用于认证 LDAP 服务器的身份标识，即登录到 LDAP 服务器时使用的用户身份。
    - 密码：与绑定 DN 配对使用的密码，用于验证绑定 DN 的身份。
    - 用户OU：OU 是组织单元（Organizational Unit）的缩写，用来表示 LDAP 树中存放用户的特定路径（子树或分支）。
    - 用户过滤器：这是一个 LDAP 查询字符串，用于筛选特定的用户对象。可以用来查找满足条件的用户。
    - LDAP属性映射：将 LDAP 服务器中的属性对应到 DataEase 中的字段，account、name、email 为 DataEase 用户信息字段。

## 4 OAuth2
![5.1 单点登录（6）.png](../img/embedded/5.1 单点登录（6）.png){ width="900px" }
!!! Abstract ""
    - 授权端地址：用户进行授权时访问的 URL，通常用于获取授权码（Authorization Code）。
    - Token 端地址：交换授权码（Authorization Code）或凭证（Client Credentials）以获取访问令牌（Access Token）。
    - 用户信息获取地址：授权服务器提供的 API 端点，用于在获得访问令牌后获取用户的个人信息（如用户名、邮箱等）。
    - 连接范围（scope）：定义应用程序可以访问的资源范围，如用户信息、电子邮件、角色等。
    - 客户端 ：OAuth2 应用的唯一标识。
    - 客户端密钥：与 Client ID 配合使用，确保应用身份验证的安全性。
    - 回调地址：OAuth2 认证完成后，重定向回应用的地址。
    - 字段映射：将 OAuth2 服务器中的属性对应到 DataEase 中的字段，account、name、email 为 DataEase 用户信息字段。

