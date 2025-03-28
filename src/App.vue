<template>
  <div id="app" class="app-container">
    <!-- 页面标题 -->
    <header class="main-header">
      <div class="header-content">
        <div class="logo-container">
          <div class="logo-icon">A</div>
          <div class="title-container">
            <h1>股市头条</h1>
          </div>
        </div>
        
        <!-- 主题切换按钮 -->
        <div class="theme-switcher-container">
          <ThemeSwitcher @theme-changed="handleThemeChange"/>
        </div>
      </div>
    </header>

    <!-- 内容区域 -->
    <div class="content-container">
      <!-- 股市头条部分 -->
      <div class="grid-row">
        <StockHeadlines />
      </div>
      
      <!-- 世界经济和政策催化部分 -->
      <div class="grid-row two-columns">
        <WorldEconomy />
        <PolicyCatalysts />
      </div>
      
      <!-- 埋伏机会和行业焦点部分 -->
      <div class="grid-row two-columns">
        <InvestmentOpportunity />
        <IndustryFocus />
      </div>
      
      <!-- 其他组件部分 -->
      <div class="grid-row">
        <CustomChart />
      </div>
      
      <div class="grid-row">
        <CompanyNews />
      </div>
      
      <div class="grid-row">
        <FinancialCalendar />
      </div>
    </div>

  </div>
</template>

<script>
import ThemeSwitcher from './components/ui/ThemeSwitcher.vue'
import StockHeadlines from './components/StockHeadlines.vue'
import WorldEconomy from './components/WorldEconomy.vue'
import PolicyCatalysts from './components/PolicyCatalysts.vue'
import InvestmentOpportunity from './components/InvestmentOpportunity.vue'
import IndustryFocus from './components/IndustryFocus.vue'
import CustomChart from './components/CustomChart.vue'
import CompanyNews from './components/CompanyNews.vue'
import FinancialCalendar from './components/FinancialCalendar.vue'

export default {
  name: 'App',
  components: {
    ThemeSwitcher,
    StockHeadlines,
    WorldEconomy,
    PolicyCatalysts,
    InvestmentOpportunity,
    IndustryFocus,
    CustomChart,
    CompanyNews,
    FinancialCalendar
  },
  data() {
    return {
      currentTheme: 'default'
    }
  },
  methods: {
    handleThemeChange(theme) {
      // 移除当前主题
      document.documentElement.removeAttribute('data-theme');
      
      // 设置新主题
      if (theme !== 'default') {
        document.documentElement.setAttribute('data-theme', theme);
      }
      
      // 更新当前主题
      this.currentTheme = theme;
    }
  }
}
</script>

<style lang="scss">
:root {
  // 颜色系统
  --color-primary: #ff3b57;
  --color-secondary: #246bf8;
  --color-tertiary: #ff9500;
  --color-success: #00e676;
  --color-danger: #ff3b57;
  --color-warning: #ffbb00;
  --color-info: #0dcaf0;
  
  // RGB变量（用于透明度调整）
  --primary-rgb: 255, 59, 87;
  --secondary-rgb: 36, 107, 248;
  --tertiary-rgb: 255, 149, 0;
  --success-rgb: 0, 230, 118;
  --danger-rgb: 255, 59, 87;
  --warning-rgb: 255, 187, 0;
  --info-rgb: 13, 202, 240;
  
  // 背景色系统
  --bg-page: #0f1117;
  --bg-card: #1a202e;
  --bg-card-light: #242a38;
  --bg-highlight: rgba(255, 255, 255, 0.05);
  
  // 文字颜色
  --text-primary: #ffffff;
  --text-secondary: #a9b2c3;
  --text-tertiary: #6b7897;
  
  // 边框色
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(255, 255, 255, 0.15);
  
  // 尺寸变量
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  // 投影
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 8px 30px rgba(0, 0, 0, 0.3);
  
  // 圆角
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  
  // 过渡时间
  --transition-fast: 0.2s;
  --transition-normal: 0.3s;
  --transition-slow: 0.5s;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  color: var(--text-primary);
  background-color: var(--bg-page);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  
  .content-container {
    padding: var(--spacing-lg);
    display: grid;
    gap: var(--spacing-lg);
    
    .grid-row {
      display: grid;
      gap: var(--spacing-lg);
      
      &.two-columns {
        grid-template-columns: repeat(2, 1fr);
      }
      
      // 添加响应式布局
      @media (max-width: 1024px) {
        &.two-columns {
          grid-template-columns: 1fr;
        }
      }
    }
  }
}

.main-header {
  background-color: var(--bg-card);
  padding: var(--spacing-md) var(--spacing-lg);
  box-shadow: var(--shadow-sm);
  position: sticky;
  top: 0;
  z-index: 100;
  
  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
    width: 100%;
  }
  
  .logo-container {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
  }
  
  .logo-icon {
    width: 36px;
    height: 36px;
    border-radius: var(--radius-sm);
    background: var(--color-primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
  }
  
  .title-container {
    h1 {
      font-size: 20px;
      font-weight: 600;
      margin-bottom: 2px;
    }
    
    p {
      font-size: 12px;
      color: var(--text-secondary);
      margin: 0;
    }
  }
}

.content-container {
  flex: 1;
  padding: var(--spacing-lg) var(--spacing-md);
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-lg);
}

.grid-row {
  display: grid;
  gap: var(--spacing-md);
  
  &.main-row {
    grid-template-columns: 1fr;
  }
  
  &.split-row {
    grid-template-columns: repeat(2, 1fr);
  }
}

.card {
  background-color: var(--bg-card);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  padding: var(--spacing-md);
  
  &.full-width {
    width: 100%;
  }
  
  .card-title {
    font-size: 18px;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: var(--spacing-sm);
    color: var(--text-primary);
    display: flex;
    align-items: center;
    
    &:before {
      content: "";
      display: inline-block;
      width: 3px;
      height: 18px;
      margin-right: var(--spacing-sm);
      border-radius: 2px;
    }
    
    &.primary-title:before {
      background: var(--color-primary);
    }
    
    &.secondary-title:before {
      background: var(--color-secondary);
    }
    
    &.tertiary-title:before {
      background: var(--color-tertiary);
    }
  }
  
  .card-subtitle {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 0;
    margin-bottom: var(--spacing-md);
    padding-left: calc(3px + var(--spacing-sm));
  }
}

.main-footer {
  background-color: var(--bg-card);
  color: var(--text-tertiary);
  padding: var(--spacing-md);
  text-align: center;
  font-size: 12px;
  border-top: 1px solid var(--border-subtle);
  
  p {
    margin: 0;
  }
}

// 响应式调整
@media (max-width: 1200px) {
  .content-container {
    padding: var(--spacing-md);
  }
}

@media (max-width: 992px) {
  .grid-row {
    &.split-row {
      grid-template-columns: 1fr;
    }
  }
}

@media (max-width: 768px) {
  .main-header {
    padding: var(--spacing-sm) var(--spacing-md);
    
    .logo-icon {
      width: 32px;
      height: 32px;
      font-size: 18px;
    }
    
    .title-container {
      h1 {
        font-size: 18px;
      }
    }
  }
  
  .content-container {
    padding: var(--spacing-md) var(--spacing-sm);
  }
  
  .card {
    padding: var(--spacing-sm);
  }
}
</style>
