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

export default {
  name: 'FinancialCalendar',
  components: {
    FullCalendar,
    DropdownSelect
  },
  data() {
    // 获取当前日期
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();
    
    return {
      currentDate: new Date(),
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
        firstDay: 0, // 将周日设为一周的第一天
        dayMaxEvents: 3, // 每天最多显示的事件数
        height: 'auto',
        eventClick: this.handleEventClick,
        eventDisplay: 'block',
        eventTimeFormat: {
          hour: '2-digit',
          minute: '2-digit',
          meridiem: false,
          hour12: false
        },
        dayHeaderFormat: { weekday: 'short' },
        events: [],
        // 给表格添加类，以便更好控制样式
        viewClassNames: 'fc-custom-view',
        dayHeaderClassNames: 'fc-custom-header',
        dayCellClassNames: 'fc-custom-cell',
        // 头部工具栏类
        headerToolbarOptions: {
          classNames: 'fc-custom-toolbar'
        },
        // 移除默认边框
        borderColor: 'transparent',
        // 完全控制表格背景
        slotLabelClassNames: 'fc-custom-slot-label',
        dayCellDidMount: function(info) {
          if (info.isToday) {
            info.el.classList.add('custom-today-cell');
            // 只设置背景色，不添加装饰
            info.el.style.backgroundColor = 'rgba(var(--hx-brand-color-rgb, 59, 130, 246), 0.08)';
          } else {
            // 强制设置背景色
            info.el.style.backgroundColor = 'var(--hx-bg-color-container)';
          }
        },
        // 添加视图挂载事件处理
        viewDidMount: function(arg) {
          // 设置视图背景
          arg.el.style.backgroundColor = 'var(--hx-bg-color-container)';
          
          // 强制设置表头背景色
          const headers = arg.el.querySelectorAll('.fc-col-header, .fc-col-header-cell');
          headers.forEach(header => {
            header.style.backgroundColor = 'var(--hx-bg-color-specialcomponent)';
          });
          
          // 修复表体背景
          const bodyCells = arg.el.querySelectorAll('.fc-daygrid-body, .fc-scrollgrid, .fc-scrollgrid-section');
          bodyCells.forEach(cell => {
            cell.style.backgroundColor = 'var(--hx-bg-color-container)';
          });
        }
      },
      rawEvents: [
        // 4月份数据
        {
          date: new Date(currentYear, currentMonth, 1),
          title: '中国制造业PMI数据',
          description: '预期51.2，前值50.8，关注制造业景气度变化',
          importance: 3, // 高重要性
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 1),
          title: '美国ISM制造业指数',
          description: '预期48.5，前值47.8，关注制造业回暖情况',
          importance: 3,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 2),
          title: '日本央行会议纪要',
          description: '关注货币政策变化信号，通胀预期调整',
          importance: 2, // 中等重要性
          category: '政策'
        },
        {
          date: new Date(currentYear, currentMonth, 3),
          title: '韩国CPI数据',
          description: '预期同比增长2.2%，关注通胀趋势',
          importance: 1, // 低重要性
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 4),
          title: '德国工业产出数据',
          description: '预期环比增长0.3%，关注经济复苏势头',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 5),
          title: '美国非农就业数据',
          description: '预期新增就业18.5万，前值27.5万，关注就业市场变化',
          importance: 3,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 8),
          title: '中国贸易数据',
          description: '预期出口同比增长7.5%，进口增长5.2%',
          importance: 2,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 9),
          title: '法国工业信心调查',
          description: '预期指数101.5，前值100.2，关注企业信心变化',
          importance: 1,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 10),
          title: '美国CPI数据',
          description: '预期同比3.4%，前值3.2%，通胀是否重新抬头',
          importance: 3,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 10),
          title: '美国原油库存数据',
          description: '预期减少100万桶，前值增加400万桶',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 11),
          title: '欧洲央行利率决议',
          description: '预期维持利率不变，关注降息前瞻指引',
          importance: 3,
          category: '政策'
        },
        {
          date: new Date(currentYear, currentMonth, 12),
          title: '英国GDP数据',
          description: '预期季度增长0.2%，关注经济增长动力',
          importance: 3,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 15),
          title: '中国GDP一季度数据',
          description: '预期同比增长5.2%，关注经济复苏情况',
          importance: 3,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 15),
          title: '中国零售销售数据',
          description: '预期同比增长5.5%，关注消费复苏情况',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 16),
          title: '日本贸易数据',
          description: '预期出口增长7.8%，进口增长2.3%',
          importance: 2,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 17),
          title: '欧元区CPI终值',
          description: '预期同比2.4%，核心CPI 2.9%',
          importance: 2,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 18),
          title: '腾讯控股财报',
          description: '2023年Q4及全年业绩，关注增长情况',
          importance: 2,
          category: '公司'
        },
        {
          date: new Date(currentYear, currentMonth, 18),
          title: '欧元区消费者信心初值',
          description: '预期指数-15.0，前值-15.5',
          importance: 1,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 19),
          title: '德国PPI数据',
          description: '预期同比-2.8%，前值-3.1%',
          importance: 1,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 20),
          title: '特斯拉财报',
          description: '2024年Q1财报，关注销量和利润',
          importance: 2,
          category: '公司'
        },
        {
          date: new Date(currentYear, currentMonth, 20),
          title: '加拿大零售销售数据',
          description: '预期环比增长0.3%，前值0.1%',
          importance: 1,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 22),
          title: '美国服务业PMI初值',
          description: '预期53.0，前值52.3，关注服务业景气度',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 22),
          title: '欧元区服务业PMI初值',
          description: '预期52.5，前值51.5，关注经济活动情况',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 23),
          title: '英国服务业PMI初值',
          description: '预期52.8，前值52.9，关注经济走势',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 24),
          title: '美国耐用品订单',
          description: '预期环比增长0.5%，前值1.2%',
          importance: 2,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 25),
          title: '微软财报',
          description: '2024年Q1财报，关注AI业务增长',
          importance: 2,
          category: '公司'
        },
        {
          date: new Date(currentYear, currentMonth, 25),
          title: '谷歌财报',
          description: '2024年Q1财报，关注广告业务和云服务',
          importance: 2,
          category: '公司'
        },
        {
          date: new Date(currentYear, currentMonth, 26),
          title: '美国GDP初值',
          description: '预期年化季环比2.0%，前值3.4%',
          importance: 3,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, 26),
          title: '苹果财报',
          description: '2024年Q2财报，关注iPhone销量和服务业务',
          importance: 3,
          category: '公司'
        },
        {
          date: new Date(currentYear, currentMonth, 28),
          title: '美国PCE物价指数',
          description: '美联储首选通胀指标，关注通胀走势',
          importance: 3,
          category: '政策'
        },
        {
          date: new Date(currentYear, currentMonth, 29),
          title: '中国官方PMI数据',
          description: '预期制造业PMI 51.5，服务业PMI 52.0',
          importance: 3,
          category: '行业'
        },
        {
          date: new Date(currentYear, currentMonth, 30),
          title: '欧元区GDP初值',
          description: '预期季度增长0.1%，同比增长0.4%',
          importance: 3,
          category: '全球'
        },
        // 为当日特别添加数据
        {
          date: new Date(currentYear, currentMonth, currentDate.getDate()),
          title: '今日特别数据',
          description: '这是针对今天特别添加的数据，会随日期变化',
          importance: 3,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, currentDate.getDate()),
          title: '今日市场焦点',
          description: '当前市场关注的热点事件和数据',
          importance: 2,
          category: '全球'
        },
        {
          date: new Date(currentYear, currentMonth, currentDate.getDate()),
          title: '今日政策动向',
          description: '重要经济政策和监管变化',
          importance: 2,
          category: '政策'
        }
      ],
      selectedCategories: [], // 已选类别
    }
  },
  computed: {
    // 增加类别选项计算属性
    categoryOptions() {
      return [
        { label: '全球', value: '全球', badgeClass: 'global' },
        { label: '政策', value: '政策', badgeClass: 'policy' },
        { label: '行业', value: '行业', badgeClass: 'industry' },
        { label: '公司', value: '公司', badgeClass: 'company' }
      ];
    },
    
    // 根据选中类别过滤事件
    filteredEvents() {
      if (this.selectedCategories.length === 0) {
        return this.rawEvents; // 未选择时显示所有事件
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
  },
  mounted() {
    this.initCalendar();
    
    // 延迟执行，等待日历渲染完成
    setTimeout(() => {
      this.fixHeaderBorder();
      this.adjustEmptyRows();
      this.fixBorderGaps();
      this.fixCalendarBackground(); // 添加新方法
    }, 100);
  },
  methods: {
    initCalendar() {
      this.initCalendarWithEvents(this.filteredEvents);
    },
    initCalendarWithEvents(eventsToShow) {
      // 将事件数据转换为FullCalendar格式
      const events = eventsToShow.map(event => {
        // 根据类别设置左侧边框颜色，而不是根据重要性
        let borderColor, textColor = 'var(--hx-text-color-primary)';
        
        // 根据事件类别设置颜色
        switch(event.category) {
          case '全球':
            borderColor = 'var(--hx-brand-color-3)'; // 蓝色
            break;
          case '政策':
            borderColor = 'var(--hx-warning-color-3)'; // 黄色
            break;
          case '行业':
            borderColor = 'var(--hx-sec-brand-color-3)'; // 红色
            break;
          case '公司':
            borderColor = 'var(--hx-success-color-3)'; // 绿色
            break;
          default:
            borderColor = 'var(--hx-gray-color-6)';
        }
        
        // 格式化日期
        const year = event.date.getFullYear();
        const month = String(event.date.getMonth() + 1).padStart(2, '0');
        const day = String(event.date.getDate()).padStart(2, '0');
        const dateStr = `${year}-${month}-${day}`;
        
        // 在标题前添加类别标识
        const displayTitle = `${event.category} | ${event.title}`;
        
        return {
          title: displayTitle,
          start: dateStr,
          description: event.description,
          category: event.category,
          importance: event.importance,
          backgroundColor: 'transparent',
          borderColor: borderColor,
          textColor: textColor,
          extendedProps: {
            description: event.description,
            category: event.category,
            importance: event.importance,
            originalTitle: event.title
          }
        };
      });
      
      // 更新日历事件
      if (this.$refs.fullCalendar) {
        const calendarApi = this.$refs.fullCalendar.getApi();
        calendarApi.removeAllEvents();
        calendarApi.addEventSource(events);
      } else {
        this.calendarOptions.events = events;
      }
    },
    handleEventClick(info) {
      // 获取事件详情
      this.selectedEvent = {
        title: info.event.extendedProps.originalTitle,
        description: info.event.extendedProps.description,
        category: info.event.extendedProps.category,
        importance: info.event.extendedProps.importance
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
    updateCalendarEvents() {
      // 调用初始化日历方法，使用过滤后的事件
      this.initCalendarWithEvents(this.filteredEvents);
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
    }
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
      padding: 0 2px;
      margin-top: 2px;
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
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        font-weight: normal;
        padding: 0;
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
      
      .fc-popover-header {
        background-color: var(--hx-bg-color-specialcomponent);
        color: var(--hx-text-color-primary);
        padding: 6px 8px;
        font-size: 12px;
        border-bottom: 1px solid var(--hx-border-level-1-color);
        
        .fc-popover-title {
          color: var(--hx-text-color-primary);
          font-weight: 500;
        }
        
        .fc-popover-close {
          color: var(--hx-text-color-tertiary);
          font-size: 14px;
          
          &:hover {
            color: var(--hx-text-color-primary);
          }
        }
      }
      
      .fc-popover-body {
        padding: 6px;
        background-color: var(--hx-bg-color-container);
        
        .fc-event {
          margin: 2px 0;
        }
      }
    }
    
    /* 事件容器更紧凑 */
    .fc-daygrid-day-events {
      padding: 0 1px !important;
      margin-top: 0 !important;
      margin-bottom: 0 !important;
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