<template>
  <div class="event-tag" :class="eventClass">
    {{ text }}
  </div>
</template>

<script>
export default {
  name: 'EventTag',
  props: {
    text: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: null
    },
    typeMap: {
      type: Object,
      default: () => ({})
    }
  },
  computed: {
    eventClass() {
      // 优先使用传入的明确类型
      if (this.type) {
        return this.type;
      }
      
      // 其次使用类型映射
      if (this.typeMap[this.text]) {
        return this.typeMap[this.text];
      }
      
      // 最后使用默认类型映射
      const defaultClasses = {
        '高层会议': 'official',
        '部委政策': 'planning',
        '地方政策': 'local',
        '国际政策': 'international',
        '金融政策': 'financial',
        '产业政策': 'industry',
        '数据': 'data',
        '指标': 'metric',
        '经济': 'economy',
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      };
      
      return defaultClasses[this.text] || 'other';
    }
  }
}
</script>

<style lang="scss" scoped>
.event-tag {
  font-size: 11px;
  font-weight: normal;
  padding: 0px 4px;
  border-radius: 2px;
  flex-shrink: 0;
  white-space: nowrap;
  
  &.official {
    background-color: rgba(36, 107, 248, 0.15);
    color: var(--hx-brand-color-3);
  }
  
  &.planning {
    background-color: rgba(255, 149, 0, 0.15);
    color: var(--hx-warning-color-2);
  }
  
  &.local {
    background-color: rgba(250, 204, 21, 0.15);
    color: #facc15;
  }
  
  &.international {
    background-color: rgba(6, 182, 212, 0.15);
    color: var(--hx-info-color-2);
  }
  
  &.financial {
    background-color: rgba(16, 185, 129, 0.15);
    color: var(--hx-success-color-2);
  }
  
  &.industry {
    background-color: rgba(139, 92, 246, 0.15);
    color: var(--hx-purple-color-2, #8b5cf6);
  }
  
  &.data, &.metric, &.economy {
    background-color: rgba(36, 107, 248, 0.15);
    color: var(--hx-brand-color-3);
  }
  
  &.time-short {
    background-color: rgba(239, 68, 68, 0.15);
    color: #ef4444;
  }
  
  &.time-mid {
    background-color: rgba(245, 158, 11, 0.15);
    color: #f59e0b;
  }
  
  &.time-long {
    background-color: rgba(6, 182, 212, 0.15);
    color: #06b6d4;
  }
  
  &.other {
    background-color: rgba(100, 116, 139, 0.15);
    color: var(--hx-text-color-tertiary);
  }
}
</style> 