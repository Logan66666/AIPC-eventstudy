<template>
  <div class="chart-container" :style="{ width: chartWidth, height: chartHeight }">
    <h2 class="chart-title">{{ title }}</h2>
    <div ref="chartRef" class="chart-main"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'CustomChart',
  props: {
    title: {
      type: String,
      default: '图表标题'
    },
    chartWidth: {
      type: String,
      default: '100%'
    },
    chartHeight: {
      type: String,
      default: '400px'
    },
    chartData: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      chart: null
    };
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.chartRef);
      const option = {
        title: {
          text: this.title,
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
        xAxis: {
          type: 'category',
          data: this.chartData.map(item => item.name),
          axisLine: {
            lineStyle: {
              color: getComputedStyle(document.documentElement).getPropertyValue('--hx-border-level-1-color').trim()
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: '{value}%',
            color: getComputedStyle(document.documentElement).getPropertyValue('--hx-text-color-secondary').trim()
          }
        },
        series: [
          {
            name: '数据系列',
            type: 'line',
            data: this.chartData.map(item => item.value),
            lineStyle: {
              color: getComputedStyle(document.documentElement).getPropertyValue('--hx-brand-color-3').trim()
            }
          }
        ]
      };
      this.chart.setOption(option);
    }
  },
  mounted() {
    this.initChart();
    window.addEventListener('resize', this.chart.resize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.chart.resize);
  }
}
</script>

<style scoped>
.chart-container {
  background-color: var(--hx-bg-color-container);
  border-radius: var(--hx-radius-medium);
  margin: var(--hx-size-4);
  padding: var(--hx-size-4);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.chart-title {
  font: var(--hx-font-title-large);
  color: var(--hx-text-color-primary);
  margin-bottom: var(--hx-size-4);
}

.chart-main {
  width: 100%;
  height: 100%;
}
</style> 