!!! Abstract ""

    Webhook 是组织级别的内容，以便于统一管理和扩展消息推送，当前主要用于图表的阈值告警推送。
    字段说明：

    - 名称：简短描述 Webhook 的用途，便于快速理解和区分。
    - URL：DataEase 将告警信息回调给指定 URL。
    - 内容类型：指定 Webhook 数据发送的内容类型（如 application/json 或 application/x-www-form-urlencoded）。
    - Secret（可选）：如果填写 Secret，DataEase 会使用它计算加密的哈希签名，用于数据加密和验证。

![更新1](../../newimg/3.2%20新增%20Webhook%20管理1.png){ width="900px" }

!!! Abstract ""
    在具体图表的阈值告警中，可以选择需要生效的 Webhook。

![更新1](../../newimg/3.2%20新增%20Webhook%20管理2.png){ width="900px" }
