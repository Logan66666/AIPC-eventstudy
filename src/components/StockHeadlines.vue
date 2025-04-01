<template>
  <div class="stock-headlines">
    <div class="headlines-grid">
      <div 
        v-for="(item, index) in headlines" 
        :key="index"
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
            <!-- 看点 -->
            <div class="detail-row highlights">
              <div class="row-label">
                <i class="fas fa-bullseye"></i>
                <span>看点</span>
              </div>
              <div class="row-content">
                <span v-for="(highlight, idx) in item.Highlights.split('/')" 
                      :key="idx" 
                      class="highlight-item">
                  {{ highlight }}
                </span>
              </div>
            </div>
            
            <!-- 影响分析区域 -->
            <div class="impact-analysis">
              <!-- 利好影响 -->
              <div v-if="item.PositiveImpact.length" class="impact-row positive">
                <div class="impact-label">
                  <i class="fas fa-arrow-up"></i>
                  <span>利好</span>
                </div>
                <div class="impact-tags">
                  <div v-for="(tag, idx) in item.PositiveImpact" 
                       :key="idx" 
                       class="impact-tag positive">
                    {{ tag }}
                  </div>
                </div>
              </div>
              
              <!-- 利空影响 -->
              <div v-if="item.NegativeImpact.length" class="impact-row negative">
                <div class="impact-label">
                  <i class="fas fa-arrow-down"></i>
                  <span>利空</span>
                </div>
                <div class="impact-tags">
                  <div v-for="(tag, idx) in item.NegativeImpact" 
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
    </div>
  </div>
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css'

export default {
  name: 'StockHeadlines',
  components: {
  },
  data() {
    return {
      currentTime: new Date().toLocaleTimeString(),
      headlines: [
        {
          "EventName": "全国两会政策落地",
          "Time": "2025/3/5",
          "Introduction": "2025年政府工作报告设定GDP增长5%目标，赤字率提升至4%，重点部署科技创新（量子计算、AI产业链）、消费提振（新能源汽车置换补贴）和金融改革（5000亿特别国债注资银行）三大战略方向。这是年度最高规格经济政策风向标，直接决定全年财政资金流向。",
          "Highlights": "特别国债注资规模超预期/半导体扶持/新能源汽车补贴",
          "PositiveImpact": ["半导体设备", "新能源汽车", "国有大行"],
          "NegativeImpact": [],
          "EventTag": "政策"
        },
        {
          "EventName": "中美贸易摩擦升级",
          "Time": "2025/3/10",
          "Introduction": "中国宣布对美国鸡肉（15%）、大豆（10%）加征关税，并限制15家美企对华出口。这是2024年贸易争端以来最大规模反制措施，涉及2024年中美贸易额约380亿美元的农产品和科技产品。",
          "Highlights": "后续谈判可能性/国内农产品储备投放计划/被制裁美企替代方案",
          "PositiveImpact": ["农业种植", "食品加工", "国产替代"],
          "NegativeImpact": ["消费电子代工", "纺织服装", "跨境电商"],
          "EventTag": "全球"
        },
        {
          "EventName": "央行释放宽松信号",
          "Time": "2025/3/21",
          "Introduction": "央行一季度例会明确实施适度宽松货币政策，强调加强逆周期调节，特别提及将综合运用存款准备金率、政策利率等工具。这是继2024年11月降准后，首次释放明确降息预期信号。",
          "Highlights": "MLF利率调整窗口期/普惠金融定向降准可能性/汇率波动容忍度",
          "PositiveImpact": ["新基建", "科技成长股", "房地产龙头"],
          "NegativeImpact": [],
          "EventTag": "政策"
        }
      ]
    }
  },
  methods: {
    formatTime(time) {
      return time;
    },
    getBorderClass(tag) {
      const classes = {
        '政策': 'policy-border',
        '全球': 'global-border',
        '行业': 'industry-border'
      };
      return classes[tag] || 'policy-border';
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
  },
  mounted() {
    // 定时更新时间
    setInterval(() => {
      this.currentTime = new Date().toLocaleTimeString();
    }, 60000);
    
    // 增强可访问性
    this.$nextTick(() => {
      const cards = document.querySelectorAll('.headline-card');
      cards.forEach(card => {
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'article');
        card.setAttribute('aria-label', '市场事件');
      });
    });
  }
}
</script>

<style lang="scss" scoped>
.stock-headlines {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: var(--hx-comp-margin-m);
  
  .headlines-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--hx-size-4);
    padding-bottom: var(--hx-size-2);
    border-bottom: 1px solid var(--hx-border-level-1-color);
    
    .header-left {
      .section-title {
        font-size: 18px;
        font-weight: 600;
        margin: 0 0 4px 0;
        color: var(--hx-text-color-primary);
        background: linear-gradient(to right, var(--hx-brand-color-3), var(--hx-sec-brand-color-3));
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
      }
      
      .subtitle {
        font-size: 13px;
        color: var(--hx-text-color-secondary);
      }
    }
    
    .header-right {
      .refresh-status {
        display: flex;
        align-items: center;
        
        .pulse-dot {
          width: 8px;
          height: 8px;
          background-color: var(--hx-success-color-3);
          border-radius: 50%;
          margin-right: 8px;
          position: relative;
          
          &:before {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background-color: var(--hx-success-color-3);
            border-radius: 50%;
            opacity: 0.6;
            animation: pulse 2s infinite;
          }
        }
        
        .time {
          font-size: 13px;
          color: var(--hx-text-color-secondary);
        }
      }
    }
  }
  
  .headlines-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--hx-size-4);
  }
  
  .headline-card {
    position: relative;
    background-color: var(--hx-bg-color-container);
    border-radius: var(--hx-radius-default);
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.25s ease;
    display: flex;
    flex-direction: column;
    
    &:hover {
      transform: translateY(-3px);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
      background-color: var(--hx-bg-color-specialcomponent);
    }
    
    &:focus-visible {
      outline: none;
      box-shadow: 0 0 0 2px var(--hx-brand-color-3), 0 4px 16px rgba(0, 0, 0, 0.15);
    }
    
    .card-accent {
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: linear-gradient(to bottom, var(--hx-brand-color-3), var(--hx-sec-brand-color-3), var(--hx-warning-color-3));
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
      
      .event-intro {
        margin-bottom: var(--hx-size-3);
        position: relative;
        
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
          
          &:after {
            opacity: 1;
          }
        }
        
        &:after {
          content: '';
          position: absolute;
          bottom: -4px;
          right: 0;
          background-color: var(--hx-text-color-tertiary);
          color: var(--hx-text-color-primary);
          font-size: 10px;
          padding: 1px 4px;
          border-radius: 2px;
          opacity: 0;
          transition: opacity 0.2s ease;
        }
      }
      
      .event-details {
        
        .detail-row {
          display: flex;
          margin-bottom: 8px;
          
          .row-label {
            display: flex;
            align-items: center;
            margin-right: 8px;
            color: var(--hx-text-color-emphasize);
            font-size: 12px;
            min-width: 36px;
            
            .icon-target {
              margin-right: 4px;
            }
          }
          
          .row-content {
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
          }
        }
        
        .impact-analysis {
          display: flex;
          flex-direction: column;
          gap: 6px;
          
          .impact-row {
            display: flex;
            align-items: flex-start;
            
            .impact-label {
              display: flex;
              align-items: center;
              font-size: 12px;
              min-width: 28px;
              margin-right: 8px;
              
              i {
                margin-right: 4px;
              }
              
              span {
                white-space: nowrap;
              }
            }
            
            &.positive .impact-label {
              color: var(--hx-raise-color-2);
            }
            
            &.negative .impact-label {
              color: var(--hx-fall-color-2);
            }
            
            .impact-tags {
              display: flex;
              flex-wrap: wrap;
              gap: 4px;
              
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
  
  @keyframes pulse {
    0% { transform: scale(1); opacity: 0.6; }
    50% { transform: scale(1.8); opacity: 0; }
    100% { transform: scale(1); opacity: 0; }
  }
  
  @media (max-width: 1200px) {
    .headlines-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }
  
  @media (max-width: 992px) {
    .headlines-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 768px) {
    .headlines-header {
      flex-direction: column;
      align-items: flex-start;
      
      .header-right {
        margin-top: 8px;
      }
    }
    
    .headlines-grid {
      grid-template-columns: 1fr;
    }
    
    .headline-card {
      .card-header {
        .event-meta {
          .event-title-wrapper {
            .event-title {
              font-size: 14px;
            }
          }
        }
      }
      
      .card-content {
        .event-intro {
          p {
            font-size: 12px;
          }
        }
      }
    }
  }
}
</style> 