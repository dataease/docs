
!!! Abstract ""
    浏览器的同源策略（Same-Origin Policy）规定，只有当协议（protocol）、域名（domain）和端口（port）完全相同的情况下，网页才能自由访问另一个源的资源。如果请求的资源与当前网页的源不同，为跨域请求。具体如下：

    1. 不同的协议
    ```
    示例：从 http://example.com 请求 https://example.com。
    原因：即使主机名和端口相同，协议不同也算跨域。
    ```

    2. 不同的端口
    ```
    示例：从 http://example.com:3000 请求 http://example.com:4000。
    原因：端口不同，即使协议和主机名相同。
    ```

    3. 不同的顶级域名
    ```
    示例：从 http://example.com 请求 http://anotherexample.com。
    原因：顶级域名不同。
    ```

    4. 子域名和顶级域名
    ```
    示例：从 http://sub.example.com 请求 http://example.com。
    原因：子域名和顶级域名不同，也算跨域。
    ```

    5. 子域名和子域名
    ```
    示例：从 http://sub1.example.com 请求 http://sub2.example.com。
    原因：子域名和子域名不同，也算跨域。
    ```