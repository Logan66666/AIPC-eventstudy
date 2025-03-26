<template>
  <div class="card policy-card">
    <h2 class="card-title">政策催化</h2>
    <p class="card-subtitle">已发生与未来可能的政策事件</p>
    
    <div class="tabs">
      <div class="tab active">已发布</div>
      <div class="tab">预计6月</div>
      <div class="tab">预计Q3</div>
    </div>
    
    <div class="policy-list">
      <div class="policy-item">
        <div class="policy-content">
          <div class="policy-title">比如到2025年数字经济核心产业增加值GDP比重达到10%</div>
          <div class="policy-meta">
            <span class="tag policy">政策</span>
            <span class="policy-field">科技政策</span>、<span class="policy-field">推动数字经济</span>
          </div>
          <div class="policy-tags">
            <span class="tag field">科技</span>
            <span class="tag industry">新能源</span>
            <span class="tag stock">数字经济</span>
          </div>
        </div>
      </div>
      
      <div class="policy-item">
        <div class="policy-content">
          <div class="policy-title">出台20条措施，推动民营经济发展壮大</div>
          <div class="policy-meta">
            <span class="tag policy">政策</span>
            <span class="policy-field">经济政策</span>
          </div>
          <div class="policy-tags">
            <span class="tag field">科技</span>
            <span class="tag industry">新能源</span>
            <span class="tag stock">数字经济</span>
          </div>
        </div>
      </div>
      
      <div class="policy-item predicted">
        <div class="policy-content">
          <div class="policy-title">预计将出台新一轮新能源汽车购置补贴政策</div>
          <div class="policy-meta">
            <span class="tag manufacturing">传闻</span>
            <span class="policy-field">汽车产业</span>、<span class="policy-field">补贴政策</span>
          </div>
          <div class="policy-tags">
            <span class="tag field">科技</span>
            <span class="tag industry">新能源汽车</span>
          </div>
        </div>
      </div>
      
      <div class="policy-item predicted">
        <div class="policy-content">
          <div class="policy-title">预计将出台新一轮集成电路产业支持政策</div>
          <div class="policy-meta">
            <span class="tag ai">预测</span>
            <span class="policy-field">芯片产业</span>、<span class="policy-field">科技创新</span>
          </div>
          <div class="policy-tags">
            <span class="tag field">科技</span>
            <span class="tag industry">半导体</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PolicyCatalyst'
}
</script>

<style scoped lang="scss">
.policy-card {
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container) !important;
  height: 100%;
}

.card-title {
  margin-bottom: 4px;
}

.card-subtitle {
  margin-bottom: 16px;
  color: var(--hx-text-color-tertiary);
}

.tabs {
  display: flex;
  margin-bottom: 16px;
  border-bottom: 1px solid var(--hx-border-level-1-color);
}

.tab {
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  color: var(--hx-text-color-tertiary);
  position: relative;
  
  &.active {
    color: var(--hx-text-color-primary);
    font-weight: 500;
    
    &:after {
      content: '';
      position: absolute;
      left: 0;
      bottom: -1px;
      width: 100%;
      height: 2px;
      background-color: var(--hx-brand-color-1);
    }
  }
  
  &:hover:not(.active) {
    color: var(--hx-text-color-secondary);
  }
}

.policy-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  flex: 1;
  overflow-y: auto;
}

.policy-item {
  padding: 16px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--hx-border-level-1-color);
  display: flex;
  flex-direction: column;
  
  &.predicted {
    border-left: 3px solid #FF9F0A;
  }
}

.policy-content {
  flex: 1;
}

.policy-title {
  font-size: 14px;
  font-weight: 500;
  color: var(--hx-text-color-primary);
  margin-bottom: 8px;
  line-height: 1.4;
}

.policy-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  font-size: 12px;
  color: var(--hx-text-color-tertiary);
}

.policy-field {
  color: var(--hx-text-color-tertiary);
}

.policy-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  
  &.policy {
    background-color: #0071E3;
    color: white;
  }
  
  &.manufacturing {
    background-color: #FF9F0A;
    color: white;
  }
  
  &.ai {
    background-color: #34C759;
    color: white;
  }
  
  &.field {
    background-color: rgba(0, 113, 227, 0.1);
    color: #0071E3;
  }
  
  &.industry {
    background-color: rgba(52, 199, 89, 0.1);
    color: #34C759;
  }
  
  &.stock {
    background-color: rgba(255, 159, 10, 0.1);
    color: #FF9F0A;
  }
}
</style> 