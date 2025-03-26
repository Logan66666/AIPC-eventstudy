<template>
  <div id="app" class="app-container">
    <!-- 页面标题 -->
    <header class="main-header">
      <div class="header-content">
        <div class="logo-container">
          <div class="logo-icon">A</div>
          <div class="title-container">
            <h1>大A头条</h1>
            <p>实时掌握市场动态，发现投资机会</p>
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
      <!-- 第一行布局：股市头条（横向排列） -->
      <div class="grid-row">
        <!-- 股市头条模块 -->
        <StockHeadlines />
      </div>

      <!-- 第二行布局：世界经济 + 政策催化 -->
      <div class="grid-row">
        <!-- 世界经济模块 -->
        <WorldEconomy />

        <!-- 政策催化模块 -->
        <PolicyCatalyst />
      </div>

      <!-- 第三行布局：埋伏机会 + 行业焦点 -->
      <div class="grid-row">
        <!-- 埋伏机会模块 -->
        <InvestmentOpportunity />
        
        <!-- 行业焦点模块 -->
        <IndustryFocus />
      </div>

      <!-- 第四行布局：财经日历 + 公司动向 -->
      <div class="grid-row">
        <!-- 财经日历模块 -->
        <FinancialCalendar />

        <!-- 公司动向模块 -->
        <CompanyNews />
      </div>
    </div>

    <!-- 底部区域 -->
    <footer class="main-footer">
      <p>大A头条 © 2023 | 数据来源：Wind、同花顺iFinD、东方财富</p>
    </footer>
  </div>
</template>

<script>
import ThemeSwitcher from './components/ui/ThemeSwitcher.vue'
import StockHeadlines from './components/StockHeadlines.vue'
import WorldEconomy from './components/WorldEconomy.vue'
import PolicyCatalyst from './components/PolicyCatalyst.vue'
import InvestmentOpportunity from './components/InvestmentOpportunity.vue'
import IndustryFocus from './components/IndustryFocus.vue'
import FinancialCalendar from './components/FinancialCalendar.vue'
import CompanyNews from './components/CompanyNews.vue'

export default {
  name: 'App',
  components: {
    ThemeSwitcher,
    StockHeadlines,
    WorldEconomy,
    PolicyCatalyst,
    InvestmentOpportunity,
    IndustryFocus,
    FinancialCalendar,
    CompanyNews
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
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  color: var(--hx-text-color-primary);
  background-color: var(--hx-bg-color-page);
}

.main-header {
  background-color: var(--hx-bg-color-specialcomponent);
  color: var(--hx-text-color-primary);
  padding: var(--hx-size-5) var(--hx-size-6);
  border-bottom: 1px solid var(--hx-border-level-1-color);
  
  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .logo-container {
    display: flex;
    align-items: center;
    gap: var(--hx-size-3);
  }
  
  .logo-icon {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    background-color: var(--hx-brand-color-1);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
  }
  
  .title-container {
    h1 {
      font-size: 22px;
      font-weight: 600;
      margin-bottom: 4px;
    }
    
    p {
      font-size: 14px;
      color: var(--hx-text-color-tertiary);
      margin: 0;
    }
  }
}

.content-container {
  flex: 1;
  padding: var(--hx-size-6) var(--hx-size-4);
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.grid-row {
  display: flex;
  margin-bottom: var(--hx-size-5);
  gap: var(--hx-size-5);
  
  @media (max-width: 768px) {
    flex-direction: column;
  }
}

.card {
  background-color: var(--hx-bg-color-container);
  border-radius: 8px;
  padding: var(--hx-size-5);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  flex: 1;
}

.full-width {
  width: 100%;
}

.main-footer {
  background-color: var(--hx-bg-color-specialcomponent);
  color: var(--hx-text-color-tertiary);
  padding: var(--hx-size-4);
  text-align: center;
  font-size: 13px;
  border-top: 1px solid var(--hx-border-level-1-color);
  
  p {
    margin: 0;
  }
}

@media (max-width: 768px) {
  .grid-row {
    flex-direction: column;
  }
  
  .card {
    margin-bottom: var(--hx-size-4);
  }
}
</style>
