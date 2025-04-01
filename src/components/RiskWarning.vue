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

        <template v-slot:item-preview="{ item }">
          <div class="item-preview-content">
            <div class="preview-header">
              <div class="risk-level">
                <i class="fas fa-exclamation-triangle" :class="getRiskLevelIconClass(item.riskLevel)"></i>
                <span>风险等级 {{ item.riskLevel }}</span>
              </div>
            </div>
            <h3 class="event-title">{{ item.title }}</h3>
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

export default {
  name: 'RiskWarning',
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
      riskTypes: [
        { code: 'stock', name: '个股风险' },
        { code: 'industry', name: '行业风险' },
        { code: 'market', name: '市场风险' }
      ],
      riskData: {
        stock: [
          {
            date: '2025/5/15',
            title: '【腾讯控股】业绩不及预期，云计算业务增速放缓',
            summary: '公司Q1营收同比下降15%，毛利率下滑，现金流承压',
            context: '受行业竞争加剧和成本上升影响，公司经营压力加大。',
            timeTag: '短期',
            riskLevel: '高风险',
            importance: 3,
            highlights: [
              {
                tag: '业绩下滑',
                reason: '营收和利润双双下滑，现金流压力大'
              }
            ],
            benefits: [
              {
                tag: '风险提示',
                reason: '及时提示投资者关注公司经营风险'
              }
            ],
            drawbacks: [
              {
                tag: '股价承压',
                reason: '可能对公司股价造成较大压力'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【恒瑞医药】研发失败，重点新药临床不达预期',
            summary: '公司重点研发项目III期临床试验未达到预期目标',
            context: '研发失败将影响公司未来业绩增长。',
            timeTag: '中期',
            riskLevel: '中风险',
            importance: 2,
            highlights: [
              {
                tag: '研发风险',
                reason: '临床试验数据不及预期，项目可能终止'
              }
            ],
            benefits: [
              {
                tag: '风险提示',
                reason: '帮助投资者了解公司研发风险'
              }
            ],
            drawbacks: [
              {
                tag: '估值承压',
                reason: '可能影响公司估值水平'
              }
            ]
          }
        ],
        industry: [
          {
            date: '2025/5/15',
            title: '【房地产】政策收紧，多地出台调控措施',
            summary: '多地出台房地产调控政策，融资渠道收紧',
            context: '房地产行业面临政策调控和融资压力。',
            timeTag: '中期',
            riskLevel: '高风险',
            importance: 3,
            highlights: [
              {
                tag: '政策风险',
                reason: '调控政策持续收紧，行业景气度下行'
              }
            ],
            benefits: [
              {
                tag: '风险提示',
                reason: '提示投资者关注行业政策风险'
              }
            ],
            drawbacks: [
              {
                tag: '行业承压',
                reason: '可能影响整个行业估值水平'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '【新能源】补贴退坡，行业格局面临重塑',
            summary: '新能源汽车补贴政策调整，补贴力度减弱',
            context: '补贴退坡将影响行业整体盈利能力。',
            timeTag: '短期',
            riskLevel: '中风险',
            importance: 2,
            highlights: [
              {
                tag: '政策调整',
                reason: '补贴政策调整影响行业盈利'
              }
            ],
            benefits: [
              {
                tag: '风险提示',
                reason: '帮助投资者了解政策变化影响'
              }
            ],
            drawbacks: [
              {
                tag: '盈利承压',
                reason: '可能影响行业整体盈利水平'
              }
            ]
          }
        ],
        market: [
          {
            date: '2025/5/15',
            title: '【美股】流动性收紧，美联储加息预期升温',
            summary: '美联储加息预期升温，全球流动性趋紧',
            context: '全球流动性收紧可能影响市场整体估值。',
            timeTag: '长期',
            riskLevel: '高风险',
            importance: 3,
            highlights: [
              {
                tag: '流动性风险',
                reason: '全球流动性收紧影响市场估值'
              }
            ],
            benefits: [
              {
                tag: '风险提示',
                reason: '提示投资者关注宏观风险'
              }
            ],
            drawbacks: [
              {
                tag: '市场承压',
                reason: '可能影响市场整体估值水平'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【港股】地缘政治风险上升，外资流出加剧',
            summary: '国际关系紧张，地缘政治风险加大',
            context: '地缘政治风险可能影响市场风险偏好。',
            timeTag: '中期',
            riskLevel: '中风险',
            importance: 2,
            highlights: [
              {
                tag: '地缘风险',
                reason: '地缘政治风险影响市场情绪'
              }
            ],
            benefits: [
              {
                tag: '风险提示',
                reason: '帮助投资者了解外部风险'
              }
            ],
            drawbacks: [
              {
                tag: '情绪承压',
                reason: '可能影响市场风险偏好'
              }
            ]
          },
          {
            date: '2025/5/8',
            title: '【A股】流动性风险上升，融资环境收紧',
            summary: '央行货币政策回归中性，市场流动性边际收紧',
            context: '流动性环境变化导致风险偏好下降。',
            timeTag: '短期',
            riskLevel: '中风险',
            importance: 2,
            highlights: [
              {
                tag: '流动性变化',
                reason: '货币政策边际转向，流动性环境收紧'
              }
            ],
            benefits: [
              {
                tag: '风险防范',
                reason: '有助于投资者提前应对流动性风险'
              }
            ],
            drawbacks: [
              {
                tag: '估值承压',
                reason: '高估值板块面临调整压力'
              }
            ]
          }
        ]
      }
    }
  },
  computed: {
    currentTypeItems() {
      const items = this.riskData[this.currentType] || []
      return items.sort((a, b) => new Date(a.date) - new Date(b.date))
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
    },
    handleItemExpanded() {
      // 空方法，保留以便接收事件
    },
    getRiskLevelIconClass(level) {
      return {
        '高风险': 'risk-high-icon',
        '中风险': 'risk-mid-icon',
        '低风险': 'risk-low-icon'
      }[level] || ''
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
      
      .risk-level {
        display: flex;
        align-items: center;
        gap: 4px;
        font-size: 11px;
        padding: 2px 6px;
        border-radius: 2px;
        background-color: rgba(var(--hx-error-color-rgb, 255, 0, 0), 0.1);
        
        i {
          font-size: 12px;
          
          &.risk-high-icon {
            color: var(--hx-error-color-3);
          }
          
          &.risk-mid-icon {
            color: var(--hx-warning-color-3);
          }
          
          &.risk-low-icon {
            color: var(--hx-success-color-3);
          }
        }
        
        span {
          color: var(--hx-text-color-secondary);
          white-space: nowrap;
        }
      }
    }
    
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