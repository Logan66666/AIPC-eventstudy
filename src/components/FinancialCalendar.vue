<template>
  <div class="financial-calendar card">
    <div class="calendar-header">
      <div class="header-main">
        <h2 class="card-title secondary-title">财经日历</h2>
        <div class="card-subtitle">重要经济数据与财报发布安排</div>
      </div>
      
      <!-- 添加筛选下拉菜单 -->
      <div class="filter-section">
        <DropdownSelect
          v-model="selectedCategories"
          :options="categoryOptions"
          placeholder="筛选类别"
          all-text="全部类别"
        />
      </div>
    </div>
    
    <div class="calendar-content">
      <!-- 加载状态 -->
      <div v-if="isLoading" class="loading-overlay">
        <div class="loading-spinner"></div>
        <div class="loading-text">加载财经数据中...</div>
      </div>
      
      <FullCalendar 
        ref="fullCalendar"
        :options="calendarOptions"
        class="custom-calendar"
      />
      
      <!-- 事件详情弹窗 -->
      <div class="event-popup" v-if="selectedEvent" :style="popupPosition">
        <div class="popup-header">
          <h3 class="event-title">{{ selectedEvent.title }}</h3>
          <button class="close-btn" @click="selectedEvent = null">×</button>
        </div>
        <div class="popup-content">
          <div class="event-description">{{ selectedEvent.description }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import DropdownSelect from './ui/DropdownSelect.vue'
import axios from 'axios'
import { financialCalendarMockData } from '../utils/mockData'

export default {
  name: 'FinancialCalendar',
  components: {
    FullCalendar,
    DropdownSelect
  },
  data() {
    return {
      currentDate: new Date(),
      currentViewStartDate: null,
      currentViewEndDate: null,
      selectedEvent: null,
      popupPosition: {
        top: '50px',
        left: '50px'
      },
      calendarOptions: {
        plugins: [dayGridPlugin, interactionPlugin],
        initialView: 'dayGridMonth',
        headerToolbar: {
          left: 'prev',
          center: 'title',
          right: 'next'
        },
        locale: 'zh-cn',
        firstDay: 0,
        dayMaxEvents: 5,
        height: 'auto',
        eventDisplay: 'block',
        eventTimeFormat: {
          hour: '2-digit',
          minute: '2-digit',
          meridiem: false,
          hour12: false
        },
        dayHeaderFormat: { weekday: 'short' },
        events: [],
        datesSet: this.handleDatesSet,
        viewClassNames: 'fc-custom-view',
        dayHeaderClassNames: 'fc-custom-header',
        dayCellClassNames: 'fc-custom-cell',
        eventOrder: (a, b) => {
          // 首先按类别排序（行业排在前面）
          if (a.extendedProps.category !== b.extendedProps.category) {
            return a.extendedProps.category === '行业' ? -1 : 1;
          }
          // 其次按时间排序
          return new Date(a.start) - new Date(b.start);
        },
        moreLinkClick: 'popover',
        eventDidMount: this.handleEventMount,
        viewDidMount: this.handleViewMount,
        eventClick: this.handleEventClick
      },
      rawEvents: [],
      selectedCategories: [],
      isLoading: false,
      loadError: null
    }
  },
  computed: {
    // 修改类别选项
    categoryOptions() {
      return [
        { label: '财经', value: '财经', badgeClass: 'global' },
        { label: '行业', value: '行业', badgeClass: 'industry' }
      ];
    },
    
    // 根据选中类别过滤事件
    filteredEvents() {
      if (this.selectedCategories.length === 0) {
        return this.rawEvents;
      }
      
      return this.rawEvents.filter(event => 
        this.selectedCategories.includes(event.category)
      );
    }
  },
  watch: {
    // 监听筛选变化，更新日历
    filteredEvents: {
      handler() {
        this.updateCalendarEvents();
      },
      deep: true
    }
  },
  created() {
    // 初始化选择所有类别
    this.selectedCategories = this.categoryOptions.map(option => option.value);
    
    // 获取财经日历数据
    this.fetchCalendarData();
  },
  mounted() {
    // 确保日历初始化在DOM加载后执行
    this.$nextTick(() => {
      this.initCalendar();
      
      // 延迟执行，等待日历渲染完成
      setTimeout(() => {
        this.fixHeaderBorder();
        this.adjustEmptyRows();
        this.fixBorderGaps();
        this.fixCalendarBackground();
      }, 100);
    });
  },
  methods: {
    // 初始化日历
    initCalendar() {
      if (!this.$refs.fullCalendar) return;
      
      // 获取今天的日期
      const today = new Date();
      
      // 设置日历视图为当前月
      const calendarApi = this.$refs.fullCalendar.getApi();
      if (calendarApi) {
        calendarApi.gotoDate(today);
      }
    },
    
    // 处理日期变化
    handleDatesSet(arg) {
      // 保存当前视图的日期范围
      this.currentViewStartDate = arg.start;
      this.currentViewEndDate = arg.end;
    },
    
    // 处理事件挂载
    handleEventMount(info) {
      if (info.event.extendedProps.category === '行业') {
        const container = info.el.closest('.fc-daygrid-day-events, .fc-popover-body');
        if (container && !container.dataset.industryEventsProcessed) {
          // 收集容器中所有行业事件
          const industryEvents = Array.from(container.querySelectorAll('.fc-event'))
            .filter(el => {
              const eventId = el.getAttribute('data-event-id');
              const event = info.view.calendar.getEventById(eventId);
              return event && event.extendedProps.category === '行业';
            });
          
          // 如果有超过一个行业事件，按顺序移到容器顶部
          if (industryEvents.length > 0) {
            // 逆序处理，确保顺序正确
            for (let i = industryEvents.length - 1; i >= 0; i--) {
              container.insertBefore(industryEvents[i], container.firstChild);
            }
          }
          
          // 标记容器已处理过行业事件排序
          container.dataset.industryEventsProcessed = 'true';
        }
      }
    },

    // 处理视图挂载
    handleViewMount(arg) {
      arg.el.style.backgroundColor = 'var(--hx-bg-color-container)';
      const headers = arg.el.querySelectorAll('.fc-col-header, .fc-col-header-cell');
      headers.forEach(header => {
        header.style.backgroundColor = 'var(--hx-bg-color-specialcomponent)';
      });
      const bodyCells = arg.el.querySelectorAll('.fc-daygrid-body, .fc-scrollgrid, .fc-scrollgrid-section');
      bodyCells.forEach(cell => {
        cell.style.backgroundColor = 'var(--hx-bg-color-container)';
      });
    },

    // 获取事件的唯一标识
    getEventKey(event) {
      // 只使用日期的年月日部分
      const dateStr = event.date.toISOString().split('T')[0];
      return `${dateStr}_${event.title}_${event.category}`;
    },

    // 处理API返回的事件数据
    processApiEvents(eventData) {
      if (!Array.isArray(eventData) || eventData.length === 0) return [];

      // 使用 Map 存储事件，确保唯一性
      const eventMap = new Map();

      // 处理行业事件
      eventData.forEach(item => {
        const date = new Date(item.date);
        // 规范化日期，只保留年月日
        date.setHours(0, 0, 0, 0);
        
        const event = {
          date,
          title: item.title,
          description: item.title,
          importance: 2,
          category: '行业',
          blockName: item.blocks?.[0]?.name || '行业'
        };
        
        const key = this.getEventKey(event);
        if (!eventMap.has(key)) {
          eventMap.set(key, event);
        }
      });

      // 处理财经事件
      if (financialCalendarMockData.data?.data) {
        financialCalendarMockData.data.data.forEach(dayData => {
          if (dayData.eventModelList) {
            dayData.eventModelList.forEach(event => {
              const date = new Date(event.date);
              // 规范化日期，只保留年月日
              date.setHours(0, 0, 0, 0);
              
              const financialEvent = {
                date,
                title: event.event,
                description: `${event.event} (预期值: ${event.qz || '-'}, 前值: ${event.ycz || '-'})`,
                importance: parseInt(event.importanceEn) || 2,
                category: '财经',
                time: event.time
              };
              
              const key = this.getEventKey(financialEvent);
              if (!eventMap.has(key)) {
                eventMap.set(key, financialEvent);
              }
            });
          }
        });
      }

      // 转换为数组并按日期和标题排序
      return Array.from(eventMap.values()).sort((a, b) => {
        // 首先按日期排序
        const dateCompare = a.date.getTime() - b.date.getTime();
        if (dateCompare !== 0) return dateCompare;
        
        // 如果日期相同，按标题排序
        return a.title.localeCompare(b.title);
      });
    },

    // 转换事件为日历格式
    formatEventForCalendar(event) {
      const displayTitle = event.category === '行业'
        ? `${event.blockName} | ${event.title}`
        : `${event.category} | ${event.title}`;
        
      // 创建唯一ID
      const dateStr = event.date.toISOString().split('T')[0];
      const eventId = `${dateStr}_${event.category}_${event.title}`.replace(/\s+/g, '_');

      return {
        id: eventId, // 添加唯一ID
        title: displayTitle,
        start: event.date.toISOString().split('T')[0],
        description: event.description,
        category: event.category,
        importance: event.importance,
        backgroundColor: 'transparent',
        borderColor: event.category === '行业' 
          ? 'var(--hx-sec-brand-color-3)' 
          : 'var(--hx-brand-color-3)',
        textColor: 'var(--hx-text-color-primary)',
        extendedProps: {
          description: event.description,
          category: event.category,
          importance: event.importance,
          originalTitle: event.title,
          blockName: event.blockName
        },
        classNames: [`event-category-${event.category.toLowerCase()}`]
      };
    },

    // 更新日历事件
    updateCalendarEvents() {
      const events = this.filteredEvents.map(this.formatEventForCalendar);
      
      if (this.$refs.fullCalendar) {
        const calendarApi = this.$refs.fullCalendar.getApi();
        
        // 先清除所有容器的处理标记
        const containers = this.$refs.fullCalendar.$el.querySelectorAll('.fc-daygrid-day-events, .fc-popover-body');
        containers.forEach(container => {
          delete container.dataset.industryEventsProcessed;
        });
        
        // 确保在添加新事件前先清除旧事件
        calendarApi.getEventSources().forEach(source => source.remove());
        calendarApi.removeAllEvents();
        
        // 添加新事件
        calendarApi.addEventSource({
          events: events,
          id: 'mainEventSource'
        });
      } else {
        this.calendarOptions.events = events;
      }
    },

    // 获取财经日历数据
    async fetchCalendarData() {
      this.isLoading = true;
      try {
        const response = await axios.get('http://zx.10jqka.com.cn/hotblock/calendar/get', {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          timeout: 10000
        });

        if (response.data?.errorcode === 0 && response.data.result) {
          this.rawEvents = this.processApiEvents(response.data.result);
          this.updateCalendarEvents();
        }
      } catch (error) {
        this.loadError = error.message;
      } finally {
        this.isLoading = false;
      }
    },

    handleEventClick(info) {
      // 获取事件详情
      this.selectedEvent = {
        title: info.event.extendedProps.originalTitle,
        description: info.event.extendedProps.description,
        category: info.event.extendedProps.category,
        importance: info.event.extendedProps.importance,
        blockName: info.event.extendedProps.blockName // 保存行业板块名称
      };
      
      // 获取事件元素位置与窗口位置信息
      const rect = info.el.getBoundingClientRect();
      const calendarRect = this.$refs.fullCalendar.$el.getBoundingClientRect();
      const calendarWidth = calendarRect.width;
      const calendarHeight = calendarRect.height;
      
      // 弹窗尺寸
      const popupWidth = 260;
      const popupHeight = 200; // 估计高度
      
      // 初始位置计算
      let left = rect.left - calendarRect.left;
      let top = rect.top - calendarRect.top + rect.height + 5;
      
      // 如果弹窗会超出右边界，则向左偏移
      if (left + popupWidth > calendarWidth) {
        left = Math.max(0, calendarWidth - popupWidth - 10);
      }
      
      // 如果弹窗会超出底部边界，则向上弹出
      if (top + popupHeight > calendarHeight) {
        top = rect.top - calendarRect.top - popupHeight - 5;
      }
      
      // 确保弹窗不会超出顶部边界
      if (top < 0) {
        // 尝试显示在点击位置的右侧
        left = rect.left - calendarRect.left + rect.width + 5;
        top = rect.top - calendarRect.top;
        
        // 如果仍然会超出右侧边界，则回到原位置但调整到可见区域内
        if (left + popupWidth > calendarWidth) {
          left = Math.max(0, calendarWidth - popupWidth - 10);
          top = Math.max(10, Math.min(calendarHeight - popupHeight - 10, rect.top - calendarRect.top));
        }
      }
      
      // 设置弹窗位置
      this.popupPosition = {
        top: `${top}px`,
        left: `${left}px`
      };
    },
    formatTime(time) {
      if (!time) return '';
      return time;
    },
    getImportanceValue(importance) {
      // 直接返回重要性值，因为已经是1-3的数值
      return importance;
    },
    // 修复表头下方边框问题
    fixHeaderBorder() {
      const headerCells = this.$refs.fullCalendar.$el.querySelectorAll('.fc-col-header-cell');
      headerCells.forEach(cell => {
        // 移除默认样式
        cell.style.borderBottomColor = 'var(--hx-border-level-1-color)';
        
        // 添加额外的边框元素
        const borderElement = document.createElement('div');
        borderElement.style.position = 'absolute';
        borderElement.style.bottom = '0';
        borderElement.style.left = '0';
        borderElement.style.right = '0';
        borderElement.style.height = '1px';
        borderElement.style.backgroundColor = 'var(--hx-border-level-1-color)';
        borderElement.style.zIndex = '10';
        cell.style.position = 'relative';
        cell.appendChild(borderElement);
      });
    },
    // 调整空行高度
    adjustEmptyRows() {
      const rows = this.$refs.fullCalendar.$el.querySelectorAll('.fc-daygrid-row');
      
      rows.forEach(row => {
        const hasEvents = row.querySelector('.fc-daygrid-day-events:not(:empty)');
        
        // 如果整行没有事件，则添加特殊类
        if (!hasEvents) {
          row.classList.add('fc-row-empty');
          
          // 修改该行所有单元格的高度
          const cells = row.querySelectorAll('.fc-daygrid-day');
          cells.forEach(cell => {
            const frame = cell.querySelector('.fc-daygrid-day-frame');
            if (frame) {
              frame.style.minHeight = '30px';
            }
          });
        }
      });
    },
    // 修复边框间隙问题
    fixBorderGaps() {
      // 获取表格主体
      const tableBody = this.$refs.fullCalendar.$el.querySelector('.fc-scrollgrid-body');
      if (!tableBody) return;
      
      // 确保表格有完整的外边框
      const scrollGrid = this.$refs.fullCalendar.$el.querySelector('.fc-scrollgrid');
      if (scrollGrid) {
        scrollGrid.style.borderWidth = '1px';
        scrollGrid.style.borderStyle = 'solid';
        scrollGrid.style.borderColor = 'var(--hx-border-level-1-color)';
      }
      
      // 修复单元格垂直分隔线
      const cells = this.$refs.fullCalendar.$el.querySelectorAll('.fc-daygrid-day');
      cells.forEach(cell => {
        cell.style.borderRight = '1px solid var(--hx-border-level-1-color)';
        cell.style.borderBottom = '1px solid var(--hx-border-level-1-color)';
      });
      
      // 修复表格底部线条
      const lastRow = this.$refs.fullCalendar.$el.querySelector('.fc-scrollgrid-section:last-child');
      if (lastRow) {
        const cells = lastRow.querySelectorAll('td');
        cells.forEach(cell => {
          cell.style.borderBottom = '1px solid var(--hx-border-level-1-color)';
        });
      }
    },
    // 添加一个新方法专门处理背景色问题
    fixCalendarBackground() {
      if (!this.$refs.fullCalendar) return;
      
      const calendarEl = this.$refs.fullCalendar.$el;
      
      // 1. 强制设置所有相关元素的背景色
      const elementsToFix = [
        '.fc-view',
        '.fc-view-harness',
        '.fc-scroller',
        '.fc-scroller-liquid',
        '.fc-scroller-liquid-absolute',
        '.fc-daygrid',
        '.fc-daygrid-body',
        '.fc-scrollgrid',
        '.fc-scrollgrid-section',
        '.fc-scrollgrid-section > *',
        'tbody',
        'thead'
      ];
      
      elementsToFix.forEach(selector => {
        const elements = calendarEl.querySelectorAll(selector);
        elements.forEach(el => {
          el.style.backgroundColor = 'var(--hx-bg-color-container)';
        });
      });
      
      // 2. 特别处理表头
      const headerElements = calendarEl.querySelectorAll('.fc-col-header, .fc-col-header-cell');
      headerElements.forEach(el => {
        el.style.backgroundColor = 'var(--hx-bg-color-specialcomponent)';
        el.style.border = '1px solid var(--hx-border-level-1-color)';
      });
      
      // 3. 为可能出现背景问题的元素添加覆盖层
      const viewHarness = calendarEl.querySelector('.fc-view-harness');
      if (viewHarness) {
        // 检查是否已经有覆盖层
        const existingOverlay = viewHarness.querySelector('.background-overlay');
        if (!existingOverlay) {
          const overlay = document.createElement('div');
          overlay.className = 'background-overlay';
          overlay.style.position = 'absolute';
          overlay.style.top = '0';
          overlay.style.left = '0';
          overlay.style.right = '0';
          overlay.style.bottom = '0';
          overlay.style.backgroundColor = 'var(--hx-bg-color-container)';
          overlay.style.zIndex = '-1';
          overlay.style.pointerEvents = 'none';
          viewHarness.style.position = 'relative';
          viewHarness.appendChild(overlay);
        }
      }
    },
  }
}
</script>

<style lang="scss" scoped>
.financial-calendar {
  height: auto;
  display: flex;
  flex-direction: column;
  background-color: var(--hx-bg-color-container);
  padding: 0;
  position: relative;
  
  .calendar-header {
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
    
    .filter-section {
      display: flex;
      gap: 10px;
    }
  }
  
  .calendar-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 0 var(--hx-comp-paddingLR-s) var(--hx-comp-paddingTB-s);
    overflow: hidden;
    position: relative;
    background-color: var(--hx-bg-color-container);
    
    /* 加载状态与错误信息样式 */
    .loading-overlay, .error-message {
      position: absolute;
      z-index: 10;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255,255,255,0.8);
    }
    
    .loading-overlay {
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      flex-direction: column;
      
      .loading-spinner {
        width: 40px;
        height: 40px;
        border: 3px solid rgba(59,130,246,0.2);
        border-top-color: #3b82f6;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 10px;
      }
      
      @keyframes spin {
        to { transform: rotate(360deg); }
      }
    }
    
    .error-message {
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      flex-direction: column;
      background: white;
      border: 1px solid #f56c6c;
      border-radius: 6px;
      padding: 16px;
      width: 280px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      
      .retry-button {
        margin-top: 10px;
        background: #f56c6c;
        color: white;
        border: none;
        padding: 6px 12px;
        border-radius: 4px;
        cursor: pointer;
      }
    }
  }
  
  /* 自定义FullCalendar样式 */
  :deep(.fc) {
    font-family: inherit;
    font-size: 12px;
    background-color: var(--hx-bg-color-container);
    
    /* 修改日历组件的视图背景色 */
    .fc-view-harness {
      background-color: var(--hx-bg-color-container);
    }
    
    /* 修改日历主体部分背景 */
    .fc-daygrid-body {
      background-color: var(--hx-bg-color-container);
    }
    
    /* 修改月视图表格背景 */
    .fc-daygrid-body table {
      background-color: var(--hx-bg-color-container);
    }
    
    /* 修改各类型单元格的背景色 */
    td.fc-day {
      background-color: var(--hx-bg-color-container);
    }
    
    /* 特别处理白色背景问题 */
    .fc-scrollgrid,
    .fc-scrollgrid-section,
    .fc-scrollgrid tbody,
    .fc-scroller {
      background-color: var(--hx-bg-color-container) !important;
    }
    
    .fc-header-toolbar {
      margin-bottom: 12px;
      padding: 0;
      
      .fc-toolbar-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--hx-text-color-secondary);
      }
      
      .fc-prev-button, .fc-next-button {
        background-color: transparent;
        border: 1px solid var(--hx-border-level-1-color);
        color: var(--hx-text-color-secondary);
        border-radius: 4px;
        
        &:hover {
          background-color: var(--hx-bg-color-specialcomponent);
          color: var(--hx-brand-color-3);
          border-color: var(--hx-brand-color-3);
        }
        
        &:focus {
          box-shadow: none;
        }
      }
    }
    
    /* 表头样式增强 */
    .fc-col-header {
      background-color: var(--hx-bg-color-specialcomponent);
      border-radius: 4px 4px 0 0;
    }
    
    .fc-col-header-cell {
      padding: 4px 0;
      font-weight: 500;
      font-size: 11px;
      color: var(--hx-text-color-tertiary);
      text-transform: uppercase;
      
      &.fc-day-sun, &.fc-day-sat {
        color: var(--hx-text-color-quaternary);
      }
    }
    
    /* 表格边框样式 */
    .fc-scrollgrid {
      border-color: var(--hx-border-level-1-color);
    }
    
    .fc-scrollgrid-section > * {
      border-color: var(--hx-border-level-1-color);
    }
    
    .fc-scrollgrid-section-header > th {
      border-color: var(--hx-border-level-1-color);
    }
    
    .fc-scrollgrid-section-body > tr > td {
      border-color: var(--hx-border-level-1-color);
    }
    
    /* 修改所有分割线颜色 */
    .fc-theme-standard .fc-scrollgrid {
      border: 1px solid var(--hx-border-level-1-color);
    }
    
    .fc-theme-standard td, 
    .fc-theme-standard th {
      border: 1px solid var(--hx-border-level-1-color);
    }
    
    /* 表头底部分割线 */
    .fc-col-header-cell {
      border-color: var(--hx-border-level-1-color) !important;
    }
    
    /* 日期单元格所有边框 */
    .fc-daygrid-day {
      border-color: var(--hx-border-level-1-color) !important;
    }
    
    /* 确保表格内所有边框都使用主题颜色 */
    * {
      border-color: var(--hx-border-level-1-color);
    }
    
    /* 移除今日单元格的表格线 */
    .fc-day-today {
      border-color: var(--hx-border-level-1-color) !important;
    }
    
    /* 覆盖默认表格线样式 */
    table {
      border-collapse: collapse;
      border-color: var(--hx-border-level-1-color);
    }
    
    /* 确保表头和内容部分之间的边框颜色一致 */
    .fc-scrollgrid-sync-inner {
      border-color: var(--hx-border-level-1-color);
    }
    
    /* 重新设计今日单元格样式，仅保留背景色变化 */
    .fc-daygrid-day.fc-day-today {
      background-color: rgba(var(--hx-brand-color-rgb, 59, 130, 246), 0.08) !important;
      position: relative;
      
      /* 移除左侧装饰条 */
      &::before {
        display: none;
      }
      
      /* 移除其它装饰条和标记 */
      &::after {
        display: none;
      }
      
      .fc-daygrid-day-frame::after {
        display: none;
      }
      
      /* 只保留日期颜色变化 */
      .fc-daygrid-day-number {
        font-weight: 600;
        color: var(--hx-brand-color-3);
        font-size: 13px;
      }
    }
    
    /* 日期单元格样式 */
    .fc-daygrid-day {
      transition: background-color 0.2s;
      
      &:hover {
        background-color: var(--hx-bg-color-specialcomponent);
      }
    }
    
    td.fc-day {
      border-color: var(--hx-border-level-1-color);
    }
    
    .fc-daygrid-day-frame {
      min-height: 40px;
    }
    
    .fc-daygrid-day-number {
      font-size: 13px;
      color: var(--hx-text-color-secondary);
      padding: 5px 8px 2px;
      text-align: right;
      width: 100%;
    }
    
    /* 事件显示样式 */
    .fc-daygrid-day-events {
      padding: 0 3px !important; 
      margin-top: 3px !important;
      margin-bottom: 3px !important;
    }
    
    /* 事件本身的样式 */
    :deep(.fc-event) {
      margin-bottom: 4px !important;
      padding: 3px 4px !important;
      line-height: 1.4 !important;
    }
    
    .fc-event {
      border-radius: 0;
      padding: 0 2px;
      font-size: 12px;
      cursor: pointer;
      margin-bottom: 0;
      border-width: 0;
      border-left-width: 2px;
      box-shadow: none;
      background: transparent !important;
      transition: none;
      line-height: 1.3;
      
      &:hover {
        transform: none;
        box-shadow: none;
        background-color: var(--hx-bg-color-specialcomponent) !important;
      }
      
      .fc-event-main {
        color: var(--hx-text-color-primary);
        padding: 0;
      }
      
      .fc-event-title {
        white-space: normal; /* 允许换行 */
        overflow: hidden;
        text-overflow: ellipsis;
        font-weight: normal;
        padding: 1px 0;
        /* 限制为最多两行 */
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        max-height: 2.8em; /* 增加行高 */
      }
      
      // 修改财经事件的装饰条颜色
      &[data-category="财经"] {
        border-left-color: var(--hx-brand-color-3) !important;
      }
      
      // 修改行业事件的装饰条颜色
      &[data-category="行业"] {
        border-left-color: var(--hx-sec-brand-color-3) !important;
      }
    }
    
    /* 高重要性事件 -> 修改为类别样式：全球 */
    .fc-event.fc-daygrid-event[style*="var(--hx-brand-color-3)"] {
      .fc-event-main {
        color: var(--hx-text-color-primary);
      }
    }
    
    /* 中等重要性事件 -> 修改为类别样式：政策 */
    .fc-event.fc-daygrid-event[style*="var(--hx-warning-color-3)"] {
      .fc-event-main {
        color: var(--hx-text-color-primary);
      }
    }
    
    /* 低重要性事件 -> 修改为类别样式：行业 */
    .fc-event.fc-daygrid-event[style*="var(--hx-sec-brand-color-3)"] {
      .fc-event-main {
        color: var(--hx-text-color-primary);
      }
    }
    
    /* 添加新的类别样式：公司 */
    .fc-event.fc-daygrid-event[style*="var(--hx-success-color-3)"] {
      .fc-event-main {
        color: var(--hx-text-color-primary);
      }
    }
    
    .fc-daygrid-more-link {
      font-size: 10px;
      padding: 0 2px;
      margin-top: 0;
      line-height: 1.3;
      font-weight: normal;
      color: var(--hx-brand-color-3);
      background-color: rgba(var(--hx-brand-color-rgb, 59, 130, 246), 0.08);
      
      &:hover {
        color: var(--hx-brand-color-4);
        background-color: rgba(var(--hx-brand-color-rgb, 59, 130, 246), 0.12);
      }
    }
    
    /* 周末列样式 */
    .fc-day-sat, .fc-day-sun {
      background-color: rgba(var(--hx-bg-color-specialcomponent-rgb, 30, 30, 30), 0.3);
    }
    
    /* 其他月份日期样式 */
    .fc-day-other {
      opacity: 0.5;
      background-color: rgba(var(--hx-bg-color-specialcomponent-rgb, 30, 30, 30), 0.15);
      
      .fc-daygrid-day-number {
        color: var(--hx-text-color-tertiary);
      }
    }
    
    /* 空行自适应高度 */
    .fc-daygrid-day-events:empty + .fc-daygrid-day-bottom {
      margin-top: 0;
    }
    
    /* 空行单元格样式 */
    .fc-daygrid-day-events:empty {
      margin: 0;
      padding: 0;
      
      & + .fc-daygrid-day-bottom {
        padding: 0;
      }
    }
    
    /* 当一周内所有天都没有事件时进一步缩小高度 */
    .fc-daygrid-row:has(.fc-daygrid-day-events:empty) {
      .fc-daygrid-day-frame {
        min-height: 30px;
      }
    }
    
    /* More弹窗样式修复 */
    .fc-popover {
      background-color: var(--hx-bg-color-container);
      border: 1px solid var(--hx-border-level-1-color);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      opacity: 1 !important;
      
      .fc-popover-header {
        background-color: var(--hx-bg-color-specialcomponent);
        color: var(--hx-text-color-primary);
        padding: 6px 8px;
        font-size: 12px;
        border-bottom: 1px solid var(--hx-border-level-1-color);
        opacity: 1 !important;
        
        .fc-popover-title {
          color: var(--hx-text-color-primary);
          font-weight: 500;
          opacity: 1 !important;
        }
        
        .fc-popover-close {
          color: var(--hx-text-color-tertiary);
          font-size: 14px;
          opacity: 1 !important;
          
          &:hover {
            color: var(--hx-text-color-primary);
          }
        }
      }
      
      .fc-popover-body {
        padding: 8px;
        background-color: var(--hx-bg-color-container);
        opacity: 1 !important;
        
        .fc-event {
          margin: 4px 0;
          opacity: 1 !important;
          padding: 3px 4px !important;
        }
      }
    }
    
    /* 日期数字更紧凑 */
    .fc-daygrid-day-number {
      font-size: 12px !important;
      padding: 2px 4px 0 !important;
      text-align: right;
      width: 100%;
    }
  }
  
  /* 事件详情弹窗样式 */
  .event-popup {
    position: absolute;
    z-index: 20; // 提高z-index确保显示在最上层
    width: 260px;
    max-height: 80vh; // 限制最大高度防止超出视口
    background-color: var(--hx-bg-color-container);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); // 加深阴影
    border-radius: var(--hx-radius-medium, 6px);
    border: 1px solid var(--hx-border-level-2-color);
    overflow: hidden;
    animation: popup-appear 0.2s ease-out;
    
    @keyframes popup-appear {
      from {
        opacity: 0;
        transform: translateY(10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    
    .popup-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      padding: 12px 14px 8px;
      border-bottom: 1px solid var(--hx-border-level-1-color);
      background-color: var(--hx-bg-color-specialcomponent);
      
      .event-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--hx-text-color-primary);
        margin: 0;
        padding-right: 20px;
        line-height: 1.4;
        word-break: break-word; // 允许长标题自动换行
      }
      
      .close-btn {
        background: none;
        border: none;
        font-size: 18px;
        line-height: 1;
        color: var(--hx-text-color-tertiary);
        cursor: pointer;
        padding: 0 4px;
        border-radius: 4px;
        
        &:hover {
          color: var(--hx-text-color-primary);
          background-color: rgba(var(--hx-border-level-2-color-rgb, 58, 63, 85), 0.5);
        }
      }
    }
    
    .popup-content {
      padding: 12px 14px 14px;
      
      .event-description {
        font-size: 13px;
        color: var(--hx-text-color-secondary);
        margin: 0;
        line-height: 1.6;
      }
    }
  }
  
  /* 下拉菜单类别标签样式 */
  :deep(.type-badge) {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-left: auto;
    
    &.global {
      background-color: var(--hx-brand-color-3);
    }
    
    &.policy {
      background-color: var(--hx-warning-color-3);
    }
    
    &.industry {
      background-color: var(--hx-sec-brand-color-3);
    }
    
    &.company {
      background-color: var(--hx-success-color-3);
    }
    
    &.all-types {
      background: linear-gradient(90deg, 
        var(--hx-brand-color-3) 25%, 
        var(--hx-warning-color-3) 25%, 
        var(--hx-warning-color-3) 50%, 
        var(--hx-sec-brand-color-3) 50%, 
        var(--hx-sec-brand-color-3) 75%, 
        var(--hx-success-color-3) 75%);
    }
  }
}

@media (max-width: 768px) {
  .financial-calendar {
    .calendar-content {
      padding: 0 var(--hx-comp-paddingLR-xs) var(--hx-comp-paddingTB-xs);
    }
    
    :deep(.fc) {
      font-size: 11px;
      
      .fc-toolbar-title {
        font-size: 13px;
      }
      
      .fc-daygrid-day-frame {
        min-height: 70px;
      }
      
      .fc-daygrid-day-number {
        font-size: 12px;
        padding: 2px 4px;
      }
      
      .fc-event {
        font-size: 10px;
        padding: 1px 2px;
      }
    }
    
    .event-popup {
      width: 220px;
      
      .popup-header {
        padding: 10px 12px 6px;
        
        .event-title {
          font-size: 13px;
        }
      }
      
      .popup-content {
        padding: 8px 12px 12px;
        
        .event-description {
          font-size: 11px;
        }
      }
    }
  }
}

/* 修改所有分割线颜色 - 全新写法 */
:deep(.fc-theme-standard) {
  /* 全局边框重置为主题颜色 */
  border-color: var(--hx-border-level-1-color) !important;
  
  /* 所有表格相关元素的边框 */
  .fc-scrollgrid,
  .fc-scrollgrid-section,
  .fc-scrollgrid-section > *,
  .fc-scrollgrid-section > * > *,
  td, th,
  tr, tbody, thead {
    border-color: var(--hx-border-level-1-color) !important;
  }
  
  /* 确保弹窗完全不透明 */
  .fc-popover,
  .fc-popover-header,
  .fc-popover-body {
    opacity: 1 !important;
    background-color: var(--hx-bg-color-container) !important;
  }
  
  .fc-popover-header {
    background-color: var(--hx-bg-color-specialcomponent) !important;
  }
  
  /* 保留弹窗中事件的样式 */
  .fc-popover .fc-event {
    opacity: 1 !important;
    background-color: transparent !important;
  }
  
  .fc-popover .fc-event[data-category="财经"] {
    border-left-color: var(--hx-brand-color-3) !important;
  }
  
  .fc-popover .fc-event[data-category="行业"] {
    border-left-color: var(--hx-sec-brand-color-3) !important;
  }
  
  /* 确保单元格边框完整显示 */
  .fc-scrollgrid {
    border-bottom: 1px solid var(--hx-border-level-1-color) !important;
    border-right: 1px solid var(--hx-border-level-1-color) !important;
    
    /* 修复Firefox中的边框显示问题 */
    border-collapse: separate;
    border-spacing: 0;
  }
  
  /* 修复表格底部线条 */
  .fc-scrollgrid-section:last-child > td {
    border-bottom: 1px solid var(--hx-border-level-1-color) !important;
  }
  
  /* 修复垂直线与底部边界的连接 */
  .fc-scrollgrid-section:last-child > td {
    position: relative;
    
    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 1px;
      background-color: var(--hx-border-level-1-color);
      z-index: 5;
    }
  }
  
  /* 特别处理垂直边框 */
  .fc-scrollgrid-section td,
  .fc-scrollgrid-section th {
    border-right: 1px solid var(--hx-border-level-1-color) !important;
  }
  
  /* 修复单元格间隙 */
  .fc-daygrid-body {
    width: 100% !important;
    
    table {
      width: 100% !important;
    }
    
    .fc-daygrid-day {
      border-bottom: 1px solid var(--hx-border-level-1-color) !important;
      
      &:last-child {
        border-right: none;
      }
    }
  }
}

/* 完全覆盖FullCalendar白色背景问题的解决方案 */
.custom-calendar {
  /* 1. 设置全局背景色 */
  background-color: var(--hx-bg-color-container);
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: var(--hx-bg-color-container);
    z-index: -1;
  }
  
  /* 2. 深度选择器修改所有可能的背景色相关元素 */
  :deep(.fc-view),
  :deep(.fc-view-harness),
  :deep(.fc-scroller),
  :deep(.fc-scroller-liquid),
  :deep(.fc-scroller-liquid-absolute),
  :deep(.fc-daygrid),
  :deep(.fc-daygrid-body),
  :deep(.fc-scrollgrid),
  :deep(.fc-scrollgrid-section),
  :deep(.fc-scrollgrid-section > *),
  :deep(table),
  :deep(tbody),
  :deep(tr),
  :deep(td),
  :deep(th) {
    background-color: var(--hx-bg-color-container) !important;
  }
  
  /* 3. 覆盖表头背景色 */
  :deep(.fc-col-header),
  :deep(.fc-col-header-cell) {
    background-color: var(--hx-bg-color-specialcomponent) !important;
  }
  
  /* 4. 特殊处理视图容器 */
  :deep(.fc-view-harness) {
    position: relative;
    z-index: 0;
    
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: var(--hx-bg-color-container);
      z-index: -1;
    }
  }
  
  /* 5. 处理表格与背景之间可能出现的间隙 */
  :deep(.fc-scrollgrid) {
    border-collapse: collapse !important;
    border-spacing: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    background-color: var(--hx-bg-color-container) !important;
  }
  
  /* 6. 强制修复任何可能的白色背景 */
  :deep([style*="background"]) {
    background-color: var(--hx-bg-color-container) !important;
  }
  
  /* 7. 专门处理表头下方可能出现的白色间隙 */
  :deep(.fc-scrollgrid-section:first-child),
  :deep(.fc-scrollgrid-section:first-child td),
  :deep(.fc-scrollgrid-section:first-child th),
  :deep(.fc-scrollgrid-section:first-child + .fc-scrollgrid-section),
  :deep(.fc-scrollgrid-section:first-child + .fc-scrollgrid-section td),
  :deep(.fc-scrollgrid-section:first-child + .fc-scrollgrid-section td > div) {
    background-color: var(--hx-bg-color-container) !important;
    border-top-color: var(--hx-border-level-1-color) !important;
  }
}
</style>