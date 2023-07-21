# 数据关系和 AntV、ECharts 图表解析
!!! Abstract ""
    在实际的数据分析场景中，我们经常会遇到的数据关系包括以下五种：即趋势、比较、分布、关系和空间位置。而在制作仪表板的的时候，根据不同的业务场景，为数据关系和数据类型选择合适的视图是十分重要的。

    DataEase 开源数据可视化分析平台支持 AntV 和 ECharts 两种视图类型。两种视图类型在设置上存在细微的差别，因此在制作视图时需要根据不同的显示要求选择不同的视图类型。

!!! Abstract ""
    **在了解数据关系之前，需要首先明确数据的类型**：   
    
    * **定性数据**  
    类别数据：包含有限的类别数或可区分组数。类别数据可能不是逻辑顺序，例如，性别、材料类型、付款方式等。  

    * **定量数据**  
    离散数据：在两个值之间具有可计数的值的数据，离散数据始终为数值。例如，客户投诉数量，瑕疵或缺陷数，学校的学生人数等；  
    连续数据：在两个任意值之间具有无限个值的数据，连续型数据可以是数值，也可以是日期/时间。例如，零件的长度、商品的价格、销量、收付款时间等。  

## 1 趋势数据
![趋势常见视图](https://blog.fit2cloud.com/upload/%E5%9B%BE01-ouhv.png){ width="900px" }
!!! Abstract ""
    **视图所需的数据类型**：

    * 数据集中只包含一列连续数据的日期变量；

    * 数据集中至少包含一列连续数据的数值变量。

    数据示例：各年度价格与销量的变化。
![趋势数据示例](https://blog.fit2cloud.com/upload/%E8%A1%A81-tjiv.png){ width="900px" }

!!! Abstract ""

    * AntV 包含的趋势图：

![AntV趋势数据](https://blog.fit2cloud.com/upload/%E5%9B%BE02-txcq.png){ width="900px" }
!!! Abstract ""

    * ECharts 包含的趋势图：

![ECharts趋势数据](https://blog.fit2cloud.com/upload/%E5%9B%BE03-cqfa.png){ width="900px" }

!!! Abstract ""
    **AntV 和 ECharts 的趋势图对比**：

    * 视图类型：AntV 相比 ECharts 少了组合图，当数据集中两列指标的数据差距较大时，用组合图可以设置主轴值与副轴值，使两列数据都可以有较好地呈现；

    * 数据设置：AntV 相比 ECharts 多了数值格式设置，当原始数据类型是小数时，通过数值格式可以修改为百分比等其他数值格式；

    * 样式设置：AntV 相比 ECharts 少了”外间距“的功能（外间距是指图表相对视图组件的距离），以下以基础折线图为例：

!!! Abstract ""

    * 当不设置外间距时，图像自动显示如下：

![不设置外间距时](https://blog.fit2cloud.com/upload/%E5%9B%BE04-qevm.png ){ width="900px" }
!!! Abstract ""

    * 设置外间距后图像显示如下：：

![设置外间距](https://blog.fit2cloud.com/upload/%E5%9B%BE05-xoij.png){ width="900px" }

## 2 比较数据
![比较常见视图](https://blog.fit2cloud.com/upload/%E5%9B%BE06-gdyc.png){ width="900px" }
!!! Abstract ""
    **视图所需的数据类型**：

    * 类别数据：  
        • 数据集中只包含一列类别数据：柱状图；

        • 数据集中包含两列类别数据：堆叠图；

        • 数据集中包含三列类别数据：分组堆叠图。

    * 连续型数据：数据集中至少包含一列连续型数据。

    数据示例：不同类别的产品价格与销量的对比。
![比较数据示例](https://blog.fit2cloud.com/upload/%E8%A1%A82.png){ width="900px" }
!!! Abstract ""

    * AntV 包含的比较图：

![AntV比较数据](https://blog.fit2cloud.com/upload/%E5%9B%BE07-hfpi.png){ width="900px" }
!!! Abstract ""

    * ECharts 包含的比较图：

![ECharts比较数据](https://blog.fit2cloud.com/upload/%E5%9B%BE08-lwzj.png){ width="900px" }
!!! Abstract ""
    **AntV 和 ECharts 的比较图对比**：

    * 视图类型：AntV 相比 ECharts 多了瀑布图（主要用于展示股票趋势变动）、百分比图（着重展示比例信息、例如高校男女占比等，主要用于国家统计、用户调查等）、对称柱状图（主要用于两个类别不同指标间的比较，例如某班级男女生各科成绩比较等）；

    * 数据设置：AntV 相比 ECharts 多了数值格式设置；

    * 样式设置：AntV 相比 ECharts 少了“外间距”的功能。

## 3 分布数据
![分布常见视图](https://blog.fit2cloud.com/upload/%E5%9B%BE09-ptef.png){ width="900px" }
!!! Abstract ""
    **视图所需的数据类型**：

    * 数据集中只包含一列类别数据；

    * 数据集中只包含一列连续型数据的数值变量。

    数据示例 1：不同类别的商品销量占比。
![分布数据示例1](https://blog.fit2cloud.com/upload/%E8%A1%A83.png){ width="900px" }
!!! Abstract ""
    所有商品都被分类了，一个商品有且仅有一个分类，不存在一个商品同时归属于两个分类的原则。从一级分类的角度看销量：使用饼图、环形图、南丁格尔玫瑰图、矩形树图，可以看出不同类别商品的销量占整体销量的占比。占比之和 = 1。
!!! Abstract ""
    数据示例 2：不同类型的用户购买商品数量占比。
![分布数据示例2](https://blog.fit2cloud.com/upload/%E8%A1%A84.png){ width="900px" }
!!! Abstract ""
    所有用户不一定被全部打上标签，也不一定只有一个标签。从用户标签角度看购买量占比：使用雷达图、词云图，可以看出各标签的影响程度。占比之和 ≠ 1。

!!! Abstract ""

    * AntV 包含的分布图：

![AntV分布数据](https://blog.fit2cloud.com/upload/%E5%9B%BE10-nmkw.png){ width="900px" }
!!! Abstract ""

    * ECharts 包含的分布图：

![ECharts分布数据](https://blog.fit2cloud.com/upload/%E5%9B%BE11-qmyy.png){ width="900px" }
!!! Abstract ""
    **AntV 和 ECharts 的分布图中的雷达图对比**：  

    * ECharts 和 AntV 的雷达图都不可以调整轴值（每格数据的大小）。假设各指标的数据为 ：90，100，95，110。  
    * ECharts 的轴值是绝对值，雷达中心点 = 0，雷达边缘点=数据指标列最大值。使用 ECharts 难以看出细微差别。  
    * 此时比较适合使用 AntV 图。AntV 的轴值为相对值，雷达中心点 = 数据指标列最小值，雷达边缘点 = 数据指标最大值。  
![AntV雷达图](https://blog.fit2cloud.com/upload/%E5%9B%BE13-sxnn.png){ width="900px" }

![ECharts雷达图](https://blog.fit2cloud.com/upload/%E5%9B%BE12-ymyl.png){ width="900px" }

## 4 关系数据
![关系常见视图](https://blog.fit2cloud.com/upload/%E5%9B%BE14-hwpg.png){ width="900px" }
!!! Abstract ""
    **气泡图数据类型**：

    * 被解释变量：Y 变量数据集中只包含一列连续型数据的数值变量；

    * 解释变量：X 变量数据集中只包含一列连续型数据的数值变量。

    数据示例 1：销量随价格的变化趋势。
![气泡图数据示例](https://blog.fit2cloud.com/upload/%E8%A1%A85.png){ width="900px" }
!!! Abstract ""
    **漏斗图数据类型**：

    * 被解释变量：Y 变量数据集中只包含一列连续型数据的数值变量；

    * 解释变量：X 变量数据集中只包含一列类别数据。

    数据示例 2：网站各页面的浏览人数。
![漏斗图数据示例](https://blog.fit2cloud.com/upload/%E8%A1%A86.png){ width="900px" }
!!! Abstract ""
    **AntV 和 ECharts 的关系图对比**：

    * AntV 和 ECharts 都包含气泡图和漏斗图，ECharts 的气泡图可以设置“外间距”。

    * ECharts 和 AntV 都不可以设置漏斗图各层级的大小，ECharts 的各层级是固定样式，AntV 的各层级大小由数值大小决定。

![AntV漏斗图](https://blog.fit2cloud.com/upload/%E5%9B%BE16-ynae.png){ width="900px" }

![ECharts漏斗图](https://blog.fit2cloud.com/upload/%E5%9B%BE15-hmes.png){ width="900px" }

## 5 空间数据
![空间常见视图](https://blog.fit2cloud.com/upload/%E5%9B%BE17-nhrq.png){ width="900px" }
!!! Abstract ""
    **符号地图数据类型**：

    * 数据集中包含一列连续型数值数据（经度）；

    * 数据集中包含一列连续型数值数据（纬度）。
!!! Abstract ""
    **流向地图数据类型**：

    * 数据集中包含一列连续型数值数据（起点经度）；

    * 数据集中包含一列连续型数值数据（起点纬度）；

    * 数据集中包含一列连续型数值数据（终点经度）；

    * 数据集中包含一列连续型数值数据（终点纬度）。
!!! Abstract ""
    **地图数据类型**：

    * 数据集中包含一列类别变量（地区名称）；

    * 数据集中包含一列连续型数值数据（代表气泡大小）。
!!! Abstract ""
    **AntV 和 ECharts 的空间地图对比**：

    * AntV：包含流向地图与符号地图，有经纬度时可以使用该图形，不限制国内或国外。

    * ECharts：只包含地图和气泡地图，目前只有国内地图数据。如需使用国外地图数据，需要自己手动配置。
!!! Abstract ""
    AntV 包含的空间视图：

![AntV空间图](https://blog.fit2cloud.com/upload/%E5%9B%BE18-cncr.png){ width="900px" }

!!! Abstract ""
    ECharts 包含的空间视图：
    
![ECharts空间图](https://blog.fit2cloud.com/upload/%E5%9B%BE19-ssii.png){ width="900px" }

