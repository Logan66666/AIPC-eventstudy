<template>
  <div class="investment-opportunities card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">埋伏机会</h2>
      <div class="card-subtitle">左侧投资机会前瞻</div>
      </div>
    </div>
    
    <!-- 机会类型切换标签 -->
    <div class="industry-tabs">
      <div 
        v-for="(type, index) in opportunityTypes" 
        :key="index"
        class="tab-item"
        :class="{ active: currentType === type.code }"
        @click="switchType(type.code)"
      >
        {{ type.name }}
            </div>
          </div>
          
    <!-- 内容区域 -->
    <div class="timeline-content">
      <DataTimeline 
        :items="currentTypeItems"
        @item-expanded="handleItemExpanded"
        :empty-text="`暂无${getEmptyText}数据`"
        empty-subtext="我们正在整理相关数据，请稍后查看"
      >
        <template v-slot:item-tag="{ item }">
          <EventTag 
            :text="item.timeTag" 
            :type-map="timeTagTypeMap" 
          />
        </template>
        
        <template v-slot:item-indicators="{ item }">
          <div class="importance-indicator" :title="`机会等级：${item.importance || 1}/3`">
            <i v-for="n in 3" 
                :key="n" 
                class="importance-icon fas fa-coins"
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
  InvestmentOpportunitiesMockData_stock,
  InvestmentOpportunitiesMockData_industry,
  InvestmentOpportunitiesMockData_market
} from '../utils/mockData'

export default {
  name: 'InvestmentOpportunity',
  components: {
    DataTimeline,
    EventTag
  },
  data() {
    return {
      currentType: 'stock',
      timeTagTypeMap: {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      },
      opportunityTypes: [
        { code: 'stock', name: '个股机会' },
        { code: 'industry', name: '行业机会' },
        { code: 'market', name: '市场机会' }
      ],
      opportunityData: {
        stock: [],
        industry: [],
        market: []
      }
    }
  },
  computed: {
    currentTypeItems() {
      return this.opportunityData[this.currentType] || []
    },
    getEmptyText() {
      const typeMap = {
        'stock': '个股机会',
        'industry': '行业机会',
        'market': '市场机会'
      }
      return typeMap[this.currentType] || '相关'
    }
  },
  methods: {
    switchType(code) {
      this.currentType = code
    },
    handleItemExpanded() {
      // 空方法，保留以便接收事件
    },
    parseJsonFromResponse(response) {
      try {
        if (response?.response?.text) {
          const jsonStr = response.response.text.replace(/```json\n|\n```/g, '')
          return JSON.parse(jsonStr)
        }
        return []
      } catch (error) {
        console.error('Failed to parse response:', error)
        return []
      }
    }
  },
  async created() {
    try {
      // 分别获取三种类型的数据
      this.opportunityData.stock = this.parseJsonFromResponse(InvestmentOpportunitiesMockData_stock)
      this.opportunityData.industry = this.parseJsonFromResponse(InvestmentOpportunitiesMockData_industry)
      this.opportunityData.market = this.parseJsonFromResponse(InvestmentOpportunitiesMockData_market)
      
      // 对每种类型的数据按日期排序
      Object.keys(this.opportunityData).forEach(key => {
        this.opportunityData[key] = this.opportunityData[key].sort((a, b) => 
          new Date(b.date) - new Date(a.date)
        )
      })
    } catch (error) {
      console.error('Failed to fetch opportunities:', error)
    }
  }
}
</script>

<style lang="scss" scoped>
.investment-opportunities {
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
    
    .event-title {
      margin: 0 0 4px;
      font-size: 14px;
      font-weight: 600;
      color: var(--hx-text-color-primary);
      line-height: 1.4;
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
}

@media (max-width: 768px) {
  .investment-opportunities {
    .industry-tabs {
      padding: 0 var(--hx-comp-paddingLR-xs);
      
      .tab-item {
        padding: 6px 8px;
        font-size: 12px;
      }
    }
  }
}

// 重要性指标样式
.importance-indicator {
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
</style> 