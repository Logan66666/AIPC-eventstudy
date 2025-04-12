'''
# 目标：在工作流中处理，用于获取未来一周的行业事件

输入示例：
[
  {
    "id": 2937,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-01",
    "title": "2025义乌国际自行车与新能源电动车展览会",
    "blocks": [
      {
        "code": "885431",
        "name": "新能源汽车",
        "py": "xnyqj"
      }
    ],
    "stocks": []
  },
  {
    "id": 2938,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-03",
    "title": "华为将于3月3日至6日在巴塞罗那举办MWC活动",
    "blocks": [
      {
        "code": "885806",
        "name": "华为概念",
        "py": "hwgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2939,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-07",
    "title": "第32届成都医疗健康博览会将于3月7日至9日举办",
    "blocks": [
      {
        "code": "885539",
        "name": "医疗器械概念",
        "py": "ylqxgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2940,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-17",
    "title": "英伟达在美国加州圣何塞及线上举行GTC AI大会",
    "blocks": [
      {
        "code": "885728",
        "name": "人工智能",
        "py": "rgzn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2941,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-18",
    "title": "第五届中国跨境电商交易会将于3月18日至20日在福州举行",
    "blocks": [
      {
        "code": "885642",
        "name": "跨境电商",
        "py": "kjds"
      }
    ],
    "stocks": []
  },
  {
    "id": 2942,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-20",
    "title": "2025中国家电及消费电子博览会",
    "blocks": [
      {
        "code": "885800",
        "name": "消费电子概念",
        "py": "xfdzgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2943,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-23",
    "title": "第十五届中国国际储能大会暨展览会",
    "blocks": [
      {
        "code": "885921",
        "name": "储能",
        "py": "cn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2944,
    "ctime": "2025-03-03 08:30:02",
    "mtime": "2025-03-03 08:30:02",
    "isvalid": 1,
    "date": "2025-03-25",
    "title": "苹果将于3月25日在上海举行"深入探索Apple智能和机器学习"开发者活动",
    "blocks": [
      {
        "code": "885728",
        "name": "人工智能",
        "py": "rgzn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2945,
    "ctime": "2025-03-04 12:30:03",
    "mtime": "2025-03-04 12:30:03",
    "isvalid": 1,
    "date": "2025-03-04",
    "title": "全国政协十四届三次会议",
    "blocks": [
      {
        "code": "881153",
        "name": "房地产",
        "py": "fdc"
      }
    ],
    "stocks": []
  },
  {
    "id": 2946,
    "ctime": "2025-03-04 12:30:03",
    "mtime": "2025-03-04 12:30:03",
    "isvalid": 1,
    "date": "2025-03-05",
    "title": "十四届全国人大三次会议",
    "blocks": [
      {
        "code": "885740",
        "name": "化债概念(AMC概念)",
        "py": "hzgnamcgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2947,
    "ctime": "2025-03-04 12:30:03",
    "mtime": "2025-03-04 12:30:03",
    "isvalid": 1,
    "date": "2025-03-06",
    "title": "2025沃尔玛全球电商启动大会",
    "blocks": [
      {
        "code": "885642",
        "name": "跨境电商",
        "py": "kjds"
      }
    ],
    "stocks": []
  },
  {
    "id": 2948,
    "ctime": "2025-03-04 12:30:03",
    "mtime": "2025-03-04 12:30:03",
    "isvalid": 1,
    "date": "2025-03-07",
    "title": "特朗普主持首届白宫加密货币峰会",
    "blocks": [
      {
        "code": "885866",
        "name": "数字货币",
        "py": "szhb"
      }
    ],
    "stocks": []
  },
  {
    "id": 2949,
    "ctime": "2025-03-07 12:30:03",
    "mtime": "2025-03-07 12:30:03",
    "isvalid": 1,
    "date": "2025-03-12",
    "title": "中国信息通信研究院拟在浙江大学计算机创新技术研究院举办"AI眼镜产业推进专题研讨会"",
    "blocks": [
      {
        "code": "885728",
        "name": "人工智能",
        "py": "rgzn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2950,
    "ctime": "2025-03-07 12:30:03",
    "mtime": "2025-03-07 12:30:03",
    "isvalid": 1,
    "date": "2025-03-12",
    "title": "中国信息通信研究院拟在浙江大学计算机创新技术研究院举办"AI眼镜产业推进专题研讨会"",
    "blocks": [
      {
        "code": "885728",
        "name": "人工智能",
        "py": "rgzn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2951,
    "ctime": "2025-03-10 23:30:03",
    "mtime": "2025-03-10 23:30:03",
    "isvalid": 1,
    "date": "2025-03-11",
    "title": "2025中国国际纺织纱线（春夏）展览会",
    "blocks": [
      {
        "code": "881136",
        "name": "服装家纺",
        "py": "fzjf"
      }
    ],
    "stocks": []
  },
  {
    "id": 2952,
    "ctime": "2025-03-10 23:30:03",
    "mtime": "2025-03-10 23:30:03",
    "isvalid": 1,
    "date": "2025-03-13",
    "title": "2025中国医学装备大会暨医学装备展览会",
    "blocks": [
      {
        "code": "881144",
        "name": "医疗器械",
        "py": "ylqx"
      }
    ],
    "stocks": []
  },
  {
    "id": 2953,
    "ctime": "2025-03-10 23:30:03",
    "mtime": "2025-03-10 23:30:03",
    "isvalid": 1,
    "date": "2025-03-19",
    "title": "2025中国种子大会暨南繁硅谷论坛",
    "blocks": [
      {
        "code": "885812",
        "name": "农业种植",
        "py": "nyzz"
      }
    ],
    "stocks": []
  },
  {
    "id": 2954,
    "ctime": "2025-03-10 23:30:03",
    "mtime": "2025-03-10 23:30:03",
    "isvalid": 1,
    "date": "2025-03-19",
    "title": "2025势银绿色液体燃料产业大会暨绿氨、绿醇及绿色航煤市场与技术研讨会",
    "blocks": [
      {
        "code": "885775",
        "name": "燃料电池",
        "py": "rldc"
      }
    ],
    "stocks": []
  },
  {
    "id": 2955,
    "ctime": "2025-03-10 23:30:03",
    "mtime": "2025-03-10 23:30:03",
    "isvalid": 1,
    "date": "2025-03-20",
    "title": "CESC2025国际储能大会",
    "blocks": [
      {
        "code": "885921",
        "name": "储能",
        "py": "cn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2956,
    "ctime": "2025-03-12 23:30:02",
    "mtime": "2025-03-12 23:30:02",
    "isvalid": 1,
    "date": "2025-03-26",
    "title": "半导体大会SEMICON China 2025将于3月26日至28日在上海举办",
    "blocks": [
      {
        "code": "885756",
        "name": "芯片概念",
        "py": "xpgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2957,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-01",
    "title": "第50届光网络与通信研讨会及博览会（OFC）",
    "blocks": [
      {
        "code": "881129",
        "name": "通信设备",
        "py": "txsb"
      }
    ],
    "stocks": []
  },
  {
    "id": 2958,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-01",
    "title": "2025中国生成式AI大会（北京站）",
    "blocks": [
      {
        "code": "885728",
        "name": "人工智能",
        "py": "rgzn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2959,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-09",
    "title": "第十三届中国电子信息博览会（CITE2025）",
    "blocks": [
      {
        "code": "885800",
        "name": "消费电子概念",
        "py": "xfdzgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2960,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-09",
    "title": "第八届中国国际管道会议（CIPC）",
    "blocks": [
      {
        "code": "885692",
        "name": "地下管网",
        "py": "dxgw"
      }
    ],
    "stocks": []
  },
  {
    "id": 2961,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-10",
    "title": "2025全球6G技术与产业生态大会",
    "blocks": [
      {
        "code": "881162",
        "name": "通信服务",
        "py": "txfw"
      }
    ],
    "stocks": []
  },
  {
    "id": 2962,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-13",
    "title": "全球首个人形机器人半程马拉松",
    "blocks": [
      {
        "code": "885517",
        "name": "机器人概念",
        "py": "jqrgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2963,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-14",
    "title": "第三届中国国际通用航空与无人机发展大会",
    "blocks": [
      {
        "code": "885564",
        "name": "无人机",
        "py": "wrj"
      }
    ],
    "stocks": []
  },
  {
    "id": 2964,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-16",
    "title": "CLNB 2025新能源全产业链博览会",
    "blocks": [
      {
        "code": "885431",
        "name": "新能源汽车",
        "py": "xnyqj"
      }
    ],
    "stocks": []
  },
  {
    "id": 2965,
    "ctime": "2025-04-01 08:30:03",
    "mtime": "2025-04-01 08:30:03",
    "isvalid": 1,
    "date": "2025-04-17",
    "title": "中国城镇供水排水协会2025年会暨城镇水务技术与产品展示",
    "blocks": [
      {
        "code": "885412",
        "name": "污水处理",
        "py": "wscl"
      }
    ],
    "stocks": []
  },
  {
    "id": 2966,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-21",
    "title": "2025中国固态电池技术与应用交流大会",
    "blocks": [
      {
        "code": "885710",
        "name": "锂电池概念",
        "py": "ldcgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2967,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-22",
    "title": "第31届中国国际广播电视信息网络展览会（CCBN2025）",
    "blocks": [
      {
        "code": "885418",
        "name": "文化传媒概念",
        "py": "whzmgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2968,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-23",
    "title": "2025势银长时储能产业大会（LDESIC）",
    "blocks": [
      {
        "code": "885921",
        "name": "储能",
        "py": "cn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2969,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-23",
    "title": "2025年中国航天大会",
    "blocks": [
      {
        "code": "885574",
        "name": "卫星导航",
        "py": "wxdh"
      }
    ],
    "stocks": []
  },
  {
    "id": 2970,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-25",
    "title": "2025中国人形机器人生态大会",
    "blocks": [
      {
        "code": "885517",
        "name": "机器人概念",
        "py": "jqrgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2971,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-26",
    "title": "2025世界机器人大赛——首届具身智能机器人运动会",
    "blocks": [
      {
        "code": "885517",
        "name": "机器人概念",
        "py": "jqrgn"
      }
    ],
    "stocks": []
  },
  {
    "id": 2972,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-26",
    "title": "第二届全球低空经济论坛春季会",
    "blocks": [
      {
        "code": "885564",
        "name": "无人机",
        "py": "wrj"
      }
    ],
    "stocks": []
  },
  {
    "id": 2973,
    "ctime": "2025-04-02 23:30:03",
    "mtime": "2025-04-02 23:30:03",
    "isvalid": 1,
    "date": "2025-04-29",
    "title": "Meta举行首届LlamaCon—专门面向生成式人工智能的开发者大会",
    "blocks": [
      {
        "code": "885728",
        "name": "人工智能",
        "py": "rgzn"
      }
    ],
    "stocks": []
  }
]

输出要求：
    - 按照date，筛选出未来一周的行业事件，包括date,title,blocks,stocks,按照原格式输出

'''


from datetime import datetime, timedelta
import json

def main(params):
    """
    获取未来一周的行业事件
    
    Args:
        params: 包含date参数的字典，date格式为'YYYYMMDD'
        
    Returns:
        dict: 包含筛选后的事件列表，每个事件只包含date、title和blocks字段
    """
    try:
        # 获取输入日期
        date_str = params['date']
        if not date_str:
            raise ValueError('未提供日期参数')
            
        # 解析日期
        try:
            current_date = datetime.strptime(date_str, '%Y%m%d')
        except ValueError:
            raise ValueError('日期格式错误，应为YYYYMMDD')
        
        # 计算一周后的日期
        end_date = current_date + timedelta(days=7)
        
        # 获取输入数据
        input_data = params['input_data']
        if not input_data:
            raise ValueError('未提供事件数据')
            
        # 如果输入是字符串，尝试解析JSON
        if isinstance(input_data, str):
            try:
                events = json.loads(input_data)
            except json.JSONDecodeError:
                raise ValueError('事件数据JSON格式错误')
        else:
            events = input_data
            
        if not isinstance(events, list):
            raise ValueError('事件数据必须是列表格式')
        
        # 从输入数据中筛选未来一周的事件，并只保留需要的字段
        filtered_events = []
        for event in events:
            try:
                event_date = datetime.strptime(event['date'], '%Y-%m-%d')
                if current_date <= event_date <= end_date:
                    # 只保留需要的字段
                    filtered_event = {
                        'date': event['date'],
                        'title': event['title'],
                        'blocks': event['blocks']
                    }
                    filtered_events.append(filtered_event)
            except (KeyError, ValueError):
                continue  # 跳过无效的事件数据
        
        # 按日期排序
        filtered_events.sort(key=lambda x: x['date'])
        
        # 构造返回值
        ret = {
            "events": filtered_events
        }
        
        return ret
        
    except Exception as e:
        return {
            "error": str(e),
            "events": []
        }



