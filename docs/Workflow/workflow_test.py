import re   # 需要导入 re 模块

def main(params):
    # 从params中提取JSON数据
    json_data = params['data']
    
    try:
        # 1. 移除 Markdown 代码块标记
        processed_data = json_data.removeprefix("```json\n").removesuffix("\n```").strip()

        # 2. 使用正则表达式查找所有 stockname
        # 正则表达式解释:
        # "stockname"  : 匹配字面量 "stockname"
        # \s*:\s*     : 匹配可能的空格和冒号
        # "           : 匹配起始引号
        # ([^"]+)    : 匹配一个或多个非引号字符，并将其捕获 (这就是我们要的 stockname)
        # "           : 匹配结束引号
        stocknames = re.findall(r'"stockname"\s*:\s*"([^"]+)"', processed_data)

        # 拼接结果
        result = "，".join(stocknames)
        
        # 构造返回值
        ret = {
            "stocknames": result
        }
        
        return ret
    
    except Exception as e:
        return {
            "error": f"发生错误: {str(e)}"
        }

# 输出示例：{'stocknames': '恩捷股份，夏厦精密，盛视科技，绿色动力，华达科技，固高科技'}



def main2(params, mockdata):
    """
    提取 marketid, stockcode, stockname，根据 mockdata 中的市场代码替换 marketid。
    
    Args:
        params: 包含原始 JSON 数据的字典
        mockdata: 包含股票代码和市场信息的表格字符串
    """
    json_data = params['data']
    try:
        # 1. 从 mockdata 中解析市场信息
        market_mapping = {}
        for line in mockdata.split('\n'):
            if '.SZ|' in line or '.SH|' in line:
                code_market = line.split('|')[1].strip()  # 获取如 "001306.SZ" 的部分
                code = code_market.split('.')[0]  # 股票代码
                market = code_market.split('.')[1]  # SZ 或 SH
                market_id = '33' if market == 'SZ' else '17'  # SZ->33, SH->17
                market_mapping[code] = market_id

        # 2. 移除 Markdown 代码块标记
        processed_data = json_data.removeprefix("```json\n").removesuffix("\n```").strip()

        # 3. 定义正则表达式模式
        pattern = r'("item"\s*:\s*{[^{}]*?"marketid"\s*:\s*")(\d+)(".*?stockcode"\s*:\s*")(\d+)(".*?\})'

        # 4. 定义替换函数
        def replacer(match):
            prefix = match.group(1)
            original_market_id = match.group(2)
            middle = match.group(3)
            stockcode = match.group(4)
            suffix = match.group(5)

            # 使用 market_mapping 查找正确的市场代码
            new_market_id = market_mapping.get(stockcode, original_market_id)
            return prefix + new_market_id + middle + stockcode + suffix

        # 5. 使用 re.sub 和替换函数进行全局替换
        modified_json_string = re.sub(pattern, replacer, processed_data, flags=re.DOTALL)

        # 6. 返回包含修改后字符串的字典
        return {"modified_data": modified_json_string}

    except Exception as e:
        return {"error": f"在 main2 中发生错误: {str(e)}"}

if __name__ == "__main__":
    # 示例数据 (从文档注释中提取)
    example_json_data = "```json\n[\n  {\n    \"date\": \"2025/04/06\",\n    \"item\": {\n      \"marketid\": \"32\",\n      \"stockcode\": \"002812\",\n      \"stockname\": \"恩捷股份\"\n    },\n    \"title\": \"签订美国车企锂电池隔离膜大额订单\",\n    \"summary\": \"子公司与美国知名车企签订2026-2030年9.73亿平方米锂电池隔离膜供应协议，锁定期长且金额巨大，直接利好新能源汽车产业链核心材料环节。\",\n    \"context\": \"作为全球锂电池隔膜龙头企业，本次长约订单验证了公司在技术迭代中的领先地位。按当前市场价格估算，协议总价值超200亿元，约占公司2024年营收的1.5倍。随着美国新能源补贴政策延期及4680电池量产加速，高端隔膜需求持续攀升。公司通过本土化建厂规避贸易风险，未来三年北美基地产能释放将保障订单执行。\",\n    \"timeTag\": \"中期\",\n    \"importance\": 3,\n    \"highlights\": [\n      {\n        \"tag\": \"订单锁定\",\n        \"reason\": \"覆盖2026-2030年需求，业绩确定性极高\"\n      },\n      {\n        \"tag\": \"技术壁垒\",\n        \"reason\": \"湿法隔膜专利布局完善，客户认证周期长\"\n      }\n    ],\n    \"benefits\": [\n      {\n        \"tag\": \"隔膜设备商\",\n        \"reason\": \"产线扩建带动设备采购需求\"\n      }\n    ],\n    \"drawbacks\": []\n  },\n  {\n    \"date\": \"2025/04/06\",\n    \"item\": {\n      \"marketid\": \"32\",\n      \"stockcode\": \"001306\",\n      \"stockname\": \"夏厦精密\"\n    },\n    \"title\": \"10亿元投建智能传动核心零部件项目\",\n    \"summary\": \"拟建设精密齿轮、行星滚柱丝杠等智能传动系统核心部件生产基地，契合人形机器人产业爆发前夜的设备需求。\",\n    \"context\": \"行星滚柱丝杠是人形机器人关节核心部件，当前国产化率不足5%。项目达产后预计年产200万套精密传动部件，对应产值约30亿元。公司已具备特斯拉Cybertruck转向器量产经验，设备协同开发模式可降低30%生产成本。与秦川机床等设备商的联合研发协议保障技术落地。\",\n    \"timeTag\": \"长期\",\n    \"importance\": 3,\n    \"highlights\": [\n      {\n        \"tag\": \"技术突破\",\n        \"reason\": \"突破人形机器人关键零部件制造\"\n      },\n      {\n        \"tag\": \"产能规划\",\n        \"reason\": \"建设周期3年匹配产业爆发时点\"\n      }\n    ],\n    \"benefits\": [\n      {\n        \"tag\": \"机床厂商\",\n        \"reason\": \"专用设备采购需求激增\"\n      }\n    ],\n    \"drawbacks\": []\n  },\n  {\n    \"date\": \"2025/04/06\",\n    \"item\": {\n      \"marketid\": \"32\",\n      \"stockcode\": \"002990\",\n      \"stockname\": \"盛视科技\"\n    },\n    \"title\": \"中标1.9亿元机场维保项目\",\n    \"summary\": \"获得成都天府国际机场十年期设备维保合同，智慧口岸业务进入收获期。\",\n    \"context\": \"项目年均收入1900万元，毛利率超60%。公司AIoT智慧口岸解决方案已覆盖全国70%枢纽机场，设备全生命周期服务模式提升客户粘性。随着RCEP全面实施，2025年口岸智能化改造市场规模预计达80亿元，公司市占率有望提升至35%。\",\n    \"timeTag\": \"中期\",\n    \"importance\": 2,\n    \"highlights\": [\n      {\n        \"tag\": \"模式升级\",\n        \"reason\": \"从设备销售转向服务运营\"\n      }\n    ],\n    \"benefits\": [],\n    \"drawbacks\": []\n  },\n  {\n    \"date\": \"2025/04/06\",\n    \"item\": {\n      \"marketid\": \"16\",\n      \"stockcode\": \"601330\",\n      \"stockname\": \"绿色动力\"\n    },\n    \"title\": \"联手固高科技布局智能巡检机器人\",\n    \"summary\": \"战略合作推进垃圾焚烧行业智能巡检应用，破解高危场景作业难题。\",\n    \"context\": \"协议涵盖无人机巡检、智慧园区平台等六大方向。公司运营62个垃圾焚烧项目，年处理量超3000万吨，设备巡检需求刚性。引入固高科技运动控制技术，可使巡检效率提升40%，人工成本下降60%。环保行业智能化改造财政补贴比例最高可达50%。\",\n    \"timeTag\": \"短期\",\n    \"importance\": 2,\n    \"highlights\": [\n      {\n        \"tag\": \"降本增效\",\n        \"reason\": \"高危场景替代人工效果显著\"\n      }\n    ],\n    \"benefits\": [\n      {\n        \"tag\": \"固高科技\",\n        \"reason\": \"技术输出打开新应用场景\"\n      }\n    ],\n    \"drawbacks\": []\n  },\n  {\n    \"date\": \"2025/04/06\",\n    \"item\": {\n      \"marketid\": \"16\",\n      \"stockcode\": \"603358\",\n      \"stockname\": \"华达科技\"\n    },\n    \"title\": \"战略合作切入新能源热管理系统\",\n    \"summary\": \"与飞龙股份联合研发新能源汽车热管理解决方案，切入千亿级蓝海市场。\",\n    \"context\": \"协议涵盖储能和数据中心热管理，2025年全球热管理系统市场规模预计达1800亿元。公司冲压件业务积累的精密制造能力，结合飞龙电子水泵技术，可形成完整的热管理总成供应能力。重点突破800V高压平台液冷方案，已获某头部车企B点供应商资格。\",\n    \"timeTag\": \"中期\",\n    \"importance\": 2,\n    \"highlights\": [\n      {\n        \"tag\": \"技术协同\",\n        \"reason\": \"机械+电子技术深度融合\"\n      }\n    ],\n    \"benefits\": [],\n    \"drawbacks\": []\n  },\n  {\n    \"date\": \"2025/03/31\",\n    \"item\": {\n      \"marketid\": \"32\",\n      \"stockcode\": \"301510\",\n      \"stockname\": \"固高科技\"\n    },\n    \"title\": \"机器人运动控制技术获重大突破\",\n    \"summary\": \"通过战略合作切入环保巡检领域，运动控制技术应用场景持续拓宽。\",\n    \"context\": \"公司作为国产运动控制器龙头，在光伏、锂电领域市占率达25%。本次合作验证了其在特种环境下的技术适配能力，垃圾焚烧场景拓展使目标市场扩容40%。新一代驱控一体产品支持EtherCAT总线，响应速度达微秒级，技术指标比肩贝加莱。\",\n    \"timeTag\": \"中期\",\n    \"importance\": 2,\n    \"highlights\": [\n      {\n        \"tag\": \"场景扩展\",\n        \"reason\": \"突破工业母机向多元场景延伸\"\n      }\n    ],\n    \"benefits\": [],\n    \"drawbacks\": []\n  }\n]\n```"
    mockdata = "\n为您找到6条数据\n|股票代码|股票简称|\n|---|---|\n|001306.SZ|夏厦精密|\n|301510.SZ|固高科技|\n|601330.SH|绿色动力|\n|603358.SH|华达科技|\n|002812.SZ|恩捷股份|\n|002990.SZ|盛视科技|\n"

    # 构造输入参数
    params = {
        "data": example_json_data
    }
    
    # ----- 测试 main2 函数 -----
    result_main2 = main2(params, mockdata)
    print("--- Result from main2 (modified data): ---")
    print(result_main2)
    print("-------------------------------------------")



######################################

mockdata="\n为您找到6条数据\n|股票代码|股票简称|\n|---|---|\n|001306.SZ|夏厦精密|\n|301510.SZ|固高科技|\n|601330.SH|绿色动力|\n|603358.SH|华达科技|\n|002812.SZ|恩捷股份|\n|002990.SZ|盛视科技|\n"

