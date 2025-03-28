<template>
  <div class="investment-opportunities card">
    <div class="opportunity-header">
      <h2 class="card-title tertiary-title">埋伏机会</h2>
      <div class="card-subtitle">左侧投资机会前瞻</div>
    </div>
    
    <div class="opportunity-content">
      <div class="opportunity-list">
        <div v-for="(opportunity, index) in opportunities" :key="index" class="opportunity-item">
          <div class="opportunity-header-row">
            <h3 class="opportunity-title">{{ opportunity.title }}</h3>
            <div class="opportunity-timing">
              <span class="timing-icon">⏳</span>
              <span class="timing-text">{{ opportunity.timeWindow }}</span>
            </div>
          </div>
          
          <p class="opportunity-description">{{ opportunity.description }}</p>
          
          <div class="opportunity-stocks">
            <span class="stocks-label">相关标的</span>
            <div class="stocks-list">
              <span 
                v-for="(stock, stockIndex) in opportunity.stocks" 
                :key="stockIndex" 
                class="stock-tag"
              >
                {{ stock }}
              </span>
            </div>
          </div>
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
.investment-opportunities {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .opportunity-header {
    margin-bottom: var(--spacing-md);
  }
  
  .opportunity-content {
    flex: 1;
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
  
  .opportunity-list {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
  }
  
  .opportunity-item {
    background-color: rgba(255, 149, 0, 0.05);
    border-radius: var(--radius-sm);
    padding: var(--spacing-md);
    transition: all 0.25s ease;
    
    &:hover {
      background-color: rgba(255, 149, 0, 0.08);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }
    
    .opportunity-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: var(--spacing-sm);
      
      .opportunity-title {
        font-size: 15px;
        font-weight: 600;
        color: var(--text-primary);
        margin: 0;
        line-height: 1.4;
      }
      
      .opportunity-timing {
        display: flex;
        align-items: center;
        gap: 4px;
        font-size: 12px;
        color: var(--color-tertiary);
        background-color: rgba(255, 149, 0, 0.1);
        padding: 2px 8px;
        border-radius: 12px;
        
        .timing-icon {
          font-size: 11px;
        }
        
        .timing-text {
          white-space: nowrap;
        }
      }
    }
    
    .opportunity-description {
      font-size: 13px;
      color: var(--text-secondary);
      margin: 0 0 var(--spacing-md) 0;
      line-height: 1.5;
    }
    
    .opportunity-stocks {
      display: flex;
      align-items: baseline;
      
      .stocks-label {
        font-size: 12px;
        color: var(--text-tertiary);
        margin-right: var(--spacing-sm);
        white-space: nowrap;
      }
      
      .stocks-list {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        
        .stock-tag {
          display: inline-block;
          padding: 2px 8px;
          background-color: rgba(255, 149, 0, 0.1);
          color: var(--color-tertiary);
          border-radius: 12px;
          font-size: 12px;
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .investment-opportunities {
    .opportunity-item {
      padding: var(--spacing-sm);
      
      .opportunity-header-row {
        .opportunity-title {
          font-size: 14px;
        }
        
        .opportunity-timing {
          font-size: 11px;
        }
      }
      
      .opportunity-description {
        font-size: 12px;
      }
      
      .opportunity-stocks {
        flex-direction: column;
        
        .stocks-label {
          margin-bottom: 4px;
        }
        
        .stocks-list {
          .stock-tag {
            font-size: 11px;
          }
        }
      }
    }
  }
}
</style> 