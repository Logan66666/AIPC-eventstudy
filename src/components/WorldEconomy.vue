<template>
  <div class="world-economy card">
    <div class="economy-header">
      <h2 class="card-title secondary-title">世界经济</h2>
      <div class="card-subtitle">全球重要经济数据动态解读</div>
    </div>
    
    <div class="economy-content">
      <div class="data-timeline">
        <!-- 左侧固定宽度的时间线容器 -->
        <div class="timeline-indicator">
          <div class="timeline-line"></div>
        </div>
        
        <!-- 右侧滚动内容区 -->
        <div class="data-items">
          <div 
            v-for="(item, index) in sortedEconomyData" 
            :key="index"
            class="data-item"
            :class="{
              'is-today': isToday(item.date),
              'is-hover': hoveredIndex === index
            }"
            @mouseenter="hoveredIndex = index"
            @mouseleave="hoveredIndex = null"
            role="article"
            :aria-label="item.title + '数据详情'"
          >
            <!-- 圆点标记容器，需要与时间线对齐 -->
            <div class="date-marker">
              <div class="marker" :class="{
                'pulse': isToday(item.date),
                'past-or-today': isTodayOrBefore(item.date)
              }"></div>
              <div class="date-text" :class="{'past-or-today': isTodayOrBefore(item.date)}">
                {{ formattedDates(item.date) }}
              </div>
              <div class="today-text" v-if="isToday(item.date)">今日</div>
            </div>
            
            <!-- 数据内容 -->
            <div class="item-content">
              <div class="item-header">
                <h3 class="item-title">{{ item.title }}</h3>
                <div class="detail-metrics" role="group" :aria-label="item.title + '的具体数据'">
                  <div class="metric" role="group" aria-label="前值">
                    <div class="metric-label">前值</div>
                    <div class="metric-value">{{ item.previous }}</div>
                  </div>
                  <div class="metric" role="group" aria-label="预期值">
                    <div class="metric-label">预期</div>
                    <div class="metric-value">{{ item.expected }}</div>
                  </div>
                  <div class="metric" role="group" aria-label="实际值">
                    <div class="metric-label">实际</div>
                    <div class="metric-value" :class="[item.actual && item.actual !== '--' ? getChangeClass(item.actualChange) : '']">
                      {{ item.actual }}
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="item-details">
                <div class="impact-content">{{ item.impact }}</div>
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
    const today = new Date();
    const formattedToday = `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`;
    
    return {
      hoveredIndex: null,
      economyData: [
        {
          date: '2025/3/12',
          title: '美国CPI数据公布',
          actual: '+3.1%',
          expected: '+3.3%',
          previous: '+3.2%',
          actualChange: 'negative',
          impact: '通胀数据低于预期，美联储6月暂停加息概率升至95%，美股期货走高，美债收益率下行，美元指数承压。'
        },
        {
          date: '2025/3/20',
          title: '美国PCE物价指数发布',
          actual: '+4.2%',
          expected: '+4.1%',
          previous: '+4.4%',
          actualChange: 'positive',
          impact: '数据略高于预期但整体符合市场预期，美联储维持现有货币政策立场概率增大，美股震荡走高，美元指数小幅走强，黄金价格承压。'
        },
        {
          date: '2025/3/23',
          title: '欧元区PMI数据公布',
          actual: '50.8',
          expected: '51.2',
          previous: '53.6',
          actualChange: 'negative',
          impact: '服务业PMI超预期增长，显示欧元区经济动能强劲，欧元兑美元走强，欧洲股市普涨，能源和银行板块表现尤为突出。'
        },
        {
          date: formattedToday,
          title: '中国5月PMI数据',
          actual: '50.2',
          expected: '50.5',
          previous: '50.4',
          actualChange: 'negative',
          impact: '制造业PMI低于预期但仍处于扩张区间，国内需求恢复缓慢，A股市场小幅回调，关注后续政策刺激举措。'
        },
        {
          date: '2025/4/2',
          title: '美国就业数据',
          actual: '--',
          expected: '18万',
          previous: '23.6万',
          actualChange: 'neutral',
          impact: '关注数据与预期差异，将直接影响美联储6月议息会议决策，进而影响全球资本市场走向。'
        },
        {
          date: '2025/4/3',
          title: '欧元区CPI初值公布',
          actual: '--',
          expected: '+2.5%',
          previous: '+2.6%',
          actualChange: 'negative',
          impact: '通胀数据低于预期，欧央行降息预期升温，欧元区主要股指普涨，欧元兑美元小幅走弱，欧债收益率下行。'
        },
        {
          date: '2025/4/5',
          title: '美国非农就业报告',
          actual: '--',
          expected: '20万',
          previous: '23.6万',
          actualChange: 'positive',
          impact: '就业数据强于预期，表明劳动力市场依然稳健，美联储6月降息预期降温，美元指数走强，美债收益率上行，黄金价格承压。'
        }
      ]
    }
  },
  computed: {
    sortedEconomyData() {
      return this.economyData.slice().sort((a, b) => new Date(a.date) - new Date(b.date));
    },
    formattedDates() {
      const cache = new Map();
      return (dateStr) => {
        if (cache.has(dateStr)) return cache.get(dateStr);
        const date = new Date(dateStr);
        const formatted = `${date.getMonth() + 1}月${date.getDate()}日`;
        cache.set(dateStr, formatted);
        return formatted;
      };
    }
  },
  methods: {
    isToday(dateStr) {
      if (!this._today) {
        this._today = new Date().setHours(0, 0, 0, 0);
      }
      return new Date(dateStr).setHours(0, 0, 0, 0) === this._today;
    },
    isTodayOrBefore(dateStr) {
      if (!this._today) {
        this._today = new Date().setHours(0, 0, 0, 0);
      }
      return new Date(dateStr).setHours(0, 0, 0, 0) <= this._today;
    },
    getChangeClass(changeType) {
      switch(changeType) {
        case 'positive':
          return 'better-than-expected';
        case 'negative':
          return 'worse-than-expected';
        default:
          return 'change-neutral';
      }
    },
    getChangeDescription(changeType) {
      switch(changeType) {
        case 'positive':
          return '好于预期';
        case 'negative':
          return '差于预期';
        default:
          return '符合预期';
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.world-economy {
  height: 100%;
  max-height: 600px;  // 设置最大高度
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  
  .economy-header {
    padding: var(--hx-comp-paddingTB-xs) var(--hx-comp-paddingLR-s);
    flex-shrink: 0;  // 防止header被压缩
  }
  
  .economy-content {
    flex: 1;
    overflow: hidden;
    min-height: 0;  // 确保flex布局下的滚动正常工作
    
    .data-timeline {
      display: flex;
      height: 100%;
      
      .timeline-indicator {
        width: 0px;  //直线宽度，改为0之后圆点重合
        position: relative;
        display: flex;
        justify-content: center;
        flex-shrink: 0;
        
        .timeline-line {
          position: absolute;
          top: 0;
          bottom: 0;
          left: 20px;
          width: 2px;
          background-color: var(--hx-border-level-2-color);
          opacity: 0.3;
          transform: translateX(-50%);
        }
      }
      
      .data-items {
        flex: 1;
        overflow-y: auto;
        padding-right: var(--hx-comp-paddingLR-s);
        
        // 自定义滚动条样式
        &::-webkit-scrollbar {
          width: 8px;  // 保持细滚动条
        }
        
        &::-webkit-scrollbar-track {
          background: var(--hx-bg-color-container);  // 使用容器背景色
          border-radius: 4px;
          margin: var(--hx-comp-margin-l) 0;  // 保持较短的滚动条
        }
        
        &::-webkit-scrollbar-thumb {
          background: var(--hx-bg-color-specialcomponent);  // 使用边框颜色
          border-radius: 4px;
          
          &:hover {
            background: var(--hx-border-level-2-color);  // hover时使用深一级的边框颜色
          }
        }

        .data-item {
          display: flex;
          margin-bottom: var(--hx-comp-margin-m);
          position: relative;
          
          &.is-today {
            .item-content {
              border: 1px solid var(--hx-brand-color-3)
            }
            
            .today-text {
              position: absolute;
              left: 30px;
              top: 26px;  // 位于日期下方
              font-size: 11px;
              color: var(--hx-brand-color-3);
              font-weight: 500;
            }
          }
          
          .date-marker {
            width: 80px;  // 圆点和日期的宽度
            position: relative;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;  // 改为纵向排列
            align-items: flex-start;
            
            .marker {
              position: absolute;
              width: 8px;
              height: 8px;
              border-radius: 50%;
              background-color: var(--hx-bg-color-container);
              border: 2px solid var(--hx-border-level-2-color);
              top: 14px;
              left: 20px;
              transform: translateX(-50%);
              z-index: 1;

              &.past-or-today {
                border-color: var(--hx-text-color-secondary);
              }
            }

            .date-text {
              position: absolute;
              left: 30px;
              top: 8px;
              font-size: 12px;
              color: var(--hx-text-color-tertiary);

              &.past-or-today {
                color: var(--hx-text-color-secondary);
              }
            }
          }
          
          .item-content {
            flex: 1;
            margin-left: var(--hx-size-4);
            background-color: var(--hx-bg-color-specialcomponent);
            border-radius: var(--hx-radius-small);
            padding: var(--hx-comp-paddingTB-xxs) var(--hx-comp-paddingLR-s);
            
            .item-header {
              display: flex;
              justify-content: space-between;
              align-items: center;
              margin-bottom: 0;
              
              .item-title {
                font-size: 14px;
                font-weight: 600;
                color: var(--hx-text-color-primary);
                margin: 0;
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
                    font-size: 12px;
                    color: var(--hx-text-color-tertiary);
                    opacity: 0.8;
                  }
                  
                  .metric-value {
                    font-size: 14px;
                    color: var(--hx-text-color-secondary);
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    
                    &.better-than-expected {
                      color: var(--hx-raise-color-2);
                      &::after {
                        content: '超过预期';
                        font-size: 11px;
                        padding: 2px 4px;
                        border-radius: 2px;
                        background-color: rgba(239, 68, 68, 0.1);
                        color: var(--hx-raise-color-2);
                        white-space: nowrap;
                      }
                    }
                    
                    &.worse-than-expected {
                      color: var(--hx-fall-color-2);
                      &::after {
                        content: '低于预期';
                        font-size: 11px;
                        padding: 2px 4px;
                        border-radius: 2px;
                        background-color: rgba(16, 185, 129, 0.1);
                        color: var(--hx-fall-color-2);
                        white-space: nowrap;
                      }
                    }

                    &.change-neutral {
                      color: var(--hx-text-color-secondary);
                      &::after {
                        content: '符合预期';
                        font-size: 11px;
                        padding: 2px 4px;
                        border-radius: 2px;
                        background-color: rgba(0, 0, 0, 0.1);
                        color: var(--hx-text-color-tertiary);
                        white-space: nowrap;
                      }
                    }
                  }
                }
              }
            }
            
            .item-details {
              border-top: 1px solid var(--hx-border-level-1-color);
              padding-top: var(--hx-comp-paddingTB-xxs);
              
              .impact-content {
                font-size: 13px;
                color: var(--hx-text-color-secondary);
                line-height: 1.5;
              }
            }
          }
        }
      }
    }
  }
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

@keyframes pulse {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.6;
  }
  70% {
    transform: translate(-50%, -50%) scale(2);
    opacity: 0;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@media (max-width: 1200px) {
  .world-economy {
    .data-timeline {
      .data-items {
        .data-item {
          .item-content {
            .item-header {
              flex-direction: column;
              gap: var(--hx-comp-margin-s);
              
              .detail-metrics {
                width: 100%;
                justify-content: space-between;
              }
            }
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .world-economy {
    .data-timeline {
      .timeline-indicator {
        width: var(--hx-size-10);
      }
      
      .data-items {
        padding: 0 var(--hx-comp-paddingLR-xs);
        
        .data-item {
          .date-marker {
            width: var(--hx-size-10);
          }
          
          .item-content {
            .item-header {
              .detail-metrics {
                .metric {
                  padding: var(--hx-comp-paddingTB-xxs) var(--hx-comp-paddingLR-xs);
                  
                  .metric-label {
                    font-size: 11px;
                  }
                  
                  .metric-value {
                    font-size: 13px;
                  }
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