!!! Abstract ""

    Webhook 管理位于【组织管理中心】下。Webhook 是组织级别的内容，以便于统一管理和扩展消息推送，当前主要用于图表的阈值告警推送。
    字段说明：

    - 名称：简短描述 Webhook 的用途，便于快速理解和区分。
    - URL：DataEase 将告警信息回调给指定 URL。
    - 内容类型：指定 Webhook 请求 Body 的发送格式（如 application/json 或 application/x-www-form-urlencoded）。
    - Secret（可选）：如果填写 Secret，DataEase 会使用它计算加密的哈希签名，用于数据加密和验证。
    - 消息模板：支持自定义 Webhook 请求 Body 内容，用于适配企业微信、钉钉、飞书或其他第三方系统对请求体格式的要求。可用占位符：`${title}`、`${content}`、`${messageId}`，发送告警时系统会自动替换为对应的告警标题、告警内容和消息 ID。

![更新1](../newimg/3.2%20新增%20Webhook%20管理1.png){ width="900px" }

## 1 消息模板示例

!!! Abstract ""

    消息模板用于自定义 Webhook 请求 Body。以下示例以文本消息为例，仅供参考。

    **注意：**

    - 第三方平台机器人消息格式可能随平台更新而变化，实际配置请以对应平台官方文档为准。
    - 配置以下示例时，内容类型请选择 `application/json`。

### 1.1 企业微信

!!! Abstract ""

    企业微信文本消息模板可参考如下格式，官方说明请参考 [企业微信群机器人配置说明](https://developer.work.weixin.qq.com/document/path/91770){ target="_blank" rel="noopener" }。

```json
{
  "msgtype": "text",
  "text": {
    "content": "${title}\n${content}\n消息ID：${messageId}"
  }
}
```

### 1.2 钉钉

!!! Abstract ""

    钉钉文本消息模板可参考如下格式，官方说明请参考 [钉钉机器人消息类型](https://open.dingtalk.com/document/development/robot-message-type){ target="_blank" rel="noopener" }。

```json
{
  "msgtype": "text",
  "text": {
    "content": "${title}\n${content}\n消息ID：${messageId}"
  }
}
```

### 1.3 飞书

!!! Abstract ""

    飞书文本消息模板可参考如下格式，官方说明请参考 [飞书自定义机器人使用指南](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot?lang=zh-CN){ target="_blank" rel="noopener" }。

```json
{
  "msg_type": "text",
  "content": {
    "text": "${title}\n${content}\n消息ID：${messageId}"
  }
}
```

## 2 阈值告警中选择 Webhook

!!! Abstract ""
    在具体图表的阈值告警中，可以选择需要生效的 Webhook。

![更新1](../newimg/3.2%20新增%20Webhook%20管理2.png){ width="900px" }
