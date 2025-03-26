<template>
  <div class="card company-card">
    <h2 class="card-title">公司动向</h2>
    <p class="card-subtitle">自选股动态</p>
    
    <div class="company-filter">
      <button 
        v-for="(filter, index) in filters" 
        :key="index" 
        :class="['company-filter-btn', { active: currentFilter === filter.id }]"
        @click="currentFilter = filter.id"
      >
        {{ filter.name }}
      </button>
    </div>
    
    <div class="company-list">
      <div v-for="(news, index) in filteredCompanyNews" :key="index" class="company-item">
        <div class="company-info">
          <span class="company-name">{{ news.companyName }}</span>
          <span class="company-code">{{ news.companyCode }}</span>
        </div>
        <div class="company-news">
          <span :class="['company-news-tag', news.tagType]">{{ news.tagText }}</span>
          <p>{{ news.content }}</p>
        </div>
        <span class="company-date">{{ news.date }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CompanyNews',
  data() {
    return {
      currentFilter: 'all',
      filters: [
        { id: 'all', name: '全部' },
        { id: 'performance', name: '业绩' },
        { id: 'announcement', name: '公告' },
        { id: 'research', name: '研报' }
      ],
      companyNews: [
        {
          companyName: '贵州茅台',
          companyCode: '600519',
          tagType: 'announcement',
          tagText: '公告',
          content: '发布2023年一季度财报，营收同比增长18.2%，净利润同比增长20.3%',
          date: '2023-04-28',
          type: 'announcement'
        },
        {
          companyName: '宁德时代',
          companyCode: '300750',
          tagType: 'research',
          tagText: '研报',
          content: '知名券商发布研报，预计公司Q2电池出货量环比增长15%，维持"买入"评级',
          date: '2023-05-12',
          type: 'research'
        },
        {
          companyName: '比亚迪',
          companyCode: '002594',
          tagType: 'news',
          tagText: '新闻',
          content: '公司发布新款高端电动车型，预售价格35-50万元，针对豪华电动车市场',
          date: '2023-05-15',
          type: 'news'
        },
        {
          companyName: '招商银行',
          companyCode: '600036',
          tagType: 'performance',
          tagText: '业绩',
          content: '2023年一季度营收同比增长8.6%，净利润同比增长6.2%，不良贷款率1.20%',
          date: '2023-04-30',
          type: 'performance'
        },
        {
          companyName: '顺丰控股',
          companyCode: '002352',
          tagType: 'announcement',
          tagText: '公告',
          content: '公司发布股权激励计划，向核心员工授予限制性股票，激励期限4年',
          date: '2023-05-08',
          type: 'announcement'
        }
      ]
    }
  },
  computed: {
    filteredCompanyNews() {
      if (this.currentFilter === 'all') {
        return this.companyNews
      }
      return this.companyNews.filter(news => news.type === this.currentFilter)
    }
  }
}
</script>

<style scoped lang="scss">
.company-card {
  background-color: var(--hx-bg-color-container) !important;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.company-filter {
  display: flex;
  margin-bottom: var(--hx-size-4);
  overflow-x: auto;
  
  &::-webkit-scrollbar {
    height: 4px;
  }
}

.company-filter-btn {
  background: transparent;
  border: 1px solid var(--hx-border-level-1-color);
  padding: var(--hx-size-1) var(--hx-size-3);
  margin-right: var(--hx-size-2);
  border-radius: var(--hx-radius-default);
  color: var(--hx-text-color-secondary);
  white-space: nowrap;
  
  &:hover {
    border-color: var(--hx-brand-color-hover);
    color: var(--hx-brand-color-hover);
  }
  
  &.active {
    background-color: var(--hx-brand-color-3);
    color: var(--hx-gray-color-1);
    border-color: var(--hx-brand-color-3);
  }
}

.company-list {
  display: flex;
  flex-direction: column;
  gap: var(--hx-size-3);
}

.company-item {
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: var(--hx-radius-default);
  padding: var(--hx-size-3);
  border: 1px solid var(--hx-border-level-1-color);
}

.company-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: var(--hx-size-2);
}

.company-name {
  font-weight: 500;
  color: var(--hx-text-color-primary);
}

.company-code {
  color: var(--hx-text-color-tertiary);
  font-size: var(--hx-font-size-body-small);
}

.company-news {
  display: flex;
  align-items: flex-start;
  gap: var(--hx-size-2);
  margin-bottom: var(--hx-size-2);
  
  p {
    margin: 0;
    flex: 1;
    font-size: var(--hx-font-size-body-small);
  }
}

.company-news-tag {
  display: inline-block;
  padding: var(--hx-size-1) var(--hx-size-2);
  border-radius: var(--hx-radius-small);
  font-size: var(--hx-font-size-body-small);
  flex-shrink: 0;
  
  &.announcement {
    background-color: var(--hx-brand-color-1);
    color: var(--hx-brand-color-5);
  }
  
  &.research {
    background-color: var(--hx-warning-color-1);
    color: var(--hx-warning-color-5);
  }
  
  &.news {
    background-color: var(--hx-success-color-1);
    color: var(--hx-success-color-5);
  }
  
  &.performance {
    background-color: var(--hx-raise-color-1);
    color: var(--hx-raise-color-5);
  }
}

.company-date {
  display: block;
  text-align: right;
  font-size: var(--hx-font-size-body-small);
  color: var(--hx-text-color-tertiary);
}
</style> 