## 创建 Excel 数据集时，对 Excel 文件的格式有什么要求？

>Excel 中如存在合并单元格则无法导入；另外文件的第一行不能为空，第一行是标题行。
可以用格式刷保持格式统一。

## 添加excel数据集，提示"java.sql.SQLSyntaxErrorException: errCode = 2, detailMessage = The size of a row (1048587) exceed the maximal row size: 1000000"

>1. 修改配置文件: /opt/dataease/conf/fe.conf，将参数改为：max_layout_length_per_row=10000000

>2. 重启 doris-fe: docker restart doris-fe