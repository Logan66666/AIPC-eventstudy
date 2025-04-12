<template>
  <div class="policy-catalysts card">
    <div class="policy-header">
      <div class="header-main">
      <h2 class="card-title secondary-title">政策催化</h2>
      <div class="card-subtitle">重要经济政策与市场影响</div>
    </div>
    
      <!-- 使用新的下拉菜单组件 -->
      <DropdownSelect
        v-model="selectedTypes"
        :options="sourceTypes.map(type => ({
          label: type,
          value: type,
          badgeClass: getSourceClass(type)
        }))"
        placeholder="筛选类型"
        all-text="全部类型"
      />
    </div>
    
    <div class="policy-content">
      <!-- 使用DataTimeline组件 -->
      <DataTimeline 
        :items="filteredPolicies" 
        :expanded-item="expandedItem" 
        @item-expanded="handleExpand">
        <!-- 自定义源标签 -->
        <template v-slot:item-tag="{ item }">
          <EventTag :text="item.source" />
        </template>
        
        <!-- 自定义指标 -->
        <template v-slot:item-indicators="{ item }">
          <div class="importance-indicator" :title="`重要性：${item.importance}/3`">
            <i v-for="n in 3" 
                :key="n" 
                class="importance-icon"
                :class="{ 
                  'fas fa-star filled': n <= item.importance,
                  'far fa-star': n > item.importance 
                }"
            ></i>
          </div>
        </template>
      </DataTimeline>
    </div>
  </div>
</template>

<script>
// 引入FontAwesome
import '@fortawesome/fontawesome-free/css/all.css'
// 引入自定义组件
import DataTimeline from './ui/DataTimeline.vue'
import EventTag from './ui/EventTag.vue'
import DropdownSelect from './ui/DropdownSelect.vue'
// 引入mock数据
import { policyCatalystMockData } from '../utils/mockData.js'

export default {
  name: 'PolicyCatalysts',
  components: {
    DataTimeline,
    EventTag,
    DropdownSelect
  },
  
  methods: {
    formatPolicyDate(dateStr) {
      // 确保返回统一的日期格式，如 YYYY/MM/DD
      const date = new Date(dateStr);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      return `${year}/${month}/${day}`;
    },
    
    handleExpand(data) {
      this.expandedItem = data.expanded ? data.index : null;
    },
    
    getSourceClass(source) {
      const classes = {
        '高层会议': 'official',
        '部委政策': 'planning',
        '地方政策': 'local',
        '国际政策': 'international',
        '金融政策': 'financial',
        '产业政策': 'industry'
      };
      return classes[source] || 'other';
    }
  },
  
  data() {
    // 解析JSON数据
    const policyDataJson = JSON.parse(policyCatalystMockData.response.text.trim().replace(/```json\n|\n```/g, ''));
    
    return {
      expandedItem: null,
      selectedTypes: [], // 存储多选的类型
      policies: policyDataJson.map(item => {
        return {
          source: item.item.type,
          date: this.formatPolicyDate(item.date),
          title: item.title,
          summary: item.summary,
          importance: item.importance,
          context: item.context,
          highlights: item.highlights,
          benefits: item.benefits,
          drawbacks: item.drawbacks || []
        };
      })
    }
  },
  created() {
    // 初始化时选择所有类型
    this.selectedTypes = [...this.sourceTypes];
  },
  beforeDestroy() {
    // 清理事件监听
  },
  computed: {
    sourceTypes() {
      const types = new Set();
      this.policies.forEach(policy => {
        types.add(policy.source);
      });
      return Array.from(types);
    },
    
    filteredPolicies() {
      const sorted = [...this.policies].sort((a, b) => {
        // 修改为倒序排列，最新的在上面
        return new Date(b.date) - new Date(a.date);
      });
      
      if (this.selectedTypes.length === 0 || 
          this.selectedTypes.length === this.sourceTypes.length) {
        return sorted;
      }
      
      return sorted.filter(policy => this.selectedTypes.includes(policy.source));
    }
  }
}
</script>

<style lang="scss" scoped>
.policy-catalysts {
  height: 100%;
  max-height: 600px;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  
  .policy-header {
    padding: var(--hx-comp-paddingTB-s) var(--hx-comp-paddingLR-s);
    flex-shrink: 0;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    
    .header-main {
      flex: 1;
      
      .secondary-title {
        position: relative;
        
        &::before {
          content: '';
          display: inline-block;
          width: 4px;
          height: 16px;
          background-color: var(--hx-border-level-3-color);
          margin-right: 8px;
          border-radius: 2px;
          vertical-align: middle;
        }
      }
    }
  }
  
  .policy-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    min-height: 0;
  }
}

// 重要性指标样式
.importance-indicator {
  display: flex;
  gap: 2px;
  flex-shrink: 0;
  
  .importance-icon {
    font-size: 10px;
    
    &.filled {
      color: var(--hx-warning-color-2);
    }
    
    &:not(.filled) {
      color: var(--hx-border-level-2-color);
    }
  }
}

@media (max-width: 768px) {
  .policy-catalysts {
    .policy-content {
      .data-timeline {
        .policy-list {
          .policy-item {
            .date-marker {
              width: var(--hx-size-10);
            }
            
            .item-content {
      .policy-title-row {
        .policy-title {
                  font-size: 13px;
        }
      }
      
      .policy-preview {
        font-size: 12px;
              }
            }
          }
        }
      }
    }
  }
}
</style> 