<template>
  <div class="dropdown-select" ref="dropdown">
    <div 
      class="dropdown-trigger" 
      @click="toggleDropdown" 
      :class="{'active': isOpen}"
    >
      <span class="selected-text">{{ displayText }}</span>
      <span class="dropdown-arrow" :class="{'open': isOpen}">▼</span>
    </div>
    <div class="dropdown-menu" v-show="isOpen">
      <div 
        v-if="showSelectAll" 
        class="dropdown-item" 
        @click="selectAll"
      >
        <div class="checkbox" :class="{'checked': isAllSelected}"></div>
        <span>{{ allText }}</span>
        <span v-if="showBadges" class="type-badge all-types"></span>
      </div>
      <div 
        v-for="(option, index) in options" 
        :key="index" 
        class="dropdown-item"
        @click="toggleOption(option.value)"
      >
        <div class="checkbox" :class="{'checked': isSelected(option.value)}"></div>
        <span>{{ option.label }}</span>
        <span v-if="showBadges" class="type-badge" :class="option.badgeClass"></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DropdownSelect',
  props: {
    options: {
      type: Array,
      required: true,
      // 期望格式: [{label: '显示文本', value: '值', badgeClass: '可选的badge类名'}]
    },
    value: {
      type: Array,
      default: () => []
    },
    placeholder: {
      type: String,
      default: '请选择'
    },
    allText: {
      type: String,
      default: '全部'
    },
    showSelectAll: {
      type: Boolean,
      default: true
    },
    showBadges: {
      type: Boolean,
      default: true
    },
    maxDisplay: {
      type: Number,
      default: 2
    }
  },
  data() {
    return {
      isOpen: false,
      selected: []
    }
  },
  created() {
    // 初始化已选值
    this.selected = [...this.value]
    
    // 添加点击外部关闭下拉菜单的事件监听
    document.addEventListener('click', this.closeOnClickOutside)
  },
  beforeDestroy() {
    // 移除事件监听器
    document.removeEventListener('click', this.closeOnClickOutside)
  },
  watch: {
    value: {
      handler(newVal) {
        this.selected = [...newVal]
      },
      deep: true
    }
  },
  computed: {
    isAllSelected() {
      return this.selected.length === this.options.length
    },
    displayText() {
      if (this.selected.length === 0) {
        return this.placeholder
      } else if (this.selected.length === this.options.length && this.showSelectAll) {
        return this.allText
      } else if (this.selected.length <= this.maxDisplay) {
        // 将值映射回显示文本
        const selectedLabels = this.selected.map(value => {
          const option = this.options.find(opt => opt.value === value)
          return option ? option.label : value
        })
        return selectedLabels.join('、')
      } else {
        return `已选${this.selected.length}项`
      }
    }
  },
  methods: {
    toggleDropdown(event) {
      this.isOpen = !this.isOpen
      event.stopPropagation()
    },
    closeOnClickOutside(event) {
      if (this.$refs.dropdown && !this.$refs.dropdown.contains(event.target)) {
        this.isOpen = false
      }
    },
    isSelected(value) {
      return this.selected.includes(value)
    },
    toggleOption(value) {
      const index = this.selected.indexOf(value)
      if (index === -1) {
        this.selected.push(value)
      } else {
        this.selected.splice(index, 1)
      }
      this.$emit('input', this.selected)
      event.stopPropagation()
    },
    selectAll() {
      if (this.isAllSelected) {
        this.selected = []
      } else {
        this.selected = this.options.map(option => option.value)
      }
      this.$emit('input', this.selected)
      event.stopPropagation()
    }
  }
}
</script>

<style lang="scss" scoped>
.dropdown-select {
  position: relative;
  min-width: 120px;
  z-index: 10;
  
  .dropdown-trigger {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0px 8px;
    border-radius: var(--hx-radius-small);
    background-color: transparent;
    border: 1px solid var(--hx-border-level-2-color);
    cursor: pointer;
    transition: all 0.2s ease;
    
    &:hover, &.active {
      border-color: var(--hx-brand-color-3);
      
      .selected-text, .dropdown-arrow {
        color: var(--hx-brand-color-3);
      }
    }
    
    .selected-text {
      font-size: 12px;
      color: var(--hx-text-color-secondary);
      margin-right: 6px;
      transition: color 0.2s ease;
    }
    
    .dropdown-arrow {
      font-size: 10px;
      color: var(--hx-text-color-tertiary);
      transition: all 0.2s ease;
      
      &.open {
        transform: rotate(180deg);
      }
    }
  }
  
  .dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    margin-top: 4px;
    background-color: var(--hx-bg-color-container);
    border-radius: var(--hx-radius-small);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    width: 120px;
    max-height: 240px;
    overflow-y: auto;
    border: 1px solid var(--hx-border-level-2-color);
    
    &::-webkit-scrollbar {
      width: 4px;
    }
    
    &::-webkit-scrollbar-track {
      background: var(--hx-bg-color-container);
    }
    
    &::-webkit-scrollbar-thumb {
      background: var(--hx-border-level-2-color);
      border-radius: 2px;
      
      &:hover {
        background: var(--hx-border-level-3-color);
      }
    }
    
    .dropdown-item {
      display: flex;
      align-items: center;
      padding: 4px 8px;
      cursor: pointer;
      transition: all 0.2s;
      font-size: 12px;
      
      &:hover {
        background-color: var(--hx-bg-color-specialcomponent);
      }
      
      .checkbox {
        width: 14px;
        height: 14px;
        border-radius: 2px;
        border: 1px solid var(--hx-border-level-2-color);
        margin-right: 8px;
        position: relative;
        
        &.checked {
          background-color: var(--hx-brand-color-3);
          border-color: var(--hx-brand-color-3);
          
          &:after {
            content: '';
            position: absolute;
            left: 4px;
            top: 1px;
            width: 5px;
            height: 8px;
            border: solid white;
            border-width: 0 2px 2px 0;
            transform: rotate(45deg);
          }
        }
      }
      
      span {
        color: var(--hx-text-color-secondary);
      }
      
      .type-badge {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-left: auto;
        
        &.all-types {
          background: linear-gradient(45deg, var(--hx-brand-color-3), var(--hx-warning-color-2), var(--hx-info-color-2));
        }
      }
    }
  }
}
</style> 