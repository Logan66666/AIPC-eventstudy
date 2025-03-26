<template>
  <div class="card timeline-card">
    <h2 class="card-title">世界经济</h2>
    <p class="card-subtitle">全球重要经济数据解读</p>
    
    <div class="timeline">
      <div v-for="(event, index) in economyEvents" :key="index" class="timeline-item">
        <div class="timeline-date">
          <span class="date-text">{{ event.date }}</span>
          <span class="date-connector"></span>
        </div>
        <div class="timeline-content">
          <h3>{{ event.title }}</h3>
          <p>{{ event.description }}</p>
          <div class="timeline-decorator"></div>
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
      economyEvents: [
        {
          date: '5月20日',
          title: '美国PCE物价指数发布',
          description: '预计同比增长4.2%，环比增长0.3%，通胀压力继续缓解'
        },
        {
          date: '5月23日',
          title: '欧元区PMI数据公布',
          description: '制造业PMI预期51.2，服务业PMI预期54.5，经济复苏动能增强'
        },
        {
          date: '5月31日',
          title: '中国5月PMI数据',
          description: '市场预期制造业PMI保持在扩张区间，经济恢复趋势向好'
        },
        {
          date: '6月2日',
          title: '美国就业数据',
          description: '非农就业人口预期增加18万，失业率维持在3.4%，就业市场仍然强劲'
        }
      ]
    }
  }
}
</script>

<style scoped lang="scss">
.timeline-card {
  position: relative;
  backdrop-filter: blur(10px);
  
  /* 添加科技感装饰 */
  &:before {
    content: '';
    position: absolute;
    bottom: 20px;
    left: 20px;
    width: 60px;
    height: 60px;
    background: radial-gradient(circle, var(--hx-sec-brand-color-1) 1px, transparent 1px);
    background-size: 8px 8px;
    opacity: 0.2;
    z-index: 0;
  }
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: var(--hx-size-3);
  position: relative;
  z-index: 1;
  padding-left: var(--hx-size-2);
}

.timeline-item {
  display: flex;
  gap: var(--hx-size-3);
  position: relative;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  
  &:hover {
    transform: translateX(4px);
    
    .timeline-content {
      border-color: var(--hx-border-level-2-color);
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    .timeline-date .date-connector {
      background: var(--hx-sec-brand-color-1);
      box-shadow: 0 0 10px var(--hx-sec-brand-color-1);
    }
    
    .timeline-decorator {
      opacity: 1;
    }
  }
}

.timeline-date {
  flex: 0 0 65px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  position: relative;
  
  .date-text {
    font-weight: 500;
    color: var(--hx-text-color-tertiary);
    font-size: var(--hx-font-size-body-small);
    padding-right: var(--hx-size-2);
    transition: color 0.3s ease;
  }
  
  .date-connector {
    position: absolute;
    right: -7px;
    top: 8px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--hx-border-level-2-color);
    border: 2px solid var(--hx-bg-color-container);
    z-index: 2;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  }
  
  &:after {
    content: '';
    position: absolute;
    right: 0;
    top: 15px;
    bottom: -30px;
    width: 1px;
    background: linear-gradient(to bottom, var(--hx-border-level-2-color), transparent);
    z-index: 1;
  }
}

.timeline-content {
  flex: 1;
  background-color: rgba(var(--hx-bg-color-container), 0.5);
  border-radius: var(--hx-radius-default);
  padding: var(--hx-size-3);
  border: 1px solid var(--hx-border-level-1-color);
  position: relative;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  overflow: hidden;
  
  h3 {
    font-size: var(--hx-font-size-title-small);
    color: var(--hx-text-color-primary);
    margin-bottom: var(--hx-size-2);
    font-weight: 600;
    position: relative;
    display: inline-block;
    
    /* 添加标题下划线效果 */
    &:after {
      content: '';
      position: absolute;
      left: 0;
      bottom: -3px;
      width: 0;
      height: 1px;
      background-color: var(--hx-sec-brand-color-1);
      transition: width 0.3s ease;
    }
  }
  
  &:hover h3:after {
    width: 100%;
  }
  
  p {
    font-size: var(--hx-font-size-body-small);
    color: var(--hx-text-color-secondary);
    margin: 0;
    line-height: 1.5;
  }
  
  &:before {
    content: '';
    position: absolute;
    left: -8px;
    top: 10px;
    width: 0;
    height: 0;
    border-top: 6px solid transparent;
    border-bottom: 6px solid transparent;
    border-right: 8px solid var(--hx-border-level-1-color);
    transition: border-right-color 0.3s ease;
  }
  
  &:hover:before {
    border-right-color: var(--hx-border-level-2-color);
  }
}

.timeline-decorator {
  position: absolute;
  right: 10px;
  bottom: 10px;
  width: 40px;
  height: 40px;
  background: radial-gradient(circle, var(--hx-sec-brand-color-1) 1px, transparent 1px);
  background-size: 8px 8px;
  opacity: 0.3;
  transition: opacity 0.3s ease;
}

.timeline-item:last-child .timeline-date:after {
  display: none;
}
</style> 