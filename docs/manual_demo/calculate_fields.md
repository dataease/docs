## 计算字段概述

!!! Abstract ""
    【计算字段】可在当前数据集字段的基础上通过公式或函数生成新的字段，例如需要新的字段为数据集中原有两个字段的和（字段 A+字段 B）。  
![image.png](../img/calculate_fields/新建计算字段-选择字段.png){width="900px"}
![image.png](../img/calculate_fields/新建计算字段-求和.png){width="900px"}

!!! Abstract ""
    **使用数据集对应数据库类型所支持的函数，语法同对应数据库；**  
    如日期格式化：  

    - MySQL 使用 DATE_FORMAT(date,format)；
    - Oracle 使用 TO_DATE(X,[,fmt])；
    - 非直连模式数据集，使用 Doris 数据库函数，可参考 Doris 官网 http://doris.apache.org/master/zh-CN/。

<table style="foot_color:rgba(0, 0, 0, 0.87)">
	<tr>
		<td bgcolor="#3779d9" align="middle" style="font-weight:bold;color: white;width: 150px">
			函数模块
		</td>
		<td bgcolor="#3779d9" align="middle" style="font-weight:bold;color: white;width: 170px">
			函数简介
		</td>
		<td bgcolor="#3779d9" align="middle" style="font-weight:bold;color: white;width: 750px"> 
			函数描述
		</td>
	</tr>
	<tr>
		<td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			函数入门
		</td>
		<td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			函数语法介绍
		</td>
		<td style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			函数和参数
		</td>
	</tr>
	<tr>
		<td rowspan="6" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			字符串处理
		</td>
		<td rowspan="3" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			字符处理
		</td>
		<td>
			<a href="#字符串空格去除" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;hover{text-decoration:underline}">字符串空格去除</a>
		</td>
    </tr>
    <tr>
        <td>
			<a href="#大小写转换" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">大小写转换</a>
		</td>
    </tr>
    <tr>
        <td>
			<a href="#字符反转" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">字符反转</a> 
		</td>
    </tr>
    <tr>
		<td rowspan="3" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
            截取/拼接字符
		</td>
		<td>
			<a href="#截取字符" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">截取字符</a> 
		</td>
	</tr>
    <tr>
        <td>
			<a href="#替换字符" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">替换字符</a>
		</td>
    </tr>
    <tr>
        <td>
			<a href="#拼接字符" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">拼接字符</a>
		</td>
    </tr>
	<tr>
		<td rowspan="2" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			日期函数
		</td>
		<td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			日期数据获取
		</td>
		<td>
			<a href="#返回当前时间函数" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">返回当前时间函数</a>
		</td>
	</tr>
	<tr>
		<td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			日期数据转换
		</td>
		<td>
			<a href="#日期转换" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">日期转换</a>
		</td>
	</tr>
	<tr>
		<td rowspan="5" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			数据运算
		</td>
		<td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			常量
		</td>
		<td>
			<a href="#PI" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">PI</a>
		</td>
	</tr>
    <tr> 
        <td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			计算函数
		</td>
		<td>
			<a href="#绝对值/对数/乘方/余数" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">绝对值，对数，乘方和余数</a>
		</td>
    </tr>
    <tr> 
        <td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			三角函数
		</td>
		<td>
			<a href="#三角函数" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">三角函数</a>
		</td>
    </tr>
    <tr> 
        <td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			取整
		</td>
		<td>
			<a href="#取整" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">向下取整，向上取整和就近取整</a>
		</td>
    </tr>
    <tr> 
        <td rowspan="1" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">
			条件表达式函数
		</td>
		<td>
			<a href="#巧用IF和CASE-WHEN函数" style="color:rgba(0, 0, 0, 0.87);text-decoration:none;">IF和CASE-WHEN函数</a> 
		</td>
    </tr>
</table>





# 函数入门

!!! Abstract ""
    在计算字段管理中。点击【新建计算字段】按钮会有弹窗，需要依次输入新建计算字段的"字段名"、"数据类型"、"字段类型”和"字段表达式"完成新建。
![image.png](../img/calculate_fields/函数入门.png){width="900px"}

# 函数语法介绍
## <a id="函数和参数" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">函数和参数</a>

!!! Abstract ""
    图中字符表达式是由函数和参数构成。函数的用法可通过鼠标悬浮在函数上查看，函数之间可以组合使用。函数参数的数字类型一般用 x 表示，字符类型用 str、s 表示，条件表达式用 expr 表示。

![image.png](../img/calculate_fields/函数和参数.jpg){width="900px"}

# 字符处理
## <a id="字符串空格去除" style="color:hsla(0,0%,0%,0.82);text-decoration:none;">字符串空格去除</a>
### 1.去除左边空格函数

!!! Abstract ""
    LTRIM(s)：返回字符串 s，其左边所有空格被删除，其中 s 需根据需要选择维度或指标中的一个字段，下图展示了用指标中的"用户 id" 作为参数 s。

![image.png](../img/calculate_fields/去除左边空格RTRIM.png){width="900px"}
### 2.去除右边空格函数

!!! Abstract ""
    RTRIM(s)：返回字符串 s，其右边所有空格被删除，其中 s 需根据需要选择维度或指标中的一个字段。

![image.png](../img/calculate_fields/去除右边空格RTRIM.png){width="900px"}

### 3.去除俩边空格函数

!!! Abstract ""
    TRIM(s)：返回字符串 s 删除了两边空格之后的字符串，其中 s 需根据需要选择维度或指标中的一个字段。

![image.png](../img/calculate_fields/去除俩边空格TRIM.png){width="900px"}

## <a id="大小写转换" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">大小写转换函数</a>

!!! Abstract ""
    LOWER(str)：将 str 中的字母全部转换成小写，其中 str 需根据需要选择维度或指标中的一个字段。

![image.png](../img/calculate_fields/转小写转换.png){width="900px"}

!!! Abstract ""
    UPPER(str)：将字符串中的字母全部转换成大写，其中 str 需根据需要选择维度或指标中的一个字段。注意：str 是字符串类型。

![image.png](../img/calculate_fields/转大写转换.png){width="900px"}

## <a id="字符反转" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">字符反转函数</a>

!!! Abstract ""
    REVERSE(s)：将字符串 s 反转，其中 str 需根据需要选择维度或指标中的一个字段。注意：str 是字符串类型。
    
    **提示：SQL数据集支持此函数。**

![image.png](../img/calculate_fields/字符反转.png){width="900px"}

## <a id="截取字符" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">截取字符函数</a>

!!! Abstract ""
    SUBSTRING(s,n,len)：获取从字符串 s 中的第 n 个位置开始长度为 len 的字符串，其中 s 需根据需要选择维度或指标中的一个字段。注意：s 是字符串类型，n 和 len为正整数。


![image.png](../img/calculate_fields/截取字符.png){width="900px"}

!!! Abstract ""
    LEFT(s,n)：返回字符串 s 从最左边开始的 n 个字符，其中 s 需根据需要选择维度或指标中的一个字段。注意：s 是字符串类型，n 是正整数。

    **提示：SQL数据集支持此函数。**

![image.png](../img/calculate_fields/LEFT(s,n).png){width="900px"}
## <a id="替换字符"style="color:hsla(0,0%,0%,0.62);text-decoration:none;">替换字符函数</a>

!!! Abstract ""
    REPLACE(s,s1,s2)：返回一个字符串，用字符串 s2 替代字符串 s 中所有的字符串 s1，其中 s 需根据需要选择维度或指标中的一个字段。注意：s、s1、s2 是字符串类型。

![image.png](../img/calculate_fields/REPLACE(s,s1,s2).png){width="900px"}

!!! Abstract ""
    INSERT(s1,x,len,s2)：返回字符串 s1，其子字符串起始于位置 x，被字符串 s2 取代 len 个字符。注意：s1 和 s2 是字符串类型，x 和 len 为正整数。

![image.png](../img/calculate_fields/INSERT(s1,x,len,s2).png){width="900px"}

!!! Abstract ""
    REPEAT(s,n)：返回一个由重复字符串 s 组成的字符串，字符串s的数目等于 n。其中 s 需根据需要选择维度或指标中的一个字段。注意：s 是字符串类型，n 为正整数。
    
    **提示：SQL数据集支持此函数。**

![image.png](../img/calculate_fields/REPEAT(s,n).png){width="900px"}
## <a id="拼接字符" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">拼接字符函数</a>

!!! Abstract ""
    数据库类型数据集特有SPACE(n)：返回一个由 n 个空格组成的字符串，如下图展示顶一个计算字段是有 8 个空格的。
    
    **提示：此函数可用于对字符串拼接空格使用。**

![image.png](../img/calculate_fields/拼接空格字符.png){width="900px"}

# 时间函数
## 返回时间函数
### <a id="返回当前时间函数" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">1.返回当前时间函数</a>

!!! Abstract ""
    NOW()：返回当前日期和时间值，格式为 "YYYY_MM-DD HH:MM:SS" 或 "YYYYMMDDHHMMSS"，具体格式根据函数用在字符串或数字语境中而定，不带参数的函数直接返回即可。具体步骤按照下图所示。

![image.png](../img/calculate_fields/NOW().png){width="900px"}

!!! Abstract ""
    SYSDATE()：返回当前日期和时间值，格式为 "YYYY_MM-DD HH:MM:SS" 或 "YYYYMMDDHHMMSS"，具体格式根据函数用在字符串或数字语境中而定。具体步骤按照下图所示。

![image.png](../img/calculate_fields/SYSDATE().png){width="900px"}

!!! Abstract ""
LOCALTIME()：返回当前日期和时间值，格式为 "YYYY_MM-DD HH:MM:SS" 或 "YYYYMMDDHHMMSS"，具体格式根据函数用在字符串或数字语境中而定。具体步骤按照下图所示。

![image.png](../img/calculate_fields/LOCALTIME().png){width="900px"}

!!! Abstract ""
CURDATE()：将当前日期按照 "YYYY-MM-DD" 或者 "YYYYMMDD" 格式的值返回，具体格式根据函数用在字符串或是数字语境中而定。具体步骤按照下图所示。

![image.png](../img/calculate_fields/CURDATE().png){width="900px"}


!!! Abstract ""
CURRENT_DATE()：将当前日期按照 "YYYY-MM-DD" 或者 "YYYYMMDD" 格式的值返回，具体格式根据函数用在字符串或是数字语境中而定。具体步骤按照下图所示。

![image.png](../img/calculate_fields/CURRENT_DATE().png){width="900px"}


!!! Abstract ""
    UNIX_TIMESTAMP()：返回一个格林尼治标准时间 1970-01-01 00:00:00 到现在的秒数。具体步骤按照下图所示。

![image.png](../img/calculate_fields/UNIX_TIMESTAMP().png){width="900px"}


!!! Abstract ""
    UNIX_TIMESTAMP(date)：返回一个格林尼治标准时间 1970-01-01 00:00:00 到指定时间 date 的秒数。其中 date 需根据需要选择维度或指标中的一个字段。注意：date 是时间类型。具体步骤按照下图所示。

![image.png](../img/calculate_fields/UNIX_TIMESTAMP(date).png){width="900px"}

### <a id="日期转化" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">2.日期转化函数</a>
!!! Abstract ""
    可以对日期数据进行格式的转换。
    
    **提示：根据不同的数据集类型，支持的新建计算字段函数也不一致，使用数据集对应数据库类型所支持的函数，语法同对应数据库 如日期格式化：MySQL 使用 DATE_FORMAT(date,format)；Oracle 使用 TO_DATE(X,[,fmt])
    非直连模式数据集，使用 Doris 数据库函数，可参考 Doris 官网 http://doris.apache.org/master/zh-CN/。**

# 数字运算
## 常量
### <a id="PI" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">1.PI()函数</a>

!!! Abstract ""
    PI()：返回圆周率 π，默认显示 6 位小数。

![image.png](../img/calculate_fields/PI().png){width="900px"}

## 计算函数

### <a id="绝对值/对数/乘方/余数" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">1.绝对值函数</a>

!!! Abstract ""
    ABS(x)：返回 x 的绝对值。其中 x 需根据需要选择维度或指标中的一个字段或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/ABS(x).png){width="900px"}

### 2.对数

!!! Abstract ""
    LOG(x)：返回 x 的自然对数，x 相对于基数 e 的对数。其中 x 需根据需要选择维度或指标中的一个字段或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/LOG(x).png){width="900px"}

### 3.乘方


!!! Abstract ""
    POW(x,y)：x 的 y 次方 ，返回 x 的 y 次乘方的值。其中 x 和 y 需根据需要选择维度或指标中的一个字段或指定数字或指定数字。注意：x和y 是数字类型。

![image.png](../img/calculate_fields/POW(x,y).png){width="900px"}

!!! Abstract ""
    EXP(x)：返回 e 的 x 乘方后的值。其中 x 需根据需要选择维度或指标中的一个字段或指定数字或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/EXP(x).png){width="900px"}

### 4.余数
!!! Abstract ""
    MOD(x,y)：返回 x 被 y 除后的余数。其中 x，y 可需根据需要选择维度或指标中的一个字段或指定数字。注意：x，y 是数字类型。

![image.png](../img/calculate_fields/MOD(x,y).png){width="900px"}

## <a id="三角函数" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">三角函数</a>

!!! Abstract ""
    COS(x)：返回 x 的余弦，其中 x 为给定的弧度值。对应的还有其他三角函数，比如 SIN(x)。其中 x 需根据需要选择维度或指标中的一个字段或指定数字或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/COS(x).png){width="900px"}

## 取整
### 1.向上取整

!!! Abstract ""
    CEIL(x) ：返回不小于 x 的最小整数。其中 x 需根据需要选择维度或指标中的一个字段或指定数字或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/CEIL(x).png){width="900px"}

### 2.向下取整

!!! Abstract ""
    数据库类型的数据集，FLOOR(x) ：返回不大于 x 的最大整数。其中 x 需根据需要选择维度或指标中的一个字段或指定数字或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/FLOOR(x).png){width="900px"}

### 3.就近取整

!!! Abstract ""
    ROUND(x) ：返回离 x 最近的整数。其中 x 需根据需要选择维度或指标中的一个字段或指定数字或指定数字。注意：x 是数字类型。

![image.png](../img/calculate_fields/ROUND(x).png){width="900px"}

## <a id="巧用IF和CASE-WHEN函数" style="color:hsla(0,0%,0%,0.62);text-decoration:none;">IF和CASE-WHEN函数</a>

### 1.IF函数
!!! Abstract ""
    在进行数据分析时，用户经常会使用到 IF 判断条件，来对已有的数据进行数据清洗和处理。
    在IF函数中，如果 expr 是 TRUE 则返回 v1，否则返回 v2。注意：expr 是表达式，v1 和 v2 是确定的返回值。

![image.png](../img/calculate_fields/IF函数-1.png){width="900px"}

![image.png](../img/calculate_fields/IF函数-2.png){width="900px"}
### 2.CASE-WHEN函数

!!! Abstract ""
    CASE-WHEN 函数和 IF 的用法类似，区别是对于条件表达式的返回值，CASE-WHEN更加细化（除了能对 v1 和 v2 俩个返回值有不同的结果外，还能对第三种返回值有 rn 的结果），表达式之间也支持嵌套使用。
    注意：expr 是表达式，v1 和 v2 是确定的返回值。

![image.png](../img/calculate_fields/CASE-WHEN.png){width="900px"}


