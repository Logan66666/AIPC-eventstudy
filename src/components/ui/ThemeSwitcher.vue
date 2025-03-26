<template>
  <div class="theme-switcher">
    <button @click="switchTheme('default')" class="theme-btn" :class="{ active: currentTheme === 'default' }">默认主题</button>
    <button @click="switchTheme('dark')" class="theme-btn" :class="{ active: currentTheme === 'dark' }">暗黑主题</button>
    <button @click="switchTheme('light')" class="theme-btn" :class="{ active: currentTheme === 'light' }">亮色主题</button>
  </div>
</template>

<script>
export default {
  name: 'ThemeSwitcher',
  data() {
    return {
      currentTheme: 'default'
    }
  },
  methods: {
    switchTheme(theme) {
      // 移除当前主题
      document.documentElement.removeAttribute('data-theme');
      
      // 设置新主题
      if (theme !== 'default') {
        document.documentElement.setAttribute('data-theme', theme);
      }
      
      // 更新当前主题
      this.currentTheme = theme;
      
      // 触发主题变更事件
      this.$emit('theme-changed', theme);
    }
  },
  mounted() {
    // 初始化时获取当前主题
    const theme = document.documentElement.getAttribute('data-theme') || 'default';
    this.currentTheme = theme;
  }
}
</script>