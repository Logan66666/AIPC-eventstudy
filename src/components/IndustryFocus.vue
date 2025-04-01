<template>
  <div class="industry-focus card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">行业洞察</h2>
        <div class="card-subtitle">热门行业动态与发展趋势</div>
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
          <EventTag :text="item.eventType" :type="getEventTypeClass(item.eventType)" />
        </template>
        
        <template v-slot:item-title="{ item }">
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
  name: 'IndustryFocus',
  components: {
    DataTimeline,
    EventTag
  },
  data() {
    return {
      currentIndustry: 'real_estate',
      timeTagTypeMap: {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      },
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
            title: '【房地产】一线城市房价环比上涨，市场预期改善',
            summary: '一线城市新房和二手房价格环比上涨，成交量持续回暖，市场信心逐步恢复',
            context: '房地产市场企稳回暖，重点城市带动作用显现。',
            timeTag: '短期',
            importance: 3,
            eventType: '市场表现',
            highlights: [
              {
                tag: '成交回暖',
                reason: '一线城市带动，市场预期改善'
              }
            ],
            benefits: [
              {
                tag: '信心恢复',
                reason: '市场预期改善带动相关产业链复苏'
              }
            ],
            drawbacks: [
              {
                tag: '分化加剧',
                reason: '城市间分化明显，三四线压力仍大'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '【房企科技】智慧社区解决方案突破，获多地采用',
            summary: '龙头房企智慧社区解决方案在多个城市落地，物业服务数字化升级提速',
            context: '房地产行业数字化转型提速，服务模式创新。',
            timeTag: '中期',
            importance: 2,
            eventType: '技术突破',
            highlights: [
              {
                tag: '技术创新',
                reason: '智慧社区解决方案实现突破，服务效率提升'
              }
            ],
            benefits: [
              {
                tag: '服务升级',
                reason: '物业服务数字化带来新的增长点'
              }
            ],
            drawbacks: [
              {
                tag: '投入压力',
                reason: '技术升级需要较大资金投入'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【房地产政策】差异化住房信贷政策出台',
            summary: '央行、银保监会联合发文，实施城市差异化住房信贷政策',
            context: '因城施策持续深化，政策工具箱不断丰富。',
            timeTag: '长期',
            importance: 3,
            eventType: '政策动向',
            highlights: [
              {
                tag: '政策优化',
                reason: '差异化信贷政策有利于市场平稳发展'
              }
            ],
            benefits: [
              {
                tag: '融资改善',
                reason: '优质房企融资环境有望改善'
              }
            ],
            drawbacks: [
              {
                tag: '执行难度',
                reason: '政策落地执行存在不确定性'
              }
            ]
          }
        ],
        technology: [
          {
            date: '2025/5/15',
            title: '【AI芯片】国产AI芯片算力突破，性能提升50%',
            summary: '多家芯片企业发布新一代AI芯片，算力较上代提升显著，获头部互联网公司采购',
            context: '国产AI芯片加速突破，产业链本土化提速。',
            timeTag: '短期',
            importance: 3,
            eventType: '技术突破',
            highlights: [
              {
                tag: '性能提升',
                reason: '新一代产品性能大幅提升，达到国际先进水平'
              }
            ],
            benefits: [
              {
                tag: '市场认可',
                reason: '头部客户采购证明产品竞争力'
              }
            ],
            drawbacks: [
              {
                tag: '研发投入',
                reason: '持续突破需要大量研发投入'
              }
            ]
          },
          {
            date: '2025/5/13',
            title: '【软件服务】国产基础软件市占率提升',
            summary: '国产操作系统和数据库在政企市场渗透率持续提升，商业化生态逐步完善',
            context: '基础软件国产化进程加速，产业链生态持续完善。',
            timeTag: '中期',
            importance: 2,
            eventType: '市场表现',
            highlights: [
              {
                tag: '份额提升',
                reason: '政企市场国产化率显著提升'
              }
            ],
            benefits: [
              {
                tag: '生态完善',
                reason: '商业化生态逐步成熟'
              }
            ],
            drawbacks: [
              {
                tag: '竞争加剧',
                reason: '国际厂商加大本土化力度'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【科技监管】数据安全法配套政策落地',
            summary: '多部委联合发布数据安全配套政策，明确重点行业监管要求',
            context: '数据安全监管框架完善，行业发展更加规范。',
            timeTag: '长期',
            importance: 3,
            eventType: '政策动向',
            highlights: [
              {
                tag: '政策完善',
                reason: '监管框架更加清晰，有利于长期发展'
              }
            ],
            benefits: [
              {
                tag: '规范发展',
                reason: '有助于行业良性竞争'
              }
            ],
            drawbacks: [
              {
                tag: '合规成本',
                reason: '企业合规成本上升'
              }
            ]
          }
        ],
        healthcare: [
          {
            date: '2025/5/15',
            title: '【医疗器械】国产高端医疗设备获批上市',
            summary: '多款国产高端医疗设备获批上市，打破国外垄断，性价比优势明显',
            context: '高端医疗器械国产化取得突破，进口替代加速。',
            timeTag: '短期',
            importance: 3,
            eventType: '技术突破',
            highlights: [
              {
                tag: '技术突破',
                reason: '关键技术取得突破，打破国外垄断'
              }
            ],
            benefits: [
              {
                tag: '成本优势',
                reason: '高性价比优势有利于市场推广'
              }
            ],
            drawbacks: [
              {
                tag: '市场考验',
                reason: '临床认可需要时间积累'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '【医药流通】"两票制"推广深化，行业集中度提升',
            summary: '医药流通"两票制"向更多地区推广，龙头企业市占率持续提升',
            context: '医药流通领域改革深化，行业整合加速。',
            timeTag: '中期',
            importance: 2,
            eventType: '市场表现',
            highlights: [
              {
                tag: '集中度提升',
                reason: '政策推动行业整合，龙头优势扩大'
              }
            ],
            benefits: [
              {
                tag: '效率提升',
                reason: '渠道扁平化提升流通效率'
              }
            ],
            drawbacks: [
              {
                tag: '转型压力',
                reason: '中小企业转型压力加大'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【医保政策】医保目录调整政策出台',
            summary: '国家医保局发布新版医保目录调整方案，优化准入规则',
            context: '医保支付改革持续深化，行业格局面临重塑。',
            timeTag: '长期',
            importance: 3,
            eventType: '政策动向',
            highlights: [
              {
                tag: '政策优化',
                reason: '准入规则更加科学，激励创新'
              }
            ],
            benefits: [
              {
                tag: '创新激励',
                reason: '有利于创新药研发投入'
              }
            ],
            drawbacks: [
              {
                tag: '价格压力',
                reason: '医保控费趋严，降价压力加大'
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
    getEventTypeClass(type) {
      const typeClasses = {
        '政策动向': 'event-policy',
        '技术突破': 'event-tech',
        '市场表现': 'event-market'
      };
      return typeClasses[type] || '';
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

/* 自定义EventTag样式 */
:deep(.event-tag) {
  &.event-policy {
    background-color: rgba(245, 158, 11, 0.15);
    color: #f59e0b; /* 黄色 - 政策动向 */
  }
  
  &.event-tech {
    background-color: rgba(239, 68, 68, 0.15);
    color: #ef4444; /* 红色 - 技术突破 */
  }
  
  &.event-market {
    background-color: rgba(36, 107, 248, 0.15);
    color: var(--hx-brand-color-3); /* 蓝色 - 市场表现 */
  }
}

/* 调整preview-header样式 */
.preview-header {
  display: flex;
  gap: 8px;
  margin-bottom: 4px;
}
</style> 