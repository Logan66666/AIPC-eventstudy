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
        market: [
          {
            date: '2025/5/15',
            title: '【A股】货币政策微调窗口',
            summary: '随着经济企稳，央行货币政策或边际转向，市场流动性环境面临微调',
            context: '经济复苏背景下，货币政策关注点从总量转向结构性调整。',
            timeTag: '短期',
            importance: 3,
          highlights: [
              {
                tag: '流动性变化',
                reason: '资金面边际收紧，银行间利率小幅上行'
              }
            ],
            benefits: [
              {
                tag: '板块机会',
                reason: '金融、地产等低估值板块估值修复空间打开'
              }
            ],
            drawbacks: [
              {
                tag: '高估值风险',
                reason: '高估值成长股可能面临估值压力'
              }
            ]
          },
          {
            date: '2025/5/13',
            title: '【黄金】地缘冲突加剧，避险需求上升',
            summary: '全球多地地缘政治风险升级，避险资金涌入黄金市场，金价创近期新高',
            context: '避险情绪推动贵金属价格上涨，黄金投资需求增加。',
            timeTag: '短期',
            importance: 2,
            highlights: [
              {
                tag: '避险情绪',
                reason: '全球不确定性增加，资金寻求安全资产配置'
              }
            ],
            benefits: [
              {
                tag: '价格上涨',
                reason: '避险需求+通胀预期，黄金价格表现强劲'
              }
            ],
            drawbacks: [
              {
                tag: '波动加剧',
                reason: '市场情绪波动可能导致价格剧烈震荡'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '【港股】全球贸易格局变化',
            summary: '全球贸易政策调整，区域经济合作加强，出口产业链迎来新机遇',
            context: '随着全球经济格局重塑，区域贸易合作深化。',
            timeTag: '中期',
            importance: 2,
            highlights: [
              {
                tag: '贸易政策',
                reason: '区域全面经济伙伴关系协定（RCEP）深化落地'
              }
            ],
            benefits: [
              {
                tag: '出口机会',
                reason: '相关产业链出口订单回暖，盈利能力提升'
              }
            ],
            drawbacks: [
              {
                tag: '竞争加剧',
                reason: '部分行业面临更激烈的国际竞争'
              }
            ]
          },
          {
            date: '2025/5/8',
            title: '【美股】科技巨头财报季表现超预期',
            summary: '美国科技巨头财报普遍超预期，AI相关业务收入高速增长，带动美股科技板块走强',
            context: 'AI革命进入商业化落地阶段，龙头公司优势明显。',
            timeTag: '中期',
            importance: 3,
            highlights: [
              {
                tag: 'AI商业化',
                reason: 'AI应用场景扩展，商业化落地明显加速'
              }
            ],
            benefits: [
              {
                tag: '龙头效应',
                reason: '行业整合加剧，头部企业市占率提升'
              }
            ],
            drawbacks: [
              {
                tag: '估值压力',
                reason: '高增长预期已部分反映在估值中，需警惕调整风险'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【北交所】资本市场深化改革',
            summary: '注册制全面推行，退市制度完善，资本市场生态持续优化',
            context: '资本市场制度建设不断深化，市场化程度提升。',
            timeTag: '长期',
            importance: 2,
            highlights: [
              {
                tag: '市场机制',
                reason: '优胜劣汰机制更加完善，市场资源配置效率提升'
              }
            ],
            benefits: [
              {
                tag: '优质公司',
                reason: '业绩稳健、治理规范的优质公司有望获得更高溢价'
              }
            ],
            drawbacks: [
              {
                tag: '壳资源贬值',
                reason: '退市常态化导致"壳价值"进一步降低'
              }
            ]
          },
          {
            date: '2025/5/5',
            title: '【债券】利率债供需格局改善',
            summary: '财政节奏调整，利率债供给压力缓解，叠加外资回流，债市配置价值凸显',
            context: '经济基本面企稳但仍存下行压力，债券市场韧性增强。',
            timeTag: '长期',
            importance: 1,
            highlights: [
              {
                tag: '供需改善',
                reason: '财政节奏优化，利率债供给压力缓解'
              }
            ],
            benefits: [
              {
                tag: '配置价值',
                reason: '中长期利率债收益率处于合理区间，配置价值显现'
              }
            ],
            drawbacks: [
              {
                tag: '通胀风险',
                reason: '潜在通胀压力可能影响债市表现'
              }
            ]
          }
        ],
        industry: [
          {
            date: '2025/5/15',
            title: '【新能源汽车】补贴政策出台带动销量回升',
            summary: '随着新一轮新能源汽车补贴政策出台，叠加传统汽车消费季，预计Q3智能电动车销量将迎来拐点',
            context: '政策支持叠加消费旺季，新能源汽车产业链迎来机遇。',
            timeTag: '短期',
            importance: 3,
            highlights: [
              {
                tag: '政策支持',
                reason: '新一轮补贴政策提振消费信心'
              }
            ],
            benefits: [
              {
                tag: '销量提升',
                reason: '旺季叠加政策效应，销量有望超预期'
              }
            ],
            drawbacks: [
              {
                tag: '竞争加剧',
                reason: '行业竞争日趋激烈，部分企业面临降价压力'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '【光伏产业】组件价格企稳，龙头优势显现',
            summary: '光伏组件价格企稳，产业链利润分配趋于合理，龙头企业优势显现',
            context: '光伏行业进入高质量发展阶段，产业链格局优化。',
            timeTag: '中期',
            importance: 2,
            highlights: [
              {
                tag: '价格企稳',
                reason: '组件价格止跌回升，行业盈利水平改善'
              }
            ],
            benefits: [
              {
                tag: '格局优化',
                reason: '龙头企业市占率提升，议价能力增强'
              }
            ],
            drawbacks: [
              {
                tag: '产能过剩',
                reason: '需关注新增产能释放节奏'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【半导体】国产化进程加速，自主可控成关键词',
            summary: '随着国家集成电路产业政策落地以及下半年消费电子需求回暖，国产芯片设计和制造企业有望受益',
            context: '国产替代进程加速，芯片产业链景气度提升。',
            timeTag: '长期',
            importance: 3,
            highlights: [
              {
                tag: '产业政策',
                reason: '集成电路产业支持政策持续推进'
              }
            ],
            benefits: [
              {
                tag: '需求回暖',
                reason: '下游消费电子需求逐步恢复'
              }
            ],
            drawbacks: [
              {
                tag: '技术门槛',
                reason: '高端制程仍存在较大差距'
              }
            ]
          }
        ],
        stock: [
          {
            date: '2025/5/15',
            title: '【腾讯控股】一季度业绩超预期，云计算和AI业务增速亮眼',
            summary: '龙头科技公司一季度业绩超预期，云计算和AI业务增速亮眼',
            context: 'AI和云计算需求持续增长，龙头公司业绩弹性显现。',
            timeTag: '短期',
            importance: 3,
            highlights: [
              {
                tag: '业绩超预期',
                reason: '营收同比增长25%，净利润增长30%，超市场预期'
              }
            ],
            benefits: [
              {
                tag: '估值提升',
                reason: '强劲业绩有望带动估值修复'
              }
            ],
            drawbacks: [
              {
                tag: '竞争压力',
                reason: '行业竞争加剧，研发投入压力大'
              }
            ]
          },
          {
            date: '2025/5/12',
            title: '【恒瑞医药】创新药获批上市，填补国内市场空白',
            summary: '创新药研发龙头企业创新药获批上市，填补国内市场空白',
            context: '创新药研发取得突破，进入收获期。',
            timeTag: '中期',
            importance: 2,
            highlights: [
              {
                tag: '产品突破',
                reason: '首个国产创新药获批，市场规模超百亿'
              }
            ],
            benefits: [
              {
                tag: '业绩增长',
                reason: '新药上市后有望贡献可观收入，推动业绩增长'
              }
            ],
            drawbacks: [
              {
                tag: '销售不确定性',
                reason: '新药商业化存在不确定性，需关注进医保进展'
              }
            ]
          },
          {
            date: '2025/5/10',
            title: '【宁德时代】宣布重大扩产计划，产能有望翻倍',
            summary: '新能源电池龙头宣布重大扩产计划，产能有望翻倍',
            context: '行业需求旺盛，龙头企业加速扩张。',
            timeTag: '长期',
            importance: 3,
            highlights: [
              {
                tag: '产能扩张',
                reason: '未来三年产能有望翻倍，市场份额进一步提升'
              }
            ],
            benefits: [
              {
                tag: '规模效应',
                reason: '产能扩张带来规模效应，成本优势进一步增强'
              }
            ],
            drawbacks: [
              {
                tag: '资金压力',
                reason: '大规模扩产带来资金压力，可能影响短期现金流'
              }
            ]
          }
        ]
      }
    }
  },
  computed: {
    currentTypeItems() {
      const items = this.opportunityData[this.currentType] || []
      return items.sort((a, b) => new Date(a.date) - new Date(b.date))
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