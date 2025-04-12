<template>
  <div class="stock-headlines">
    
    <!-- 加载状态显示 - 优化后的版本 -->
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
      <p class="loading-stage">{{ loadingStageText }}</p>
      <div v-if="processingTime > 5" class="loading-note">
        <i class="fas fa-info-circle"></i>
        <span>AI数据收集处理中，请稍候...</span>
      </div>
    </div>
            
    <!-- 错误提示 -->
    <div v-if="error && !loading" class="error-message">
      <i class="fas fa-exclamation-circle"></i>
      <p>{{ error }}</p>
    </div>
              
    <!-- 轮播内容容器 -->
    <div class="swiper-container-wrapper">
      <!-- 轮播内容 -->
      <swiper 
        v-if="!loading && !error && headlines.length > 0"
        :options="swiperOptions"
        ref="mySwiper" 
        class="headlines-swiper"
      >
        <swiper-slide v-for="(item, index) in headlines" :key="index" class="headline-slide">
          <HeadlineCard :item="item" />
        </swiper-slide>
      </swiper>
      
      <!-- 左侧遮罩 -->
      <div class="swiper-mask left-mask"></div>
      
      <!-- 右侧遮罩 -->
      <div class="swiper-mask right-mask"></div>
      
      <!-- 自定义导航按钮 - 添加点击事件 -->
      <div class="swiper-button-prev custom-nav-btn" 
           v-if="!loading && !error && headlines.length > 0"
           @click="slidePrev">
        <i class="fas fa-chevron-left"></i>
      </div>
      <div class="swiper-button-next custom-nav-btn" 
           v-if="!loading && !error && headlines.length > 0"
           @click="slideNext">
        <i class="fas fa-chevron-right"></i>
      </div>
    </div>
    
    <!-- 无数据显示 -->
    <div v-if="!loading && !error && headlines.length === 0" class="no-data">
      <i class="fas fa-info-circle"></i>
      <p>暂无市场要闻</p>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper';
import 'swiper/css/swiper.css';
import '@fortawesome/fontawesome-free/css/all.css';
import HeadlineCard from './ui/HeadlineCard.vue';
import { fetchHeadlinesData, setUseMockData } from '../utils/api.js';
import { stockHeadlinesMockData } from '../utils/mockData';

export default {
  name: 'StockHeadlines',
  components: {
    Swiper,
    SwiperSlide,
    HeadlineCard
  },
  directives: {
    swiper: directive
  },
  data() {
    // 从 mockAsyncResponse 中提取初始数据
    const getMockData = () => {
      try {
        const textContent = stockHeadlinesMockData.response.text.trim();
        // const jsonMatch = textContent.match(/```json\\n([\\s\\S]*)\\n```/); // 这行正则匹配可能不再需要，因为我们直接存储JSON字符串了
        // const jsonStr = jsonMatch ? jsonMatch[1] : textContent;
        return JSON.parse(textContent); // 直接解析textContent
      } catch (e) {
        console.error('解析模拟数据失败:', e);
        return [];
      }
    };

    return {
      loading: false,
      error: null,
      headlines: getMockData(), // 使用解析后的模拟数据
      swiperOptions: {
        slidesPerView: 'auto',
        spaceBetween: 8, // 减小间距，因为我们已经在slide中添加了padding
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        },
        watchOverflow: true,
        observer: true,
        observeParents: true,
        updateOnWindowResize: true,
        resizeObserver: true,
        loop: false, // 确保不循环，避免右侧出现重复卡片
        slidesOffsetBefore: 0,
        slidesOffsetAfter: 0,
        breakpoints: {
          // 当窗口宽度大于等于1600px
          1600: {
            slidesPerView: 4,
            spaceBetween: 8
          },
          // 当窗口宽度大于等于1200px
          1200: {
            slidesPerView: 3,
            spaceBetween: 8
          },
          // 当窗口宽度大于等于768px
          768: {
            slidesPerView: 2,
            spaceBetween: 8
          },
          // 当窗口宽度小于768px
          320: {
            slidesPerView: 1,
            spaceBetween: 8
          }
        }
      },
      useMockApi: true,
      loadingStageText: '正在加载数据...',
      processingTime: 0,
      processingTimer: null,
    };
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper?.$swiper;
    }
  },
  methods: {
    getBorderClass(tag) {
      const classes = {
        '政策': 'policy-border',
        '全球': 'global-border',
        '行业': 'industry-border'
      };
      return classes[tag] || 'policy-border';
    },
    getIconClass(tag) {
      const classes = {
        '政策': 'policy-icon',
        '全球': 'global-icon',
        '行业': 'industry-icon'
      };
      return classes[tag] || 'policy-icon';
    },
    getTagClass(tag) {
      const classes = {
        '政策': 'policy-tag',
        '全球': 'global-tag',
        '行业': 'industry-tag'
      };
      return classes[tag] || 'policy-tag';
    },
    getIconForTag(tag) {
      const icons = {
        '政策': 'fas fa-landmark',
        '全球': 'fas fa-globe-asia',
        '行业': 'fas fa-industry'
      };
      return icons[tag] || 'fas fa-info';
    },
    // 获取实时头条数据
    async fetchRealTimeHeadlines() {
      try {
        this.loading = true;
        this.error = null;
        this.loadingStageText = '正在请求数据...';
        this.processingTime = 0;
        
        // 清除可能存在的旧计时器
        if (this.processingTimer) {
          clearInterval(this.processingTimer);
        }
        
        // 启动计时器
        this.processingTimer = setInterval(() => {
          this.processingTime++;
        }, 1000);
        
        // 调用API获取头条数据，添加状态回调
        const query = "stock_headlines";
        const result = await fetchHeadlinesData(query, ({ stage, message, attempt, total, progress }) => {
          // 更新加载状态文本
          this.loadingStageText = message;
          
          // 如果是轮询阶段，更新进度信息
          if (stage === 'POLLING' && total) {
            this.loadingStageText = `${message} (${attempt}/${total})`;
          }
          
          console.log('加载状态更新:', { stage, message, attempt, total, progress });
        });
        
        // 确保返回的结果是有效数据才更新
        if (result && Array.isArray(result) && result.length > 0) {
          // 更新头条数据
          this.headlines = result;
          
          // 更新完数据后，需要更新swiper
          this.$nextTick(() => {
            if (this.swiper) {
              this.swiper.update();
            }
          });
        } else {
          console.warn('获取到的数据为空或格式不正确');
          this.error = '获取数据格式不正确';
        }
      } catch (error) {
        console.error('获取实时头条失败:', error);
        this.error = `获取数据失败: ${error.message}`;
      } finally {
        // 清除计时器
        if (this.processingTimer) {
          clearInterval(this.processingTimer);
          this.processingTimer = null;
        }
        this.loading = false;
        this.processingTime = 0;
      }
    },
    
    // 切换API模式
    toggleApiMode() {
      this.useMockApi = !this.useMockApi;
      console.log('已切换API模式:', this.useMockApi ? '模拟' : '真实');
      setUseMockData(this.useMockApi);
    },
    
    // 修复swiper右侧滚动问题
    fixSwiperScrolling() {
      this.$nextTick(() => {
        if (this.swiper) {
          // 获取所有slide和容器宽度
          // 移除未使用的变量
          // const slides = this.swiper.slides;
          
          // 如果滑块已经到达最后，强制修正位置
          if (this.swiper.isEnd) {
            this.swiper.translateTo(this.swiper.maxTranslate());
          }
          
          // 更新swiper以应用新的设置
          this.swiper.update();
          
          console.log('修复了swiper滚动问题');
        }
      });
    },
    
    // 添加手动滚动方法
    slidePrev() {
      if (this.swiper) {
        this.swiper.slidePrev();
      }
    },
    
    slideNext() {
      if (this.swiper) {
        this.swiper.slideNext();
      }
    },

    parseJsonFromResponse(response) {
      try {
        if (response?.response?.text) {
          // 获取原始文本
          let jsonStr = response.response.text;
          
          // 移除所有可能的markdown标记和空白
          jsonStr = jsonStr.replace(/^[\s\n]*```json[\s\n]*/gmi, '');  // 移除开头的```json
          jsonStr = jsonStr.replace(/[\s\n]*```[\s\n]*$/gmi, '');      // 移除结尾的```
          jsonStr = jsonStr.trim();  // 移除首尾空白
          
          // 调试输出
          console.log('处理后的JSON字符串:', jsonStr.substring(0, 200));
          
          // 尝试解析JSON
          let parsedData;
          try {
            parsedData = JSON.parse(jsonStr);
          } catch (parseError) {
            console.error('JSON解析错误，尝试修复格式:', parseError);
            // 尝试修复常见的JSON格式问题
            jsonStr = jsonStr.replace(/,(\s*[}\]])/g, '$1');  // 移除尾随逗号
            jsonStr = jsonStr.replace(/([^"\\])"/g, '$1\\"');  // 转义未转义的引号
            jsonStr = jsonStr.replace(/\n/g, '\\n');  // 转义换行符
            console.log('修复后的JSON字符串:', jsonStr.substring(0, 200));
            parsedData = JSON.parse(jsonStr);
          }
          
          // 打印解析结果用于调试
          console.log('解析成功，数据条数:', Array.isArray(parsedData) ? parsedData.length : '非数组');
          if (Array.isArray(parsedData) && parsedData.length > 0) {
            console.log('第一条数据示例:', parsedData[0]);
          }
          
          return parsedData;
        }
        return []
      } catch (error) {
        console.error('解析JSON失败:', error);
        console.error('原始响应:', response);
        if (response?.response?.text) {
          console.error('原始文本前100个字符:', response.response.text.substring(0, 100));
        }
        return []
      }
    },
  },
  mounted() {
    // 使用预设ID获取初始数据
    this.fetchRealTimeHeadlines();
    
    // 增强可访问性
    this.$nextTick(() => {
      const cards = document.querySelectorAll('.headline-card');
      cards.forEach(card => {
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'article');
        card.setAttribute('aria-label', '市场事件');
      });
    });

    // 如果需要在mounted后执行一些操作
    this.$nextTick(() => {
      // 如需更新swiper
      if (this.swiper) {
        this.swiper.update();
      }
    });

    // 在swiper初始化后修复滚动问题
    this.$nextTick(() => {
      if (this.swiper) {
        // 监听滑动事件，以便在滑动到最后时修复位置
        this.swiper.on('slideChange', () => {
          if (this.swiper.isEnd) {
            // 如果滑到最后，确保没有额外空间
            this.swiper.translateTo(this.swiper.maxTranslate());
          }
        });
        
        // 初始化后修复一次
        this.fixSwiperScrolling();
      }
    });
  },
  beforeUnmount() {
    // 在swiper初始化后修复滚动问题
    this.$nextTick(() => {
      if (this.swiper) {
        // 监听滑动事件，以便在滑动到最后时修复位置
        this.swiper.on('slideChange', () => {
          if (this.swiper.isEnd) {
            // 如果滑到最后，确保没有额外空间
            this.swiper.translateTo(this.swiper.maxTranslate());
          }
        });
        
        // 初始化后修复一次
        this.fixSwiperScrolling();
      }
    });
  },
}
</script>

<style lang="scss" scoped>
.stock-headlines {
  width: 100%;
  max-width: 100%;
  position: relative;
  box-sizing: border-box;
  overflow-x: hidden; // 防止水平溢出
  
  .headlines-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    
    h2 {
      margin: 0;
      font-size: 18px;
      color: var(--hx-text-color-primary);
    }
  }
  
  // 轮播容器包装器
  .swiper-container-wrapper {
    position: relative;
    width: 100%;
    padding: 0;
    box-sizing: border-box;
    overflow: hidden;
  }
  
  // 遮罩样式
  .swiper-mask {
    position: absolute;
    top: 0;
    height: 100%;
    width: 60px; // 遮罩宽度
    z-index: 10;
    pointer-events: none; // 允许点击穿透
    
    &.left-mask {
      left: 0;
      background: linear-gradient(to right, var(--hx-bg-color-page) 30%,var(--hx-bg-color-page) 70%, transparent);
    }
    
    &.right-mask {
      right: 0;
      width: 70px; // 增加右侧遮罩宽度
      background: linear-gradient(to left, var(--hx-bg-color-page) 40%, var(--hx-bg-color-page) 80%, transparent);
    }
  }
  
  .headlines-swiper {
    padding: 0 60px; // 增加左右padding，给按钮和卡片留出更多空间
    width: 100%; // 确保swiper容器宽度为100%
    box-sizing: border-box; // 确保padding计算在宽度内
    
    .headline-slide {
      height: auto;
      width: 360px; // 设置默认宽度，但会被slidesPerView自动调整
      padding: 0 8px; // 为每个slide添加内边距，确保卡片间有间隔
      box-sizing: border-box;
      display: flex; // 使用flex布局
      justify-content: center; // 内容居中
      align-items: center; // 内容垂直居中
      
      @media (max-width: 768px) {
        width: 100%;
      }
    }
    
    .swiper-wrapper {
      // 修复swiper计算问题，确保对齐
      display: flex;
      align-items: stretch;
      will-change: transform;
      box-sizing: content-box;
    }
  }
  
  // 导航按钮样式
  .custom-nav-btn {
    position: absolute; // 确保绝对定位
    top: 50%; // 垂直居中
    transform: translateY(-50%); // 垂直居中调整
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--hx-text-color-brand); // 使用品牌色作为按钮背景色
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2); // 添加阴影增强视觉效果
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 30; // 提高z-index，确保在遮罩上方
    margin: 0;
    
    &.swiper-button-prev {
      left: 15px; // 调整左按钮位置
    }
    
    &.swiper-button-next {
      right: 15px; // 调整右按钮位置
    }
    
    &:after {
      display: none; // 移除默认箭头
    }
    
    i {
      color: var(--hx-text-color-primary); // 白色图标，与品牌色背景形成对比
      font-size: 14px;
      font-weight: bold; // 加粗图标
    }
    
    &:hover {
      background: var(--hx-bg-color-specialcomponent);
    }
    
    &.swiper-button-disabled {
      opacity: 0.5;
      pointer-events: none;
      background: var(--hx-bg-color-page); // 禁用状态使用不同背景色
      
      i {
        color: var(--hx-text-color-secondary); // 禁用状态使用次要文字颜色
      }
    }
  }
}

// 响应式调整
@media (max-width: 768px) {
  .stock-headlines {
    .custom-nav-btn {
      width: 28px;
      height: 28px;
          
          i {
            font-size: 12px;
          }
        }
      }
}

.loading-container {
  width: 100%;
  height: 200px;
      display: flex;
      flex-direction: column;
  align-items: center;
  justify-content: center;
  
  .loading-spinner {
    width: 40px;
    height: 40px;
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-radius: 50%;
    border-top-color: var(--hx-text-color-brand);
    animation: spin 1s ease-in-out infinite;
    margin-bottom: 16px;
  }
  
  p {
          color: var(--hx-text-color-secondary);
    font-size: 14px;
  }
  
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
}

.error-message {
  width: 100%;
  padding: 24px;
  text-align: center;
  color: var(--hx-text-color-danger);
  
  i {
    font-size: 32px;
    margin-bottom: 16px;
  }
  
  p {
    font-size: 14px;
  }
}

.no-data {
  width: 100%;
  height: 200px;
          display: flex;
          flex-direction: column;
              align-items: center;
  justify-content: center;
  color: var(--hx-text-color-secondary);
  
  i {
    font-size: 32px;
    margin-bottom: 16px;
  }
  
  p {
              font-size: 14px;
  }
}
</style> 