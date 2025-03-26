<template>
  <div class="card financial-calendar">
    <div class="calendar-header">
      <div class="title-area">
        <h2 class="card-title">财经日历</h2>
        <p class="card-subtitle">重要财经事件日历</p>
      </div>
      
      <div class="calendar-controls">
        <button class="calendar-nav prev" @click="prevMonth">
          <span class="nav-icon">&#10094;</span>
        </button>
        <span class="calendar-current">{{ currentYearMonth }}</span>
        <button class="calendar-nav next" @click="nextMonth">
          <span class="nav-icon">&#10095;</span>
        </button>
      </div>
    </div>
    
    <div class="calendar-grid">
      <div class="weekday-header">
        <div v-for="day in weekDays" :key="day" class="weekday-cell">{{ day }}</div>
      </div>
      
      <div class="days-grid">
        <div 
          v-for="(day, index) in calendarDays" 
          :key="index"
          :class="[
            'day-cell', 
            { 'prev-month': day.isPrevMonth },
            { 'next-month': day.isNextMonth },
            { 'today': day.isToday },
            { 'has-events': day.events.length > 0 },
            { 'selected': selectedDate === day.fullDate }
          ]"
          @click="selectDate(day)"
        >
          <div class="day-number">{{ day.day }}</div>
          <div class="day-events">
            <div 
              v-for="(event, eventIndex) in day.events.slice(0, 2)" 
              :key="eventIndex" 
              :class="['event-tag', event.type]"
            >
              {{ event.title }}
            </div>
            <div v-if="day.events.length > 2" class="more-events">
              +{{ day.events.length - 2 }}
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 选中日期详情 -->
    <div v-if="selectedDay && selectedDay.fullDate" class="selected-day-details">
      <div class="selected-day-header">
        <span>{{ selectedDay.fullDate }} 事件</span>
        <button class="close-btn" @click="closeDetails">×</button>
      </div>
      <div v-if="selectedDay.events.length > 0" class="selected-day-events">
        <div 
          v-for="(event, index) in selectedDay.events" 
          :key="index" 
          :class="['event-detail', event.type]"
        >
          <span class="event-time">{{ event.time }}</span>
          <div class="event-content">
            <div class="event-title">{{ event.title }}</div>
            <div class="event-description">{{ event.description }}</div>
          </div>
        </div>
      </div>
      <div v-else class="no-events">
        当日无重要事件
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FinancialCalendar',
  data() {
    return {
      currentDate: new Date(),
      weekDays: ['日', '一', '二', '三', '四', '五', '六'],
      events: [
        { 
          date: '2023-03-01', 
          time: '22:00', 
          title: '美国ISM制造业PMI', 
          description: '预期46.9，前值47.4，关注就业和价格分项',
          type: 'economic'
        },
        { 
          date: '2023-03-02', 
          time: '20:45', 
          title: '欧洲央行利率决议', 
          description: '预期加息50个基点至3.00%，关注后续加息路径指引',
          type: 'policy'
        },
        { 
          date: '2023-03-03', 
          time: '11:00', 
          title: '日本央行利率决议', 
          description: '预期维持-0.1%不变，关注收益率曲线控制政策',
          type: 'policy'
        },
        { 
          date: '2023-03-08', 
          time: '09:30', 
          title: '中国CPI、PPI', 
          description: '预计CPI同比增长1.9%，PPI同比下降1.3%',
          type: 'economic'
        },
        { 
          date: '2023-03-09', 
          time: '21:30', 
          title: '美国非农就业数据', 
          description: '预期新增20.5万人，失业率3.4%',
          type: 'economic'
        },
        { 
          date: '2023-03-12', 
          time: '21:30', 
          title: '美国CPI数据', 
          description: '预期同比6.2%，核心CPI同比5.5%',
          type: 'economic'
        },
        { 
          date: '2023-03-14', 
          time: '20:45', 
          title: '欧洲央行利率决议', 
          description: '预期加息25个基点，关注后续指引',
          type: 'policy'
        },
        { 
          date: '2023-03-16', 
          time: '09:20', 
          title: '中国MLF操作', 
          description: '关注操作量和利率变化',
          type: 'policy'
        },
        { 
          date: '2023-03-16', 
          time: '02:00', 
          title: '美联储FOMC会议', 
          description: '预期加息25个基点，关注点阵图变化',
          type: 'policy'
        },
        { 
          date: '2023-03-17', 
          time: '17:45', 
          title: '腾讯业绩发布', 
          description: '预期营收增长缓慢，利润可能回升',
          type: 'business'
        },
        { 
          date: '2023-03-19', 
          time: '16:30', 
          title: '平台业绩发布', 
          description: '关注用户增长和商业化进展',
          type: 'business'
        },
        { 
          date: '2023-03-22', 
          time: '09:30', 
          title: '中国PMI数据', 
          description: '制造业PMI预期50.2，非制造业PMI预期54.0',
          type: 'economic'
        },
        { 
          date: '2023-03-24', 
          time: '09:15', 
          title: 'LPR报价发布', 
          description: '预期1年期和5年期LPR保持不变',
          type: 'policy'
        },
        { 
          date: '2023-03-27', 
          time: '17:00', 
          title: '工商银行业绩', 
          description: '关注资产质量和净息差变化',
          type: 'business'
        },
        { 
          date: '2023-03-30', 
          time: '20:30', 
          title: '美国GDP终值', 
          description: '预期年化环比增长2.7%',
          type: 'economic'
        }
      ],
      selectedDate: null,
      selectedDay: null
    }
  },
  computed: {
    currentYearMonth() {
      return `${this.currentDate.getFullYear()}年${this.currentDate.getMonth() + 1}月`
    },
    calendarDays() {
      const year = this.currentDate.getFullYear()
      const month = this.currentDate.getMonth()
      
      // 当月第一天是星期几（0-6，0是周日）
      const firstDay = new Date(year, month, 1).getDay()
      
      // 当月最后一天是几号
      const lastDate = new Date(year, month + 1, 0).getDate()
      
      // 上个月的最后几天
      const prevMonthLastDate = new Date(year, month, 0).getDate()
      const prevMonthDays = []
      for (let i = 0; i < firstDay; i++) {
        const day = prevMonthLastDate - firstDay + i + 1
        const prevMonth = month === 0 ? 11 : month - 1
        const prevYear = month === 0 ? year - 1 : year
        const dateStr = `${prevYear}-${String(prevMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`
        const dayEvents = this.events.filter(event => event.date === dateStr)
        
        prevMonthDays.push({
          day,
          fullDate: dateStr,
          isPrevMonth: true,
          isNextMonth: false,
          isToday: false,
          events: dayEvents
        })
      }
      
      // 当月的天数
      const currentMonthDays = []
      const today = new Date()
      const isCurrentMonth = today.getFullYear() === year && today.getMonth() === month
      
      for (let i = 1; i <= lastDate; i++) {
        const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`
        const dayEvents = this.events.filter(event => event.date === dateStr)
        
        currentMonthDays.push({
          day: i,
          fullDate: dateStr,
          isPrevMonth: false,
          isNextMonth: false,
          isToday: isCurrentMonth && today.getDate() === i,
          events: dayEvents
        })
      }
      
      // 下个月的前几天
      const nextMonthDays = []
      const totalDays = prevMonthDays.length + currentMonthDays.length
      const remainingDays = 42 - totalDays // 6行7列 = 42天
      
      for (let i = 1; i <= remainingDays; i++) {
        const nextMonth = month === 11 ? 0 : month + 1
        const nextYear = month === 11 ? year + 1 : year
        const dateStr = `${nextYear}-${String(nextMonth + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`
        const dayEvents = this.events.filter(event => event.date === dateStr)
        
        nextMonthDays.push({
          day: i,
          fullDate: dateStr,
          isPrevMonth: false,
          isNextMonth: true,
          isToday: false,
          events: dayEvents
        })
      }
      
      return [...prevMonthDays, ...currentMonthDays, ...nextMonthDays]
    }
  },
  methods: {
    prevMonth() {
      const newDate = new Date(this.currentDate)
      newDate.setMonth(newDate.getMonth() - 1)
      this.currentDate = newDate
      this.selectedDate = null
      this.selectedDay = null
    },
    nextMonth() {
      const newDate = new Date(this.currentDate)
      newDate.setMonth(newDate.getMonth() + 1)
      this.currentDate = newDate
      this.selectedDate = null
      this.selectedDay = null
    },
    selectDate(day) {
      this.selectedDate = day.fullDate
      this.selectedDay = day
    },
    closeDetails() {
      this.selectedDate = null
      this.selectedDay = null
    }
  },
  mounted() {
    // 初始化选中今天
    const today = new Date()
    const dateStr = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`
    this.selectedDate = dateStr
    
    // 找到今天对应的日期对象
    const todayObj = this.calendarDays.find(day => day.isToday)
    if (todayObj) {
      this.selectedDay = todayObj
    }
  }
}
</script>

<style lang="scss" scoped>
.financial-calendar {
  position: relative;
  overflow: hidden;
  min-height: 500px;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
}

.calendar-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.calendar-nav {
  background: transparent;
  border: 1px solid var(--hx-border-level-1-color);
  color: var(--hx-text-color-secondary);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
  
  .nav-icon {
    font-size: 12px;
    line-height: 1;
  }
}

.calendar-current {
  font-size: 16px;
  font-weight: 500;
  color: var(--hx-text-color-primary);
}

.calendar-grid {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
}

.weekday-header {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  background-color: rgba(255, 255, 255, 0.05);
  
  .weekday-cell {
    padding: 10px;
    text-align: center;
    font-weight: 500;
    font-size: 14px;
    color: var(--hx-text-color-tertiary);
  }
}

.days-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: minmax(80px, auto);
  background-color: rgba(255, 255, 255, 0.02);
  gap: 1px;
}

.day-cell {
  position: relative;
  padding: 8px;
  background-color: rgba(255, 255, 255, 0.03);
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.2s;
  min-height: 85px;
  
  &:hover {
    background-color: rgba(255, 255, 255, 0.05);
  }
  
  &.prev-month, &.next-month {
    opacity: 0.5;
    
    .day-number {
      color: var(--hx-text-color-quaternary);
    }
  }
  
  &.today {
    background-color: rgba(0, 113, 227, 0.15);
    
    .day-number {
      background-color: var(--hx-brand-color-1);
      color: #fff;
      border-radius: 50%;
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
    }
  }
  
  &.selected {
    border-color: var(--hx-brand-color-1);
    background-color: rgba(0, 113, 227, 0.1);
  }
  
  &.has-events {
    .day-number {
      font-weight: 600;
    }
  }
}

.day-number {
  font-size: 14px;
  margin-bottom: 4px;
  color: var(--hx-text-color-secondary);
}

.day-events {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 12px;
}

.event-tag {
  padding: 2px 6px;
  border-radius: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 11px;
  
  &.economic {
    background-color: rgba(83, 177, 117, 0.2);
    color: #53b175;
  }
  
  &.policy {
    background-color: rgba(0, 113, 227, 0.2);
    color: #0071e3;
  }
  
  &.business {
    background-color: rgba(255, 159, 10, 0.2);
    color: #ff9f0a;
  }
}

.more-events {
  font-size: 11px;
  color: var(--hx-text-color-tertiary);
  text-align: center;
}

.selected-day-details {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: var(--hx-bg-color-container);
  border-top: 1px solid var(--hx-border-level-1-color);
  padding: 16px;
  z-index: 10;
  border-radius: 16px 16px 0 0;
  box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.1);
  animation: slideUp 0.3s forwards;
}

.selected-day-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  font-weight: 600;
  color: var(--hx-text-color-primary);
}

.close-btn {
  background: transparent;
  border: none;
  color: var(--hx-text-color-tertiary);
  font-size: 20px;
  cursor: pointer;
}

.selected-day-events {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-height: 200px;
  overflow-y: auto;
}

.event-detail {
  display: flex;
  gap: 12px;
  padding: 8px;
  border-radius: 8px;
  
  &.economic {
    background-color: rgba(83, 177, 117, 0.1);
  }
  
  &.policy {
    background-color: rgba(0, 113, 227, 0.1);
  }
  
  &.business {
    background-color: rgba(255, 159, 10, 0.1);
  }
}

.event-time {
  font-weight: 500;
  color: var(--hx-text-color-secondary);
  white-space: nowrap;
}

.event-content {
  flex: 1;
  
  .event-title {
    font-weight: 500;
    margin-bottom: 4px;
    color: var(--hx-text-color-primary);
  }
  
  .event-description {
    font-size: 12px;
    color: var(--hx-text-color-tertiary);
  }
}

.no-events {
  text-align: center;
  padding: 12px;
  color: var(--hx-text-color-tertiary);
}

@keyframes slideUp {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}
</style> 