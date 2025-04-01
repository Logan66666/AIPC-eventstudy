<template>
  <div id="app" class="app-container">
    <!-- 页面标题 -->
    <header class="main-header">
      <div class="header-content">
        <div class="logo-container">
          <div class="title-container">
            <h1>A股事件</h1>
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
      
      <!-- 埋伏机会和风险预警部分 -->
      <div class="grid-row two-columns">
        <InvestmentOpportunity />
        <RiskWarning />
      </div>

      <!-- 财经日历部分 -->
      <div class="grid-row">
        <FinancialCalendar />
      </div>

      <!-- 世界经济和政策催化部分 -->
      <div class="grid-row two-columns">
        <WorldEconomy />
        <PolicyCatalysts />
      </div>
      
      <!-- 行业焦点和公司新闻部分 -->
      <div class="grid-row two-columns">
        <IndustryFocus />
        <CompanyNews />
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
import CompanyNews from './components/CompanyNews.vue'
import FinancialCalendar from './components/FinancialCalendar.vue'
import RiskWarning from './components/RiskWarning.vue'

export default {
  name: 'App',
  components: {
    ThemeSwitcher,
    StockHeadlines,
    WorldEconomy,
    PolicyCatalysts,
    InvestmentOpportunity,
    IndustryFocus,
    CompanyNews,
    FinancialCalendar,
    RiskWarning
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
.app-container {
  min-height: 100vh;
  background-color: var(--hx-bg-color-page);
  color: var(--hx-text-color-primary);
  font: var(--hx-font-body-medium);
  
  .content-container {
    padding: var(--hx-size-6);
    display: grid;
    gap: var(--hx-size-6);
    
    .grid-row {
      display: grid;
      gap: var(--hx-size-6);
      
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
  background-color: var(--hx-bg-color-container);
  padding: var(--hx-comp-paddingTB-m) var(--hx-comp-paddingLR-l);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
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
    gap: var(--hx-size-2);
  }
  
  .logo-icon {
    width: var(--hx-comp-size-m);
    height: var(--hx-comp-size-m);
    border-radius: var(--hx-radius-small);
    background: var(--hx-brand-color-3);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font: var(--hx-font-mark-medium);
  }
  
  .title-container {
    h1 {
      font: var(--hx-font-headline-medium);
      color: var(--hx-text-color-primary);
      margin: 0;
    }
  }
}

.content-container {
  flex: 1;
  padding: var(--hx-size-6) var(--hx-comp-paddingLR-s);
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--hx-comp-margin-m);
}

.grid-row {
  display: grid;
  gap: var(--hx-comp-margin-m);
  
  &.main-row {
    grid-template-columns: 1fr;
  }
  
  &.split-row {
    grid-template-columns: repeat(2, 1fr);
  }
}

.card {
  background-color: var(--hx-bg-color-container);
  border-radius: var(--hx-radius-medium);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  height: 100%;
  display: flex;
  flex-direction: column;

  .card-title {
    font: var(--hx-font-title-medium);
    margin: 0 0 var(--hx-size-2) 0;
    position: relative;
    padding-left: var(--hx-comp-paddingLR-s);
    display: flex;
    align-items: center;

    &:before {
      content: "";
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 3px;
      height: 70%;
      border-radius: 2px;
    }

    &.primary-title:before {
      background-color: var(--hx-brand-color-3);
    }

    &.secondary-title:before {
      background-color: var(--hx-sec-brand-color-3);
    }

    &.tertiary-title:before {
      background-color: var(--hx-warning-color-3);
    }
  }

  .card-subtitle {
    margin: 0 0 var(--hx-comp-margin-m) 0;
    padding-left: var(--hx-comp-paddingLR-s);
    color: var(--hx-text-color-tertiary);
    font: var(--hx-font-body-small);
  }
}

.main-footer {
  background-color: var(--hx-bg-color-container);
  color: var(--hx-text-color-secondary);
  padding: var(--hx-comp-paddingTB-s) var(--hx-comp-paddingLR-s);
  text-align: center;
  font: var(--hx-font-link-small);
  border-top: 1px solid var(--hx-border-level-1-color);
  
  p {
    margin: 0;
  }
}

// 响应式调整
@media (max-width: 1200px) {
  .content-container {
    padding: var(--hx-comp-paddingTB-s) var(--hx-comp-paddingLR-xs);
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
  .app-container {
    .content-container {
      padding: var(--hx-comp-paddingTB-s) var(--hx-comp-paddingLR-xs);
      gap: var(--hx-comp-margin-s);
      
      .grid-row {
        gap: var(--hx-comp-margin-s);
      }
    }
  }
  
  .main-header {
    padding: var(--hx-comp-paddingTB-xs) var(--hx-comp-paddingLR-s);
    
    .logo-icon {
      width: var(--hx-comp-size-s);
      height: var(--hx-comp-size-s);
      font: var(--hx-font-mark-small);
    }
    
    .title-container {
      h1 {
        font: var(--hx-font-headline-small);
      }
    }
  }
}
</style>
