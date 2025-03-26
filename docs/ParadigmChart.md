# 快速上手
本节内容为标准范式图表组件库ParadigmChart的接入使用文档。
## 相关链接
1. 组件库配置项：https://datav.iwencai.com/components/paradigm-chart/docs/apis/option
2. APIs:https://datav.iwencai.com/components/paradigm-chart/docs/apis/api
3. 主题配置：https://datav.iwencai.com/components/paradigm-chart/docs/apis/theme
4. 公共组件APIs：
AxisPointer: https://datav.iwencai.com/components/paradigm-chart/docs/apis/component/axisPointer
Grid: https://datav.iwencai.com/components/paradigm-chart/docs/apis/component/grid
roam: https://datav.iwencai.com/components/paradigm-chart/docs/apis/component/roam
Tooltips:https://datav.iwencai.com/components/paradigm-chart/docs/apis/component/tooltip
xAxis:https://datav.iwencai.com/components/paradigm-chart/docs/apis/component/xaxis
yAxis:https://datav.iwencai.com/components/paradigm-chart/docs/apis/component/yaxis

5. 图表组件APIs
柱状图：https://datav.iwencai.com/components/paradigm-chart/docs/apis/series/bar
雷达图：https://datav.iwencai.com/components/paradigm-chart/docs/apis/series/dvRadar
矩形树图：https://datav.iwencai.com/components/paradigm-chart/docs/apis/series/treemap
折线图：https://datav.iwencai.com/components/paradigm-chart/docs/apis/series/line
动态排名图：https://datav.iwencai.com/components/paradigm-chart/docs/apis/series/dvRankLine

LineTimeLineHelper：https://datav.iwencai.com/components/paradigm-chart/docs/apis/helper/LineTimeLineHelper

## 安装

如果是外网开发，可以通过cdn直接引入构建的 JS 文件
  {
    "version": "1.7.3",
    "assets": [
      "https://s.thsi.cn/cd/iwc-datav-standard-chart/1.7.3/bundle.umd.min.js",
      "https://s.thsi.cn/cd/iwc-datav-standard-chart/1.7.3/bundle.umd.js",
      "https://s.thsi.cn/cd/iwc-datav-standard-chart/1.7.3/bundle.esm.min.js",
      "https://s.thsi.cn/cd/iwc-datav-standard-chart/1.7.3/bundle.esm.js"
    ]
  },

// umd
<script src="path/to/bundle.umd.min.js"></script>;
const chart = ThsDataVStandardChart.init(dom, theme?, initOption?);

// esm
import { init } from 'path/to/bundle.esm.min.js';
const chart = init(dom, theme?, initOption?);

CDN 资源
会同时提供压缩版本 (.min.js) 和未压缩版本 (.js)，前者为生产环境使用，后者可用于开发环境便于调试（还将提供相应的 sourcemap 文件）。


## 使用
要使用标准范式图表组件，请先将组件库依赖安装到项目，然后参考以下示例代码即可初始化一个组件实例：

import { init } from 'thsc-datav-standard-chart';

// 初始化一个图表实例
const chart = init(dom);

// 渲染图表数据并播放动画
chart.play({
  option: {
    xAxis: {
      data: [1, 2, 3, 4],
    },
    yAxis: {},
    series: [
      {
        type: 'bar',
        data: [50, 100, 150, 200],
      },
    ],
  },
});


# 常见问题
常见问题及解决方案
如果使用标准范式图表组件库的过程中遇到问题，请加入 Vanish 的“数据可视化问题反馈”公开群进行反馈。

## 提示
组件库的底层基于 ECharts 开发，可以参考 ECharts 的常见问题文档（https://echarts.apache.org/zh/faq.html）。


## 使用组件时，英文文本无法渲染？
该问题是由于组件部分场景下默认使用 THSJinRongTi 的字体，该字体目前仅支持纯数字，暂未适配英文字母。如果遇到，在对应的样式配置项中，重新声明其他字体覆盖组件默认配置即可。

## 性能问题
大数据量下，在左右滑动过程中，tooltip 在部分位置不显示数据信息？
场景：大数据量（1200+，取决于容器宽度），折线图，使用了主题配置（如 mobile-app-light）
表现：在左右滑动的过程中，部分位置的点信息不展示（tooltip 没有数据信息），去掉主题配置后问题消失
原因：主题内部为了对性能做优化，配置了 sampling: 'lttb'，其对大数据量下的点做了降采样，导致部分点不渲染
解决方案：在业务侧配置 sampling: '' 覆盖主题配置，观察线上测试时是否有性能问题
大数据量下，拖动dataZoom过程中卡顿?
以折线图为例，在有dataZoom的情况下，只有1个series且其数据量在10^3量级上无卡顿。如果出现卡顿的现象，请检查图表实例是否被作为一个响应式对象挂载在vue实例上导致内存占用太大，理论上不需要将图表实例作为一个响应式对象，需要更新图标应该使用play方法。

## dataZoom
多系列叠加的场景下 dataZoom.slider 背景中展示的数据趋势与系列的关系？
经过测试，在多系列叠加的情况下，dataZoom.slider 的背景数据趋势实际上与 series 数组中第一个系列的数据相关联，所以想让其关联指定系列的数据，把该系列放在 series 数组的首个元素位置即可。

对于堆叠柱状图的场景，可以添加一个隐藏的系列放在 series 数组首位只用来和 dataZoom.slider 背景数据趋势做关联展示的作用。

dataZoom.slider 和 dataZoom.inside 同时存在时 startValue 和 endValue 失效？
不要同时配置，二选一。

1. 柱状图
堆叠柱状图系列的标签文本会自动加文本描边效果？
当柱状图用在堆叠场景下时，会发现柱子标签文本会随背景色的变化出现文本描边效果，使用以下配置即可消除（参考文档）：

series.label.textBorderColor: 'transparent';

2. 折线图
3. 矩形树图
如何触发矩形树图的偏移和缩放
可以通过官方提供的Action实现（未在文档中申明，需要查阅源码）

dispatchAction({
    type:'treemapRender',
    seriesId: string,
    rootRect: {x:number, y:number, width:number, height:number}
})

如何触发矩形树图聚焦于某个节点
可以通过官方提供的Action实现（未在文档中申明，需要查阅源码）

dispatchAction({
    type:'treemapZoomToNode',
    seriesId: string,
    targetNode: TreeNode
})

如何触发矩形树图下钻于某个节点
可以通过官方提供的Action实现（未在文档中申明，需要查阅源码）

dispatchAction({
    type:'treemapRootToNode',
    seriesId: string,
    targetNode?: TreeNode | string,
    targetNodeId?: string,
    direction: "rollUp" | "drillDown"

})

如何获取矩形树图当前的偏移量和缩放倍数
可以与actiontreemapRender结合使用

ECharts使用外接矩形变量rootRect:{x:number, y:number, width:number, height:number}保存偏移量与缩放倍数

该变量可以通过以下API获取到

// 具体定位方法可以自行打印getModel上挂载的get方法，比如getByName，getById等
const treeMapModel = chart.getModel().getSeriesByIndex(0)
const treeMapView = chart.getViewOfSeriesModel(treeMapModel)
// 由于外接矩形为引用类型，故需要clone
const rootRect = treeMapView._containerGroup.getBoundingRect().clone()

其中x,y默认为0，后续读取到的值即为偏移量

后续读取到的width与height与初始读取到的相除即可获得缩放倍数

连续setOption时如何取消矩形树图的入场动画
setOption前执行ECharts上的clear方法即可

4. 气泡图（散点图）
为什么部分label的配置项（比如blur.label）不生效？
由于气泡从原有的单图元转为多图元，所以需要指定每个图元的label

目前默认只需配置主图元的label，但不能保证后续没有其他复杂场景

需要在气泡图自定义配置项series.dvItemStyle或dataItem.itemStyle中配置

为什么ContainBubblede辅助函数中返回的是NaN
该函数只是通过入参生成比例尺，请检查入参是否含有非数字的部分

尤其需要注意，是否在调用该函数时，dom还未初始化，导致内部获取dom宽高进行计算时出错

如何实现标签换行
简单的换行只需要在字符串中穿插换行符号：'/n'

如果还需要不同行由不同样式，则需要用到ECharts官方支持的富文本标签