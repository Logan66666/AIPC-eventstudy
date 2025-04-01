<template>
  <div class="policy-catalysts card">
    <div class="policy-header">
      <div class="header-main">
      <h2 class="card-title secondary-title">政策催化</h2>
      <div class="card-subtitle">重要经济政策与市场影响</div>
    </div>
    
      <!-- 使用新的下拉菜单组件 -->
      <DropdownSelect
        v-model="selectedTypes"
        :options="sourceTypes.map(type => ({
          label: type,
          value: type,
          badgeClass: getSourceClass(type)
        }))"
        placeholder="筛选类型"
        all-text="全部类型"
      />
    </div>
    
    <div class="policy-content">
      <!-- 使用DataTimeline组件 -->
      <DataTimeline :items="filteredPolicies" @item-expanded="handleExpand">
        <!-- 自定义源标签 -->
        <template v-slot:item-tag="{ item }">
          <EventTag :text="item.source" />
        </template>
        
        <!-- 自定义指标 -->
        <template v-slot:item-indicators="{ item }">
          <div class="importance-indicator" :title="`重要性：${item.importance}/3`">
            <i v-for="n in 3" 
                :key="n" 
                class="importance-icon"
                :class="{ 
                  'fas fa-star filled': n <= item.importance,
                  'far fa-star': n > item.importance 
                }"
            ></i>
          </div>
        </template>
      </DataTimeline>
    </div>
  </div>
</template>

<script>
// 引入FontAwesome
import '@fortawesome/fontawesome-free/css/all.css'
// 引入自定义组件
import DataTimeline from './ui/DataTimeline.vue'
import EventTag from './ui/EventTag.vue'
import DropdownSelect from './ui/DropdownSelect.vue'

export default {
  name: 'PolicyCatalysts',
  components: {
    DataTimeline,
    EventTag,
    DropdownSelect
  },
  data() {
    return {
      expandedItem: null,
      selectedTypes: [], // 存储多选的类型
      policies: [
        // 假设这条是今日政策（根据日期判断）
        {
          source: '金融政策',
          date: '2025/4/1', // 保持原始日期不变
          title: '央行今日公布新一轮金融开放措施',
          summary: '央行宣布进一步扩大金融业对外开放，降低外资金融机构准入门槛，优化跨境投资管理',
          importance: 3,
          context: '在全球金融格局深刻调整的背景下，我国金融开放按下"加速键"。通过有序开放，引入更多海外金融机构参与国内市场，有利于提高金融体系活力和国际竞争力。',
          highlights: [
            { tag: '准入放宽', reason: '取消外资银行、证券公司、基金管理公司等机构的资产规模限制' },
            { tag: '业务扩容', reason: '允许外资金融机构在更多领域开展业务，包括支付清算、信用评级等' }
          ],
          benefits: [
            { tag: '金融科技', reason: '开放带来更多合作机会，国内金融科技企业有望获得更多海外市场拓展机会' },
            { tag: '资本市场', reason: '外资参与度提升，A股流动性改善，市场机制更加成熟' }
          ],
          drawbacks: [
            { tag: '中小银行', reason: '外资机构竞争加剧，中小银行在高端客户和创新业务方面面临更大挑战' }
          ]
        },
        {
          source: '高层会议',
          date: '2025/5/15',
          title: '中央政治局会议研究部署经济工作',
          summary: '会议强调加大宏观政策逆周期调节力度，实施更加积极的财政政策和稳健有效的货币政策',
          importance: 3,
          context: '在全球经济不确定性增加、国内经济下行压力加大的背景下，本次会议是年内第二次专门研究经济工作的政治局会议，释放出明显的政策加码信号。',
          highlights: [
            { tag: '政策定调', reason: '明确提出"以超常规政策应对超预期冲击"，政策力度超过市场预期' },
            { tag: '组合发力', reason: '财政政策提出扩大有效投资，货币政策强调降低实体经济融资成本' }
          ],
          fields: ['宏观经济', '财政政策', '货币政策'],
          benefits: [
            { tag: '银行', reason: '货币政策支持力度加大，银行信贷规模有望扩大' },
            { tag: '基建', reason: '财政前置发力，下半年基建投资增速提升确定性增强' }
          ],
          drawbacks: [
            { tag: '纯消费', reason: '政策重心偏向供给侧和投资端，短期内消费刺激力度有限' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: '金融板块',
              explanation: '政策宽松预期增强，银行、证券等金融板块有望受益'
            },
            {
              direction: 'positive',
              target: '基建领域',
              explanation: '积极财政政策下基建投资加速，相关建材、工程机械等板块受益'
            }
          ]
        },
        {
          source: '产业政策',
          date: '2025/2/18',
          title: '工信部发布新一代信息技术产业发展规划',
          summary: '规划提出到2025年，我国信息技术产业规模突破3万亿元，培育10家以上具有国际竞争力的龙头企业',
          importance: 2,
          context: '继上一轮信息技术产业规划到期后，本次规划进一步提高了产业目标，并首次明确提出自主可控的关键性目标，体现了在全球科技竞争背景下中国加速科技自立自强的决心。',
          highlights: [
            { tag: '目标提升', reason: '产业规模目标从上一轮规划的2万亿提升至3万亿，龙头企业培育目标翻倍' },
            { tag: '重点方向', reason: '明确提出芯片、操作系统、工业软件等关键领域的突破路线图' }
          ],
          fields: ['信息技术', '芯片', '软件'],
          benefits: [
            { tag: '芯片设计', reason: '规划明确将加大对EDA工具、IP核的补贴力度' },
            { tag: '工业软件', reason: '首次提出工业软件国产化具体目标和时间表' }
          ],
          drawbacks: [
            { tag: '中小企业', reason: '资源向龙头集中，中小企业竞争压力加大' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: '科技板块',
              explanation: '政策支持下国产替代加速，半导体、软件等科技板块迎来发展机遇'
            },
            {
              direction: 'positive',
              target: '数字经济',
              explanation: '信息技术赋能传统产业，云计算、大数据、人工智能等应用场景扩大'
            }
          ]
        },
        {
          source: '地方政策',
          date: '2023/11/15',
          title: '上海市发布金融科技发展三年行动计划',
          summary: '计划提出打造全球金融科技中心，未来三年投入100亿元专项资金支持金融科技发展',
          importance: 2,
          context: '作为中国金融中心，上海近年来持续推进金融科技创新，本次三年行动计划是继金融科技创新监管试点后的又一重大举措，旨在巩固上海国际金融中心地位并提升金融科技竞争力。',
          highlights: [
            { tag: '资金支持', reason: '三年投入100亿元，较上一轮50亿元资金规模翻倍' },
            { tag: '多维度支持', reason: '金融科技企业可获税收优惠、办公场地补贴和人才引进绿色通道' }
          ],
          fields: ['金融科技', '区域发展', '创新'],
          benefits: [
            { tag: '金融科技企业', reason: '本地金融科技初创企业最高可获千万级别资金支持' },
            { tag: '数据服务商', reason: '金融大数据、云计算服务商将获重点扶持' }
          ],
          drawbacks: [
            { tag: '传统金融', reason: '纯线下业务模式的金融机构面临转型压力' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: '金融科技企业',
              explanation: '本地金融科技企业将获得资金、人才、场地等多方面支持，业务发展提速'
            },
            {
              direction: 'positive',
              target: '上海地区银行',
              explanation: '传统银行数字化转型加速，线上业务比重提升，运营效率提高'
            }
          ]
        },
        {
          source: '金融政策',
          date: '2025/4/2',
          title: '央行宣布年内二次降准',
          summary: '央行宣布于6月5日实施全面降准0.5个百分点，释放长期资金约1.2万亿元，并提出加大普惠小微企业支持力度',
          importance: 3,
          context: '在经济复苏动力不足、信贷需求偏弱的背景下，央行年内二次降准，释放流动性力度超出市场预期，反映了稳增长压力加大，货币政策转向更加宽松。',
          highlights: [
            { tag: '降准力度', reason: '年内第二次降准，且力度达0.5个百分点，超出市场预期的0.25个百分点' },
            { tag: '政策指向', reason: '明确提出降准释放资金要重点支持小微企业、科技创新和绿色发展' }
          ],
          fields: ['货币政策', '银行', '小微企业'],
          benefits: [
            { tag: '中小银行', reason: '降准对中小银行释放资金占比更高，降低负债成本效果明显' },
            { tag: '地产链', reason: '政策对地产金融支持力度增强，相关企业融资环境改善' }
          ],
          drawbacks: [
            { tag: '大型国有银行', reason: '净息差压力进一步加大，盈利能力受到挑战' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: '债券市场',
              explanation: '降准释放流动性，利好债券市场，长端利率有望进一步下行'
            },
            {
              direction: 'positive',
              target: '成长股',
              explanation: '流动性改善利好股市风险偏好提升，科技成长板块有望受益'
            }
          ]
        },
        {
          source: '部委政策',
          date: '2025/4/1',
          title: '扩大内需促消费政策出台',
          summary: '国务院发布《关于进一步扩大内需促进消费的政策措施》，涉及汽车消费、家电更新、文旅消费等多个领域',
          importance: 3,
          context: '在宏观压力加大、出口下滑的背景下，促消费成为稳增长的重要抓手。本次政策是自2023年以来最大规模的消费刺激计划，覆盖领域广、举措具体。',
          highlights: [
            { tag: '汽车消费', reason: '取消部分城市汽车限购，增加购车补贴，下调购置税' },
            { tag: '以旧换新', reason: '推出家电、家具等大件商品的以旧换新补贴，单件最高补贴千元' }
          ],
          fields: ['消费', '汽车', '家电', '旅游'],
          benefits: [
            { tag: '汽车整车', reason: '限购放松和购置税优惠直接带动增量需求' },
            { tag: '家电零售', reason: '以旧换新激活更新需求，高端家电渗透率提升' }
          ],
          drawbacks: [
            { tag: '线下百货', reason: '政策聚焦大件商品，对传统百货刺激有限' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: '消费板块',
              explanation: '家电、汽车、旅游等相关板块有望受益，尤其是高端消费品和新能源车市场'
            },
            {
              direction: 'positive',
              target: '零售指数',
              explanation: '政策有望提振5-6月社零数据，带动GDP增长贡献'
            }
          ]
        },
        {
          source: '国际政策',
          date: '2025/5/30',
          title: 'G20财长会议达成数字货币监管共识',
          summary: '二十国集团财长和央行行长会议就全球数字货币监管框架达成共识，将推动统一监管标准',
          importance: 2,
          context: '随着数字货币在全球范围内的快速发展，跨境监管合作日益重要。本次G20会议首次就数字货币监管达成框架性共识，标志着全球数字金融监管协调进入新阶段。',
          highlights: [
            { tag: '全球标准', reason: '首次提出全球统一的数字货币监管标准时间表，计划两年内完成' },
            { tag: '央行数字货币', reason: '鼓励各国积极探索央行数字货币，促进跨境支付效率提升' }
          ],
          fields: ['数字货币', '国际监管', '金融合作'],
          benefits: [
            { tag: '合规平台', reason: '已获牌照的合规数字货币交易所将获得更大发展空间' },
            { tag: '跨境支付', reason: '基于数字货币的跨境支付解决方案迎来发展机遇' }
          ],
          drawbacks: [
            { tag: '小型交易所', reason: '监管标准提高，合规成本上升，中小交易平台面临淘汰' },
            { tag: '匿名币种', reason: '强调反洗钱要求，匿名特性的加密货币将面临更严监管' }
          ],
          impacts: [
            {
              direction: 'negative',
              target: '加密货币',
              explanation: '全球监管协调加强，部分投机性加密资产面临合规压力'
            },
            {
              direction: 'positive',
              target: '合规数字金融',
              explanation: '符合监管要求的数字金融业务获得发展空间，传统金融机构数字化转型受益'
            }
          ]
        },
        {
          source: '产业政策',
          date: '2025/6/10',
          title: '新一轮集成电路产业支持政策',
          summary: '工信部牵头制定新一轮集成电路产业支持政策，预计将从资金、税收、人才等多方面加大支持力度',
          importance: 2,
          context: '在全球芯片供应链重构和技术限制背景下，国产芯片自主可控成为国家战略。本次政策延续了"十四五"规划中的芯片强国战略，并针对卡脖子环节提出更具体的支持措施。',
          highlights: [
            { tag: '重点领域', reason: '首次明确EDA工具软件、高端芯片制造设备等领域的具体攻关目标' },
            { tag: '产业基金', reason: '新增1000亿元国家级集成电路产业投资基金，重点支持卡脖子环节' }
          ],
          fields: ['科技', '半导体', '集成电路'],
          benefits: [
            { tag: '芯片设备', reason: '本土设备厂商将获得更多应用验证机会和采购倾斜' },
            { tag: '设计企业', reason: '自主CPU、GPU等核心芯片设计企业获政策优先支持' }
          ],
          drawbacks: [
            { tag: 'IDM模式企业', reason: '政策鼓励专业化分工，不利于垂直整合模式' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: '半导体产业链',
              explanation: '国产替代加速，设计、制造、封测、设备材料全产业链公司受益'
            },
            {
              direction: 'negative',
              target: '进口芯片代理商',
              explanation: '国产替代加速可能导致进口芯片市场份额缩减'
            }
          ]
        },
        {
          source: '金融政策',
          date: '2025/6/20',
          title: '证监会发布ESG信息披露指引',
          summary: '证监会发布上市公司环境、社会和公司治理(ESG)信息披露指引，要求分步实施强制披露',
          importance: 2,
          context: '随着全球ESG投资理念的兴起和绿色低碳转型的加速，中国资本市场ESG建设提速。本次披露指引是中国ESG投资体系建设的里程碑，标志着ESG要素正式纳入资本市场基础制度。',
          highlights: [
            { tag: '分步实施', reason: '按市值和行业分步推进，2026年起全面实施强制披露' },
            { tag: '重点指标', reason: '重点关注碳排放、能源消耗、公司治理等关键指标' }
          ],
          fields: ['资本市场', 'ESG', '信息披露'],
          benefits: [
            { tag: 'ESG评级机构', reason: 'ESG数据需求增加，第三方评级和数据服务机构业务扩张' },
            { tag: '绿色先进企业', reason: 'ESG表现优异企业获得估值溢价，融资成本降低' }
          ],
          drawbacks: [
            { tag: '高排放企业', reason: '碳排放和环境表现差的企业估值受到负面影响' },
            { tag: '中小企业', reason: 'ESG披露增加合规成本，中小企业负担加重' }
          ],
          impacts: [
            {
              direction: 'positive',
              target: 'ESG优质企业',
              explanation: 'ESG表现优异的企业估值有望提升，吸引更多长期资金配置'
            },
            {
              direction: 'negative',
              target: '高污染行业',
              explanation: '环境表现差的企业面临更大压力，合规成本上升'
            }
          ]
        }
      ]
    }
  },
  created() {
    // 初始化时选择所有类型
    this.selectedTypes = [...this.sourceTypes];
  },
  beforeDestroy() {
    // 清理事件监听
  },
  computed: {
    sourceTypes() {
      const types = new Set();
      this.policies.forEach(policy => {
        types.add(policy.source);
      });
      return Array.from(types);
    },
    
    filteredPolicies() {
      const sorted = [...this.policies].sort((a, b) => {
        return new Date(a.date) - new Date(b.date);
      });
      
      if (this.selectedTypes.length === 0 || 
          this.selectedTypes.length === this.sourceTypes.length) {
        return sorted;
      }
      
      return sorted.filter(policy => this.selectedTypes.includes(policy.source));
    }
  },
  methods: {
    handleExpand(data) {
      this.expandedItem = data.expanded ? data.index : null;
    },
    
    getSourceClass(source) {
      const classes = {
        '高层会议': 'official',
        '部委政策': 'planning',
        '地方政策': 'local',
        '国际政策': 'international',
        '金融政策': 'financial',
        '产业政策': 'industry'
      };
      return classes[source] || 'other';
    }
  }
}
</script>

<style lang="scss" scoped>
.policy-catalysts {
  height: 100%;
  max-height: 600px;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  
  .policy-header {
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
    }
  }
  
  .policy-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    min-height: 0;
  }
}

// 重要性指标样式
.importance-indicator {
  display: flex;
  gap: 2px;
  flex-shrink: 0;
  
  .importance-icon {
    font-size: 10px;
    
    &.filled {
      color: var(--hx-warning-color-2);
    }
    
    &:not(.filled) {
      color: var(--hx-border-level-2-color);
    }
  }
}

@media (max-width: 768px) {
  .policy-catalysts {
    .policy-content {
      .data-timeline {
        .policy-list {
          .policy-item {
            .date-marker {
              width: var(--hx-size-10);
            }
            
            .item-content {
      .policy-title-row {
        .policy-title {
                  font-size: 13px;
        }
      }
      
      .policy-preview {
        font-size: 12px;
              }
            }
          }
        }
      }
    }
  }
}
</style> 