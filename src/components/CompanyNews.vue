<template>
  <div class="company-news card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">公司动向</h2>
        <div class="card-subtitle">自选股动态</div>
      </div>
    </div>
    
    <!-- 事件类型切换标签 -->
    <div class="industry-tabs">
      <div 
        v-for="(type, index) in eventTypes" 
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
      >
        <template v-slot:item-tag="{ item }">
          <EventTag 
            :text="item.timeTag" 
            :type-map="timeTagTypeMap" 
          />
        </template>
        
        <template v-slot:item-indicators="{ item }">
          <div class="importance-indicator" :title="`重要性：${item.importance || 1}/3`">
            <i v-for="n in 3" 
                :key="n" 
                class="importance-icon fas fa-star"
                :class="{ 
                  'filled': n <= (item.importance || 1),
                  'empty': n > (item.importance || 1)
                }"
            ></i>
          </div>
        </template>
        
        <template v-slot:item-title="{ item }">
          <div class="company-info">
            <span class="company-name">{{ item.companyName }}</span>
            <span class="company-code">{{ item.companyCode }}</span>
          </div>
          <h3 class="item-title">{{ item.title }}</h3>
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

export default {
  name: 'CompanyNews',
  components: {
    DataTimeline,
    EventTag
  },
  data() {
    return {
      currentType: 'performance',
      timeTagTypeMap: {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      },
      eventTypes: [
        { code: 'performance', name: '业绩动态' },
        { code: 'major', name: '重大事项' },
        { code: 'operation', name: '经营动态' },
        { code: 'investor', name: '投资者关系' }
      ],
      companyEvents: {
        performance: [
          {
            companyName: '贵州茅台',
            companyCode: '600519',
            date: '2025/5/15',
            title: '发布2025年一季度业绩快报',
            summary: '公司发布2025年Q1业绩快报，营收同比增长23.5%，净利润同比增长25.8%，超市场预期',
            context: '白酒行业复苏，高端酒企业绩弹性显现。',
            timeTag: '短期',
            importance: 3,
            eventType: '业绩快报',
            highlights: [
              {
                tag: '超预期增长',
                reason: '营收和利润增速均超市场预期'
              }
            ],
            benefits: [
              {
                tag: '行业复苏',
                reason: '高端白酒需求回暖，渠道库存健康'
              }
            ],
            drawbacks: [
              {
                tag: '高基数',
                reason: '下半年面临去年高基数影响'
              }
            ]
          },
          {
            companyName: '招商银行',
            companyCode: '600036',
            date: '2025/5/13',
            title: '发布2024年年度报告',
            summary: '营收同比增长12.3%，净利润增长15.6%，不良率1.02%，资本充足率15.8%',
            context: '银行业经营稳健，资产质量持续改善。',
            timeTag: '中期',
            importance: 3,
            eventType: '年报',
            highlights: [
              {
                tag: '稳健增长',
                reason: '主要经营指标稳步提升'
              }
            ],
            benefits: [
              {
                tag: '质量改善',
                reason: '资产质量保持优良，拨备充足'
              }
            ],
            drawbacks: [
              {
                tag: '息差压力',
                reason: '净息差仍面临收窄压力'
              }
            ]
          }
        ],
        major: [
          {
            companyName: '宁德时代',
            companyCode: '300750',
            date: '2025/5/14',
            title: '签署重大战略合作协议',
            summary: '与三家国际车企签署电池供应战略协议，预计未来三年供应规模超过200GWh',
            context: '全球电动化加速，动力电池龙头持续扩大市场份额。',
            timeTag: '长期',
            importance: 3,
            eventType: '战略合作',
            highlights: [
              {
                tag: '订单增长',
                reason: '新增订单显著提升未来业绩确定性'
              }
            ],
            benefits: [
              {
                tag: '份额提升',
                reason: '全球市占率有望进一步提升'
              }
            ],
            drawbacks: [
              {
                tag: '竞争加剧',
                reason: '海外市场竞争日趋激烈'
              }
            ]
          }
        ],
        operation: [
          {
            companyName: '比亚迪',
            companyCode: '002594',
            date: '2025/5/13',
            title: '发布新一代旗舰车型',
            summary: '发布新一代高端车型，搭载自研芯片和操作系统，预售价45-60万元',
            context: '新能源车企加速向上突破，品牌溢价提升。',
            timeTag: '中期',
            importance: 2,
            eventType: '新品发布',
            highlights: [
              {
                tag: '产品升级',
                reason: '技术升级带动产品力提升'
              }
            ],
            benefits: [
              {
                tag: '品牌提升',
                reason: '高端产品助力品牌向上'
              }
            ],
            drawbacks: [
              {
                tag: '市场竞争',
                reason: '高端市场竞争激烈'
              }
            ]
          },
          {
            companyName: '华为汽车',
            companyCode: '888888',
            date: '2025/5/11',
            title: '智能驾驶技术突破',
            summary: '发布新一代智能驾驶解决方案，复杂场景识别准确率提升40%',
            context: '智能驾驶技术迭代加快，产业化进程提速。',
            timeTag: '中期',
            importance: 3,
            eventType: '技术突破',
            highlights: [
              {
                tag: '技术领先',
                reason: '核心技术取得突破性进展'
              }
            ],
            benefits: [
              {
                tag: '竞争优势',
                reason: '技术优势带来市场机遇'
              }
            ],
            drawbacks: [
              {
                tag: '落地周期',
                reason: '技术产业化需要时间验证'
              }
            ]
          }
        ],
        investor: [
          {
            companyName: '招商银行',
            companyCode: '600036',
            date: '2025/5/12',
            title: '公布2024年度分红方案',
            summary: '拟每10股派发现金红利5.2元，股息率达4.5%',
            context: '银行业稳健经营，现金分红能力强。',
            timeTag: '短期',
            importance: 2,
            eventType: '利润分配',
            highlights: [
              {
                tag: '分红提升',
                reason: '分红力度超过去年，股息率具有吸引力'
              }
            ],
            benefits: [
              {
                tag: '回报提升',
                reason: '高分红提升股东回报'
              }
            ],
            drawbacks: [
              {
                tag: '资本约束',
                reason: '需平衡分红与资本补充'
              }
            ]
          }
        ]
      }
    }
  },
  computed: {
    currentTypeItems() {
      const items = this.companyEvents[this.currentType] || []
      return items.sort((a, b) => new Date(b.date) - new Date(a.date))
    }
  },
  methods: {
    switchType(code) {
      this.currentType = code
    },
    handleItemExpanded() {
      // 空方法，保留以便接收事件
    }
  }
}
</script>

<style lang="scss" scoped>
.company-news {
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
    
    .event-summary {
      margin: 0;
      font-size: 12px;
      color: var(--hx-text-color-secondary);
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      line-clamp: 2;
      overflow: hidden;
    }
  }

  .company-info {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
    
    .company-name {
      font-weight: 600;
      color: var(--hx-text-color-primary);
    }
    
    .company-code {
      font-size: 12px;
      color: var(--hx-text-color-secondary);
    }
  }

  .importance-indicator {
    display: flex;
    gap: 2px;
    
    .importance-icon {
      font-size: 12px;
      
      &.filled {
        color: var(--hx-warning-color-2);
      }
      
      &.empty {
        color: var(--hx-border-level-2-color);
      }
    }
  }
}

@media (max-width: 768px) {
  .company-news {
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
