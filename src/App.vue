<template>
  <div id="app">
    <!-- 页面标题：使用CSS变量方式自定义样式 -->
    <header class="stock-header">
      <h1>A股事件分析平台</h1>
      <p>实时监控市场动态，深入分析事件影响</p>
    </header>

    <!-- 数据卡片区域：使用Tailwind工具类方式 -->
    <div class="bg-gray-10 p-4 rounded-medium m-4 shadow">
      <h2 class="text-brand mb-4">市场概览</h2>
      
      <div class="flex space-between">
        <div class="bg-white p-3 rounded-default mr-4 flex-1">
          <h3 class="text-title-medium text-gray-9">上证指数</h3>
          <p class="text-raise font-bold">3,521.62 <span class="text-sm">+0.85%</span></p>
        </div>

        <div class="bg-white p-3 rounded-default mr-4 flex-1">
          <h3 class="text-title-medium text-gray-9">深证成指</h3>
          <p class="text-raise font-bold">14,328.38 <span class="text-sm">+1.24%</span></p>
        </div>

        <div class="bg-white p-3 rounded-default flex-1">
          <h3 class="text-title-medium text-gray-9">创业板指</h3>
          <p class="text-fall font-bold">2,854.45 <span class="text-sm">-0.32%</span></p>
        </div>
      </div>
    </div>

    <!-- 图表区域：混合使用方式（Tailwind + 自定义类） -->
    <div class="chart-container">
      <h2 class="chart-title">重大事件市场影响分析</h2>
      <div class="chart-tabs">
        <button class="tab-item active">政策发布</button>
        <button class="tab-item">财报发布</button>
        <button class="tab-item">重大并购</button>
      </div>
      <!-- ECharts图表容器 -->
      <div ref="chartRef" class="chart-main"></div>
    </div>

    <!-- 事件列表：使用CSS变量方式 -->
    <div class="event-list">
      <h2>近期重大事件</h2>
      <ul>
        <li class="event-item">
          <span class="event-date">2023-03-24</span>
          <span class="event-tag policy">政策</span>
          <span class="event-title">央行降准0.5个百分点，释放长期资金约1.2万亿元</span>
          <span class="event-impact positive">积极</span>
        </li>
        <li class="event-item">
          <span class="event-date">2023-03-20</span>
          <span class="event-tag report">财报</span>
          <span class="event-title">茅台发布2022年报，净利润同比增长18.5%</span>
          <span class="event-impact positive">积极</span>
        </li>
        <li class="event-item">
          <span class="event-date">2023-03-15</span>
          <span class="event-tag merger">并购</span>
          <span class="event-title">某科技企业宣布收购AI创业公司，交易金额50亿元</span>
          <span class="event-impact neutral">中性</span>
        </li>
        <li class="event-item">
          <span class="event-date">2023-03-10</span>
          <span class="event-tag policy">政策</span>
          <span class="event-title">监管部门发布新能源汽车补贴新政策</span>
          <span class="event-impact negative">消极</span>
        </li>
      </ul>
    </div>

    <div>
       <CustomChart
         title="政策发布后市场表现"
         :chartData="chartData"
         chartWidth="100%"
         chartHeight="400px"
       />
     </div>

    <!-- 主题切换按钮 -->
    <div class="theme-switcher">
      <ThemeSwitcher @theme-changed="handleThemeChange"/>
    </div>

    <!-- 底部区域 -->
    <footer class="bg-gray-9 p-4 text-gray-3 text-center">
      A股事件分析平台 © 2023
    </footer>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import ThemeSwitcher from '@/components/ui/ThemeSwitcher.vue'
import CustomChart from '@/components/CustomChart.vue'

export default {
  name: 'App',
  components: {
    ThemeSwitcher,
    CustomChart
  },
  data() {
    return {
      chart: null,
      currentTheme: 'default',
      chartData: [
           { name: '政策发布当天', value: 0.2 },
           { name: '1天后', value: 0.5 },
           { name: '3天后', value: 0.8 },
           { name: '1周后', value: 1.2 },
           { name: '2周后', value: 0.9 },
           { name: '1个月后', value: 1.5 }
         ]
    }
  },
  methods: {
    handleThemeChange(theme) {
      // 移除当前主题
      document.documentElement.removeAttribute('data-theme');
      
      // 设置新主题
      if (theme !== 'default') {
        document.documentElement.setAttribute('data-theme', theme);
      }
      
      // 更新当前主题
      this.currentTheme = theme;
      
      // 更新图表主题
      this.$nextTick(() => {
        if (this.chart) {
          this.initChart();
        }
      });
    },
    initChart() {
      // 基于准备好的dom，初始化echarts实例
      this.chart = echarts.init(this.$refs.chartRef)
      
      // 使用CSS变量获取品牌颜色
      const brandColor = getComputedStyle(document.documentElement).getPropertyValue('--hx-brand-color-3').trim()
      const raiseColor = getComputedStyle(document.documentElement).getPropertyValue('--hx-raise-color-3').trim()
      const fallColor = getComputedStyle(document.documentElement).getPropertyValue('--hx-fall-color-3').trim()
      
      // 指定图表的配置项和数据
      const option = {
        title: {
          text: '政策发布后市场表现',
          textStyle: {
            color: getComputedStyle(document.documentElement).getPropertyValue('--hx-text-color-primary').trim()
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['大盘涨跌幅', '行业涨跌幅', '相关股票涨跌幅'],
          textStyle: {
            color: getComputedStyle(document.documentElement).getPropertyValue('--hx-text-color-secondary').trim()
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ['政策发布当天', '1天后', '3天后', '1周后', '2周后', '1个月后'],
          axisLine: {
            lineStyle: {
              color: getComputedStyle(document.documentElement).getPropertyValue('--hx-border-level-1-color').trim()
            }
          },
          axisLabel: {
            color: getComputedStyle(document.documentElement).getPropertyValue('--hx-text-color-secondary').trim()
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: '{value}%',
            color: getComputedStyle(document.documentElement).getPropertyValue('--hx-text-color-secondary').trim()
          },
          splitLine: {
            lineStyle: {
              color: getComputedStyle(document.documentElement).getPropertyValue('--hx-border-level-1-color').trim(),
              opacity: 0.3
            }
          }
        },
        series: [
          {
            name: '大盘涨跌幅',
            type: 'line',
            data: [0.2, 0.5, 0.8, 1.2, 0.9, 1.5],
            lineStyle: {
              color: brandColor
            },
            itemStyle: {
              color: brandColor
            }
          },
          {
            name: '行业涨跌幅',
            type: 'line',
            data: [0.5, 1.2, 1.5, 1.8, 1.3, 2.0],
            lineStyle: {
              color: raiseColor
            },
            itemStyle: {
              color: raiseColor
            }
          },
          {
            name: '相关股票涨跌幅',
            type: 'line',
            data: [-0.3, 0.2, 0.5, 0.8, 0.4, 1.0],
            lineStyle: {
              color: fallColor
            },
            itemStyle: {
              color: fallColor
            }
          }
        ]
      }
      
      // 使用配置项和数据显示图表
      this.chart.setOption(option)
    }
  },
  mounted() {
    // 初始化图表
    this.initChart()
  }
}
</script>

<style lang="scss">
/* 方式1：直接使用CSS变量定义样式 */
.stock-header {
  background-color: var(--hx-brand-color-3);
  color: var(--hx-gray-color-1);
  padding: var(--hx-size-6);
  text-align: center;
  
  h1 {
    font: var(--hx-font-headline-large);
    margin-bottom: var(--hx-size-4);
  }
  
  p {
    font: var(--hx-font-body-large);
    opacity: 0.9;
  }
}

/* 方式2：自定义图表组件样式 */
.chart-container {
  background-color: var(--hx-bg-color-container);
  border-radius: var(--hx-radius-medium);
  margin: var(--hx-size-4);
  padding: var(--hx-size-4);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  
  .chart-title {
    font: var(--hx-font-title-large);
    color: var(--hx-text-color-primary);
    margin-bottom: var(--hx-size-4);
  }
  
  .chart-tabs {
    display: flex;
    margin-bottom: var(--hx-size-4);
    
    .tab-item {
      background: transparent;
      border: 1px solid var(--hx-border-level-1-color);
      padding: var(--hx-size-2) var(--hx-size-4);
      margin-right: var(--hx-size-2);
      border-radius: var(--hx-radius-default);
      color: var(--hx-text-color-secondary);
      cursor: pointer;
      transition: all 0.3s;
      
      &:hover {
        border-color: var(--hx-brand-color-hover);
        color: var(--hx-brand-color-hover);
      }
      
      &.active {
        background-color: var(--hx-brand-color-3);
        color: var(--hx-gray-color-1);
        border-color: var(--hx-brand-color-3);
      }
    }
  }
  
  .chart-main {
    height: 400px;
    width: 100%;
  }
}

/* 方式3：事件列表样式 */
.event-list {
  background-color: var(--hx-bg-color-container);
  border-radius: var(--hx-radius-medium);
  margin: var(--hx-size-4);
  padding: var(--hx-size-4);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  
  h2 {
    font: var(--hx-font-title-large);
    color: var(--hx-text-color-primary);
    margin-bottom: var(--hx-size-4);
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  .event-item {
    display: flex;
    align-items: center;
    padding: var(--hx-size-3) 0;
    border-bottom: 1px solid var(--hx-border-level-1-color);
    
    &:last-child {
      border-bottom: none;
    }
    
    .event-date {
      color: var(--hx-text-color-tertiary);
      width: 100px;
      flex-shrink: 0;
    }
    
    .event-tag {
      padding: var(--hx-size-1) var(--hx-size-2);
      border-radius: var(--hx-radius-small);
      margin-right: var(--hx-size-3);
      font-size: var(--hx-font-size-body-small);
      
      &.policy {
        background-color: var(--hx-brand-color-1);
        color: var(--hx-brand-color-5);
      }
      
      &.report {
        background-color: var(--hx-warning-color-1);
        color: var(--hx-warning-color-5);
      }
      
      &.merger {
        background-color: var(--hx-success-color-1);
        color: var(--hx-success-color-5);
      }
    }
    
    .event-title {
      flex-grow: 1;
      color: var(--hx-text-color-primary);
    }
    
    .event-impact {
      width: 60px;
      text-align: center;
      padding: var(--hx-size-1) var(--hx-size-2);
      border-radius: var(--hx-radius-small);
      
      &.positive {
        background-color: var(--hx-raise-color-3);
        color: var(--hx-gray-color-1);
      }
      
      &.neutral {
        background-color: var(--hx-gray-color-5);
        color: var(--hx-gray-color-1);
      }
      
      &.negative {
        background-color: var(--hx-fall-color-3);
        color: var(--hx-gray-color-1);
      }
    }
  }
}

/* Tailwind自定义扩展 通过tailwind.config.js自动获取*/

</style>
