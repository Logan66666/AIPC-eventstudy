<template>
  <div class="company-news card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">热股动向</h2>
        <div class="card-subtitle">热门股票最新事件跟踪</div>
      </div>
    </div>
    
    <!-- 事件类型切换标签 -->
    <div class="industry-tabs">
      <div 
        v-for="(type, index) in eventTypes" 
        :key="index"
        class="tab-item"
        :class="{ active: currentType === type.code }"
        @click="switchType(type.code)"
      >
        {{ type.name }}
      </div>
    </div>
    
    <!-- 时间线内容 -->
    <div class="timeline-content">
      <DataTimeline 
        :items="currentTypeItems"
        :expanded-item="expandedItem"
        @item-expanded="handleItemExpanded"
      >
        <template v-slot:item-tag="{ item }">
          <EventTag 
            :text="item.timeTag" 
            :type-map="timeTagTypeMap" 
          />
        </template>
        
        <template v-slot:item-indicators="{ item }">
          <div class="importance-indicator" :title="`重要性：${item.importance || 1}/3`">
            <i v-for="n in 3" 
                :key="n" 
                class="importance-icon fas fa-star"
                :class="{ 
                  'filled': n <= (item.importance || 1),
                  'empty': n > (item.importance || 1)
                }"
            ></i>
          </div>
        </template>
        
        <template v-slot:item-title="{ item }">

          <h3 class="item-title">【{{ item.companyName }}】{{ item.title }}</h3>
        </template>
        
        <template v-slot:item-preview="{ item }">
          <div class="item-preview-content">
            <p class="event-summary">{{ item.summary }}</p>
          </div>
        </template>
      </DataTimeline>
    </div>
  </div>
</template>

<script>
import DataTimeline from './ui/DataTimeline.vue'
import EventTag from './ui/EventTag.vue'
import { companyNewsMockData } from '@/utils/mockData' // 引入 mock 数据

// Mock数据中的中文类型 -> 组件内部使用的code
const typeCodeMap = {
  '重大事项': 'major',
  '业绩动态': 'performance',
  '经营动态': 'operation',
  '市场表现': 'market',
  '投资者关系': 'investor',
};

// 组件内部使用的code -> Mock数据中的中文类型 (如果需要反向查找)
// const codeTypeMap = Object.fromEntries(Object.entries(typeCodeMap).map(a => a.reverse()));

export default {
  name: 'CompanyNews',
  components: {
    DataTimeline,
    EventTag
  },
  data() {
    return {
      currentType: 'major', // 默认选中 "重大事项" 可能更合适
      expandedItem: null,
      timeTagTypeMap: {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      },
      // 更新事件类型以匹配 mock 数据
      eventTypes: [
        { code: 'major', name: '重大事项' },  
        { code: 'performance', name: '业绩动态' },
        { code: 'operation', name: '经营动态' },
        { code: 'market', name: '市场表现' }, // 新增
        { code: 'investor', name: '投资者关系' }
      ],
      // companyEvents: { ... } // 删除旧的静态数据
    }
  },
  computed: {
    // 解析并合并所有 mock 事件数据
    allParsedEvents() {
      try {
        const allEvents = companyNewsMockData.response.text.reduce((acc, jsonText) => {
          try {
            // 移除 markdown 标记并解析 JSON
            const cleanedJsonText = jsonText.replace(/```json\n|\n```/g, '');
            const newsArray = JSON.parse(cleanedJsonText);
            // 确保解析出来的是数组
            if (Array.isArray(newsArray)) {
               // 添加兼容字段
               const compatibleArray = newsArray.map(event => ({
                 ...event,
                 companyName: event.item?.stockname || 'N/A', // 兼容模板
                 companyCode: event.item?.stockcode || 'N/A', // 兼容模板
               }));
              return [...acc, ...compatibleArray];
            } else {
              console.warn('解析结果非数组:', newsArray);
              return acc;
            }
          } catch (e) {
            console.error('解析单个JSON失败:', jsonText, e);
            return acc; // 跳过解析失败的部分
          }
        }, []);
        return allEvents;
      } catch (e) {
        console.error('处理新闻数据失败:', e);
        return []; // 出错时返回空数组
      }
    },
    // 根据当前选中的类型筛选事件
    currentTypeItems() {
      const selectedTypeCode = this.currentType;
      const filteredEvents = this.allParsedEvents.filter(event => {
        // 使用映射关系将事件的中文类型转换为内部代码进行比较
        return typeCodeMap[event.type] === selectedTypeCode;
      });
      // 按日期降序排序
      return filteredEvents.sort((a, b) => new Date(b.date) - new Date(a.date));
    }
  },
  methods: {
    switchType(code) {
      this.currentType = code;
      this.expandedItem = null; // 切换类型时收起展开项
    },
    handleItemExpanded(data) {
      this.expandedItem = data.expanded ? data.index : null;
    }
  }
}
</script>

<style lang="scss" scoped>
.company-news {
  height: 100%;
  max-height: 600px;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  
  .industry-header {
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
      
      .card-subtitle {
        margin-top: 4px;
        font-size: 12px;
        color: var(--hx-text-color-secondary);
      }
    }
  }
  
  .industry-tabs {
    display: flex;
    padding: 0 var(--hx-comp-paddingLR-s);
    gap: var(--hx-comp-margin-s);
    background-color: var(--hx-bg-color-container);
    overflow-x: auto;
    border-bottom: 1px solid var(--hx-border-level-1-color); // 添加分割线可能更好看
    flex-shrink: 0; // 防止被压缩
    
    &::-webkit-scrollbar {
      height: 4px;
    }
    
    &::-webkit-scrollbar-track {
      background: var(--hx-bg-color-container);
    }
    
    &::-webkit-scrollbar-thumb {
      background: var(--hx-bg-color-specialcomponent);
      border-radius: 2px;
    }

    .tab-item {
      padding: 8px 12px; // 稍微增大点击区域
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
      color: var(--hx-text-color-secondary);
      font-size: 13px;
      position: relative;
      
      &:hover {
        color: var(--hx-text-color-primary);
      }
      
      &.active {
        color: var(--hx-brand-color-3);
        font-weight: 600;
        
        &::after {
          content: '';
          position: absolute;
          bottom: -1px; // 贴合边框
          left: 0;
          width: 100%;
          height: 2px;
          background-color: var(--hx-brand-color-3);
        }
      }
    }
  }

  .timeline-content {
    flex: 1;
    overflow-y: auto; // 允许内容滚动
    padding: var(--hx-comp-paddingTB-s) 0;
     // 兼容性滚动条样式
     &::-webkit-scrollbar {
        width: 6px;
      }
      &::-webkit-scrollbar-track {
        background: transparent;
      }
      &::-webkit-scrollbar-thumb {
        background: var(--hx-bg-color-specialcomponent);
        border-radius: 3px;
      }
  }

  .item-preview-content {
    flex: 1;
    min-width: 0;
    
    .event-summary {
      margin: 0;
      font-size: 12px;
      color: var(--hx-text-color-secondary);
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      line-clamp: 2;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  }

  .company-info {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
    
    .company-name {
      font-weight: 600;
      color: var(--hx-text-color-primary);
      font-size: 14px; // 稍微放大
    }
    
    .company-code {
      font-size: 12px;
      color: var(--hx-text-color-secondary);
    }
  }

  .importance-indicator {
    display: flex;
    gap: 2px;
    
    .importance-icon {
      font-size: 12px;
      
      &.filled {
        color: var(--hx-warning-color-2);
      }
      
      &.empty {
        color: var(--hx-border-level-2-color);
      }
    }
  }
}

@media (max-width: 768px) {
  .company-news {
    .industry-tabs {
      padding: 0 var(--hx-comp-paddingLR-xs);
      
      .tab-item {
        padding: 6px 8px;
        font-size: 12px;
      }
    }
    .timeline-content {
       padding: var(--hx-comp-paddingTB-xs) 0;
    }
  }
}
</style> 
