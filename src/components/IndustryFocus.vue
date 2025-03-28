<template>
  <div class="industry-focus card">
    <div class="industry-header">
      <h2 class="card-title secondary-title">行业焦点</h2>
      <div class="card-subtitle">行业重要事件解读</div>
    </div>
    
    <div class="industry-content">
      <div class="industry-tabs">
        <div 
          v-for="(industry, index) in industries" 
          :key="index" 
          class="industry-tab"
          :class="{'active': currentIndustry === industry.id}"
          @click="currentIndustry = industry.id"
        >
          {{ industry.name }}
        </div>
      </div>
      
      <div class="industry-news-grid">
        <div v-for="(news, index) in currentIndustryNews" :key="index" class="industry-news-item">
          <h3 class="news-title">{{ news.title }}</h3>
          <p class="news-content">{{ news.content }}</p>
          <div class="news-date">{{ news.date }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndustryFocus',
  data() {
    return {
      currentIndustry: 'tech',
      industries: [
        { id: 'tech', name: '科技' },
        { id: 'medical', name: '医药' },
        { id: 'finance', name: '金融' },
        { id: 'consumer', name: '消费' },
        { id: 'newEnergy', name: '新能源' }
      ],
      industryNews: {
        tech: [
          {
            title: '国内GPU研发取得突破',
            content: '国内AI芯片企业发布新一代GPU，算力相比上一代提升3倍，标志着国产GPU在AI领域的重要进展',
            date: '2023-05-18'
          },
          {
            title: '华为发布新一代自研芯片',
            content: '华为发布麒麟系列新芯片，采用先进工艺，信号处理能力大幅提升',
            date: '2023-05-15'
          },
          {
            title: '国内光刻机研发进展',
            content: '国产28nm光刻机研发取得突破，预计年内可实现量产，推动半导体制造国产化',
            date: '2023-05-10'
          }
        ],
        medical: [
          {
            title: '国产创新药获批上市',
            content: '本土企业研发的抗肿瘤创新药获批上市，打破国外药企在该领域的垄断',
            date: '2023-05-16'
          },
          {
            title: '医保谈判结果公布',
            content: '新一轮医保目录调整谈判结果公布，多款国产创新药纳入医保，价格大幅下降',
            date: '2023-05-12'
          }
        ],
        finance: [
          {
            title: '银行业一季度业绩公布',
            content: '上市银行一季度业绩整体平稳，资产质量持续改善，净息差环比回升',
            date: '2023-05-14'
          },
          {
            title: '保险业新政策出台',
            content: '监管部门发布保险业务新规定，鼓励创新，提高风险管理要求',
            date: '2023-05-08'
          }
        ],
        consumer: [
          {
            title: '618电商大促启动',
            content: '各大电商平台启动618促销活动，消费电子、家电品类预计销售同比增长',
            date: '2023-05-17'
          },
          {
            title: '白酒行业复苏趋势明显',
            content: '五一假期白酒销售数据良好，高端白酒市场需求恢复，渠道库存健康',
            date: '2023-05-10'
          }
        ],
        newEnergy: [
          {
            title: '储能产业新政策',
            content: '国家发改委发布储能产业支持政策，提出到2025年装机规模达30GW的目标',
            date: '2023-05-19'
          },
          {
            title: '海上风电项目批量核准',
            content: '多个省份批量核准海上风电项目，总装机容量超过10GW，带动风电产业链发展',
            date: '2023-05-13'
          }
        ]
      }
    }
  },
  computed: {
    currentIndustryNews() {
      return this.industryNews[this.currentIndustry] || []
    }
  }
}
</script>

<style scoped lang="scss">
.industry-focus {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .industry-header {
    margin-bottom: var(--spacing-md);
  }
  
  .industry-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  
  .industry-tabs {
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
    
    .industry-tab {
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
  
  .industry-news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: var(--spacing-md);
    overflow-y: auto;
    padding-right: var(--spacing-sm);
    
    &::-webkit-scrollbar {
      width: 4px;
    }
    
    &::-webkit-scrollbar-thumb {
      background-color: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
    }
  }
  
  .industry-news-item {
    background-color: rgba(36, 107, 248, 0.05);
    border-radius: var(--radius-sm);
    padding: var(--spacing-md);
    transition: all 0.25s ease;
    display: flex;
    flex-direction: column;
    
    &:hover {
      background-color: rgba(36, 107, 248, 0.08);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }
    
    .news-title {
      font-size: 15px;
      font-weight: 600;
      color: var(--text-primary);
      margin: 0 0 var(--spacing-sm) 0;
      line-height: 1.4;
    }
    
    .news-content {
      font-size: 13px;
      color: var(--text-secondary);
      margin: 0 0 var(--spacing-md) 0;
      line-height: 1.5;
      flex: 1;
    }
    
    .news-date {
      font-size: 12px;
      color: var(--text-tertiary);
      align-self: flex-end;
    }
  }
}

@media (max-width: 1024px) {
  .industry-focus {
    .industry-news-grid {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    }
  }
}

@media (max-width: 768px) {
  .industry-focus {
    .industry-tabs {
      .industry-tab {
        padding: 6px 8px;
        font-size: 13px;
      }
    }
    
    .industry-news-grid {
      grid-template-columns: 1fr;
    }
    
    .industry-news-item {
      padding: var(--spacing-sm);
      
      .news-title {
        font-size: 14px;
      }
      
      .news-content {
        font-size: 12px;
      }
    }
  }
}
</style> 