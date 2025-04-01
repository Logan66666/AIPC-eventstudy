<template>
  <div class="data-timeline">
    <!-- 左侧固定宽度的时间线容器 -->
    <div class="timeline-indicator">
      <div class="timeline-line"></div>
    </div>
    
    <!-- 右侧滚动内容区 -->
    <div class="timeline-items">
      <template v-if="items && items.length > 0">
        <div 
          v-for="(item, index) in items" 
          :key="index"
          class="timeline-item"
          :class="{'expanded': expandedItem === index, 'is-today': isToday(item.date)}"
          @click="toggleExpand(index)"
        >
          <!-- 圆点标记容器，需要与时间线对齐 -->
          <div class="date-marker">
            <div class="marker" :class="{'past-or-today': isTodayOrBefore(item.date)}"></div>
            <div class="date-text" :class="{'past-or-today': isTodayOrBefore(item.date)}">
              {{ formatDate(item.date) }}
            </div>
            <div class="today-text" v-if="isToday(item.date)">今日</div>
            <div class="tomorrow-text" v-if="isTomorrow(item.date)">明日</div>
          </div>
          
          <div class="item-content">
            <!-- 头部区域 -->
            <div class="item-header-row">
              <div class="item-meta">
                <slot name="item-meta" :item="item"></slot>
              </div>
            </div>
            
            <!-- 标题区域 -->
            <div class="item-title-row">
              <div class="item-tag-and-title">
                <slot name="item-tag" :item="item"></slot>
                <h3 class="item-title">{{ item.title }}</h3>
                <slot name="item-indicators" :item="item"></slot>
              </div>
              
              <div class="expand-icon">
                <i v-if="expandedItem !== index" class="fas fa-chevron-down"></i>
                <i v-else class="fas fa-chevron-up"></i>
              </div>
            </div>
            
            <!-- 预览区域 -->
            <div class="item-preview">{{ item.summary }}</div>
            
            <!-- 详情区域 -->
            <div class="item-details" v-show="expandedItem === index">
              <!-- 解读部分 -->
              <div class="context-container" v-if="item.context">
                <div class="section-label"><i class="fas fa-history"></i> 解读</div>
                <div class="context-content">{{ item.context }}</div>
              </div>
              
              <!-- 看点部分 -->
              <div class="highlights-container" v-if="item.highlights && item.highlights.length">
                <div class="section-label"><i class="fas fa-lightbulb"></i> 看点</div>
                <div class="highlights-list">
                  <div v-for="(highlight, idx) in item.highlights" :key="idx" class="highlight-item">
                    <div class="highlight-tag">{{ highlight.tag }}</div>
                    <div class="highlight-reason">{{ highlight.reason }}</div>
                  </div>
                </div>
              </div>
              
              <!-- 利好部分 -->
              <div class="benefits-container" v-if="item.benefits && item.benefits.length">
                <div class="section-label"><i class="fas fa-arrow-up"></i> 利好</div>
                <div class="benefits-list">
                  <div v-for="(benefit, idx) in item.benefits" :key="idx" class="benefit-item">
                    <div class="benefit-tag">{{ benefit.tag }}</div>
                    <div class="benefit-reason">{{ benefit.reason }}</div>
                  </div>
                </div>
              </div>
              
              <!-- 利空部分 -->
              <div class="drawbacks-container" v-if="item.drawbacks && item.drawbacks.length">
                <div class="section-label"><i class="fas fa-arrow-down"></i> 利空</div>
                <div class="drawbacks-list">
                  <div v-for="(drawback, idx) in item.drawbacks" :key="idx" class="drawback-item">
                    <div class="drawback-tag">{{ drawback.tag }}</div>
                    <div class="drawback-reason">{{ drawback.reason }}</div>
                  </div>
                </div>
              </div>
              
              <!-- 自定义内容插槽 -->
              <slot name="item-details-custom" :item="item"></slot>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <div class="empty-state">
          <div class="empty-icon">
            <svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M32 54.6668C44.6667 54.6668 54.6667 44.6668 54.6667 32.0001C54.6667 19.3334 44.6667 9.33342 32 9.33342C19.3334 9.33342 9.33337 19.3334 9.33337 32.0001C9.33337 44.6668 19.3334 54.6668 32 54.6668Z" stroke="#BFBFBF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M24 29.3334V32.0001M32 29.3334V32.0001M40 29.3334V32.0001" stroke="#BFBFBF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M26.5834 40.0001C30.1667 42.0001 33.8334 42.0001 37.4167 40.0001" stroke="#BFBFBF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="empty-text">{{ emptyText }}</div>
          <div class="empty-subtext">{{ emptySubtext }}</div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
// 引入FontAwesome
import '@fortawesome/fontawesome-free/css/all.css'

export default {
  name: 'DataTimeline',
  props: {
    items: {
      type: Array,
      required: true
    },
    initialExpandedItem: {
      type: Number,
      default: null
    },
    emptyText: {
      type: String,
      default: '暂无数据'
    },
    emptySubtext: {
      type: String,
      default: '我们正在整理相关数据，请稍后查看'
    }
  },
  data() {
    return {
      expandedItem: null
    }
  },
  methods: {
    toggleExpand(index) {
      if (this.expandedItem === index) {
        this.expandedItem = null;
      } else {
        this.expandedItem = index;
      }
      this.$emit('item-expanded', { index, item: this.items[index], expanded: this.expandedItem === index });
    },
    
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return `${date.getMonth() + 1}月${date.getDate()}日`;
    },
    
    isToday(dateStr) {
      // 把输入的日期字符串转换为日期对象
      const [year, month, day] = dateStr.split('/').map(num => parseInt(num, 10));
      const date = new Date(year, month - 1, day);
      date.setHours(0, 0, 0, 0);
      
      // 获取真实的当前日期（只考虑日期部分）
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      
      // 完整比较年月日
      return date.getTime() === today.getTime();
    },
    
    isTomorrow(dateStr) {
      // 把输入的日期字符串转换为日期对象
      const [year, month, day] = dateStr.split('/').map(num => parseInt(num, 10));
      const date = new Date(year, month - 1, day);
      date.setHours(0, 0, 0, 0);
      
      // 获取明日的日期
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      tomorrow.setHours(0, 0, 0, 0);
      
      // 完整比较年月日
      return date.getTime() === tomorrow.getTime();
    },
    
    isTodayOrBefore(dateStr) {
      // 将日期字符串转换为日期对象
      const [year, month, day] = dateStr.split('/').map(num => parseInt(num, 10));
      // 注意：JavaScript中月份从0开始，所以需要减1
      const date = new Date(year, month - 1, day);
      date.setHours(0, 0, 0, 0);
      
      // 获取真实的当前日期
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      
      // 完整比较年月日
      return date.getTime() <= today.getTime();
    }
  }
}
</script>

<style lang="scss" scoped>
.data-timeline {
  flex: 1;
  display: flex;
  height: 100%;
  
  .timeline-indicator {
    width: 0px;
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
  
  .timeline-items {
    flex: 1;
    overflow-y: auto;
    padding-right: var(--hx-comp-paddingLR-s);
    
    &::-webkit-scrollbar {
      width: 8px;
    }
    
    &::-webkit-scrollbar-track {
      background: var(--hx-bg-color-container);
      border-radius: 4px;

    }
    
    &::-webkit-scrollbar-thumb {
      background: var(--hx-bg-color-specialcomponent);
      border-radius: 4px;
      
      &:hover {
        background: var(--hx-border-level-2-color);
      }
    }

    .timeline-item {
      display: flex;
      margin-bottom: var(--hx-comp-margin-m);
      position: relative;
      
      .item-content {
        flex: 1;
        margin-left: var(--hx-size-4);
        background-color: var(--hx-bg-color-specialcomponent);
        border-radius: var(--hx-radius-small);
        padding: var(--hx-comp-paddingTB-xs) var(--hx-comp-paddingLR-s);
        border: 1px solid var(--hx-bg-color-specialcomponent);
        
        .item-header-row {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: var(--hx-comp-margin-xs);
          
          .item-meta {
            display: flex;
            align-items: center;
            gap: var(--hx-comp-margin-s);
          }
        }
        
        .item-title-row {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: var(--hx-comp-margin-xs);
          
          .item-tag-and-title {
            display: flex;
            align-items: center;
            gap: 8px;
            flex: 1;
            min-width: 0;
            overflow: hidden;
          }
          
          .item-title {
            font-size: 14px;
            font-weight: 600;
            color: var(--hx-text-color-primary);
            margin: 0;
            line-height: 1.4;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            flex-shrink: 1;
            min-width: 0;
          }
          
          .expand-icon {
            flex-shrink: 0;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background-color: var(--hx-bg-color-container);
            color: var(--hx-text-color-secondary);
            font-size: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-left: 8px;
            
            &:hover {
              background-color: var(--hx-bg-color-specialcomponent);
              color: var(--hx-brand-color-3);
            }
          }
        }
        
        .item-preview {
          font-size: 13px;
          color: var(--hx-text-color-secondary);
          margin-bottom: var(--hx-comp-margin-s);
          line-height: 1.5;
        }
        
        .item-details {
          padding-top: var(--hx-comp-margin-s);
          animation: slideDown 0.3s ease;
          
          .section-label {
            font-size: 12px;
            margin-bottom: var(--hx-comp-margin-xs);
            font-weight: 500;
            display: flex;
            align-items: center;
            
            i {
              margin-right: 4px;
              font-size: 11px;
            }
          }
          
          .context-container, .highlights-container, .benefits-container, .drawbacks-container {
            margin-bottom: var(--hx-comp-margin-s);
            position: relative;
            
            &:not(:last-child) {
              padding-bottom: var(--hx-comp-margin-s);
              border-bottom: 1px dashed var(--hx-border-level-1-color);
            }
          }
          
          .context-container {
            .section-label {
              color: var(--hx-text-color-primary);
              
              i {
                color: var(--hx-text-color-primary);
              }
            }
            
            .context-content {
              font-size: 12px;
              color: var(--hx-text-color-secondary);
              line-height: 1.5;
              background-color: var(--hx-bg-color-container);
              padding: var(--hx-comp-paddingTB-xxs) var(--hx-comp-paddingLR-xs);
              padding-left: 16px;
              border-radius: var(--hx-radius-small);
              border-left: 2px solid var(--hx-text-color-tertiary);
            }
          }
          
          .highlights-container {
            .section-label {
              color: var(--hx-brand-color-2);
              
              i {
                color: var(--hx-brand-color-2);
              }
            }
          }
          
          .benefits-container {
            .section-label {
              color: var(--hx-raise-color-2);
              
              i {
                color: var(--hx-raise-color-2);
              }
            }
          }
          
          .drawbacks-container {
            .section-label {
              color: var(--hx-fall-color-2);
              
              i {
                color: var(--hx-fall-color-2);
              }
            }
          }
          
          .highlights-list, .benefits-list, .drawbacks-list {
            display: flex;
            flex-direction: column;
            gap: var(--hx-comp-margin-xs);
            
            .highlight-item, .benefit-item, .drawback-item {
              display: flex;
              flex-direction: column;
              gap: 4px;
              background-color: var(--hx-bg-color-container);
              padding: var(--hx-comp-paddingTB-xxs) var(--hx-comp-paddingLR-xs);
              padding-left: 16px;
              border-radius: var(--hx-radius-small);
              
              .highlight-tag, .benefit-tag, .drawback-tag {
                font-size: 12px;
                font-weight: 600;
                color: var(--hx-text-color-primary);
              }
              
              .highlight-reason, .benefit-reason, .drawback-reason {
                font-size: 12px;
                color: var(--hx-text-color-secondary);
                line-height: 1.4;
              }
            }
          }
          
          .highlights-list .highlight-item {
            border-left: 2px solid var(--hx-brand-color-3);
          }
          
          .benefits-list .benefit-item {
            border-left: 2px solid var(--hx-raise-color-2);
          }
          
          .drawbacks-list .drawback-item {
            border-left: 2px solid var(--hx-fall-color-2);
          }
        }
      }
      
      &.is-today {
        .item-content {
          border: 1px solid var(--hx-brand-color-3);
        }
      }
      
      &.expanded {
        .item-content {
          border: 1px solid var(--hx-brand-color-3);
        }
        
        .expand-icon i {
          transform: rotate(180deg);
        }
      }
      
      .date-marker {
        width: 84px;
        position: relative;
        flex-shrink: 0;
        display: flex;
        flex-direction: column;
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
            border-color: var(--hx-text-color-primary);
          }
        }

        .date-text {
          position: absolute;
          left: 30px;
          top: 8px;
          font-size: 12px;
          color: var(--hx-text-color-tertiary);
          
          &.past-or-today {
            color: var(--hx-text-color-primary);
          }
        }
        
        .today-text {
          position: absolute;
          left: 30px;
          top: 26px;
          font-size: 11px;
          color: var(--hx-brand-color-3);
          font-weight: 500;
        }
        
        .tomorrow-text {
          position: absolute;
          left: 30px;
          top: 26px;
          font-size: 11px;
          color: var(--hx-warning-color-3, #d97706);
          font-weight: 500;
        }
      }
    }
    
    .empty-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100%;
      min-height: 240px;
      padding: 32px 16px;
      text-align: center;
      
      .empty-icon {
        margin-bottom: 16px;
      }
      
      .empty-text {
        font-size: 16px;
        font-weight: 500;
        color: var(--hx-text-color-secondary);
        margin-bottom: 8px;
      }
      
      .empty-subtext {
        font-size: 13px;
        color: var(--hx-text-color-tertiary);
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
  .data-timeline {
    .timeline-items {
      .timeline-item {
        .date-marker {
          width: var(--hx-size-10);
        }
        
        .item-content {
          .item-title-row {
            .item-title {
              font-size: 13px;
            }
          }
          
          .item-preview {
            font-size: 12px;
          }
        }
      }
    }
  }
}
</style> 