<template>
  <div class="card opportunity-card">
    <h2 class="card-title">埋伏机会</h2>
    <p class="card-subtitle">左侧投资机会前瞻</p>
    
    <div class="opportunity-list">
      <div v-for="(opportunity, index) in opportunities" :key="index" class="opportunity-item">
        <div class="opportunity-header">
          <h3>{{ opportunity.title }}</h3>
          <span class="opportunity-timing">时间窗口：{{ opportunity.timeWindow }}</span>
        </div>
        <p>{{ opportunity.description }}</p>
        <div class="opportunity-stocks">
          <span v-for="(stock, stockIndex) in opportunity.stocks" :key="stockIndex" class="stock-tag">{{ stock }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InvestmentOpportunity',
  data() {
    return {
      opportunities: [
        {
          title: '新能源智能汽车',
          timeWindow: '6月-8月',
          description: '随着新一轮新能源汽车补贴政策出台，叠加传统汽车消费季，预计Q3智能电动车销量将迎来拐点',
          stocks: ['比亚迪', '宁德时代', '长城汽车']
        },
        {
          title: '半导体国产化',
          timeWindow: 'Q3-Q4',
          description: '随着国家集成电路产业政策落地以及下半年消费电子需求回暖，国产芯片设计和制造企业有望受益',
          stocks: ['中芯国际', '韦尔股份', '北方华创']
        }
      ]
    }
  }
}
</script>

<style scoped lang="scss">
.opportunity-card {
  background-color: var(--hx-bg-color-container) !important;
  height: 100%;
}

.opportunity-list {
  display: flex;
  flex-direction: column;
  gap: var(--hx-size-4);
}

.opportunity-item {
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: var(--hx-radius-default);
  padding: var(--hx-size-3);
  border: 1px solid var(--hx-border-level-1-color);
}

.opportunity-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--hx-size-2);
  
  h3 {
    font-size: var(--hx-font-size-title-small);
    color: var(--hx-text-color-primary);
    margin: 0;
  }
}

.opportunity-timing {
  font-size: var(--hx-font-size-body-small);
  color: var(--hx-text-color-tertiary);
}

.opportunity-stocks {
  display: flex;
  flex-wrap: wrap;
  gap: var(--hx-size-2);
  margin-top: var(--hx-size-3);
}

.stock-tag {
  display: inline-block;
  padding: var(--hx-size-1) var(--hx-size-2);
  background-color: var(--hx-brand-color-1);
  color: var(--hx-brand-color-5);
  border-radius: var(--hx-radius-small);
  font-size: var(--hx-font-size-body-small);
}
</style> 