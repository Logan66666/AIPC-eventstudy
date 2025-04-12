<template>
  <div 
    class="headline-card"
    :class="{'has-negative': item.NegativeImpact.length > 0}"
  >
    <!-- 卡片头部 -->
    <div class="card-header">
      <div class="event-meta">
        <div class="event-title-wrapper">
          <div class="event-icon" :class="getIconClass(item.EventTag)">
            <i :class="getIconForTag(item.EventTag)"></i>
          </div>
          <h3 class="event-title">{{ item.EventName }}</h3>
        </div>
        <div class="event-time">
          <i class="far fa-clock"></i>
          {{ formatTime(item.Time) }}
        </div>
      </div>
      <div class="event-tag" :class="getTagClass(item.EventTag)">
        {{ item.EventTag }}
      </div>
    </div>
    
    <!-- 卡片内容 -->
    <div class="card-content">
      <!-- 简介部分 -->
      <div class="event-intro">
        <p>{{ item.Introduction }}</p>
      </div>
      
      <!-- 详情部分 -->
      <div class="event-details">
        <!-- 标签信息区域 -->
        <div class="details-container">
          <!-- 看点 -->
          <div class="info-row highlights">
            <div class="info-label">
              <i class="fas fa-bullseye"></i>
              <span>看点</span>
            </div>
            <div class="info-content">
              <span v-for="(highlight, idx) in item.Highlights.split('/')" 
                    :key="idx" 
                    class="highlight-item">
                {{ highlight }}
              </span>
            </div>
          </div>
          
          <!-- 利好影响 -->
          <div v-if="item.PositiveImpact.filter(tag => tag.trim() !== '').length" class="info-row positive">
            <div class="info-label">
              <i class="fas fa-arrow-up"></i>
              <span>利好</span>
            </div>
            <div class="info-content">
              <div v-for="(tag, idx) in item.PositiveImpact.filter(tag => tag.trim() !== '')" 
                   :key="idx" 
                   class="impact-tag positive">
                {{ tag }}
              </div>
            </div>
          </div>
          
          <!-- 利空影响 -->
          <div v-if="item.NegativeImpact.filter(tag => tag.trim() !== '').length" class="info-row negative">
            <div class="info-label">
              <i class="fas fa-arrow-down"></i>
              <span>利空</span>
            </div>
            <div class="info-content">
              <div v-for="(tag, idx) in item.NegativeImpact.filter(tag => tag.trim() !== '')" 
                   :key="idx" 
                   class="impact-tag negative">
                {{ tag }}
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
  name: 'HeadlineCard',
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    formatTime(time) {
      return time;
    },
    getIconClass(tag) {
      const classes = {
        '政策': 'policy-icon',
        '全球': 'global-icon',
        '行业': 'industry-icon'
      };
      return classes[tag] || 'policy-icon';
    },
    getTagClass(tag) {
      const classes = {
        '政策': 'policy-tag',
        '全球': 'global-tag',
        '行业': 'industry-tag'
      };
      return classes[tag] || 'policy-tag';
    },
    getIconForTag(tag) {
      const icons = {
        '政策': 'fas fa-landmark',
        '全球': 'fas fa-globe-asia',
        '行业': 'fas fa-industry'
      };
      return icons[tag] || 'fas fa-info';
    }
  }
}
</script>

<style lang="scss" scoped>
.headline-card {
  position: relative;
  background-color: var(--hx-bg-color-container);
  border-radius: var(--hx-radius-default);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 220px;
  
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
    background-color: var(--hx-bg-color-specialcomponent);
  }
  
  &:focus-visible {
    outline: none;
    box-shadow: 0 0 0 2px var(--hx-brand-color-3), 0 4px 16px rgba(0, 0, 0, 0.15);
  }
  
  .card-header {
    padding: var(--hx-size-4) var(--hx-size-4) var(--hx-size-2);
    display: flex;
    justify-content: space-between;
    position: relative;
    z-index: 1;
    
    &:after {
      content: '';
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      height: 1px;
      background: var(--hx-border-level-1-color);
    }
    
    .event-meta {
      flex: 1;
      
      .event-title-wrapper {
        display: flex;
        align-items: center;
        margin-bottom: 6px;
        
        .event-icon {
          width: 24px;
          height: 24px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-right: 8px;
          
          i {
            font-size: 12px;
          }
          
          &.policy-icon {
            background-color: rgba(var(--hx-brand-color-rgb), 0.1);
            color: var(--hx-brand-color-3);
          }
          
          &.global-icon {
            background-color: rgba(var(--hx-sec-brand-color-rgb), 0.1);
            color: var(--hx-sec-brand-color-3);
          }
          
          &.industry-icon {
            background-color: rgba(var(--hx-warning-color-rgb), 0.1);
            color: var(--hx-warning-color-3);
          }
        }
        
        .event-title {
          font-size: 15px;
          font-weight: 600;
          color: var(--hx-text-color-primary);
          margin: 0;
          line-height: 1.3;
        }
      }
      
      .event-time {
        display: flex;
        align-items: center;
        gap: 4px;
        margin-left: 32px;
        color: var(--hx-text-color-tertiary);
        font: var(--hx-font-body-small);
        
        i {
          font-size: 12px;
        }
      }
    }
    
    .event-tag {
      font-size: 11px;
      font-weight: normal;
      padding: 0px 4px;
      border-radius: 2px;
      white-space: nowrap;
      flex-shrink: 0;
      
      &.policy-tag {
        background-color: rgba(var(--hx-brand-color-rgb), 0.1);
        color: var(--hx-brand-color-3);
      }
      
      &.global-tag {
        background-color: rgba(var(--hx-sec-brand-color-rgb), 0.1);
        color: var(--hx-sec-brand-color-3);
      }
      
      &.industry-tag {
        background-color: rgba(var(--hx-warning-color-rgb), 0.1);
        color: var(--hx-warning-color-3);
      }
    }
  }
  
  .card-content {
    padding: var(--hx-size-2) var(--hx-size-4) var(--hx-size-4);
    display: flex;
    flex-direction: column;
    flex: 1;
    
    .event-intro {
      margin-bottom: 4px;
      position: relative;
      flex: 0 0 auto;
      
      p {
        font-size: 13px;
        color: var(--hx-text-color-secondary);
        line-height: 1.5;
        margin: 0;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
        position: relative;
        transition: all 0.3s ease;
      }
      
      &:hover {
        p {
          -webkit-line-clamp: unset;
          line-clamp: unset;
          z-index: 10;
        }
      }
    }
    
    .event-details {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      
      .details-container {
        display: flex;
        flex-direction: column;
        gap: 4px;
        
        .info-row {
          display: flex;
          align-items: flex-start;
          
          .info-label {
            display: flex;
            align-items: center;
            font-size: 12px;
            min-width: 36px;
            flex: 0 0 36px;
            margin-right: 8px;
            
            i {
              margin-right: 4px;
              width: 14px;
              text-align: center;
              font-size: 9px;
              display: flex;
              align-items: center;
              justify-content: center;
              height: 14px;
            }
            
            span {
              white-space: nowrap;
            }
          }
          
          &.highlights .info-label {
            color: var(--hx-text-color-emphasize);
          }
          
          &.positive .info-label {
            color: var(--hx-raise-color-2);
          }
          
          &.negative .info-label {
            color: var(--hx-fall-color-2);
          }
          
          .info-content {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            
            .highlight-item {
              background-color: rgba(0, 0, 0, 0.2);
              padding: 2px 4px;
              border-radius: 2px;
              font-size: 11px;
              color: var(--hx-text-color-secondary);
              white-space: nowrap;
            }
            
            .impact-tag {
              padding: 0px 4px;
              border-radius: 2px;
              font-size: 11px;
              white-space: nowrap;
              
              &.positive {
                background-color: rgba(239, 68, 68, 0.1);
                color: var(--hx-raise-color-2);
              }
              
              &.negative {
                background-color: rgba(16, 185, 129, 0.1);
                color: var(--hx-fall-color-2);
              }
            }
          }
        }
      }
    }
  }
}
</style> 