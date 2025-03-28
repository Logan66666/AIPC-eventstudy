<template>
  <div class="policy-catalysts card">
    <div class="policy-header">
      <h2 class="card-title secondary-title">政策催化</h2>
      <div class="card-subtitle">重要经济政策与市场影响</div>
    </div>
    
    <div class="policy-content">
      <div class="policy-tabs">
        <div 
          v-for="(tab, index) in tabs" 
          :key="index"
          class="policy-tab"
          :class="{'active': activeTab === index}"
          @click="activeTab = index"
        >
          {{ tab.name }}
        </div>
      </div>
      
      <div class="policy-list">
        <div 
          v-for="(policy, index) in filteredPolicies" 
          :key="index"
          class="policy-item"
          :class="{'expanded': expandedItem === index}"
          @click="toggleExpand(index)"
        >
          <div class="policy-header-row">
            <div class="policy-meta">
              <div class="policy-source-tag" :class="getSourceClass(policy.source)">
                {{ policy.source }}
              </div>
              <div class="policy-date">{{ policy.date }}</div>
            </div>
            
            <div class="importance-indicator">
              <span 
                v-for="n in 3" 
                :key="n" 
                :class="{ active: n <= policy.importance }"
                class="importance-dot"
              ></span>
            </div>
          </div>
          
          <div class="policy-title-row">
            <h3 class="policy-title">{{ policy.title }}</h3>
            <div class="expand-icon">
              <span v-if="expandedItem !== index">+</span>
              <span v-else>-</span>
            </div>
          </div>
          
          <div class="policy-preview">{{ policy.summary }}</div>
          
          <div class="policy-details" v-show="expandedItem === index">
            <div class="fields-container">
              <div class="field-label">相关领域</div>
              <div class="fields-list">
                <span 
                  v-for="(field, idx) in policy.fields" 
                  :key="idx"
                  class="field-tag"
                >{{ field }}</span>
              </div>
            </div>
            
            <div class="impact-analysis">
              <div class="impact-header">市场影响</div>
              <div class="impact-items">
                <div 
                  v-for="(impact, idx) in policy.impacts" 
                  :key="idx"
                  class="impact-item"
                >
                  <div class="impact-direction" :class="impact.direction">
                    <i class="impact-arrow" :class="getArrowClass(impact.direction)"></i>
                  </div>
                  <div class="impact-content">
                    <div class="impact-target">{{ impact.target }}</div>
                    <div class="impact-explanation">{{ impact.explanation }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PolicyCatalysts',
  data() {
    return {
      activeTab: 0,
      expandedItem: null,
      tabs: [
        { name: '已发布', filter: 'published' },
        { name: '即将出台', filter: 'upcoming' },
        { name: '市场传闻', filter: 'rumor' }
      ],
      policies: [
        {
          source: '官方政策',
          date: '5月25日',
          title: '扩大内需促消费政策出台',
          summary: '国务院发布《关于进一步扩大内需促进消费的政策措施》，涉及汽车消费、家电更新、文旅消费等多个领域',
          importance: 3,
          status: 'published',
          fields: ['消费', '汽车', '家电', '旅游'],
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
          source: '央行通告',
          date: '5月21日',
          title: '央行宣布年内二次降准',
          summary: '央行宣布于6月5日实施全面降准0.5个百分点，释放长期资金约1.2万亿元，并提出加大普惠小微企业支持力度',
          importance: 3,
          status: 'published',
          fields: ['货币政策', '银行', '小微企业'],
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
          source: '部委规划',
          date: '预计6月',
          title: '新一轮集成电路产业支持政策',
          summary: '工信部牵头制定新一轮集成电路产业支持政策，预计将从资金、税收、人才等多方面加大支持力度',
          importance: 2,
          status: 'upcoming',
          fields: ['科技', '半导体', '集成电路'],
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
          source: '市场传闻',
          date: '未确定',
          title: '新能源汽车购置补贴可能延续',
          summary: '多家媒体报道国家可能出台新一轮新能源汽车购置补贴政策，重点支持农村市场和换购需求',
          importance: 1,
          status: 'rumor',
          fields: ['新能源', '汽车', '补贴政策'],
          impacts: [
            {
              direction: 'positive',
              target: '新能源整车',
              explanation: '补贴政策延续有利于刺激需求，特别是下沉市场的渗透率提升'
            },
            {
              direction: 'positive',
              target: '锂电池产业链',
              explanation: '新能源车销量增长带动上游材料需求，电池、电机、电控等核心零部件厂商受益'
            }
          ]
        }
      ]
    }
  },
  computed: {
    filteredPolicies() {
      const filter = this.tabs[this.activeTab].filter;
      if (filter === 'all') {
        return this.policies;
      }
      return this.policies.filter(policy => policy.status === filter);
    }
  },
  methods: {
    toggleExpand(index) {
      if (this.expandedItem === index) {
        this.expandedItem = null;
      } else {
        this.expandedItem = index;
      }
    },
    getSourceClass(source) {
      const classes = {
        '官方政策': 'official',
        '央行通告': 'official',
        '部委规划': 'planning',
        '市场传闻': 'rumor'
      };
      return classes[source] || 'other';
    },
    getArrowClass(direction) {
      return direction === 'positive' ? 'arrow-up' : 'arrow-down';
    }
  }
}
</script>

<style lang="scss" scoped>
.policy-catalysts {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .policy-header {
    margin-bottom: var(--spacing-md);
  }
  
  .policy-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  
  .policy-tabs {
    display: flex;
    margin-bottom: var(--spacing-md);
    border-bottom: 1px solid var(--border-subtle);
    
    .policy-tab {
      padding: 8px 12px;
      margin-right: var(--spacing-md);
      font-size: 14px;
      color: var(--text-tertiary);
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
      
      &:hover {
        color: var(--text-secondary);
      }
      
      &.active {
        color: var(--color-secondary);
        font-weight: 600;
        
        &:after {
          content: '';
          position: absolute;
          bottom: -1px;
          left: 0;
          width: 100%;
          height: 2px;
          background-color: var(--color-secondary);
        }
      }
    }
  }
  
  .policy-list {
    flex: 1;
    overflow-y: auto;
    padding-right: var(--spacing-sm);
    
    &::-webkit-scrollbar {
      width: 4px;
    }
    
    &::-webkit-scrollbar-thumb {
      background-color: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
    }
  }
  
  .policy-item {
    margin-bottom: var(--spacing-md);
    background-color: rgba(36, 107, 248, 0.05);
    border-radius: var(--radius-sm);
    padding: var(--spacing-md);
    cursor: pointer;
    transition: all 0.25s ease;
    border-left: 3px solid transparent;
    
    &:last-child {
      margin-bottom: 0;
    }
    
    &:hover {
      background-color: rgba(36, 107, 248, 0.08);
      transform: translateY(-2px);
    }
    
    &.expanded {
      background-color: var(--bg-card-light);
    }
    
    .policy-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--spacing-sm);
      
      .policy-meta {
        display: flex;
        align-items: center;
        gap: var(--spacing-sm);
        
        .policy-source-tag {
          font-size: 11px;
          font-weight: 600;
          padding: 2px 6px;
          border-radius: 4px;
          
          &.official {
            background-color: rgba(36, 107, 248, 0.1);
            color: var(--color-secondary);
          }
          
          &.planning {
            background-color: rgba(255, 149, 0, 0.1);
            color: var(--color-tertiary);
          }
          
          &.rumor {
            background-color: rgba(100, 116, 139, 0.1);
            color: var(--color-info);
          }
        }
        
        .policy-date {
          font-size: 12px;
          color: var(--text-tertiary);
        }
      }
      
      .importance-indicator {
        display: flex;
        gap: 4px;
        
        .importance-dot {
          width: 6px;
          height: 6px;
          border-radius: 50%;
          background-color: rgba(255, 255, 255, 0.1);
          
          &.active {
            background-color: var(--color-secondary);
            box-shadow: 0 0 4px rgba(36, 107, 248, 0.4);
          }
        }
      }
    }
    
    .policy-title-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: var(--spacing-sm);
      
      .policy-title {
        font-size: 15px;
        font-weight: 600;
        color: var(--text-primary);
        margin: 0;
        line-height: 1.4;
        flex: 1;
        padding-right: var(--spacing-sm);
      }
      
      .expand-icon {
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background-color: rgba(36, 107, 248, 0.1);
        color: var(--color-secondary);
        font-size: 14px;
        font-weight: bold;
        line-height: 1;
        flex-shrink: 0;
      }
    }
    
    .policy-preview {
      font-size: 13px;
      color: var(--text-secondary);
      margin-bottom: var(--spacing-md);
      line-height: 1.5;
    }
    
    .policy-details {
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      padding-top: var(--spacing-md);
      animation: slideDown 0.3s ease;
      
      .fields-container {
        margin-bottom: var(--spacing-md);
        
        .field-label {
          font-size: 12px;
          color: var(--text-tertiary);
          margin-bottom: 6px;
        }
        
        .fields-list {
          display: flex;
          flex-wrap: wrap;
          gap: 6px;
          
          .field-tag {
            background-color: rgba(36, 107, 248, 0.08);
            color: var(--color-secondary);
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
          }
        }
      }
      
      .impact-analysis {
        .impact-header {
          font-size: 12px;
          color: var(--text-tertiary);
          margin-bottom: 8px;
        }
        
        .impact-items {
          display: flex;
          flex-direction: column;
          gap: var(--spacing-sm);
          
          .impact-item {
            display: flex;
            padding: 8px;
            background-color: rgba(0, 0, 0, 0.15);
            border-radius: var(--radius-sm);
            
            .impact-direction {
              display: flex;
              align-items: center;
              justify-content: center;
              width: 22px;
              height: 22px;
              border-radius: 50%;
              margin-right: var(--spacing-sm);
              flex-shrink: 0;
              
              &.positive {
                background-color: rgba(16, 185, 129, 0.1);
                color: var(--color-success);
              }
              
              &.negative {
                background-color: rgba(239, 68, 68, 0.1);
                color: var(--color-danger);
              }
              
              .impact-arrow {
                font-style: normal;
                font-weight: bold;
                
                &.arrow-up:after {
                  content: '↑';
                }
                
                &.arrow-down:after {
                  content: '↓';
                }
              }
            }
            
            .impact-content {
              flex: 1;
              
              .impact-target {
                font-size: 13px;
                font-weight: 600;
                color: var(--text-primary);
                margin-bottom: 2px;
              }
              
              .impact-explanation {
                font-size: 12px;
                color: var(--text-secondary);
                line-height: 1.4;
              }
            }
          }
        }
      }
    }
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .policy-catalysts {
    .policy-tabs {
      .policy-tab {
        padding: 6px 8px;
        font-size: 13px;
      }
    }
    
    .policy-item {
      padding: var(--spacing-sm);
      
      .policy-title-row {
        .policy-title {
          font-size: 14px;
        }
      }
      
      .policy-preview {
        font-size: 12px;
      }
      
      .policy-details {
        .impact-analysis {
          .impact-items {
            .impact-item {
              padding: 6px;
              
              .impact-content {
                .impact-target {
                  font-size: 12px;
                }
                
                .impact-explanation {
                  font-size: 11px;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style> 