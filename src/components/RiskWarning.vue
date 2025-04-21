<template>
  <div class="risk-warning card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">风险预警</h2>
        <div class="card-subtitle">市场风险事件提示</div>
      </div>
    </div>

    <!-- 风险类型切换标签 -->
    <div class="industry-tabs">
      <div 
        v-for="(type, index) in riskTypes" 
        :key="index"
        class="tab-item"
        :class="{ active: currentType === type.code }"
        @click="switchType(type.code)"
      >
        {{ type.name }}
      </div>
    </div>

    <!-- 时间线内容 -->
    <div class="timeline-content">
      <DataTimeline 
        :items="currentTypeItems"
        :expanded-item="expandedItem"
        @item-expanded="handleItemExpanded"
        :empty-text="`暂无${getEmptyText}数据`"
        empty-subtext="我们正在整理相关风险事件，请稍后查看"
      >
        <template v-slot:item-tag="{ item }">
          <EventTag 
            :text="item.timeTag" 
            :type-map="timeTagTypeMap" 
          />
        </template>

        <template v-slot:item-indicators="{ item }">
          <div class="risk-importance-indicator" :title="`风险等级：${item.importance || 1}/3`">
            <i v-for="n in 3" 
                :key="n" 
                class="importance-icon fas fa-exclamation-triangle"
                :class="{ 
                  'filled': n <= (item.importance || 1),
                  'empty': n > (item.importance || 1)
                }"
            ></i>
          </div>
        </template>

        <template v-slot:item-title="{ item }">
          <h3 class="item-title">{{ item.item?.stockname ? `【${item.item.stockname}】${item.title}` : item.title }}</h3>
        </template>

        <template v-slot:item-preview="{ item }">
          <div class="item-preview-content">
            <div class="preview-header">
            </div>
            <p class="event-summary">{{ item.summary }}</p>
          </div>
        </template>
      </DataTimeline>
    </div>
  </div>
</template>

<script>
import DataTimeline from './ui/DataTimeline.vue'
import EventTag from './ui/EventTag.vue'
import { 
  riskWarningMockData_stock,
  riskWarningMockData_industry,
  riskWarningMockData_market
} from '../utils/mockData'

export default {
  name: 'RiskWarning',
  components: {
    DataTimeline,
    EventTag
  },
  data() {
    return {
      currentType: 'market',
      expandedItem: null,
      timeTagTypeMap: {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      },
      riskTypes: [
        { code: 'market', name: '市场风险' },
        { code: 'industry', name: '行业风险' },
        { code: 'stock', name: '个股风险' }
      ],
      riskData: {
        stock: [],
        industry: [],
        market: []
      }
    }
  },
  computed: {
    currentTypeItems() {
      return this.riskData[this.currentType] || []
    },
    getEmptyText() {
      const typeMap = {
        'stock': '个股风险',
        'industry': '行业风险',
        'market': '市场风险'
      }
      return typeMap[this.currentType] || '相关'
    }
  },
  methods: {
    switchType(code) {
      this.currentType = code
      this.expandedItem = null
    },
    handleItemExpanded(data) {
      this.expandedItem = data.expanded ? data.index : null
    },
    parseJsonFromResponse(response) {
      try {
        if (response?.response?.text) {
          // 获取原始文本
          let jsonStr = response.response.text;
          
          // 移除markdown代码块标记
          jsonStr = jsonStr.replace(/^[\s\n]*```json[\s\n]*/i, '');
          jsonStr = jsonStr.replace(/[\s\n]*```[\s\n]*$/i, '');
          
          // 修复日期格式错误 - 处理多种情况
          jsonStr = jsonStr.replace(/"date":(\d{4}\/\d{1,2}\/\d{1,2})"/, '"date":"$1"');  // 右引号缺左引号
          jsonStr = jsonStr.replace(/"date":(\d{4}\/\d{1,2}\/\d{1,2}),/, '"date":"$1",'); // 无引号的日期
          
          // 尝试解析JSON
          let parsedData = JSON.parse(jsonStr);
          
          return parsedData;
        }
        return [];
      } catch (error) {
        console.error('解析JSON失败:', error.message);
        return [];
      }
    },
    processRiskData(mockData, type) {
      try {
        if (!mockData) {
          console.warn(`${type}风险数据不存在`);
          return [];
        }
        
        const parsedData = this.parseJsonFromResponse(mockData);
        if (!Array.isArray(parsedData)) {
          console.warn(`${type}风险数据格式错误:`, parsedData);
          return [];
        }
        
        // 标准化日期格式
        const processedData = parsedData.map(item => ({
          ...item,
          date: item.date.split('/').map(n => n.padStart(2, '0')).join('/')
        }));
        
        return processedData;
      } catch (error) {
        console.error(`处理${type}风险数据失败:`, error);
        return [];
      }
    }
  },
  async created() {
    try {
      // 统一处理三种类型的数据
      const mockDataMap = {
        stock: riskWarningMockData_stock,
        industry: riskWarningMockData_industry,
        market: riskWarningMockData_market
      };
      
      // 处理并排序所有类型的数据
      Object.entries(mockDataMap).forEach(([key, mockData]) => {
        this.riskData[key] = this.processRiskData(mockData, key)
          .sort((a, b) => new Date(b.date) - new Date(a.date));
      });
    } catch (error) {
      console.error('加载风险数据失败:', error);
    }
  }
}
</script>

<style lang="scss" scoped>
.risk-warning {
  height: 100%;
  max-height: 600px;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  
  .industry-header {
    padding: var(--hx-comp-paddingTB-s) var(--hx-comp-paddingLR-s);
    flex-shrink: 0;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    
    .header-main {
      flex: 1;
      
      .secondary-title {
        position: relative;
        
        &::before {
          content: '';
          display: inline-block;
          width: 4px;
          height: 16px;
          background-color: var(--hx-border-level-3-color);
          margin-right: 8px;
          border-radius: 2px;
          vertical-align: middle;
        }
      }
      
      .card-subtitle {
        margin-top: 4px;
        font-size: 12px;
        color: var(--hx-text-color-secondary);
      }
    }
  }

  .industry-tabs {
    display: flex;
    padding: 0 var(--hx-comp-paddingLR-s);
    gap: var(--hx-comp-margin-s);
    background-color: var(--hx-bg-color-container);
    overflow-x: auto;
    
    &::-webkit-scrollbar {
      height: 4px;
    }
    
    &::-webkit-scrollbar-track {
      background: var(--hx-bg-color-container);
    }
    
    &::-webkit-scrollbar-thumb {
      background: var(--hx-bg-color-specialcomponent);
      border-radius: 2px;
    }

    .tab-item {
      padding: 4px 8px;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
      color: var(--hx-text-color-secondary);
      font-size: 13px;
      position: relative;
      
      &:hover {
        color: var(--hx-text-color-primary);
      }
      
      &.active {
        color: var(--hx-brand-color-3);
        font-weight: 600;
        
        &::after {
          content: '';
          position: absolute;
          bottom: 0;
          left: 0;
          width: 100%;
          height: 2px;
          background-color: var(--hx-brand-color-3);
        }
      }
    }
  }

  .timeline-content {
    flex: 1;
    overflow: hidden;
    padding: var(--hx-comp-paddingTB-s) 0;
  }

  .item-preview-content {
    flex: 1;
    min-width: 0;
    
    .preview-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }
    
    .event-summary {
      margin: 0;
      font-size: 12px;
      color: var(--hx-text-color-secondary);
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
  }

  // 展开状态下移除行数限制
  .timeline-item.expanded {
    .event-summary {
      display: block;
      -webkit-line-clamp: unset;
      overflow: visible;
    }
  }

  // 重要性指标样式
  .risk-importance-indicator {
    display: flex;
    gap: 2px;
    flex-shrink: 0;
    margin-left: 6px;
    
    .importance-icon {
      font-size: 10px;
      
      &.filled {
        color: var(--hx-warning-color-2, #f59e0b);
      }
      
      &.empty {
        color: var(--hx-border-level-2-color);
      }
    }
  }
}

@media (max-width: 768px) {
  .risk-warning {
    .industry-tabs {
      padding: 0 var(--hx-comp-paddingLR-xs);
      
      .tab-item {
        padding: 6px 8px;
        font-size: 12px;
      }
    }
  }
}
</style> 