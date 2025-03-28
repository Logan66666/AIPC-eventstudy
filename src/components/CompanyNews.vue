<template>
  <div class="company-news card">
    <div class="company-header">
      <h2 class="card-title secondary-title">公司动向</h2>
      <div class="card-subtitle">自选股动态</div>
    </div>
    
    <div class="company-content">
      <div class="company-tabs">
        <div 
          v-for="(filter, index) in filters" 
          :key="index" 
          class="company-tab"
          :class="{'active': currentFilter === filter.id}"
          @click="currentFilter = filter.id"
        >
          {{ filter.name }}
        </div>
      </div>
      
      <div class="company-list">
        <div v-for="(news, index) in filteredCompanyNews" :key="index" class="company-item">
          <div class="company-header-row">
            <div class="company-info">
              <div class="company-name">{{ news.companyName }}</div>
              <div class="company-code">{{ news.companyCode }}</div>
            </div>
            <div class="company-news-tag" :class="news.tagType">{{ news.tagText }}</div>
          </div>
          <div class="company-content-row">
            <p>{{ news.content }}</p>
          </div>
          <div class="company-footer-row">
            <div class="company-date">{{ news.date }}</div>
          </div>
        </div>
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
.company-news {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .company-header {
    margin-bottom: var(--spacing-md);
  }
  
  .company-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  
  .company-tabs {
    display: flex;
    margin-bottom: var(--spacing-md);
    border-bottom: 1px solid var(--border-subtle);
    overflow-x: auto;
    
    &::-webkit-scrollbar {
      height: 4px;
    }
    
    &::-webkit-scrollbar-thumb {
      background-color: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
    }
    
    .company-tab {
      padding: 8px 12px;
      margin-right: var(--spacing-md);
      font-size: 14px;
      color: var(--text-tertiary);
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
      white-space: nowrap;
      
      &:hover {
        color: var(--text-secondary);
      }
      
      &.active {
        color: var(--color-secondary);
        font-weight: 600;
        
        &:after {
          content: '';
          position: absolute;
          bottom: -1px;
          left: 0;
          width: 100%;
          height: 2px;
          background-color: var(--color-secondary);
        }
      }
    }
  }
  
  .company-list {
    flex: 1;
    overflow-y: auto;
    padding-right: var(--spacing-sm);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
    
    &::-webkit-scrollbar {
      width: 4px;
    }
    
    &::-webkit-scrollbar-thumb {
      background-color: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
    }
  }
  
  .company-item {
    background-color: rgba(36, 107, 248, 0.05);
    border-radius: var(--radius-sm);
    padding: var(--spacing-md);
    transition: all 0.25s ease;
    
    &:hover {
      background-color: rgba(36, 107, 248, 0.08);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }
    
    .company-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--spacing-sm);
      
      .company-info {
        display: flex;
        gap: var(--spacing-sm);
        align-items: baseline;
        
        .company-name {
          font-weight: 600;
          font-size: 15px;
          color: var(--text-primary);
        }
        
        .company-code {
          color: var(--text-tertiary);
          font-size: 12px;
        }
      }
      
      .company-news-tag {
        font-size: 11px;
        font-weight: 600;
        padding: 2px 6px;
        border-radius: 4px;
        text-transform: uppercase;
        
        &.announcement {
          background-color: rgba(var(--secondary-rgb), 0.1);
          color: var(--color-secondary);
        }
        
        &.research {
          background-color: rgba(var(--tertiary-rgb), 0.1);
          color: var(--color-tertiary);
        }
        
        &.news {
          background-color: rgba(var(--success-rgb), 0.1);
          color: var(--color-success);
        }
        
        &.performance {
          background-color: rgba(var(--primary-rgb), 0.1);
          color: var(--color-primary);
        }
      }
    }
    
    .company-content-row {
      p {
        margin: 0;
        font-size: 13px;
        color: var(--text-secondary);
        line-height: 1.5;
      }
    }
    
    .company-footer-row {
      display: flex;
      justify-content: flex-end;
      margin-top: var(--spacing-sm);
      
      .company-date {
        font-size: 12px;
        color: var(--text-tertiary);
      }
    }
  }
}

@media (max-width: 768px) {
  .company-news {
    .company-tabs {
      .company-tab {
        padding: 6px 8px;
        font-size: 13px;
      }
    }
    
    .company-item {
      padding: var(--spacing-sm);
      
      .company-header-row {
        .company-info {
          .company-name {
            font-size: 14px;
          }
        }
      }
      
      .company-content-row {
        p {
          font-size: 12px;
        }
      }
    }
  }
}
</style> 