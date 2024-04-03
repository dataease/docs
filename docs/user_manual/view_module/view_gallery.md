!!! Abstract ""
    使用数据可视化分析工具时，图表样式是展现数据的关键因素之一。在 DataEase 开源数据可视化分析平台上，提供了多种图表样式，包括折线图、柱状图、饼图、雷达图、散点图等。不同的图表样式适用于不同的数据类型和数据分析需求，因此在使用 DataEase 时选择合适的图表样式非常重要。

## 1 表格
!!! Abstract ""
    表格是数据的详情罗列，能看到明细信息，表格包含汇总表和明细表。
### 1.1 汇总表

!!! Abstract ""
    汇总表

    ![echarts汇总表](../../img/view_generation/view_gallery/ECharts/2.0汇总表.png){ width="900px" }
### 1.2 明细表
!!! Abstract ""
    明细表

    ![echarts明细表](../../img/view_generation/view_gallery/ECharts/2.0汇总表.png){ width="900px" }

### 1.3 透视表
!!! Abstract ""
    透视表

    ![echarts明细表](../../img/view_generation/view_gallery/ECharts/透视图.png){ width="900px" }

## 2 指标卡
!!! Abstract ""
    通过文字、数字和符号的合理排版，对数据进行一目了然的展示。指标卡由看板标签和看板指标组成，标签由数据的维度决定，指标由数据的度量决定。
![echarts明细表](../../img/view_generation/view_gallery/ECharts/指标卡.png){ width="900px" }

## 3 柱状图

!!! Abstract ""
    柱状图又称条形图，是一种通过柱形的高度（横向的情况下则是宽度）来表现数据大小的一种常用图表类型，柱状图包括基础柱状图、堆叠柱状图、横向柱状图和横向堆叠柱状图。  
    **注意：** 柱状图当前同一维度只能显示一种颜色。
### 3.1 基础柱状图

!!! Abstract ""
    基础柱状图

    ![echarts基础柱状图](../../img/view_generation/view_gallery/ECharts/2.0基础柱状图.png){ width="900px" }

### 3.2 堆叠柱状图

!!! Abstract "" 
    堆叠柱状图是柱状图的变形，堆叠柱状图将每个柱子进行颜色分割，用于显示同系列下各个数据的大小情况，它不仅可以比较不同维度间总数的差别，还可以显示同类型下子类别的构成以及各数据的大小情况。

    ![echarts堆叠柱状图](../../img/view_generation/view_gallery/ECharts/2.0堆叠柱状图.png){ width="900px" }

### 3.3 横向柱状图
!!! Abstract ""
    横向柱状图，用于比较不同类别的数量或数值，而且柱状条是水平排列的。

    ![echarts横向柱状图](../../img/view_generation/view_gallery/ECharts/2.0横向柱状图.png){ width="900px" }

### 3.4 横向堆叠柱状图
!!! Abstract ""
    横向堆叠柱状图如同字面意思，是堆叠柱状图的横向展示。

    ![echarts横向堆叠柱状图](../../img/view_generation/view_gallery/ECharts/2.0横向堆叠柱状图.png){ width="900px" }

### 3.5 分组柱状图
!!! Abstract ""
    分组柱状图,是一种用于比较多个组内不同类别的数量关系的图表。每个组有多个并排的柱状条，每个柱状条表示一个类别。

    ![echarts横向柱状图](../../img/view_generation/view_gallery/ECharts/2.0分组柱状图.png){ width="900px" }

### 3.6 分组堆叠柱状图
!!! Abstract ""
    分组堆叠柱状图,可以同时展示多个组内的不同类别的数量关系，并且在每个组内，各类别的值可以堆叠在一起。

    ![echarts横向堆叠柱状图](../../img/view_generation/view_gallery/ECharts/2.0分组堆叠柱状图.png){ width="900px" }

### 3.7 百分比柱状图
!!! Abstract ""
    百分比柱状图，每个柱状条的总高度表示 100%，而不同颜色段表示不同类别的百分比贡献

    ![echarts横向柱状图](../../img/view_generation/view_gallery/ECharts/2.0百分比柱状图.png){ width="900px" }


### 3.8 横向百分比柱状图
!!! Abstract ""
    横向百分比柱状图

    ![echarts横向堆叠柱状图](../../img/view_generation/view_gallery/ECharts/2.0横向百分比柱状图.png){ width="900px" }

## 4 折线图

!!! Abstract ""
	折线图是用折线将各个数据点标志连接起来的图表，可用于直角坐标系和极坐标系上。

### 4.1 基础折线图
!!! Abstract ""
    基础折线图

    ![echarts基础折线图](../../img/view_generation/view_gallery/ECharts/2.0折线图.png){ width="900px" }

    ![echarts基础折线图](../../img/view_generation/view_gallery/ECharts/2.0双折线图.png){ width="900px" }

### 4.2 堆叠折线图
!!! Abstract ""
    堆叠折线图在折线图的基础上形成，折线与自变量坐标轴之间的区域使用颜色填充，堆叠折线图每一个数据的起点都是基于前一个数据，最终代表的是所有数据的和，即累计值。

    ![echarts堆叠折现图](../../img/view_generation/view_gallery/ECharts/2.0堆叠折线图.png){ width="900px" }

### 4.3 面积图
!!! Abstract ""
    面积图是通过将折线图下方的区域填充来强调数据的累积变化。

    ![echarts堆叠折现图](../../img/view_generation/view_gallery/ECharts/2.0面积图.png){ width="900px" }

## 5 气泡图

!!! Abstract ""
    气泡图是一种用于展示二维数据的图表类型，其中维度和一个额外的指标（通常表示大小）组成。

!!! Abstract ""
    气泡图

    ![](../../img/view_generation/view_gallery/ECharts/2.0气泡图.png){ width="900px" }

## 6 分布图

### 6.1 饼图

!!! Abstract ""
    饼图以饼状图形显示一个数据系列中各项的大小与各项总和的比例，也称作扇形统计图。

    ![echarts基础饼图](../../img/view_generation/view_gallery/ECharts/2.0饼图.png){ width="900px" }

### 6.2 环形饼图

!!! Abstract ""
    环形图（环形饼图）

    ![echarts环形饼图](../../img/view_generation/view_gallery/ECharts/2.0环形图.png){ width="900px" }

### 6.3 南丁格尔玫瑰图

!!! Abstract ""
    南丁格尔玫瑰图又称鸡冠花图、极坐标区域图，是由弗罗伦斯·南丁格尔所发明，其实是一种圆形的直方图，以圆弧的半径长短表示数据的大小。

!!! Abstract ""

    ![echarts南丁格尔玫瑰图](../../img/view_generation/view_gallery/ECharts/2.0玫瑰图.png){ width="900px" }

### 6.4 玫瑰环形图

!!! Abstract ""

    ![echarts玫瑰环形图](../../img/view_generation/view_gallery/ECharts/2.0玫瑰环形图.png){ width="900px" }

### 6.5 矩形树图

!!! Abstract ""
    矩形树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，便于突出展现出『树』的各层级中重要的节点。

!!! Abstract ""

    ![echarts矩形树图](../../img/view_generation/view_gallery/ECharts/2.0矩形树图.png){ width="900px" }

## 7 漏斗图

!!! Abstract ""
    漏斗图由多个梯形从上而下叠加而成，从上到下的项有逻辑上的顺序关系，梯形面积表示某个业务量与上一个环节之间的差异。

!!! Abstract ""

    ![echarts漏斗图](../../img/view_generation/view_gallery/ECharts/2.0漏斗图.png){ width="900px" }

## 8 地图
### 8.1 区域地图
!!! Abstract ""
    普通地图：用颜色的深浅来展示区域范围的数值大小。

    ![普通地图](../../img/view_generation/view_gallery/ECharts/2.0地图.png){ width="900px" }

!!! Abstract ""
    支持展示世界地图，【地图设置】中选择【世界村】。

    ![世界地图](../../img/view_generation/view_gallery/ECharts/2.0世界地图.png){ width="900px" }

### 8.2 气泡地图
!!! Abstract ""
    气泡地图：用气泡大小展示区域范围的数值大小。

    ![普通地图](../../img/view_generation/view_gallery/ECharts/气泡地图.png){ width="900px" }

## 9 雷达图

!!! Abstract ""
    雷达图又称蜘蛛网图，将多个维度的数据量映射到起始于同一个圆心的坐标轴上，结束于圆周边缘，然后将同一组的点使用线连接起来。

!!! Abstract ""

    ![echarts雷达图](../../img/view_generation/view_gallery/ECharts/2.0雷达图.png){ width="900px" }

## 10 瀑布图

!!! Abstract ""
    瀑布图采用绝对值与相对值结合的方式，适用于表达数个特定数值之间的数量变化关系，因图形形似瀑布流水所以称之为瀑布图。

!!! Abstract ""

    ![echarts雷达图](../../img/view_generation/view_gallery/ECharts/2.0瀑布图.png){ width="900px" }

## 11 仪表盘

!!! Abstract ""
    仪表盘像一个钟表或者可读盘，有刻度和指针，其中刻度表示度量，指针表示维度，指针角度表示数值，指针指向当前数值。

!!! Abstract ""

    ![echarts仪表盘](../../img/view_generation/view_gallery/ECharts/2.0仪表盘.png){ width="900px" }

## 12 水波图

!!! Abstract ""
    水波图的水波高度表示指标值，当水填满或溢出时，代表指标值已经到达目标值。

!!! Abstract ""

    ![echarts仪表盘](../../img/view_generation/view_gallery/ECharts/2.0水波图.png){ width="900px" }

## 13 词云图

!!! Abstract ""
    词云图又称文字云，是文本数据的视觉表示，由词汇组成类似云的彩色图形，用于展示大量文本数据。每个词的重要性以字体大小或颜色显示。

!!! Abstract ""

    ![echarts仪表盘](../../img/view_generation/view_gallery/ECharts/2.0词云图.png){ width="900px" }