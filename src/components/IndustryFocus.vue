<template>
  <div class="industry-focus card">
    <div class="industry-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">行业洞察</h2>
        <div class="card-subtitle">热门行业动态与发展趋势</div>
      </div>
    </div>
    
    <!-- 行业切换标签 -->
      <div class="industry-tabs">
        <div 
          v-for="(industry, index) in industries" 
          :key="index" 
        class="tab-item"
        :class="{ active: currentIndustry === industry.code }"
        @click="switchIndustry(industry.code)"
        >
          {{ industry.name }}
        </div>
      </div>
      
    <!-- 时间线内容 -->
    <div class="timeline-content">
      <DataTimeline 
        :items="currentIndustryItems"
        :expanded-item="expandedItem"
        @item-expanded="handleItemExpanded"
      >
        <template v-slot:item-tag="{ item }">
          <EventTag :text="item.type" :type="getEventTypeClass(item.type)" />
        </template>
        
        <template v-slot:item-title="{ item }">
          <h3 class="item-title">{{ item.title }}</h3>
        </template>
        
        <template v-slot:item-preview="{ item }">
          <div class="item-preview-content">
            <p class="event-summary">{{ item.content }}</p>
          </div>
        </template>
      </DataTimeline>
    </div>
  </div>
</template>

<script>
import DataTimeline from './ui/DataTimeline.vue'
import EventTag from './ui/EventTag.vue'
import { industryFocusMockData } from '../utils/mockData.js'

export default {
  name: 'IndustryFocus',
  components: {
    DataTimeline,
    EventTag
  },
  data() {
    return {
      currentIndustry: '',
      expandedItem: null,
      timeTagTypeMap: {
        '短期': 'time-short',
        '中期': 'time-mid',
        '长期': 'time-long'
      },
      industries: [],
      rawIndustryData: industryFocusMockData.response
    }
  },
  created() {
    this.initIndustriesData();
  },
  computed: {
    processedIndustries() {
      const industries = [];
      
      // 处理ind1-ind5的数据
      for (let i = 1; i <= 5; i++) {
        const key = `ind${i}`;
        const data = this.parseIndustryData(this.rawIndustryData[key]);
        if (data && data.industry) {
          industries.push({
            name: data.industry.name,
            code: data.industry.code,
            hotness: data.industry.hotness
          });
        }
      }
      
      // 按照hotness排序
      return industries.sort((a, b) => Number(a.hotness) - Number(b.hotness));
    },
    currentIndustryItems() {
      if (!this.currentIndustry) return [];
      
      // 找到对应的原始数据
      const currentKey = Object.keys(this.rawIndustryData).find(key => {
        const data = this.parseIndustryData(this.rawIndustryData[key]);
        return data && data.industry && data.industry.code === this.currentIndustry;
      });
      
      if (!currentKey) return [];
      
      const data = this.parseIndustryData(this.rawIndustryData[currentKey]);
      const events = data?.events || [];
      
      // 按日期降序排序
      return events.sort((a, b) => new Date(b.date) - new Date(a.date));
    }
  },
  methods: {
    parseIndustryData(jsonData) {
      if (!jsonData) return null;
      
      try {
        // 如果已经是对象，直接返回
        if (typeof jsonData === 'object') return jsonData;
        
        // 如果是简单字符串，不处理
        if (typeof jsonData === 'string' && !jsonData.includes('{') && !jsonData.includes('[')) {
          return null;
        }
        
        // 移除markdown标记和多余的换行
        let cleanJson = jsonData.replace(/```json\n|\n```|```/g, '').trim();
        
        // 检查是否为有效的JSON字符串
        if (!cleanJson.startsWith('{') && !cleanJson.startsWith('[')) {
          return null;
        }
        
        return JSON.parse(cleanJson);
      } catch (error) {
        console.error('解析行业数据失败:', error);
        return null;
      }
    },
    initIndustriesData() {
      if (this.processedIndustries.length > 0) {
        this.industries = this.processedIndustries;
        this.currentIndustry = this.industries[0].code;
      }
    },
    switchIndustry(code) {
      this.currentIndustry = code;
      this.expandedItem = null;
    },
    handleItemExpanded(data) {
      this.expandedItem = data.expanded ? data.index : null;
    },
    getEventTypeClass(type) {
      const typeClasses = {
        '政策动向': 'event-policy',
        '技术突破': 'event-tech',
        '市场表现': 'event-market',
        '行业趋势': 'event-trend',
        '产业链变化': 'event-chain',
        '竞争格局': 'event-competition'
      };
      return typeClasses[type] || '';
    }
  }
}
</script>

<style lang="scss" scoped>
.industry-focus {
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
      padding: 4px 8px;
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
          bottom: 0;
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
    overflow: hidden;
    padding: var(--hx-comp-paddingTB-s) 0;
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
      overflow: hidden;
    }
  }

  // 展开状态下移除行数限制
  .timeline-item.expanded {
    .event-summary {
      display: block;
      -webkit-line-clamp: unset;
      overflow: visible;
    }
  }
}

@media (max-width: 768px) {
  .industry-focus {
    .industry-tabs {
      padding: 0 var(--hx-comp-paddingLR-xs);
      
      .tab-item {
        padding: 6px 8px;
        font-size: 12px;
      }
    }
  }
}

/* 自定义EventTag样式 */
:deep(.event-tag) {
  &.event-policy {
    background-color: rgba(245, 158, 11, 0.15);
    color: #f59e0b; /* 黄色 - 政策动向 */
  }
  
  &.event-tech {
    background-color: rgba(239, 68, 68, 0.15);
    color: #ef4444; /* 红色 - 技术突破 */
  }
  
  &.event-market {
    background-color: rgba(36, 107, 248, 0.15);
    color: var(--hx-brand-color-3); /* 蓝色 - 市场表现 */
  }
  
  &.event-trend {
    background-color: rgba(16, 185, 129, 0.15);
    color: #10b981; /* 绿色 - 行业趋势 */
  }
  
  &.event-chain {
    background-color: rgba(124, 58, 237, 0.15);
    color: #7c3aed; /* 紫色 - 产业链变化 */
  }
  
  &.event-competition {
    background-color: rgba(236, 72, 153, 0.15);
    color: #ec4899; /* 粉色 - 竞争格局 */
  }
}

/* 调整preview-header样式 */
.preview-header {
  display: flex;
  gap: 8px;
  margin-bottom: 4px;
}
</style> 