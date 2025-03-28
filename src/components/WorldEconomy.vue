<template>
  <div class="world-economy card">
    <div class="economy-header">
      <h2 class="card-title secondary-title">世界经济</h2>
      <div class="card-subtitle">全球重要经济数据解读</div>
    </div>
    
    <div class="economy-content">
      <div class="data-timeline">
        <!-- 时间线指示器 -->
        <div class="timeline-indicator">
          <div class="timeline-line"></div>
        </div>
        
        <!-- 数据项目 -->
        <div class="data-items">
          <div 
            v-for="(item, index) in economyData" 
            :key="index"
            class="data-item"
            :class="{'expanded': expandedItem === index}"
            @click="toggleExpand(index)"
          >
            <!-- 日期指示 -->
            <div class="date-marker">
              <div class="date">{{ item.date }}</div>
              <div class="marker"></div>
            </div>
            
            <!-- 数据内容 -->
            <div class="item-content">
              <div class="item-header">
                <h3 class="item-title">{{ item.title }}</h3>
                <div class="expand-icon">
                  <span v-if="expandedItem !== index">+</span>
                  <span v-else>-</span>
                </div>
              </div>
              
              <div class="item-preview">{{ item.summary }}</div>
              
              <div class="item-details" v-show="expandedItem === index">
                <div class="detail-metrics">
                  <div class="metric">
                    <div class="metric-label">实际值</div>
                    <div class="metric-value" :class="getChangeClass(item.actualChange)">{{ item.actual }}</div>
                  </div>
                  <div class="metric">
                    <div class="metric-label">预期值</div>
                    <div class="metric-value">{{ item.expected }}</div>
                  </div>
                  <div class="metric">
                    <div class="metric-label">前值</div>
                    <div class="metric-value">{{ item.previous }}</div>
                  </div>
                </div>
                
                <div class="impact-analysis">
                  <div class="impact-header">市场影响</div>
                  <div class="impact-content">{{ item.impact }}</div>
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
  name: 'WorldEconomy',
  data() {
    return {
      expandedItem: null,
      economyData: [
        {
          date: '5月20日',
          title: '美国PCE物价指数发布',
          summary: '预计同比增长4.2%，环比增长0.3%，通胀压力继续缓解',
          actual: '+4.2%',
          expected: '+4.1%',
          previous: '+4.4%',
          actualChange: 'neutral',
          impact: '数据略高于预期但整体符合市场预期，美联储维持现有货币政策立场概率增大，美股震荡走高，美元指数小幅走强，黄金价格承压。'
        },
        {
          date: '5月23日',
          title: '欧元区PMI数据公布',
          summary: '制造业PMI预期51.2，服务业PMI预期54.5，经济复苏动能增强',
          actual: '50.8/55.1',
          expected: '51.2/54.5',
          previous: '50.9/53.6',
          actualChange: 'positive',
          impact: '服务业PMI超预期增长，显示欧元区经济动能强劲，欧元兑美元走强，欧洲股市普涨，能源和银行板块表现尤为突出。'
        },
        {
          date: '5月31日',
          title: '中国5月PMI数据',
          summary: '市场预期制造业PMI保持在扩张区间，经济复苏趋势向好',
          actual: '50.2',
          expected: '50.5',
          previous: '50.4',
          actualChange: 'negative',
          impact: '制造业PMI低于预期但仍处于扩张区间，国内需求恢复缓慢，A股市场小幅回调，关注后续政策刺激举措。'
        },
        {
          date: '6月2日',
          title: '美国就业数据',
          summary: '预计非农就业人数增加18万，失业率维持在3.4%左右',
          actual: '待公布',
          expected: '18万',
          previous: '23.6万',
          actualChange: 'neutral',
          impact: '关注数据与预期差异，将直接影响美联储6月议息会议决策，进而影响全球资本市场走向。'
        }
      ]
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
    getChangeClass(changeType) {
      switch(changeType) {
        case 'positive':
          return 'change-positive';
        case 'negative':
          return 'change-negative';
        default:
          return 'change-neutral';
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.world-economy {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .economy-header {
    margin-bottom: var(--spacing-md);
  }
  
  .economy-content {
    flex: 1;
    overflow: hidden;
  }
  
  .data-timeline {
    display: flex;
    height: 100%;
    
    .timeline-indicator {
      width: 24px;
      position: relative;
      
      .timeline-line {
        position: absolute;
        top: 10px;
        bottom: 0;
        left: 50%;
        width: 2px;
        background: linear-gradient(to bottom, 
          var(--color-secondary), 
          rgba(36, 107, 248, 0.3));
        transform: translateX(-50%);
      }
    }
    
    .data-items {
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
      
      .data-item {
        display: flex;
        margin-bottom: var(--spacing-md);
        cursor: pointer;
        
        &:last-child {
          margin-bottom: 0;
        }
        
        &:hover {
          .marker {
            transform: scale(1.2);
          }
          
          .item-title {
            color: var(--color-secondary);
          }
        }
        
        &.expanded {
          .marker {
            background-color: var(--color-secondary);
            border-color: var(--color-info);
            transform: scale(1.2);
          }
          
          .item-content {
            background-color: var(--bg-card-light);
          }
          
          .item-title {
            color: var(--color-secondary);
          }
        }
        
        .date-marker {
          display: flex;
          flex-direction: column;
          align-items: center;
          margin-right: var(--spacing-sm);
          width: 60px;
          
          .date {
            font-size: 12px;
            color: var(--text-secondary);
            margin-bottom: 4px;
            white-space: nowrap;
          }
          
          .marker {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: var(--bg-card-light);
            border: 2px solid var(--color-secondary);
            box-shadow: 0 0 0 2px rgba(36, 107, 248, 0.2);
            margin-top: 3px;
            transition: all 0.2s ease;
          }
        }
        
        .item-content {
          flex: 1;
          background-color: rgba(36, 107, 248, 0.05);
          border-radius: var(--radius-sm);
          padding: var(--spacing-sm);
          transition: all 0.2s ease;
          
          .item-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
            
            .item-title {
              font-size: 14px;
              font-weight: 600;
              color: var(--text-primary);
              margin: 0;
              transition: color 0.2s ease;
            }
            
            .expand-icon {
              width: 18px;
              height: 18px;
              display: flex;
              align-items: center;
              justify-content: center;
              border-radius: 50%;
              background-color: rgba(36, 107, 248, 0.1);
              color: var(--color-secondary);
              font-size: 14px;
              font-weight: bold;
              line-height: 1;
            }
          }
          
          .item-preview {
            font-size: 12px;
            color: var(--text-secondary);
            margin-bottom: var(--spacing-sm);
          }
          
          .item-details {
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: var(--spacing-sm);
            animation: slideDown 0.3s ease;
            
            .detail-metrics {
              display: flex;
              margin-bottom: var(--spacing-sm);
              gap: var(--spacing-sm);
              
              .metric {
                flex: 1;
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: var(--radius-sm);
                padding: 6px;
                text-align: center;
                
                .metric-label {
                  font-size: 10px;
                  color: var(--text-tertiary);
                  margin-bottom: 2px;
                }
                
                .metric-value {
                  font-size: 14px;
                  font-weight: 600;
                  color: var(--text-primary);
                  
                  &.change-positive {
                    color: var(--color-success);
                  }
                  
                  &.change-negative {
                    color: var(--color-danger);
                  }
                  
                  &.change-neutral {
                    color: var(--color-info);
                  }
                }
              }
            }
            
            .impact-analysis {
              .impact-header {
                font-size: 12px;
                color: var(--text-tertiary);
                margin-bottom: 4px;
              }
              
              .impact-content {
                font-size: 13px;
                color: var(--text-secondary);
                line-height: 1.5;
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
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .world-economy {
    .data-timeline {
      .timeline-indicator {
        width: 16px;
      }
      
      .data-items {
        .data-item {
          .date-marker {
            width: 50px;
          }
        }
      }
    }
  }
}
</style> 