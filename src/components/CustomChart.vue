<template>
  <div class="custom-chart card">
    <div class="chart-header">
      <h2 class="card-title tertiary-title">市场表现</h2>
      <div class="card-subtitle">关键指数与板块走势</div>
      
      <div class="chart-controls">
        <div class="period-selector">
          <button 
            v-for="period in periods" 
            :key="period.value" 
            class="period-btn" 
            :class="{ active: selectedPeriod === period.value }"
            @click="selectPeriod(period.value)"
          >
            {{ period.label }}
          </button>
        </div>
        
        <div class="chart-type-selector">
          <button 
            class="type-btn" 
            :class="{ active: chartType === 'line' }"
            @click="chartType = 'line'"
          >
            <span class="type-icon">📈</span>
          </button>
          <button 
            class="type-btn" 
            :class="{ active: chartType === 'bar' }"
            @click="chartType = 'bar'"
          >
            <span class="type-icon">📊</span>
          </button>
        </div>
      </div>
    </div>
    
    <div class="chart-content">
      <div class="chart-container" ref="chartContainer">
        <!-- 图表将在此渲染 -->
      </div>
      
      <div class="chart-legend">
        <div 
          v-for="(item, index) in chartData" 
          :key="index" 
          class="legend-item"
          @click="toggleSeries(index)"
          :class="{ 'inactive': !item.visible }"
        >
          <span class="legend-color" :style="{ backgroundColor: item.color }"></span>
          <span class="legend-label">{{ item.name }}</span>
          <span class="legend-value" :class="{ 'positive': item.change > 0, 'negative': item.change < 0 }">
            {{ item.change > 0 ? '+' : '' }}{{ item.change.toFixed(2) }}%
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts/core';
import { LineChart, BarChart } from 'echarts/charts';
import { 
  TitleComponent, 
  TooltipComponent, 
  GridComponent, 
  DatasetComponent, 
  TransformComponent,
  LegendComponent
} from 'echarts/components';
import { LabelLayout, UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';

// 注册必要的组件
echarts.use([
  TitleComponent, 
  TooltipComponent, 
  GridComponent, 
  DatasetComponent, 
  TransformComponent,
  LegendComponent,
  LabelLayout,
  UniversalTransition,
  LineChart,
  BarChart,
  CanvasRenderer
]);

export default {
  name: 'CustomChart',
  data() {
    return {
      chart: null,
      chartType: 'line',
      selectedPeriod: '1d',
      periods: [
        { label: '日', value: '1d' },
        { label: '周', value: '1w' },
        { label: '月', value: '1m' },
        { label: '季', value: '3m' },
        { label: '年', value: '1y' }
      ],
      chartData: [
        { 
          name: '上证指数', 
          color: '#FB7185', 
          data: [3250, 3260, 3270, 3265, 3280, 3290, 3310], 
          change: 1.85,
          visible: true
        },
        { 
          name: '恒生指数', 
          color: '#60A5FA', 
          data: [20100, 20050, 20200, 20300, 20250, 20400, 20500], 
          change: 1.99,
          visible: true
        },
        { 
          name: '创业板指', 
          color: '#34D399', 
          data: [2100, 2110, 2105, 2115, 2130, 2140, 2160], 
          change: 2.86,
          visible: true
        },
        { 
          name: '纳斯达克', 
          color: '#F59E0B', 
          data: [15600, 15650, 15700, 15720, 15680, 15750, 15800], 
          change: 1.28,
          visible: true
        },
        { 
          name: '道琼斯', 
          color: '#E879F9', 
          data: [34500, 34550, 34600, 34580, 34620, 34700, 34750], 
          change: 0.72,
          visible: true
        }
      ]
    }
  },
  mounted() {
    this.initChart();
    window.addEventListener('resize', this.resizeChart);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.resizeChart);
    if (this.chart) {
      this.chart.dispose();
    }
  },
  methods: {
    initChart() {
      if (this.chart) {
        this.chart.dispose();
      }
      
      this.chart = echarts.init(this.$refs.chartContainer);
      this.updateChart();
    },
    updateChart() {
      if (!this.chart) return;
      
      const visibleSeries = this.chartData
        .filter(item => item.visible)
        .map(item => {
          return {
            name: item.name,
            type: this.chartType,
            data: item.data,
            smooth: true,
            symbolSize: 0,
            lineStyle: {
              width: 2,
              color: item.color
            },
            itemStyle: {
              color: item.color
            }
          };
        });
      
      const option = {
        tooltip: {
          trigger: 'axis',
          backgroundColor: 'rgba(0, 0, 0, 0.7)',
          borderColor: 'rgba(255, 255, 255, 0.1)',
          borderWidth: 1,
          textStyle: {
            color: '#fff'
          },
          confine: true
        },
        grid: {
          left: '3%',
          right: '3%',
          bottom: '3%',
          top: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
          axisLine: {
            lineStyle: {
              color: 'rgba(255, 255, 255, 0.1)'
            }
          },
          axisLabel: {
            color: 'rgba(255, 255, 255, 0.5)'
          },
          splitLine: {
            show: false
          }
        },
        yAxis: {
          type: 'value',
          splitLine: {
            lineStyle: {
              color: 'rgba(255, 255, 255, 0.05)'
            }
          },
          axisLabel: {
            color: 'rgba(255, 255, 255, 0.5)'
          },
          axisLine: {
            show: false
          }
        },
        series: visibleSeries
      };
      
      this.chart.setOption(option);
    },
    resizeChart() {
      if (this.chart) {
        this.chart.resize();
      }
    },
    selectPeriod(period) {
      this.selectedPeriod = period;
      // 在实际应用中，这里会根据选择的时间段加载不同的数据
      this.updateChart();
    },
    toggleSeries(index) {
      this.chartData[index].visible = !this.chartData[index].visible;
      this.updateChart();
    }
  },
  watch: {
    chartType() {
      this.updateChart();
    }
  }
}
</script>

<style scoped lang="scss">
.custom-chart {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .chart-header {
    margin-bottom: var(--spacing-md);
    
    .chart-controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: var(--spacing-md);
      
      .period-selector {
        display: flex;
        background-color: rgba(255, 255, 255, 0.03);
        border-radius: var(--radius-lg);
        padding: 4px;
        
        .period-btn {
          background: none;
          border: none;
          color: var(--text-secondary);
          cursor: pointer;
          padding: 5px 12px;
          border-radius: var(--radius-md);
          font-size: 13px;
          transition: all 0.2s ease;
          
          &:hover {
            color: var(--text-primary);
          }
          
          &.active {
            background-color: rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
          }
        }
      }
      
      .chart-type-selector {
        display: flex;
        gap: 8px;
        
        .type-btn {
          background: none;
          border: none;
          color: var(--text-secondary);
          cursor: pointer;
          width: 32px;
          height: 32px;
          display: flex;
          align-items: center;
          justify-content: center;
          border-radius: var(--radius-md);
          transition: all 0.2s ease;
          background-color: rgba(255, 255, 255, 0.03);
          
          &:hover {
            background-color: rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
          }
          
          &.active {
            background-color: rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
          }
          
          .type-icon {
            font-size: 16px;
          }
        }
      }
    }
  }
  
  .chart-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    
    .chart-container {
      flex: 1;
      min-height: 240px;
    }
    
    .chart-legend {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: var(--spacing-md);
      padding-top: var(--spacing-sm);
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      
      .legend-item {
        display: flex;
        align-items: center;
        gap: 6px;
        cursor: pointer;
        transition: opacity 0.2s ease;
        
        &.inactive {
          opacity: 0.5;
        }
        
        .legend-color {
          width: 12px;
          height: 12px;
          border-radius: 3px;
        }
        
        .legend-label {
          font-size: 13px;
          color: var(--text-secondary);
        }
        
        .legend-value {
          font-size: 13px;
          font-weight: 500;
          
          &.positive {
            color: var(--color-success);
          }
          
          &.negative {
            color: var(--color-danger);
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .custom-chart {
    .chart-header {
      .chart-controls {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
        
        .period-selector {
          width: 100%;
          justify-content: space-between;
          
          .period-btn {
            padding: 4px 8px;
            font-size: 12px;
          }
        }
      }
    }
    
    .chart-content {
      .chart-container {
        min-height: 200px;
      }
      
      .chart-legend {
        flex-direction: column;
        gap: 8px;
        
        .legend-item {
          justify-content: space-between;
          
          .legend-label {
            flex: 1;
          }
        }
      }
    }
  }
}
</style> 