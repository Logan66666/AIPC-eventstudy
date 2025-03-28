<template>
  <div class="stock-headlines">
    <div class="headlines-header">
      <div class="header-left">
        <h2 class="section-title">核心事件</h2>
      </div>
      <div class="header-right">
        <div class="refresh-status">
          <span class="pulse-dot"></span>
          <span class="time">{{ currentTime }} 更新</span>
        </div>
      </div>
    </div>
    
    <div class="headlines-grid">
      <div 
        v-for="(item, index) in headlines" 
        :key="index"
        class="headline-card"
        :class="{'has-negative': item.NegativeImpact.length > 0}"
      >
        <!-- 左侧装饰条 -->
        <div class="card-accent" :class="getBorderClass(item.EventTag)"></div>
        
        <!-- 卡片头部 -->
        <div class="card-header">
          <div class="event-meta">
            <div class="event-title-wrapper">
              <div class="event-icon" :class="getIconClass(item.EventTag)">
                <i class="icon-alert"></i>
              </div>
              <h3 class="event-title">{{ item.EventName }}</h3>
            </div>
            <div class="event-time">
              <i class="icon-clock"></i>{{ formatTime(item.Time) }}
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
                <i class="icon-target"></i>
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
              <!-- 利多影响 -->
              <div v-if="item.PositiveImpact.length" class="impact-row positive">
                <div class="impact-label">
                  <i class="icon-trend-up"></i>
                  <span>利多</span>
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
                  <i class="icon-trend-down"></i>
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
export default {
  name: 'StockHeadlines',
  data() {
    return {
      currentTime: new Date().toLocaleTimeString(),
      headlines: [
        {
          "EventName": "全国两会政策落地",
          "Time": "2025/3/5",
          "Introduction": "2025年政府工作报告设定GDP增长5%目标，赤字率提升至4%，重点部署科技创新（量子计算、AI产业链）、消费提振（新能源汽车置换补贴）和金融改革（5000亿特别国债注资银行）三大战略方向。这是年度最高规格经济政策风向标，直接决定全年财政资金流向。",
          "Highlights": "特别国债注资规模超预期/半导体产业扶持政策细则/新能源汽车补贴执行标准",
          "PositiveImpact": ["半导体设备", "新能源汽车", "国有大行"],
          "NegativeImpact": [],
          "EventTag": "国内政策"
        },
        {
          "EventName": "中美贸易摩擦升级",
          "Time": "2025/3/10",
          "Introduction": "中国宣布对美国鸡肉（15%）、大豆（10%）加征关税，并限制15家美企对华出口。这是2024年贸易争端以来最大规模反制措施，涉及2024年中美贸易额约380亿美元的农产品和科技产品。",
          "Highlights": "后续谈判可能性/国内农产品储备投放计划/被制裁美企替代方案",
          "PositiveImpact": ["农业种植", "食品加工", "国产替代"],
          "NegativeImpact": ["消费电子代工", "纺织服装", "跨境电商"],
          "EventTag": "世界经济"
        },
        {
          "EventName": "央行释放宽松信号",
          "Time": "2025/3/21",
          "Introduction": "央行一季度例会明确实施适度宽松货币政策，强调加强逆周期调节，特别提及将综合运用存款准备金率、政策利率等工具。这是继2024年11月降准后，首次释放明确降息预期信号。",
          "Highlights": "MLF利率调整窗口期/普惠金融定向降准可能性/汇率波动容忍度",
          "PositiveImpact": ["新基建", "科技成长股", "房地产龙头"],
          "NegativeImpact": [],
          "EventTag": "国内政策"
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
        '国内政策': 'policy-border',
        '世界经济': 'global-border',
        '行业事件': 'industry-border'
      };
      return classes[tag] || 'policy-border';
    },
    getIconClass(tag) {
      const classes = {
        '国内政策': 'policy-icon',
        '世界经济': 'global-icon',
        '行业事件': 'industry-icon'
      };
      return classes[tag] || 'policy-icon';
    },
    getTagClass(tag) {
      const classes = {
        '国内政策': 'policy-tag',
        '世界经济': 'global-tag',
        '行业事件': 'industry-tag'
      };
      return classes[tag] || 'policy-tag';
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
  
  .headlines-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--spacing-md);
    padding-bottom: var(--spacing-sm);
    border-bottom: 1px solid var(--border-subtle);
    
    .header-left {
      .section-title {
        font-size: 18px;
        font-weight: 600;
        margin: 0 0 4px 0;
        color: var(--text-primary);
        background: linear-gradient(to right, var(--color-primary), var(--color-secondary));
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
      }
      
      .subtitle {
        font-size: 13px;
        color: var(--text-secondary);
      }
    }
    
    .header-right {
      .refresh-status {
        display: flex;
        align-items: center;
        
        .pulse-dot {
          width: 8px;
          height: 8px;
          background-color: var(--color-success);
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
            background-color: var(--color-success);
            border-radius: 50%;
            opacity: 0.6;
            animation: pulse 2s infinite;
          }
        }
        
        .time {
          font-size: 13px;
          color: var(--text-secondary);
        }
      }
    }
  }
  
  .headlines-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-md);
  }
  
  .headline-card {
    position: relative;
    background-color: rgba(36, 107, 248, 0.05);
    border-radius: var(--radius-sm);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: all 0.25s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
    
    &:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      background-color: rgba(36, 107, 248, 0.08);
    }
    
    &:focus-visible {
      outline: none;
      box-shadow: 0 0 0 2px var(--color-secondary), var(--shadow-md);
    }
    
    .card-accent {
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: linear-gradient(to bottom, var(--color-primary), var(--color-secondary), var(--color-tertiary));
    }
    
    .card-header {
      padding: var(--spacing-md) var(--spacing-md) var(--spacing-sm);
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
        background: var(--border-subtle);
      }
      
      .event-meta {
        flex: 1;
        
        .event-title-wrapper {
          display: flex;
          align-items: center;
          margin-bottom: 6px;
          
          .event-icon {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 8px;
            
            .icon-alert {
              width: 12px;
              height: 12px;
              
              &:before {
                content: "!";
                font-size: 12px;
                font-weight: bold;
                line-height: 1;
              }
            }
            
            &.policy-icon {
              background-color: rgba(255, 59, 87, 0.15);
              color: var(--color-primary);
            }
            
            &.global-icon {
              background-color: rgba(36, 107, 248, 0.15);
              color: var(--color-secondary);
            }
            
            &.industry-icon {
              background-color: rgba(255, 149, 0, 0.15);
              color: var(--color-tertiary);
            }
          }
          
          .event-title {
            font-size: 15px;
            font-weight: 600;
            color: var(--text-primary);
            margin: 0;
            line-height: 1.3;
          }
        }
        
        .event-time {
          font-size: 12px;
          color: var(--text-tertiary);
          display: flex;
          align-items: center;
          margin-left: 28px;
          
          .icon-clock {
            margin-right: 4px;
            font-size: 10px;
            
            &:before {
              content: "⏱";
            }
          }
        }
      }
      
      .event-tag {
        font-size: 11px;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 4px;
        height: fit-content;
        text-transform: capitalize;
        letter-spacing: 0.5px;
        
        &.policy-tag {
          background-color: rgba(255, 59, 87, 0.15);
          color: var(--color-primary);
        }
        
        &.global-tag {
          background-color: rgba(36, 107, 248, 0.15);
          color: var(--color-secondary);
        }
        
        &.industry-tag {
          background-color: rgba(255, 149, 0, 0.15);
          color: var(--color-tertiary);
        }
      }
    }
    
    .card-content {
      padding: var(--spacing-sm) var(--spacing-md) var(--spacing-md);
      display: flex;
      flex-direction: column;
      flex: 1;
      
      .event-intro {
        margin-bottom: var(--spacing-md);
        position: relative;
        
        p {
          font-size: 13px;
          color: var(--text-secondary);
          line-height: 1.5;
          margin: 0;
          display: -webkit-box;
          -webkit-line-clamp: 3;
          -webkit-box-orient: vertical;
          overflow: hidden;
          position: relative;
          transition: all 0.3s ease;
        }
        
        &:hover {
          p {
            -webkit-line-clamp: unset;
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
          background-color: var(--text-tertiary);
          color: var(--text-primary);
          font-size: 10px;
          padding: 1px 4px;
          border-radius: 2px;
          opacity: 0;
          transition: opacity 0.2s ease;
        }
      }
      
      .event-details {
        margin-top: auto;
        
        .detail-row {
          display: flex;
          margin-bottom: 10px;
          
          .row-label {
            display: flex;
            align-items: center;
            margin-right: 8px;
            color: var(--text-tertiary);
            font-size: 12px;
            min-width: 42px;
            
            .icon-target {
              margin-right: 4px;
              
              &:before {
                content: "◉";
                font-size: 12px;
              }
            }
          }
          
          .row-content {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            
            .highlight-item {
              background-color: rgba(0, 0, 0, 0.2);
              padding: 2px 6px;
              border-radius: 3px;
              font-size: 11px;
              color: var(--text-secondary);
              white-space: nowrap;
            }
          }
        }
        
        .impact-analysis {
          display: flex;
          flex-direction: column;
          gap: 8px;
          
          .impact-row {
            display: flex;
            align-items: flex-start;
            
            .impact-label {
              display: flex;
              align-items: center;
              font-size: 12px;
              min-width: 42px;
              margin-right: 8px;
              
              i {
                margin-right: 4px;
                
                &.icon-trend-up:before {
                  content: "↑";
                  color: var(--color-success);
                }
                
                &.icon-trend-down:before {
                  content: "↓";
                  color: var(--color-danger);
                }
              }
              
              span {
                white-space: nowrap;
              }
            }
            
            &.positive .impact-label {
              color: var(--color-success);
            }
            
            &.negative .impact-label {
              color: var(--color-danger);
            }
            
            .impact-tags {
              display: flex;
              flex-wrap: wrap;
              gap: 6px;
              
              .impact-tag {
                padding: 2px 6px;
                border-radius: 3px;
                font-size: 11px;
                white-space: nowrap;
                
                &.positive {
                  background-color: rgba(16, 185, 129, 0.1);
                  color: var(--color-success);
                }
                
                &.negative {
                  background-color: rgba(239, 68, 68, 0.1);
                  color: var(--color-danger);
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