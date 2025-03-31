<template>
  <div class="debug-style-vars">
    <h3>CSS变量调试</h3>
    <div class="var-list">
      <div v-for="(varGroup, groupName) in varGroups" :key="groupName" class="var-group">
        <h4>{{ groupName }}</h4>
        <div v-for="varName in varGroup" :key="varName" class="var-item">
          <div class="var-name">{{ varName }}</div>
          <div class="var-value">
            <div 
              v-if="isColorVar(varName)" 
              class="color-preview" 
              :style="{backgroundColor: getCSSVarValue(varName)}"
            ></div>
            {{ getCSSVarValue(varName) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DebugStyleVars',
  data() {
    return {
      varGroups: {
        '尺寸变量': [
          '--hx-size-1',
          '--hx-size-2',
          '--hx-size-3',
          '--hx-size-4',
          '--hx-size-5',
          '--hx-size-6'
        ],
        '品牌色': [
          '--hx-brand-color-1',
          '--hx-brand-color-2',
          '--hx-brand-color-3',
          '--hx-brand-color-4',
          '--hx-brand-color-5'
        ],
        '背景色': [
          '--hx-bg-color-page',
          '--hx-bg-color-container'
        ],
        '文本色': [
          '--hx-text-color-primary',
          '--hx-text-color-secondary',
          '--hx-text-color-tertiary'
        ],
        '边框色': [
          '--hx-border-level-1-color',
          '--hx-border-level-2-color',
          '--hx-border-level-3-color'
        ],
        '圆角': [
          '--hx-radius-small',
          '--hx-radius-default',
          '--hx-radius-medium',
          '--hx-radius-large'
        ]
      }
    }
  },
  methods: {
    getCSSVarValue(varName) {
      return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
    },
    isColorVar(varName) {
      return varName.includes('color');
    }
  }
}
</script>

<style scoped lang="scss">
.debug-style-vars {
  background-color: var(--hx-bg-color-container);
  border-radius: var(--hx-radius-default);
  padding: var(--hx-size-4);
  color: var(--hx-text-color-primary);
  
  h3 {
    margin-top: 0;
    border-bottom: 1px solid var(--hx-border-level-1-color);
    padding-bottom: var(--hx-size-2);
    margin-bottom: var(--hx-size-4);
  }
  
  .var-group {
    margin-bottom: var(--hx-size-4);
    
    h4 {
      margin-top: 0;
      margin-bottom: var(--hx-size-2);
      color: var(--hx-text-color-secondary);
    }
  }
  
  .var-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: var(--hx-size-1);
    font-size: 13px;
    
    .var-name {
      color: var(--hx-text-color-tertiary);
    }
    
    .var-value {
      display: flex;
      align-items: center;
      
      .color-preview {
        width: 16px;
        height: 16px;
        border-radius: 2px;
        margin-right: var(--hx-size-2);
        border: 1px solid var(--hx-border-level-1-color);
      }
    }
  }
}
</style> 