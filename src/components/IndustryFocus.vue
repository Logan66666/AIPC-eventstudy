<template>
  <div class="industry-focus card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">行业洞察</h2>
        <div class="card-subtitle">左侧行业动态前瞻</div>
      </div>
    </div>
    
    <!-- 行业切换标签 -->
      <div class="industry-tabs">
        <div 
          v-for="(industry, index) in industries" 
          :key="index" 
        class="tab-item"
        :class="{ active: currentIndustry === industry.code }"
        @click="switchIndustry(industry.code)"
        >
          {{ industry.name }}
        </div>
      </div>
      
    <!-- 时间线内容 -->
    <div class="timeline-content">
      <DataTimeline 
        :items="currentIndustryItems"
        @item-expanded="handleItemExpanded"
      >
        <template v-slot:item-tag="{ item }">
          <div class="industry-tag">
            {{ item.industry }}
          </div>
        </template>

        <template v-slot:item-preview="{ item }">
          <div class="item-preview-content">
            <div class="preview-header">
              <div class="time-tag" :class="getTimeTagClass(item.timeTag)">
                {{ item.timeTag }}
              </div>
              <div class="event-type">
                <i class="fas" :class="getEventTypeIcon(item.eventType)"></i>
                <span>{{ item.eventType }}</span>
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

export default {
  name: 'IndustryFocus',
  components: {
    DataTimeline
  },
  data() {
    return {
      currentIndustry: 'real_estate',
      industries: [
        { code: 'real_estate', name: '房地产' },
        { code: 'finance', name: '金融' },
        { code: 'technology', name: '科技' },
        { code: 'energy', name: '能源' },
        { code: 'healthcare', name: '医疗' }
      ],
      industryData: {
        real_estate: [
          {
            date: '2025/5/15',
            title: '一线城市房价持续上涨',
            summary: '北京、上海等一线城市房价环比上涨2.5%，成交量显著提升',
            context: '受政策利好和需求释放影响，一线城市房地产市场回暖。',
            industry: '房地产',
            timeTag: '短期',
            eventType: '市场动态',
            highlights: [
              {
                tag: '价格上涨',
                reason: '一线城市房价环比上涨2.5%'
              }
            ],
            benefits: [
              {
                tag: '市场回暖',
                reason: '房地产市场信心恢复'
              }
            ],
            drawbacks: [
              {
                tag: '调控压力',
                reason: '可能引发新一轮调控政策'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '房地产政策持续放松',
            summary: '多地出台购房补贴政策，首付比例下调',
            context: '地方政府加大房地产支持力度，促进市场回暖。',
            industry: '房地产',
            timeTag: '中期',
            eventType: '政策变化',
            highlights: [
              {
                tag: '政策放松',
                reason: '多地出台购房补贴政策'
              }
            ],
            benefits: [
              {
                tag: '需求释放',
                reason: '降低购房门槛，促进需求释放'
              }
            ],
            drawbacks: [
              {
                tag: '债务风险',
                reason: '可能增加地方政府债务压力'
              }
            ]
          }
        ],
        finance: [
          {
            date: '2025/5/15',
            title: '央行降准释放流动性',
            summary: '央行下调存款准备金率0.5个百分点，释放长期资金约1万亿元',
            context: '货币政策持续宽松，支持实体经济发展。',
            industry: '金融',
            timeTag: '短期',
            eventType: '政策变化',
            highlights: [
              {
                tag: '流动性释放',
                reason: '释放长期资金约1万亿元'
              }
            ],
            benefits: [
              {
                tag: '市场利好',
                reason: '增加市场流动性，提振市场信心'
              }
            ],
            drawbacks: [
              {
                tag: '通胀压力',
                reason: '可能增加通胀压力'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '银行业绩超预期',
            summary: '主要银行一季度净利润同比增长15%，不良率下降',
            context: '银行业经营状况持续改善，资产质量提升。',
            industry: '金融',
            timeTag: '中期',
            eventType: '业绩报告',
            highlights: [
              {
                tag: '业绩增长',
                reason: '净利润同比增长15%'
              }
            ],
            benefits: [
              {
                tag: '估值提升',
                reason: '业绩超预期，估值有望提升'
              }
            ],
            drawbacks: [
              {
                tag: '基数效应',
                reason: '高基数可能影响后续增长'
              }
            ]
          }
        ],
        technology: [
          {
            date: '2025/5/15',
            title: 'AI技术突破性进展',
            summary: '某科技公司发布新一代AI模型，性能提升300%',
            context: 'AI技术快速发展，推动产业升级。',
            industry: '科技',
            timeTag: '长期',
            eventType: '技术创新',
            highlights: [
              {
                tag: '技术突破',
                reason: 'AI模型性能提升300%'
              }
            ],
            benefits: [
              {
                tag: '产业升级',
                reason: '推动相关产业技术升级'
              }
            ],
            drawbacks: [
              {
                tag: '竞争加剧',
                reason: '可能加剧行业竞争'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '芯片行业新政策',
            summary: '国家出台芯片产业支持政策，加大研发投入',
            context: '政策支持芯片产业发展，提升自主创新能力。',
            industry: '科技',
            timeTag: '中期',
            eventType: '政策变化',
            highlights: [
              {
                tag: '政策支持',
                reason: '加大芯片产业研发投入'
              }
            ],
            benefits: [
              {
                tag: '发展机遇',
                reason: '为芯片企业提供发展机遇'
              }
            ],
            drawbacks: [
              {
                tag: '投入压力',
                reason: '企业面临较大研发投入压力'
              }
            ]
          }
        ],
        energy: [
          {
            date: '2025/5/15',
            title: '新能源装机量创新高',
            summary: '一季度新能源装机量同比增长50%，储能需求大增',
            context: '新能源产业快速发展，储能需求提升。',
            industry: '能源',
            timeTag: '中期',
            eventType: '市场动态',
            highlights: [
              {
                tag: '装机增长',
                reason: '新能源装机量同比增长50%'
              }
            ],
            benefits: [
              {
                tag: '产业机会',
                reason: '储能产业迎来发展机遇'
              }
            ],
            drawbacks: [
              {
                tag: '并网压力',
                reason: '电网消纳压力增加'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '储能行业规划发布',
            summary: '国家发布储能产业发展规划，明确发展目标',
            context: '储能产业迎来政策支持，发展前景广阔。',
            industry: '能源',
            timeTag: '长期',
            eventType: '政策变化',
            highlights: [
              {
                tag: '政策支持',
                reason: '明确储能产业发展目标'
              }
            ],
            benefits: [
              {
                tag: '发展机遇',
                reason: '储能产业迎来发展机遇'
              }
            ],
            drawbacks: [
              {
                tag: '技术挑战',
                reason: '面临技术突破和成本降低压力'
              }
            ]
          }
        ],
        healthcare: [
          {
            date: '2025/5/15',
            title: '创新药审批加速',
            summary: '创新药审批时间缩短50%，研发效率提升',
            context: '药品审批制度改革，促进创新药研发。',
            industry: '医疗',
            timeTag: '中期',
            eventType: '政策变化',
            highlights: [
              {
                tag: '审批加速',
                reason: '创新药审批时间缩短50%'
              }
            ],
            benefits: [
              {
                tag: '研发效率',
                reason: '提高创新药研发效率'
              }
            ],
            drawbacks: [
              {
                tag: '质量风险',
                reason: '可能增加药品质量风险'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '医保目录调整',
            summary: '医保目录新增50个创新药，支付标准优化',
            context: '医保政策支持创新药发展，提升可及性。',
            industry: '医疗',
            timeTag: '短期',
            eventType: '政策变化',
            highlights: [
              {
                tag: '目录更新',
                reason: '新增50个创新药'
              }
            ],
            benefits: [
              {
                tag: '市场扩容',
                reason: '创新药市场空间扩大'
              }
            ],
            drawbacks: [
              {
                tag: '支付压力',
                reason: '医保基金支付压力增加'
              }
            ]
          }
        ]
      }
    }
  },
  computed: {
    currentIndustryItems() {
      const items = this.industryData[this.currentIndustry] || []
      return items.sort((a, b) => new Date(a.date) - new Date(b.date))
    }
  },
  methods: {
    switchIndustry(code) {
      this.currentIndustry = code
    },
    handleItemExpanded() {
      // 空方法，保留以便接收事件
    },
    getTimeTagClass(tag) {
      return {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      }[tag] || ''
    },
    getEventTypeIcon(type) {
      return {
        '市场动态': 'fa-chart-line',
        '政策变化': 'fa-file-alt',
        '技术创新': 'fa-lightbulb',
        '业绩报告': 'fa-file-invoice-dollar'
      }[type] || 'fa-info-circle'
    }
  }
}
</script>

<style lang="scss" scoped>
.industry-focus {
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
      
      .time-tag {
        font-size: 11px;
        padding: 2px 6px;
        border-radius: 2px;
        white-space: nowrap;
        
        &.time-short {
          background-color: rgba(var(--hx-brand-color-rgb), 0.1);
          color: var(--hx-brand-color-3);
        }
        
        &.time-mid {
          background-color: rgba(var(--hx-warning-color-rgb), 0.1);
          color: var(--hx-warning-color-3);
        }
        
        &.time-long {
          background-color: rgba(var(--hx-sec-brand-color-rgb), 0.1);
          color: var(--hx-sec-brand-color-3);
        }
      }
      
      .event-type {
    display: flex;
        align-items: center;
        gap: 4px;
        font-size: 11px;
        
        i {
          font-size: 12px;
          color: var(--hx-text-color-secondary);
        }
        
        span {
          color: var(--hx-text-color-secondary);
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
}

@media (max-width: 768px) {
  .industry-focus {
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