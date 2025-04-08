// API请求工具类
import axios from 'axios';
import { stockHeadlinesMockData } from './mockData';

// 是否使用模拟数据的标志
let useMockData = true;

// 创建axios实例
const apiClient = axios.create({
  baseURL: 'http://agent-robot-engine-server/api',
  timeout: 300000,
  headers: {
    'X-Arsenal-Auth': 'arsenal-tools',
    'Content-Type': 'application/json',
    'X-Remote-Ip': '10.0.32.56',
    'X-Remote-Svc': 'ai-agent-server',
    'X-Session-Id': '16406165168564',
    'X-Trace-Id': '2564651651654',
    'X-User-Id': '516290709'
  }
});

// 设置是否使用模拟数据
export const setUseMockData = (value) => {
  useMockData = value;
  console.log(`已切换到${useMockData ? '模拟' : '真实'}API模式`);
};

// 添加日志拦截器
apiClient.interceptors.request.use(request => {
  console.log('API请求:', {
    url: request.url,
    method: request.method,
    data: request.data,
    headers: request.headers
  });
  return request;
});

apiClient.interceptors.response.use(response => {
  console.log('API响应:', {
    status: response.status,
    statusText: response.statusText,
    data: response.data
  });
  return response;
}, error => {
  console.error('API错误:', error);
  return Promise.reject(error);
});

// 获取头条数据
export const fetchHeadlinesData = async (query, onStateChange) => {
  try {
    if (onStateChange) onStateChange({ stage: 'EXECUTE', message: '开始获取数据' });
    
    if (useMockData) {
      // 使用模拟数据
      const mockData = stockHeadlinesMockData;
      
      if (mockData && mockData.status_code === 200 && mockData.execute_status === 'success') {
        const responseData = mockData.response;
        if (responseData?.text) {
          try {
            // 提取并解析 response.text 中的 JSON 字符串
            const textContent = responseData.text.trim();
            // 如果内容被包裹在 ```json ``` 中，需要提取出实际的 JSON 字符串
            const jsonMatch = textContent.match(/```json\n([\s\S]*)\n```/);
            const jsonStr = jsonMatch ? jsonMatch[1] : textContent;
            
            console.log('解析响应文本');
            const parsed = JSON.parse(jsonStr);
            if (onStateChange) onStateChange({ stage: 'SUCCESS', message: '成功获取数据' });
            return parsed;
          } catch (e) {
            console.warn('解析响应数据失败:', e);
            throw new Error('响应数据格式错误');
          }
        }
      }
    } else {
      // 使用真实 API
      const response = await apiClient.post('/pipeline/v1/sync/execute', {
        mode: 'WORK_FLOW',
        pipe_name: '11006',
        input_variable_value: { query }
      });

      if (response && response.data && response.data.status_code === 200) {
        const executeId = response.data.response?.execute_id;
        console.log('获取到执行ID:', executeId);
        
        // 轮询获取结果
        const pollResponse = await apiClient.post('/pipeline/v1/sync/result', {
          execute_id: executeId
        });

        if (pollResponse && pollResponse.data && pollResponse.data.status_code === 200 && 
            pollResponse.data.execute_status === 'success' && 
            pollResponse.data.response?.text) {
          try {
            const textContent = pollResponse.data.response.text.trim();
            const jsonMatch = textContent.match(/```json\n([\s\S]*)\n```/);
            const jsonStr = jsonMatch ? jsonMatch[1] : textContent;
            
            const parsed = JSON.parse(jsonStr);
            if (onStateChange) onStateChange({ stage: 'SUCCESS', message: '成功获取数据' });
            return parsed;
          } catch (e) {
            console.warn('解析响应数据失败:', e);
            throw new Error('响应数据格式错误');
          }
        }
      }
    }
    
    throw new Error('获取数据失败');
  } catch (error) {
    console.error('获取头条数据失败:', error);
    if (onStateChange) onStateChange({ stage: 'ERROR', message: `获取数据失败: ${error.message}` });
    throw error;
  }
};

export default {
  fetchHeadlinesData,
  setUseMockData
};