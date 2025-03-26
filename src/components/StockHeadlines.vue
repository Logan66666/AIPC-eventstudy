<template>
  <div class="card headline-card">
    <h2 class="card-title">股市头条</h2>
    <p class="card-subtitle">影响A股的重要事件</p>
    
    <div class="headline-list">
      <div v-for="(headline, index) in headlines" :key="index" class="headline-item">
        <div class="headline-content-container">
          <div class="headline-header">
            <span :class="['headline-tag', headline.tagType]">{{ headline.tagText }}</span>
            <div class="headline-date">{{ headline.date }}</div>
          </div>
          <h3 class="headline-title">{{ headline.title }}</h3>
          <p class="headline-content">{{ headline.content }}</p>
        </div>
        <div class="headline-footer">
          <span :class="['headline-impact', headline.impactType]">
            影响：{{ headline.impact }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StockHeadlines',
  data() {
    return {
      headlines: [
        {
          tagType: 'important',
          tagText: '重要',
          title: '央行超预期降息 10年期国债收益率下行',
          content: '央行宣布下调7天期逆回购利率10个基点，为年内首次降息，体现稳增长政策发力。',
          date: '2023-05-15',
          impactType: 'positive',
          impact: '积极'
        },
        {
          tagType: 'policy',
          tagText: '政策',
          title: '两部委发文支持光伏产业发展',
          content: '工信部、国家能源局联合发布文件，提出到2025年，光伏产业创新能力显著提升。',
          date: '2023-05-12',
          impactType: 'positive',
          impact: '积极'
        },
        {
          tagType: 'market',
          tagText: '市场',
          title: '美联储加息周期或接近尾声',
          content: '美国CPI同比增速连续回落，市场预期美联储年内将停止加息，全球流动性拐点临近。',
          date: '2023-05-10',
          impactType: 'neutral',
          impact: '中性'
        }
      ]
    }
  }
}
</script>

<style scoped lang="scss">
.headline-card {
  width: 100%;
}

.headline-list {
  display: flex;
  flex-direction: row;
  gap: 16px;
  
  @media (max-width: 768px) {
    flex-direction: column;
  }
}

.headline-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  border: 1px solid var(--hx-border-level-1-color);
  border-radius: 8px;
  overflow: hidden;
  transition: box-shadow 0.2s ease;
  
  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  }
}

.headline-content-container {
  flex: 1;
  padding: 16px;
}

.headline-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.headline-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--hx-text-color-primary);
  line-height: 1.3;
}

.headline-content {
  font-size: 14px;
  line-height: 1.5;
  color: var(--hx-text-color-secondary);
  margin-bottom: 0;
}

.headline-footer {
  padding: 12px 16px;
  border-top: 1px solid var(--hx-border-level-1-color);
  background-color: var(--hx-bg-color-specialcomponent);
}

.headline-tag {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  
  &.important {
    background-color: rgba(255, 59, 48, 0.15);
    color: #FF3B30;
  }
  
  &.policy {
    background-color: rgba(0, 113, 227, 0.15);
    color: #0071E3;
  }
  
  &.market {
    background-color: rgba(52, 199, 89, 0.15);
    color: #34C759;
  }
}

.headline-date {
  font-size: 12px;
  color: var(--hx-text-color-tertiary);
}

.headline-impact {
  font-size: 12px;
  padding: 3px 8px;
  border-radius: 4px;
  
  &.positive {
    color: #FF3B30;
    background-color: rgba(255, 59, 48, 0.08);
  }
  
  &.negative {
    color: #34C759;
    background-color: rgba(52, 199, 89, 0.08);
  }
  
  &.neutral {
    color: var(--hx-text-color-tertiary);
    background-color: rgba(142, 142, 147, 0.12);
  }
}
</style> 