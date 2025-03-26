module.exports = {
  purge: ['./src/**/*.{vue,js,ts,jsx,tsx}'],
  content: ['./src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // 基础色
        'white': 'var(--white)',
        'black': 'var(--black)',
        
        // 品牌色
        'brand': 'var(--hx-brand-color-3)',
        'brand-light': 'var(--hx-brand-color-1)',
        'brand-dark': 'var(--hx-brand-color-5)',
        'brand-hover': 'var(--hx-brand-color-hover)',
        'brand-active': 'var(--hx-brand-color-active)',
        'brand-disabled': 'var(--hx-brand-color-disabled)',
        
        // 功能色
        'success': 'var(--hx-success-color-3)',
        'success-light': 'var(--hx-success-color-1)',
        'success-dark': 'var(--hx-success-color-5)',
        'success-hover': 'var(--hx-success-color-hover)',
        'success-active': 'var(--hx-success-color-active)',
        
        'warning': 'var(--hx-warning-color-3)',
        'warning-light': 'var(--hx-warning-color-1)',
        'warning-dark': 'var(--hx-warning-color-5)',
        'warning-hover': 'var(--hx-warning-color-hover)',
        'warning-active': 'var(--hx-warning-color-active)',
        
        'danger': 'var(--hx-danger-color-3)',
        'danger-light': 'var(--hx-danger-color-1)',
        'danger-dark': 'var(--hx-danger-color-5)',
        
        // 涨跌色
        'raise': 'var(--hx-raise-color-3)',
        'raise-light': 'var(--hx-raise-color-1)',
        'raise-dark': 'var(--hx-raise-color-5)',
        'raise-hover': 'var(--hx-raise-color-hover)',
        'raise-active': 'var(--hx-raise-color-active)',
        
        'fall': 'var(--hx-fall-color-3)',
        'fall-light': 'var(--hx-fall-color-1)',
        'fall-dark': 'var(--hx-fall-color-5)',
        'fall-hover': 'var(--hx-fall-color-hover)',
        'fall-active': 'var(--hx-fall-color-active)',
        
        // 灰色系列
        'gray': {
          1: 'var(--hx-gray-color-1)',
          2: 'var(--hx-gray-color-2)',
          3: 'var(--hx-gray-color-3)',
          4: 'var(--hx-gray-color-4)',
          5: 'var(--hx-gray-color-5)',
          6: 'var(--hx-gray-color-6)',
          7: 'var(--hx-gray-color-7)',
          8: 'var(--hx-gray-color-8)',
          9: 'var(--hx-gray-color-9)',
          10: 'var(--hx-gray-color-10)',
          11: 'var(--hx-gray-color-11)',
        },
        
        // 文本颜色
        'text': {
          'primary': 'var(--hx-text-color-primary)',
          'secondary': 'var(--hx-text-color-secondary)',
          'tertiary': 'var(--hx-text-color-tertiary)',
          'quaternary': 'var(--hx-text-color-quaternary)',
        },
        
        // 背景颜色
        'bg': {
          'page': 'var(--hx-bg-color-page)',
          'container': 'var(--hx-bg-color-container)',
        },
        
        // 边框颜色
        'border': {
          1: 'var(--hx-border-level-1-color)',
          2: 'var(--hx-border-level-2-color)',
          3: 'var(--hx-border-level-3-color)',
          4: 'var(--hx-border-level-4-color)',
          5: 'var(--hx-border-level-5-color)',
        }
      },
      spacing: {
        // 基础尺寸
        '1': 'var(--hx-size-1)',
        '2': 'var(--hx-size-2)',
        '3': 'var(--hx-size-3)',
        '4': 'var(--hx-size-4)',
        '5': 'var(--hx-size-5)',
        '6': 'var(--hx-size-6)',
        '7': 'var(--hx-size-7)',
        '8': 'var(--hx-size-8)',
        '9': 'var(--hx-size-9)',
        '10': 'var(--hx-size-10)',
        '11': 'var(--hx-size-11)',
        '12': 'var(--hx-size-12)',
        '13': 'var(--hx-size-13)',
        '14': 'var(--hx-size-14)',
        '15': 'var(--hx-size-15)',
        '16': 'var(--hx-size-16)',
      },
      borderRadius: {
        'small': 'var(--hx-radius-small)',
        'default': 'var(--hx-radius-default)',
        'medium': 'var(--hx-radius-medium)',
        'large': 'var(--hx-radius-large)',
        'extra': 'var(--hx-radius-extraLarge)',
        'round': 'var(--hx-radius-round)',
        'circle': 'var(--hx-radius-circle)',
      },
      fontSize: {
        'xs': 'var(--hx-font-size-body-small)', // 12px
        'sm': 'var(--hx-font-size-body-small)', // 12px
        'base': 'var(--hx-font-size-body-medium)', // 14px
        'lg': 'var(--hx-font-size-body-large)', // 16px
        'xl': 'var(--hx-font-size-title-small)', // 18px
        '2xl': 'var(--hx-font-size-title-medium)', // 20px
        '3xl': 'var(--hx-font-size-title-large)', // 24px
        '4xl': 'var(--hx-font-size-headline-small)', // 30px
        '5xl': 'var(--hx-font-size-headline-medium)', // 36px
        '6xl': 'var(--hx-font-size-headline-large)', // 48px
        
        // 专用类型
        'body-small': 'var(--hx-font-size-body-small)',
        'body-medium': 'var(--hx-font-size-body-medium)',
        'body-large': 'var(--hx-font-size-body-large)',
        'title-small': 'var(--hx-font-size-title-small)',
        'title-medium': 'var(--hx-font-size-title-medium)',
        'title-large': 'var(--hx-font-size-title-large)',
        'headline-small': 'var(--hx-font-size-headline-small)',
        'headline-medium': 'var(--hx-font-size-headline-medium)', 
        'headline-large': 'var(--hx-font-size-headline-large)',
      },
      boxShadow: {
        'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'DEFAULT': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
        'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
        'none': 'none',
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ['active', 'hover', 'focus', 'disabled'],
      textColor: ['active', 'hover', 'focus', 'disabled'],
      borderColor: ['active', 'hover', 'focus', 'disabled'],
      opacity: ['disabled'],
    },
  },
  plugins: [],
}