## 1 ECharts 图库

!!! Abstract ""
    ECharts 属于 Apache 基金会下，一个基于 JavaScript 的开源可视化图表库，提供了功能强大的图表和可视化库。

### 1.1 表格

!!! Abstract ""
    表格是数据的详情罗列，能看到明细信息，表格包含汇总表和明细表。

!!! Abstract ""
    汇总表

    ![echarts汇总表](../../img/view_generation/view_gallery/ECharts/echarts汇总表.png){ width="900px" }

!!! Abstract ""
    明细表

    ![echarts明细表](../../img/view_generation/view_gallery/ECharts/echarts明细表.png){ width="900px" }

### 1.2 指标卡

!!! Abstract ""
    通过文字、数字和符号的合理排版，对数据进行一目了然的展示。指标卡由看板标签和看板指标组成，标签由数据的维度决定，指标由数据的度量决定。

!!! Abstract ""

    ![echarts指标卡](../../img/view_generation/view_gallery/ECharts/echarts指标卡.png){ width="900px" }
 
    **注意：** 指标卡只支持数值类型的数据汇总。
    
### 1.3 文本卡

!!! Abstract ""
    展示文本字段的实际文字可使用文本卡，文本卡可展示该字段原本的内容、时间、文本信息等。  
    **提示：** 文本卡拖入的字段必须是“维度”类型。

!!! Abstract ""

    ![echarts文本卡](../../img/view_generation/view_gallery/ECharts/echarts文本卡.png){ width="900px" }

### 1.4 柱状图

!!! Abstract ""
    柱状图又称条形图，是一种通过柱形的高度（横向的情况下则是宽度）来表现数据大小的一种常用图表类型，柱状图包括基础柱状图、堆叠柱状图、横向柱状图和横向堆叠柱状图。  
    **注意：** 柱状图当前同一维度只能显示一种颜色。

!!! Abstract ""
    基础柱状图

    ![echarts基础柱状图](../../img/view_generation/view_gallery/ECharts/echarts基础柱状图.png){ width="900px" }

!!! Abstract "" 
    堆叠柱状图是柱状图的变形，堆叠柱状图将每个柱子进行颜色分割，用于显示同系列下各个数据的大小情况，它不仅可以比较不同维度间总数的差别，还可以显示同类型下子类别的构成以及各数据的大小情况。

    ![echarts堆叠柱状图](../../img/view_generation/view_gallery/ECharts/echarts堆叠柱状图.png){ width="900px" }

!!! Abstract ""
    横向柱状图

    ![echarts横向柱状图](../../img/view_generation/view_gallery/ECharts/echarts横向柱状图.png){ width="900px" }

!!! Abstract ""
    横向堆叠柱状图如同字面意思，是堆叠柱状图的横向展示。

    ![echarts横向堆叠柱状图](../../img/view_generation/view_gallery/ECharts/echarts横向堆叠柱状图.png){ width="900px" }

### 1.5 折线图

!!! Abstract ""
	折线图是用折线将各个数据点标志连接起来的图表，可用于直角坐标系和极坐标系上。

!!! Abstract ""
    基础折线图

    ![echarts基础折线图](../../img/view_generation/view_gallery/ECharts/echarts基础折线图.png){ width="900px" }

!!! Abstract ""
    堆叠折线图在折线图的基础上形成，折线与自变量坐标轴之间的区域使用颜色填充，堆叠折线图每一个数据的起点都是基于前一个数据，最终代表的是所有数据的和，即累计值。

    ![echarts堆叠折现图](../../img/view_generation/view_gallery/ECharts/echarts堆叠折线图.png){ width="900px" }

### 1.6 组合图

!!! Abstract ""
    组合图由基础柱状图，基础折线图和散点图相互搭配成。

!!! Abstract ""

    ![echarts组合图](../../img/view_generation/view_gallery/ECharts/echarts组合图.png){ width="900px" }

### 1.7 散点图

!!! Abstract ""
    散点图又称 XY 散点图，将数据以点的形式展现，以显示变量间的相互关系或者影响程度，点的位置由变量的数值决定。

!!! Abstract ""
    基础散点图

    ![](../../img/view_generation/view_gallery/ECharts/echarts基础散点图.png){ width="900px" }

!!! Abstract ""
    气泡图

    ![echarts散点图](../../img/view_generation/view_gallery/ECharts/echarts散点图.png){ width="900px" }

### 1.8 雷达图

!!! Abstract ""
    雷达图又称蜘蛛网图，将多个维度的数据量映射到起始于同一个圆心的坐标轴上，结束于圆周边缘，然后将同一组的点使用线连接起来。

!!! Abstract ""

    ![echarts雷达图](../../img/view_generation/view_gallery/ECharts/echarts雷达图.png){ width="900px" }

### 1.9 仪表盘

!!! Abstract ""
    仪表盘像一个钟表或者可读盘，有刻度和指针，其中刻度表示度量，指针表示维度，指针角度表示数值，指针指向当前数值。

!!! Abstract ""

    ![echarts仪表盘](../../img/view_generation/view_gallery/ECharts/echarts仪表盘.png){ width="900px" }

### 1.10 饼图

!!! Abstract ""
    饼图以饼状图形显示一个数据系列中各项的大小与各项总和的比例，也称作扇形统计图。

    ![echarts基础饼图](../../img/view_generation/view_gallery/ECharts/echarts基础饼图.png){ width="900px" }

### 1.11 环形饼图

!!! Abstract ""
    环形图（环形饼图）

    ![echarts环形饼图](../../img/view_generation/view_gallery/ECharts/echarts环形饼图.png){ width="900px" }

### 1.12 南丁格尔玫瑰图

!!! Abstract ""
    南丁格尔玫瑰图又称鸡冠花图、极坐标区域图，是由弗罗伦斯·南丁格尔所发明，其实是一种圆形的直方图，以圆弧的半径长短表示数据的大小。

!!! Abstract ""

    ![echarts南丁格尔玫瑰图](../../img/view_generation/view_gallery/ECharts/echarts南丁格尔玫瑰图.png){ width="900px" }

### 1.13 玫瑰环形图

!!! Abstract ""

    ![echarts玫瑰环形图](../../img/view_generation/view_gallery/ECharts/echarts玫瑰环形图.png){ width="900px" }

### 1.14 漏斗图

!!! Abstract ""
    漏斗图由多个梯形从上而下叠加而成，从上到下的项有逻辑上的顺序关系，梯形面积表示某个业务量与上一个环节之间的差异。

!!! Abstract ""

    ![echarts漏斗图](../../img/view_generation/view_gallery/ECharts/echarts漏斗图.png){ width="900px" }

### 1.15 矩形树图

!!! Abstract ""
    矩形树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，便于突出展现出『树』的各层级中重要的节点。

!!! Abstract ""

    ![echarts矩形树图](../../img/view_generation/view_gallery/ECharts/echarts矩形树图.png){ width="900px" }

### 1.16 地图

!!! Abstract ""
    普通地图：用颜色的深浅来展示区域范围的数值大小。

    ![普通地图](../../img/view_generation/view_gallery/ECharts/echarts普通地图.png){ width="900px" }

    **提示：** v1.12.0 版本，地图组件 Low 与 Higt 颜色跟随主题变化，深色主题下为白色，浅色主题下为黑色。

!!! Abstract ""
    气泡地图：用气泡的大小来展示区域范围的数值大小。

    ![气泡地图](../../img/view_generation/view_gallery/ECharts/echarts气泡地图.png){ width="900px" }

!!! Abstract ""
    支持展示世界地图，【中华人民共和国】为之前默认的地图，同时自定义地图文件可在【系统参数】的【地图设置】中添加。

    ![世界地图](../../img/view_generation/view_gallery/ECharts/echarts世界地图.png){ width="900px" }

!!! Abstract ""
    支持通过添加经纬度在地图上面打标记。

    ![经纬度打标记](../../img/view_generation/view_gallery/ECharts/经纬度打标记.png){ width="900px" }

!!! Abstract ""
    支持在原有标记中进行特殊标记的功能。  
    功能详解：

	- 【序号 1】选择特殊标记条件的字段名称；
	- 【序号 2】选择特殊标记条件对应的值或者值范围，方式可选择等于、包含、不包含、结尾是以及开头是；
	- 【序号 3】点击该处可以展开 ④⑤⑥；
	- 【序号 4】选择特殊标记的颜色；
	- 【序号 5】选择特殊标记的图形，图形的类型有趋势、状态、排名、位置以及天气；
	- 【序号 6】设置完 ③ 的内容之后需要点击 ⑥ 进行设置保存；
    - 【序号 7】点击该处可以新增一行特殊标记条件值或者值范围。

    ![标记样式](../../img/view_generation/view_gallery/ECharts/标记样式.png){ width="900px" }

## 2 AntV 图库

!!! Abstract ""
    AntV 图库是蚂蚁集团可视化团队下一款开源的图表库。

### 2.1 表格

!!! Abstract ""
    表格是数据的详情罗列，能看到明细信息，AntV 图库表格包含汇总表、明细表和透视表。  
    AntV 的表格支持更详细的表格配置，支持表头、表格对齐（左对齐、居中、右对齐），支持列宽调整，比如自适应和自定义。

!!! Abstract ""
    明细表
    
    ![antv明细表格](../../img/view_generation/view_gallery/AntV/antv明细表.png){ width="900px" }

!!! Abstract ""
    汇总表

    ![antv汇总表格](../../img/view_generation/view_gallery/AntV/antv汇总表.png){ width="900px" }

!!! Abstract ""
    透视表

    ![antv透视表](../../img/view_generation/view_gallery/AntV/antv透视表.png){ width="900px" }

!!! Abstract ""
    **提示：** 透视表支持小计合计，小计会针对每层维度进行计算，总计对行或列全部数据进行计算。

    ![antv透视表_小计合计](../../img/view_generation/view_gallery/AntV/antv透视表_小计合计.png){ width="900px" }  
    ![antv透视表_小计合计设置](../../img/view_generation/view_gallery/AntV/antv透视表_小计合计设置.png){ width="900px" }

### 2.2 指标卡

!!! Abstract ""
    通过文字、数字和符号的合理排版，对数据进行一目了然的展示。指标卡由看板标签和看板指标组成，标签由数据的维度决定，指标由数据的度量决定。

!!! Abstract ""

    ![antv指标卡](../../img/view_generation/view_gallery/AntV/antv指标卡.png){ width="900px" }
 
    **注意：** 指标卡只支持数值类型的数据汇总。

### 2.3 文本卡

!!! Abstract ""
    展示文本字段的实际文字可使用文本卡，文本卡可展示该字段原本的内容、时间、文本信息等。  
    **提示：** 文本卡拖入的字段必须是“维度”类型。

!!! Abstract ""
    
    ![antv](../../img/view_generation/view_gallery/AntV/antv文本卡.png){ width="900px" }

### 2.4 柱状图

!!! Abstract ""
    柱状图又称条形图，是一种通过柱形的高度（横向的情况下则是宽度）来表现数据大小的一种常用图表类型，柱状图包括基础柱状图、堆叠柱状图、横向柱状图和横向堆叠柱状图。

!!! Abstract ""
    基础柱状图

    ![antv基础柱状图](../../img/view_generation/view_gallery/AntV/antv基础柱状图.png){ width="900px" }

!!! Abstract ""
    堆叠柱状图是柱状图的变形，堆叠柱状图将每个柱子进行颜色分割，用于显示同系列下各个数据的大小情况，它不仅可以比较不同维度间总数的差别，还可以显示同类型下子类别的构成以及各数据的大小情况。

    ![antv堆叠柱状图](../../img/view_generation/view_gallery/AntV/antv堆叠柱状图.png){ width="900px" }

!!! Abstract ""
    横向柱状图

    ![antv横向柱状图](../../img/view_generation/view_gallery/AntV/antv横向柱状图.png){ width="900px" }

!!! Abstract ""
    横向堆叠柱状图如同字面意思，是堆叠柱状图的横向展示。

    ![antv横向堆叠柱状图](../../img/view_generation/view_gallery/AntV/antv横向堆叠柱状图.png){ width="900px" }

### 2.5 分组柱状图

!!! Abstract ""
    分组柱状图，又叫聚合柱状图，可在同一个轴上显示各个分类下不同的分组。

    ![antv分组柱状图](../../img/view_generation/view_gallery/AntV/antv分组柱状图.png){ width="900px" }

### 2.6 百分比柱状图

!!! Abstract ""
    百分比柱状图根据数据类目的多个系列自动显示其百分比占比情况，能够更加清晰智能地展示各数据占比值的差异。

![antv百分比柱状图](../../img/view_generation/view_gallery/AntV/antv百分比柱状图.png){ width="900px" }

### 2.7 横向百分比柱状图

![antv横向百分比柱状图](../../img/view_generation/view_gallery/AntV/antv横向百分比柱状图.png){ width="900px" }、

### 2.8 分组堆叠柱状图

!!! Abstract ""
    分组堆叠柱状图可对比同一个分组内部不同分类的数据大小或占比，也可以对比不同分组内相同分类的数据大小，也可以对比分组的总量。

![antv分组堆叠柱状图](../../img/view_generation/view_gallery/AntV/antv分组堆叠柱状图.png){ width="900px" }

### 2.9  区间条形图

!!! Abstract ""
    区间条形图适合展示各类别数据的分布和比较。与普通条形图不同的是，区间条形图强调的是数值范围而不是单一数值点。这在展示持续时间或不同对象之间的数值范围比较时特别有用。

![antv分组堆叠柱状图](../../img/view_generation/view_gallery/AntV/antv区间条形图.png){ width="900px" }

### 2.10 基础面积图

!!! Abstract ""
    面积图又叫区域图，它是在折线图的基础之上形成的，它将折线图中折线与自变量坐标轴之间的区域使用颜色或者纹理填充，这样一个填充区域我们叫做面积，颜色的填充可以更好的突出趋势信息。

    ![antv基础面积图](../../img/view_generation/view_gallery/AntV/antv基础面积图.png){ width="900px" }

### 2.11 折线图

!!! Abstract ""
    折线图是用折线将各个数据点标志连接起来的图表，可用于直角坐标系和极坐标系上。

!!! Abstract ""
    基础折线图

    ![antv基础折线图](../../img/view_generation/view_gallery/AntV/antv基础折线图.png){ width="900px" }

!!! Abstract ""
    堆叠折线图在折线图的基础上形成，折线与自变量坐标轴之间的区域使用颜色填充，堆叠折线图每一个数据的起点都是基于前一个数据，最终代表的是所有数据的和，即累计值。

    ![antv堆叠折线图](../../img/view_generation/view_gallery/AntV/antv堆叠折线图.png){ width="900px" }

### 2.12 散点图

!!! Abstract ""
    散点图又称 XY 散点图，将数据以点的形式展现，以显示变量间的相互关系或者影响程度，点的位置由变量的数值决定。

!!! Abstract ""
    基础散点图

    ![antv散点图](../../img/view_generation/view_gallery/AntV/antv散点图.png){ width="900px" }

!!! Abstract ""
    气泡图

    ![antv气泡图](../../img/view_generation/view_gallery/AntV/antv气泡图.png){ width="900px" }

### 2.13 雷达图

!!! Abstract ""
    雷达图又称蜘蛛网图，将多个维度的数据量映射到起始于同一个圆心的坐标轴上，结束于圆周边缘，然后将同一组的点使用线连接起来。

!!! Abstract ""

    ![antv雷达图](../../img/view_generation/view_gallery/AntV/antv雷达图.png){ width="900px" }

### 2.14 仪表盘

!!! Abstract ""
    像一个钟表或者可读盘，有刻度和指针，其中刻度表示度量，指针表示维度，指针角度表示数值，指针指向当前数值。

!!! Abstract ""

    ![antv仪表盘](../../img/view_generation/view_gallery/AntV/antv仪表盘.png){ width="900px" }

### 2.15 饼图

!!! Abstract ""
    饼图以饼状图形显示一个数据系列中各项的大小与各项总和的比例，也称作扇形统计图。

    ![antv基础饼图](../../img/view_generation/view_gallery/AntV/antv基础饼图.png){ width="900px" }

### 2.16 环形图

!!! Abstract ""
    环形图（环形饼图）

    ![antv环形饼图](../../img/view_generation/view_gallery/AntV/antv环形饼图.png){ width="900px" }

### 2.17 南丁格尔玫瑰

!!! Abstract ""
    南丁格尔玫瑰图又称鸡冠花图、极坐标区域图，是由弗罗伦斯·南丁格尔所发明，其实是一种圆形的直方图，以圆弧的半径长短表示数据的大小。

!!! Abstract ""

    ![antv南丁格尔玫瑰图](../../img/view_generation/view_gallery/AntV/antv南丁格尔玫瑰图.png){ width="900px" }

### 2.18 玫瑰环形图

!!! Abstract ""
    
    ![antv玫瑰环形图](../../img/view_generation/view_gallery/AntV/antv玫瑰环形图.png){ width="900px" }

### 2.19 漏斗图

!!! Abstract ""
	漏斗图由多个梯形从上而下叠加而成。从上到下的项有逻辑上的顺序关系，梯形面积表示某个业务量与上一个环节之间的差异。

!!! Abstract ""

    ![antv漏斗图](../../img/view_generation/view_gallery/AntV/antv漏斗图.png){ width="900px" }

### 2.20 矩形树图

!!! Abstract ""
    矩形树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，便于突出展现出『树』的各层级中重要的节点。

!!! Abstract ""

    ![antv矩形树图](../../img/view_generation/view_gallery/AntV/antv矩形树图.png){ width="900px" }

### 2.21 瀑布图

!!! Abstract ""
    瀑布图采用绝对值与相对值结合的方式，适用于表达数个特定数值之间的数量变化关系，因图形形似瀑布流水所以称之为瀑布图。

!!! Abstract ""

    ![antv瀑布图](../../img/view_generation/view_gallery/AntV/antv瀑布图.png){ width="900px" }

### 2.22 水波图

!!! Abstract ""
    水波图的水波高度表示指标值，当水填满或溢出时，代表指标值已经到达目标值。

!!! Abstract ""

    ![antv水波图](../../img/view_generation/view_gallery/AntV/antv水波图.png){ width="900px" }

### 2.23 词云图

!!! Abstract ""
	词云图又称文字云，是文本数据的视觉表示，由词汇组成类似云的彩色图形，用于展示大量文本数据。每个词的重要性以字体大小或颜色显示。

!!! Abstract ""

    ![antv词云图](../../img/view_generation/view_gallery/AntV/词云图.png){ width="900px" }

### 2.24 符号地图

!!! Abstract ""
    符号地图根据经纬点绘制图形（不同于以往的行政区划名称），对点数据进行展示，体现相关对象的空间分布，符号地图可根据鼠标缩放地图范围，且范围不限制，可至全球。  
    **注意：符号地图基于高德地图，所以该组件需要在在线环境下使用，且使用符号地图的数据集字段类型需为 “地理位置”，即数据集数据需在标准的经度数值范围与纬度数值范围，示例如：经度值为 117.178191，纬度值为 36.721217。**

!!! Abstract ""
    ![antv符号地图](../../img/view_generation/view_gallery/AntV/antv符号地图.png){ width="900px" }

### 2.25 富文本视图

!!! Abstract ""
    类似组件里的富文本组件，双击富文本视图，可定义样式，并支持在编辑区引用维度与指标中字段。  
    **注意：** 

    - 引用维度与指标字段前，需要在【数据】将维度和指标拖拽到对应的维度栏和指标栏，双击富文本视图后，在右侧【选择视图字段】添加维度和指标。
    - 引用维度与指标字段时，富文本只选取第一条结果值，富文本只选取第一条结果值。

    ![antv富文本视图](../../img/view_generation/view_gallery/AntV/antv富文本视图.png){ width="900px" }

### 2.26 流向地图

!!! Abstract ""

    流向地图根据起始地点的经纬点绘制动线，在地图上显示信息或物体从一个位置到另一个位置的移动，可以通过流向地图揭示出运动中的一些规律或现象。   
    **注意：流向地图同样基于高德地图(火星坐标系)，使用流向地图的数据集字段类型需为 “地理位置”，即数据集数据需在标准的经度数值范围与纬度数值范围。示例如：出发经度值为 116.403963，出发纬度值为 39.915119；目的经度值为 114.064552，目的纬度值为 22.550058。**

!!! Abstract "" 

    ![antv流向地图](../../img/view_generation/view_gallery/AntV/antv流向地图.gif){ width="900px" }

