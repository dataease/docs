!!! Abstract ""
    点击【样式】，切换至样式设计界面，该界面主要针对【图形属性】和【组件样式】进行调整，**不同的视图类型可支持的样式会有所差异，不同的图表库（Echarts、AntV）在样式上也有一些差异。**

![视图可选维度列表](../../img/view_generation/数据样式切换.png){ width="900px" }

## 1 图形属性

### 1.1 颜色

!!! Abstract ""
    支持修改图形的颜色，支持配置系统方案（默认、复古、淡雅、未来、渐变、简洁、商务、柔和、科技、明亮、经典、清新、活力、火红、轻快、灵动）；  
    如下图所示，点击，也可以自定义配色。

![图形属性_修改颜色](../../img/view_generation/图形属性_修改颜色.png){ width="900px" }

!!! Abstract ""
    应用配色方案后，仍然可以进一步调整颜色，如下图所示，整个视图应用到的颜色都会在下方列出来，修改时不需要再在配色方案中选中，自行修改颜色后，配色方案中所展示的颜色将不会跟着改变。  
    其中柱状图、折线图、散点图、支持系列设置颜色，AntV 图库支持维度枚举值设置颜色，如下图所示。

![图形属性_自定义配色](../../img/view_generation/图形属性_自定义配色.png){ width="900px" }

!!! Abstract ""
    AntV 图库的所有柱状图、面积图，表盘支持渐变色，如下图所示，支持开启渐变色，渐变色的起始颜色和结束颜色按给定颜色 100 渐变到 30 。

![图形属性](../../img/view_generation/图形属性_渐变颜色.png){ width="900px" }

!!! Abstract ""
    ECharts 图库地图的样式配色方案中支持渐变色选项，支持悬浮组件显隐设置，即地图左侧的缩放和右侧的图例可根据需要设置成隐藏。

    - 【分离渐变】：系统内置的渐变色方案；
    - 【自定义】：可自定义开始和结束的颜色，系统会自动生成渐变色方案。

![图形属性_渐变色方案](../../img/view_generation/图形属性_渐变色方案.png){ width="900px" }

!!! Abstract ""
    AntV 和 ECharts 图库的饼图和环形图均支持 TopN 设置，即显示 TopN，其余的可以合并为其他 。

![name](../../img/release_notes/1.4 饼图:环形图支持显示 TopN.png){ width="900px" }

### 1.2 大小

!!! Abstract ""
    如下图所示，以配置"指标卡"的图形属性大小为例。

![组件样式_值与名称字体样式](../../img/view_generation/组件样式_值与名称字体样式.png){ width="900px" }

!!! Abstract ""
    水波图目标值支持设置动态值设置，应用示例如下：    
    指标放置了 ”销售价“ 并且计算方式为 “求和”。

![组件样式_AntV](../../img/view_generation/组件样式_AntV1.png){ width="900px" }

!!! Abstract ""
    目标值使用了原始价的求和，则水波图自动计算出了销售价的总数占原始价总数的多少，即整体的折扣率。

![组件样式_AntV](../../img/view_generation/组件样式_AntV2.png){ width="900px" }

!!! Abstract ""
    AntV 图库仪表盘视图支持在组件样式设置最小值、最大值、支持用视图指标来动态设置最大值和最小值，支持刻度间隔数，支持标签设置数值格式。

![组件样式_AntV](../../img/view_generation/组件样式_AntV.png){ width="900px" }

### 1.3 标签

!!! Abstract ""
    支持修改标签的颜色、大小、位置等，根据不同的图库视图所支持的配置项有所不同，以 AntV 视图图库为例，AntV 图库玫瑰图，饼图，环形图，玫瑰环形图支持标签内容显示，支持通过勾选的方式选择展示的维度、指标、占比。

![图形属性](../../img/view_generation/AntV图库标签内容.png){ width="900px" }

!!! Abstract ""
    AntV 漏斗图支持显示转换率

![name](../../img/release_notes/1.11%20AntV%20漏斗图支持显示转换率.png){ width="900px" }

### 1.4 提示

!!! Abstract ""
    支持调整视图的”提示“字体大小、字体颜色，视图提示支持背景选项。

![组件样式_背景](../../img/view_generation/组件样式_背景.png){ width="900px" }

### 1.5 表格配置
!!! Abstract ""
    支持对表格内部进行设置。

    - 字体大小与对齐方式；
    - 表格行高、列宽；
    - 自动换行；
    - 序号与表头显示；
    - 表格冻结。

    注意：Echart 和 AntV表格设置上有差异，设置会有所不同。不同设置因表格视图的不同也存在在差异，如明细表与汇总表支持冻结前 N 列/行，透视表不支持。 
![name](../../img/release_notes/v1-18-14-5.png){ width="900px" }
!!! Abstract ""
    例如：AntV 明细表/汇总表支持按列设置宽度。支持手动拖拉和针对各个字段配置所占表格宽度的百分比。  
    **注意：在预览界面与编辑界面均支持手动拖拉表格宽度，但只有编辑界面下拖拉完成保存后生效，在预览界面拖拉仅用于临时使用，刷新页面后将还原。**

!!! Abstract ""
    AntV 明细表/汇总表可控制是否启用表头排序

![name](../../img/release_notes/1.13  AntV 明细表:汇总表可控制是否启用表头排序.png){ width="900px" }

![name](../../img/release_notes/v1-18-16-3.PNG){ width="900px" }

## 2 组件样式

### 2.1 标题

!!! Abstract ""
    支持修改组件的标题（标题名称、字体大小、字体颜色、水平位置、垂直位置、字体样式）。

![组件样式_标题字体样式](../../img/view_generation/组件样式_标题字体样式.png){ width="900px" }

!!! Abstract ""
    AntV 图库标题支持双击修改。

![ AntV 图库标题](../../img/view_generation/AntV图库标题.png){ width="900px" }

!!! Abstract ""
    AntV 图库图表标题支持备注，同时支持字体、阴影和间距设置。

![组件样式_编辑标题备注](../../img/view_generation/组件样式_编辑标题备注.png){ width="900px" }

![组件样式_标题备注](../../img/view_generation/组件样式_标题备注.png){ width="900px" }

### 2.2 图例

!!! Abstract ""
    支持修改组件的图例，包括图例的图标、方向、字体大小、字体颜色、水平位置、垂直位置等。

![组件样式](../../img/view_generation/组件样式_图例.png){ width="900px" }

### 2.3 坐标轴

!!! Abstract ""
    有坐标轴的视图（柱状图、折线图等），轴值支持数值格式化设置，如下图所示，在样式的纵轴(横向图则为横轴)设置中。

![组件样式_设置格式化](../../img/view_generation/组件样式_数值格式化.png){ width="900px" }

!!! Abstract ""
    带坐标系的视图类型支持坐标轴轴线显示控制的选项。

![坐标轴轴线显示控制](../../img/view_generation/坐标轴轴线显示控制.png){ width="900px" }
!!! Abstract ""
    AntV 带轴线的图表支持虚线设置,包括虚线设置开关、虚线宽度、虚线间距。

![name](../../img/release_notes/v1-18-14-9.png){ width="900px" }

### 2.4 外边距与序号

!!! Abstract ""
    支持 ECharts 视图外边距设置。

    - 自动：系统的默认值，自动适配；
    - 绝对：配置实际距离；
    - 相对：配置相对的百分比。

![ECharts视图外边距](../../img/view_generation/ECharts视图外边距.png){ width="900px" }

![ECharts视图外边距](../../img/view_generation/ECharts视图外边距_实际距离.png){ width="900px" }

![ECharts视图外边距](../../img/view_generation/ECharts视图外边距_百分比.png){ width="900px" }

!!! Abstract ""
    **序号设置：** AntV 明细表和汇总表支持序号设置，同时支持给序号列命名。

![ECharts视图外边距](../../img/view_generation/AntV明细表和汇总表_序号设置.png){ width="900px" }

