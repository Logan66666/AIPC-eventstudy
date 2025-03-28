<template>
  <div class="financial-calendar card">
    <div class="calendar-header">
      <h2 class="card-title tertiary-title">财经日历</h2>
      <div class="card-subtitle">重要经济数据与财报发布安排</div>
      
      <div class="date-selector">
        <button class="date-nav prev" @click="navigateMonth(-1)">
          <span class="nav-icon">←</span>
        </button>
        <div class="current-date">{{ currentYearMonth }}</div>
        <button class="date-nav next" @click="navigateMonth(1)">
          <span class="nav-icon">→</span>
        </button>
      </div>
    </div>
    
    <div class="calendar-content">
      <!-- 星期表头 -->
      <div class="calendar-weekdays">
        <div class="weekday" v-for="day in weekDays" :key="day">{{ day }}</div>
      </div>
      
      <!-- 日历网格 -->
      <div class="calendar-grid">
        <div 
          v-for="(day, index) in calendarDays" 
          :key="index"
          class="calendar-day"
          :class="{
            'other-month': day.isOtherMonth,
            'has-events': day.events.length > 0,
            'today': isToday(day.date)
          }"
          @click="selectDay(day)"
        >
          <div class="day-number">{{ day.dayNumber }}</div>
          <div class="day-events" v-if="day.events.length > 0">
            <div 
              v-for="(event, eventIndex) in day.events.slice(0, 2)" 
              :key="eventIndex"
              class="event-dot"
              :class="getImportanceClass(event.importance)"
            >
              {{ event.title }}
            </div>
            <div v-if="day.events.length > 2" class="more-events">
              +{{ day.events.length - 2 }}
            </div>
          </div>
        </div>
      </div>
      
      <!-- 选中日期的事件详情 -->
      <div class="events-detail" v-if="selectedDay && selectedDay.events.length > 0">
        <div class="detail-header">
          <h3>{{ formatSelectedDate(selectedDay.date) }} 事件详情</h3>
        </div>
        <div class="event-list">
          <div 
            v-for="(event, index) in selectedDay.events" 
            :key="index"
            class="event-item"
            :class="getImportanceClass(event.importance)"
          >
            <div class="event-time">{{ event.time }}</div>
            <div class="event-info">
              <div class="event-title">{{ event.title }}</div>
              <div class="event-description">{{ event.description }}</div>
              <div class="event-meta">
                <span class="event-country">{{ event.country }}</span>
                <span class="event-importance">{{ getImportanceText(event.importance) }}</span>
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
  name: 'FinancialCalendar',
  data() {
    return {
      currentDate: new Date(),
      selectedDay: null,
      weekDays: ['日', '一', '二', '三', '四', '五', '六'],
      events: [
        {
          date: new Date(2024, 2, 3),
          time: '20:45',
          title: '欧洲行情利率决议',
          description: '预期维持利率不变，关注政策前瞻指引',
          country: '欧元区',
          importance: 'high'
        },
        {
          date: new Date(2024, 2, 3),
          time: '22:00',
          title: '欧元区CPI数据',
          description: '预期同比增长4.1%，环比增长0.3%',
          country: '欧元区',
          importance: 'medium'
        },
        {
          date: new Date(2024, 2, 4),
          time: '11:00',
          title: '日本央行利率决议',
          description: '预期维持利率不变，关注通胀预期',
          country: '日本',
          importance: 'high'
        },
        {
          date: new Date(2024, 2, 5),
          time: '09:30',
          title: '中国PMI数据',
          description: '预期制造业PMI 50.2，服务业PMI 51.0',
          country: '中国',
          importance: 'high'
        }
      ]
    }
  },
  computed: {
    currentYearMonth() {
      return `${this.currentDate.getFullYear()}年${this.currentDate.getMonth() + 1}月`;
    },
    calendarDays() {
      const year = this.currentDate.getFullYear();
      const month = this.currentDate.getMonth();
      const firstDay = new Date(year, month, 1);
      const lastDay = new Date(year, month + 1, 0);
      
      const days = [];
      
      // 添加上个月的日期
      const firstDayWeekDay = firstDay.getDay();
      for (let i = firstDayWeekDay - 1; i >= 0; i--) {
        const date = new Date(year, month, -i);
        days.push({
          date,
          dayNumber: date.getDate(),
          isOtherMonth: true,
          events: this.getEventsForDate(date)
        });
      }
      
      // 添加当前月的日期
      for (let i = 1; i <= lastDay.getDate(); i++) {
        const date = new Date(year, month, i);
        days.push({
          date,
          dayNumber: i,
          isOtherMonth: false,
          events: this.getEventsForDate(date)
        });
      }
      
      // 添加下个月的日期
      const remainingDays = 42 - days.length; // 6行7列
      for (let i = 1; i <= remainingDays; i++) {
        const date = new Date(year, month + 1, i);
        days.push({
          date,
          dayNumber: i,
          isOtherMonth: true,
          events: this.getEventsForDate(date)
        });
      }
      
      return days;
    }
  },
  methods: {
    navigateMonth(direction) {
      const newDate = new Date(this.currentDate);
      newDate.setMonth(newDate.getMonth() + direction);
      this.currentDate = newDate;
      this.selectedDay = null;
    },
    selectDay(day) {
      this.selectedDay = day;
    },
    getEventsForDate(date) {
      return this.events.filter(event => 
        event.date.getDate() === date.getDate() &&
        event.date.getMonth() === date.getMonth() &&
        event.date.getFullYear() === date.getFullYear()
      );
    },
    isToday(date) {
      const today = new Date();
      return date.getDate() === today.getDate() &&
             date.getMonth() === today.getMonth() &&
             date.getFullYear() === today.getFullYear();
    },
    formatSelectedDate(date) {
      return `${date.getMonth() + 1}月${date.getDate()}日`;
    },
    getImportanceClass(importance) {
      return {
        'importance-high': importance === 'high',
        'importance-medium': importance === 'medium',
        'importance-low': importance === 'low'
      };
    },
    getImportanceText(importance) {
      switch(importance) {
        case 'high': return '高重要性';
        case 'medium': return '中等重要性';
        case 'low': return '低重要性';
        default: return '';
      }
    }
  }
}
</script>

<style scoped lang="scss">
.financial-calendar {
  height: 100%;
  display: flex;
  flex-direction: column;
  
  .calendar-header {
    margin-bottom: var(--spacing-md);
    
    .date-selector {
      display: flex;
      align-items: center;
      margin-top: var(--spacing-md);
      background-color: rgba(255, 255, 255, 0.03);
      border-radius: var(--radius-lg);
      padding: 6px 10px;
      
      .date-nav {
        background: none;
        border: none;
        color: var(--text-secondary);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 28px;
        height: 28px;
        border-radius: var(--radius-sm);
        transition: all 0.2s ease;
        
        &:hover {
          background-color: rgba(255, 255, 255, 0.1);
          color: var(--text-primary);
        }
      }
      
      .current-date {
        flex: 1;
        text-align: center;
        font-weight: 500;
        font-size: 14px;
        color: var(--text-primary);
      }
    }
  }
  
  .calendar-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
  }
  
  .calendar-weekdays {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
    font-size: 13px;
    color: var(--text-tertiary);
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: var(--spacing-sm);
  }
  
  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 1px;
    background-color: var(--border-subtle);
    border-radius: var(--radius-sm);
    overflow: hidden;
    
    .calendar-day {
      background-color: var(--bg-card);
      aspect-ratio: 1;
      padding: var(--spacing-sm);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: all 0.2s ease;
      
      &:hover {
        background-color: var(--bg-card-light);
      }
      
      &.other-month {
        opacity: 0.5;
      }
      
      &.today {
        .day-number {
          color: var(--color-primary);
          font-weight: 600;
        }
      }
      
      &.has-events {
        background-color: rgba(255, 149, 0, 0.05);
      }
      
      .day-number {
        font-size: 13px;
        color: var(--text-secondary);
      }
      
      .day-events {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 2px;
        font-size: 11px;
        
        .event-dot {
          padding: 2px 4px;
          border-radius: 2px;
          color: var(--text-primary);
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          
          &.importance-high {
            background-color: rgba(239, 68, 68, 0.2);
          }
          
          &.importance-medium {
            background-color: rgba(251, 191, 36, 0.2);
          }
          
          &.importance-low {
            background-color: rgba(74, 222, 128, 0.2);
          }
        }
        
        .more-events {
          font-size: 10px;
          color: var(--text-tertiary);
          text-align: center;
        }
      }
    }
  }
  
  .events-detail {
    background-color: var(--bg-card-light);
    border-radius: var(--radius-sm);
    padding: var(--spacing-md);
    
    .detail-header {
      margin-bottom: var(--spacing-md);
      
      h3 {
        font-size: 14px;
        font-weight: 600;
        color: var(--text-primary);
        margin: 0;
      }
    }
    
    .event-list {
      display: flex;
      flex-direction: column;
      gap: var(--spacing-sm);
      
      .event-item {
        display: flex;
        gap: var(--spacing-md);
        padding: var(--spacing-sm);
        border-radius: var(--radius-sm);
        
        &.importance-high {
          background-color: rgba(239, 68, 68, 0.1);
        }
        
        &.importance-medium {
          background-color: rgba(251, 191, 36, 0.1);
        }
        
        &.importance-low {
          background-color: rgba(74, 222, 128, 0.1);
        }
        
        .event-time {
          font-size: 13px;
          font-weight: 600;
          color: var(--text-primary);
          min-width: 56px;
        }
        
        .event-info {
          flex: 1;
          
          .event-title {
            font-size: 14px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 4px;
          }
          
          .event-description {
            font-size: 13px;
            color: var(--text-secondary);
            margin-bottom: 8px;
          }
          
          .event-meta {
            display: flex;
            gap: 8px;
            
            span {
              font-size: 12px;
              padding: 2px 8px;
              border-radius: 12px;
              background-color: rgba(255, 255, 255, 0.05);
              color: var(--text-tertiary);
            }
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .financial-calendar {
    .calendar-grid {
      .calendar-day {
        padding: 4px;
        
        .day-number {
          font-size: 12px;
        }
        
        .day-events {
          font-size: 10px;
        }
      }
    }
    
    .events-detail {
      padding: var(--spacing-sm);
      
      .event-item {
        flex-direction: column;
        gap: var(--spacing-sm);
        
        .event-time {
          font-size: 12px;
        }
        
        .event-info {
          .event-title {
            font-size: 13px;
          }
          
          .event-description {
            font-size: 12px;
          }
        }
      }
    }
  }
}
</style> 