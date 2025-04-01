<template>
  <div class="world-economy card">
    <div class="economy-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">全球经济</h2>
        <div class="card-subtitle">重要经济数据与市场解读</div>
      </div>
    </div>
    
    <div class="economy-content">
      <!-- 使用DataTimeline组件 -->
      <DataTimeline :items="economyData" @item-expanded="handleExpand">
        <!-- 自定义标签 -->
        <template v-slot:item-tag="{ item }">
          <div v-if="item.actual !== undefined && item.actual !== '--' && item.impact !== 'pending'" 
               class="status-tag" 
               :class="getImpactClass(item)">
            {{ getImpactText(item) }}
        </div>
        </template>
        
        <!-- 添加数值指标到标题行 -->
        <template v-slot:item-indicators="{ item }">
                <div class="detail-metrics" role="group" :aria-label="item.title + '的具体数据'">
                  <div class="metric" role="group" aria-label="前值">
                    <div class="metric-label">前值</div>
              <div class="metric-value">{{ item.previous }}{{ item.unit }}</div>
                  </div>
            <div class="metric" role="group" aria-label="预期">
                    <div class="metric-label">预期</div>
              <div class="metric-value">{{ item.expected }}{{ item.unit }}</div>
                  </div>
            <div class="metric" role="group" aria-label="实际">
                    <div class="metric-label">实际</div>
              <div class="metric-value" :class="[item.actual && item.actual !== '--' ? getValueClass(item) : '']">
                {{ item.actual }}{{ item.unit }}
              </div>
            </div>
          </div>
        </template>
        
        <!-- 自定义详情内容 -->
        <template v-slot:item-details-custom>
          <!-- 不再需要详细指标容器，已移到外部 -->
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

export default {
  name: 'WorldEconomy',
  components: {
    DataTimeline
  },
  data() {
    return {
      expandedItem: null,
      economyData: [
        {
          source: '数据',
          date: '2025/3/24',
          title: '美国5月密歇根大学消费者信心指数终值',
          summary: '美国5月密歇根大学消费者信心指数预期为76.0，前值为77.2，等待数据公布',
          actual: 78,
          expected: 76.0,
          previous: 77.2,
          unit: '',
          impact: 'positive', // 'pending'=未公布, 'positive'=好于预期, 'negative'=差于预期, 'neutral'=符合预期
          context: '密歇根大学消费者信心指数是衡量美国消费者信心的重要指标，对预测美国未来几个月的消费支出具有重要参考价值。市场预计该数据将小幅下滑，需关注实际数据是否符合预期。',
          highlights: [
            { tag: '关注重点', reason: '该指标近期连续下行，若低于预期可能加剧市场对消费前景的担忧' },
            { tag: '市场情绪', reason: '指标表现将影响对美联储未来政策路径的预期' }
          ],
          benefits: [
            { tag: '可能利好', reason: '若数据好于预期，将提振消费者支出预期，利好零售板块' }
          ],
          drawbacks: [
            { tag: '潜在风险', reason: '若数据大幅低于预期，可能加剧经济放缓担忧' }
          ]
        },
        {
          source: '数据',
          date: '2025/3/28',
          title: '美国5月密歇根大学消费者信心指数初值',
          summary: '美国5月密歇根大学消费者信心指数初值为75.8，预期为76.0，前值为77.2',
          actual: 75.8,
          expected: 76.0,
          previous: 77.2,
          unit: '',
          impact: 'negative', // 'pending'=未公布, 'positive'=好于预期, 'negative'=差于预期, 'neutral'=符合预期
          context: '密歇根大学消费者信心指数是衡量美国消费者信心的重要指标，对预测美国未来几个月的消费支出具有重要参考价值。本次数据低于预期且较前值显著下降，反映出在通胀高企的背景下，美国消费者信心依然疲软。',
          highlights: [
            { tag: '指标下滑', reason: '终值较初值进一步走弱，表明月内消费者信心持续下滑' },
            { tag: '连续下降', reason: '该指标已连续三个月下降，处于近一年来的相对低位' }
          ],
          benefits: [
            { tag: '美债市场', reason: '消费信心疲软可能增加市场对美联储降息的预期，支撑美债价格' }
          ],
          drawbacks: [
            { tag: '零售消费', reason: '消费者信心下降可能导致未来几个月消费支出放缓，对零售行业形成压力' },
            { tag: '美元汇率', reason: '美国经济前景不确定性增加，可能对美元构成压力' }
          ]
        },
        {
          source: '指标',
          date: '2025/4/1',
          title: '美国上周首次申请失业救济人数',
          summary: '美国上周首次申请失业救济人数为22.5万人，预期为23.0万人，前值为23.2万人',
          actual: 225,
          expected: 230,
          previous: 232,
          unit: '千人',
          impact: 'positive',
          context: '首次申请失业救济人数是衡量美国就业市场健康状况的高频指标。本次数据好于预期，表明美国就业市场仍然保持相对稳健，企业裁员压力暂时得到缓解。',
          highlights: [
            { tag: '优于预期', reason: '实际数据低于预期值和前值，表明就业市场韧性强于预期' },
            { tag: '连续改善', reason: '该指标已连续两周下降，显示就业市场向好发展' }
          ],
          benefits: [
            { tag: '美国股市', reason: '就业数据向好提振市场对美国经济的信心，有利于股市表现' },
            { tag: '美元走势', reason: '美国经济相对强劲可能支撑美元走强' }
          ],
          drawbacks: [
            { tag: '加息预期', reason: '强劲就业数据可能减弱市场对美联储降息的预期，给风险资产带来压力' }
          ]
        },
        {
          source: '经济',
          date: '2025/5/20',
          title: '日本第一季度GDP环比终值',
          summary: '日本第一季度GDP环比终值萎缩0.4%，预期萎缩0.5%，初值萎缩0.5%',
          actual: '--',
          expected: -0.5,
          previous: -0.5,
          unit: '%',
          impact: 'pending',
          context: '日本GDP数据是衡量日本经济整体表现的重要指标。虽然第一季度GDP仍为负增长，但终值较初值有所改善，略好于市场预期，显示日本经济的韧性可能高于此前预计。',
          highlights: [
            { tag: '降幅收窄', reason: '终值较初值降幅收窄0.1个百分点，表明经济状况略好于初步估计' },
            { tag: '连续下滑', reason: '日本经济连续两个季度出现负增长，技术性衰退已成定局' }
          ],
          benefits: [
            { tag: '日元走势', reason: 'GDP数据略超预期可能减缓日元贬值压力' }
          ],
          drawbacks: [
            { tag: '日本股市', reason: '经济衰退确认可能抑制投资者对日本市场的风险偏好' },
            { tag: '政策预期', reason: '数据表明日本经济仍面临挑战，市场对日本央行收紧货币政策的预期可能减弱' }
          ]
        },
        {
          source: '数据',
          date: '2025/5/18',
          title: '中国4月规模以上工业增加值同比',
          summary: '中国4月规模以上工业增加值同比增长6.7%，预期增长6.0%，前值增长4.5%',
          actual: '--',
          expected: 6.0,
          previous: 4.5,
          unit: '%',
          impact: 'pending',
          context: '工业增加值是衡量工业企业生产活动的重要指标。本次数据大幅超出市场预期，且较前值显著回升，表明中国工业生产活动明显加速，经济复苏动能增强。',
          highlights: [
            { tag: '显著超预期', reason: '实际值比预期高出0.7个百分点，比前值大幅提高2.2个百分点' },
            { tag: '回升明显', reason: '这是近6个月来的最高增速，表明工业生产明显回暖' }
          ],
          benefits: [
            { tag: '大宗商品', reason: '中国工业活动回升可能带动对原材料需求增加，支撑大宗商品价格' },
            { tag: '工业企业', reason: '生产活动加速有利于工业企业盈利改善，特别是上游生产资料行业' }
          ],
          drawbacks: [
            { tag: '通胀压力', reason: '工业活动显著回升可能带来输入性通胀压力上升风险' }
          ]
        },
        {
          source: '指标',
          date: '2025/5/15',
          title: '欧元区第一季度GDP环比终值',
          summary: '欧元区第一季度GDP环比终值增长0.3%，预期增长0.3%，初值增长0.3%',
          actual: '--',
          expected: 0.3,
          previous: 0.3,
          unit: '%',
          impact: 'pending',
          context: '欧元区GDP数据是衡量欧元区整体经济表现的核心指标。本次终值与初值和预期保持一致，表明欧元区经济在第一季度保持了温和增长，扭转了2023年第四季度的下滑趋势，但整体复苏力度仍然有限。',
          highlights: [
            { tag: '符合预期', reason: '终值与初值和市场预期完全一致，没有带来意外因素' },
            { tag: '环比改善', reason: '相比上季度的零增长，本季度出现正增长，表明经济有所改善' }
          ],
          benefits: [
            { tag: '欧洲股市', reason: '经济增长确认可能支撑欧洲股市的基本面预期' }
          ],
          drawbacks: [
            { tag: '分化明显', reason: '数据显示欧元区内部各国表现仍存在较大分化，德国增长依然疲弱' },
            { tag: '增速有限', reason: '0.3%的增速仍处于历史较低水平，表明复苏基础仍不牢固' }
          ]
        },
        {
          source: '数据',
          date: '2025/5/12',
          title: '美国4月CPI同比',
          summary: '美国4月CPI同比上升3.4%，预期上升3.4%，前值上升3.5%',
          actual: '--',
          expected: 3.4,
          previous: 3.5,
          unit: '%',
          impact: 'pending',
          context: '消费者物价指数(CPI)是衡量美国通胀水平的关键指标。本次数据与市场预期完全一致，且较前值小幅回落，表明美国通胀压力仍在缓慢降温，但尚未达到美联储2%的目标水平。',
          highlights: [
            { tag: '符合预期', reason: '实际数据与预期完全一致，没有给市场带来明显冲击' },
            { tag: '持续降温', reason: 'CPI同比增速继续小幅下降，反映通胀压力在逐步缓解' }
          ],
          benefits: [
            { tag: '债券市场', reason: '通胀缓和有助于稳定债券收益率预期，可能支撑债市表现' }
          ],
          drawbacks: [
            { tag: '核心通胀', reason: '剔除食品和能源的核心CPI仍保持高位，显示通胀压力仍广泛存在' },
            { tag: '降息预期', reason: '通胀数据与预期一致，未能为美联储提前降息提供更多空间' }
          ]
        }
      ]
    }
  },
  methods: {
    handleExpand(data) {
      this.expandedItem = data.expanded ? data.index : null;
    },
    
    getImpactClass(item) {
      if (item.impact === 'pending') {
        return 'pending';
      } else if (item.impact === 'positive') {
        return 'better-than-expected';
      } else if (item.impact === 'negative') {
        return 'worse-than-expected';
      } else {
          return 'change-neutral';
      }
    },
    
    getImpactText(item) {
      if (item.impact === 'pending') {
        return '待公布';
      } else if (item.impact === 'positive') {
        return '超过预期';
      } else if (item.impact === 'negative') {
        return '不及预期';
      } else {
          return '符合预期';
      }
    },
    
    getValueClass(item) {
      if (item.impact === 'pending') {
        return '';
      } else if (item.impact === 'positive') {
        return 'better-than-expected';
      } else if (item.impact === 'negative') {
        return 'worse-than-expected';
      } else {
        return 'change-neutral';
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.world-economy {
  height: 100%;
  max-height: 600px;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  
  .economy-header {
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
  
  .economy-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    min-height: 0;
  }
  
  .status-tag {
    font-size: 11px;
    font-weight: normal;
    padding: 0px 4px;
    border-radius: 2px;
    white-space: nowrap;
      flex-shrink: 0;
      
    &.better-than-expected {
      background-color: rgba(239, 68, 68, 0.1);
      color: var(--hx-raise-color-2);
    }
    
    &.worse-than-expected {
      background-color: rgba(16, 185, 129, 0.1);
      color: var(--hx-fall-color-2);
    }
    
    &.change-neutral {
      background-color: rgba(0, 0, 0, 0.1);
      color: var(--hx-text-color-tertiary);
    }
    
    &.pending {
      background-color: rgba(96, 165, 250, 0.1);
      color: var(--hx-brand-color-1);
    }
  }
  
  .detail-metrics-container {
    margin-bottom: var(--hx-comp-margin-s);
    position: relative;
    padding-bottom: var(--hx-comp-margin-s);
    border-bottom: 1px dashed var(--hx-border-level-1-color);
            }

            .detail-metrics {
              display: flex;
              gap: var(--hx-comp-margin-s);
              
              .metric {
                position: relative;
                display: flex;
                align-items: center;
                gap: var(--hx-comp-margin-xs);
                
                .metric-label {
        font-size: 10px;
                  color: var(--hx-text-color-tertiary);
                  opacity: 0.8;
                }
                
                .metric-value {
        font-size: 10px;
                  color: var(--hx-text-color-secondary);
        display: flex;
        align-items: center;
                  
        &.better-than-expected {
                    color: var(--hx-raise-color-2);
        }
        
        &.worse-than-expected {
                    color: var(--hx-fall-color-2);
        }
        
        &.change-neutral {
          color: var(--hx-text-color-secondary);
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .world-economy {
              .detail-metrics {
      flex-direction: column;
      gap: var(--hx-comp-margin-xs);
    }
  }
}
</style> 