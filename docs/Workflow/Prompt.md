# System
你是一个专业的金融分析师，熟悉A股市场的运作规律，能请从各种角度进行对事件进行全面、客观、严谨的解读分析，不会被营销号或者虚假信息干扰，并按照内容要求和格式要求进行输出。

# User

## **股市头条**
```
# 任务要求
你需要根据提供的材料，选取对国内资本市场可能产生巨大影响、A股投资者最需要关注、市场关注度最高的5个重要事件，并按照要求进行客观的整理，按照时间先后顺序排列。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下：
{
  "EventName": "事件名称（50字以内）",
  "Time": "格式如2025/3/27（若发生在今天以前，则写准确日期，否则需要加上"预计"二字）",
  "Introduction": "事件简介（100字以内，介绍事件的来龙去脉和核心内容，目的是让不了解该事件的股市小白有清晰的认知。包括事件的重要性，历史情况、当前发展的节点、具体的数据表现等等）",
  "Highlights": "事件看点（事件中需要重点关注的内容，包括可能的影响、重要数据、预期偏差等等）",
  "PositiveImpact": ["", "", ""]（可能产生利多影响的行业、市场、股票等等，最多不超过3个，没有可输出空值）
  "NegativeImpact": ["", "", ""]（可能产生利空影响的行业、市场、股票等等，最多不超过3个，没有可输出空值）,
  "EventTag":"事件类型标签（可选 '全球'、'政策'、'行业'）"
}

# 输出案例
        {
          "EventName": "中美贸易摩擦升级",
          "Time": "2025/3/10",
          "Introduction": "中国宣布对美国鸡肉（15%）、大豆（10%）加征关税，并限制15家美企对华出口。这是2024年贸易争端以来最大规模反制措施，涉及2024年中美贸易额约380亿美元的农产品和科技产品。",
          "Highlights": "后续谈判可能性/国内农产品储备投放计划/被制裁美企替代方案",
          "PositiveImpact": ["农业种植", "食品加工", "国产替代"],
          "NegativeImpact": ["消费电子代工", "纺织服装", "跨境电商"],
          "EventTag": "全球"
        }

# Initiation
请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

## **投资机会**
Q：
今天是**2025年**4月8日，近期有哪些个股的重大事件值得关注
今天是**2025年**4月8日，近期有哪些行业的重大事件值得关注
今天是**2025年**4月8日，近期有哪些可能影响全市场的重大事件值得关注


### **投资机会-个股**
```
# 任务要求你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最有可能的个股投资机会。
针对每个挖掘出的事件机会，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有投资机会事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：
近期事件如下：

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "市场ID (17 代表上交所股票，33表示深交所股票)",
      "stockcode": "股票代码 (例如: '601127')",
      "stockname": "股票名称 (例如: '赛力斯')"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出核心信息。）",
    "summary": "事件简介（要求：100字以内，快速介绍事件核心内容，让股市小白也能看懂。包含：1.事件的核心内容和关键数据；2.对市场的直接影响；3.客观准确的描述。建议：先说结论，再说原因）",
    "context": "事件解读（要求：300字以内，解释该事件为什么值得关注。包含：1.事件的历史背景；2.当前发展阶段；3.未来发展方向；4.对市场的深层影响；5.具体数据支撑。建议：由浅入深，层层展开）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-3个月内有明显影响；中期：3-12个月内逐步显现；长期：1年以上的持续性影响）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高收益、高关注度；2分：中等确定性、中等收益；1分：待观察、潜在机会）",
    "highlights": [  // 事件核心看点，1-3个
      {
        "tag": "事件看点（10字以内，提炼事件核心看点，如：政策突破、业绩拐点、技术创新、产能释放等。用于快速理解该事件最值得关注的方面和未来需要关注的事件走向）",
        "reason": "具体说明（30字以内，对看点进行解释，包括当前进展、后续观察重点等）"
      }
    ],
    "benefits": [  // 受益标的，0-3个
      {
        "tag": "受益对象（10字以内，填写具体受益的股票名称、行业板块，如：新能源车、光伏设备、比亚迪等）",
        "reason": "具体说明（30字以内，说明为什么会受益，受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 利空标的，0-3个
      {
        "tag": "承压对象（10字以内，填写可能受到负面影响的股票名称、行业板块）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]



# Initiation

请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

### **投资机会-行业**
```
# 任务要求你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最有可能的行业投资机会。
针对每个挖掘出的事件机会，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有投资机会事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "市场ID (17 代表上交所股票，33表示深交所股票)",
      "stockcode": "股票代码 (例如: '601127')",
      "stockname": "股票名称 (例如: '赛力斯')"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出行业核心动态。）",
    "type": "事件类型（可选值：
      技术突破：行业内重要技术创新或突破性进展；
      行业趋势：行业整体发展方向和趋势性变化；
      竞争格局：行业内竞争态势和市场份额变化；
      产业链变化：产业链上下游关系和供应链格局的调整
    ）",
    "content": "事件内容（要求：100字以内，快速介绍事件核心内容，让股市小白也能看懂。）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高影响、高关注度；2分：中等确定性、中等影响；1分：待观察、潜在影响）",
    "timeTag": "影响期限（短期：1-4周，中期：1-6个月，长期：3-12个月）"
  }
]



# Initiation

请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

### **投资机会-市场**
```
# 任务要求你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最有可能的个股投资机会。
针对每个挖掘出的事件机会，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有投资机会事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：
近期事件如下：

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "（输出空值）",
      "stockcode": "（输出空值）",
      "stockname": "市场名称 (例如: A股，债券、美股、港股等等)"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出核心信息。）",
    "summary": "事件简介（要求：100字以内，快速介绍事件核心内容，让股市小白也能看懂。包含：1.事件的核心内容和关键数据；2.对市场的直接影响；3.客观准确的描述。建议：先说结论，再说原因）",
    "context": "事件解读（要求：300字以内，解释该事件为什么值得关注。包含：1.事件的历史背景；2.当前发展阶段；3.未来发展方向；4.对市场的深层影响；5.具体数据支撑。建议：由浅入深，层层展开）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-3个月内有明显影响；中期：3-12个月内逐步显现；长期：1年以上的持续性影响）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高收益、高关注度；2分：中等确定性、中等收益；1分：待观察、潜在机会）",
    "highlights": [  // 事件核心看点，1-3个
      {
        "tag": "事件看点（10字以内，提炼事件核心看点，如：政策突破、业绩拐点、技术创新、产能释放等。用于快速理解该事件最值得关注的方面和未来需要关注的事件走向）",
        "reason": "具体说明（30字以内，对看点进行解释，包括当前进展、后续观察重点等）"
      }
    ],
    "benefits": [  // 受益标的，0-3个
      {
        "tag": "受益对象（10字以内，填写具体受益的股票名称、行业板块，如：新能源车、光伏设备、比亚迪等）",
        "reason": "具体说明（30字以内，说明为什么会受益，受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 利空标的，0-3个
      {
        "tag": "承压对象（10字以内，填写可能受到负面影响的股票名称、行业板块）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]

# Initiation
请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

## **风险预警**

### **风险预警-个股**
```
# 任务要求
你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最可能面临风险的个股投资警示。
针对每个挖掘出的风险事件，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有个股风险事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "市场ID (17 代表上交所股票，33表示深交所股票)",
      "stockcode": "股票代码 (例如: '601127')",
      "stockname": "股票名称 (例如: '赛力斯')"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出核心风险信息。）",
    "summary": "事件简介（要求：100字以内，快速介绍风险核心内容，让股市小白也能看懂。包含：1.风险的核心内容和关键数据；2.对个股的直接影响；3.客观准确的描述。建议：先说结论，再说原因）",
    "context": "事件解读（要求：300字以内，解释该风险为什么值得警惕。包含：1.风险的历史背景；2.当前发展阶段；3.未来发展方向；4.对公司的深层影响；5.具体数据支撑。建议：由浅入深，层层展开）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-3个月内有明显影响；中期：3-12个月内逐步显现；长期：1年以上的持续性影响）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高风险、高关注度；2分：中等确定性、中等风险；1分：待观察、潜在风险）",
    "highlights": [  // 风险核心看点，1-3个
      {
        "tag": "风险看点（10字以内，提炼风险核心点，如：业绩下滑、股权质押、债务风险、监管处罚等。用于快速理解该风险最值得关注的方面和未来需要警惕的走向）",
        "reason": "具体说明（30字以内，对风险进行解释，包括当前状况、后续观察重点等）"
      }
    ],
    "benefits": [  // 风险下的受益标的，0-3个
      {
        "tag": "受益对象（10字以内，填写在此风险下可能受益的同行业竞争对手或其他标的）",
        "reason": "具体说明（30字以内，说明为何会在此风险下受益，受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 受损标的，1-3个，必须包含该个股
      {
        "tag": "受损对象（10字以内，填写受到负面影响的股票，必须包含本事件主体）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]

# Initiation
请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

### **风险预警-行业**
```
# 任务要求
你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最可能面临风险的行业投资警示。
针对每个挖掘出的风险事件，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有行业风险事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "市场ID（对于行业风险，填写'48'）",
      "stockcode": "（对于行业风险，此处留空）",
      "stockname": "行业名称（例如：半导体、新能源、医药等）"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出核心风险信息。）",
    "summary": "事件简介（要求：100字以内，快速介绍风险核心内容，让股市小白也能看懂。包含：1.风险的核心内容和关键数据；2.对行业的直接影响；3.客观准确的描述。建议：先说结论，再说原因）",
    "context": "事件解读（要求：300字以内，解释该风险为什么值得警惕。包含：1.风险的历史背景；2.当前发展阶段；3.未来发展方向；4.对行业的深层影响；5.具体数据支撑。建议：由浅入深，层层展开）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-3个月内有明显影响；中期：3-12个月内逐步显现；长期：1年以上的持续性影响）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高风险、高关注度；2分：中等确定性、中等风险；1分：待观察、潜在风险）",
    "highlights": [  // 风险核心看点，1-3个
      {
        "tag": "风险看点（10字以内，提炼风险核心点，如：政策收紧、需求下滑、产能过剩、技术瓶颈等。用于快速理解该风险最值得关注的方面和未来需要警惕的走向）",
        "reason": "具体说明（30字以内，对风险进行解释，包括当前状况、后续观察重点等）"
      }
    ],
    "benefits": [  // 风险下的受益标的，0-3个
      {
        "tag": "受益对象（10字以内，填写在此风险下可能受益的其他行业或细分领域）",
        "reason": "具体说明（30字以内，说明为何会在此风险下受益，受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 受损标的，1-3个
      {
        "tag": "受损对象（10字以内，填写受到负面影响的具体行业细分板块或代表企业）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]

# Initiation
请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

### **风险预警-市场**
```
# 任务要求
你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最可能面临风险的市场整体投资警示。
针对每个挖掘出的风险事件，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有市场风险事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "（对于市场风险，此处留空）",
      "stockcode": "（对于市场风险，此处留空）",
      "stockname": "市场名称（例如：A股、港股、美股、债券、外汇等）"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出核心风险信息。）",
    "summary": "事件简介（要求：100字以内，快速介绍风险核心内容，让股市小白也能看懂。包含：1.风险的核心内容和关键数据；2.对市场的直接影响；3.客观准确的描述。建议：先说结论，再说原因）",
    "context": "事件解读（要求：300字以内，解释该风险为什么值得警惕。包含：1.风险的历史背景；2.当前发展阶段；3.未来发展方向；4.对市场的深层影响；5.具体数据支撑。建议：由浅入深，层层展开）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-3个月内有明显影响；中期：3-12个月内逐步显现；长期：1年以上的持续性影响）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高风险、高关注度；2分：中等确定性、中等风险；1分：待观察、潜在风险）",
    "highlights": [  // 风险核心看点，1-3个
      {
        "tag": "风险看点（10字以内，提炼风险核心点，如：流动性紧缩、地缘冲突、政策变动、通胀高企等。用于快速理解该风险最值得关注的方面和未来需要警惕的走向）",
        "reason": "具体说明（30字以内，对风险进行解释，包括当前状况、后续观察重点等）"
      }
    ],
    "benefits": [  // 风险下的受益标的，0-3个
      {
        "tag": "受益对象（10字以内，填写在此风险下可能有对冲效应的资产类别或板块）",
        "reason": "具体说明（30字以内，说明为何会在此风险下受益，受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 受损标的，0-3个
      {
        "tag": "受损对象（10字以内，填写受到负面影响的市场板块或资产类别）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]

# Initiation
请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。
```

## **政策催化**

```
# 任务要求
你需要根据提供的材料，从事件中挖掘出在未来短期、中期、长期最可能产生政策催化效应的投资机会。
针对每个挖掘出的政策事件，你需要按照输出要求整理事件的详细信息。
最终输出一个包含所有政策事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "政策发布日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "type": "政策类型（可选：金融政策、高层会议、产业政策、部委政策、国际政策）",
      "source": "政策来源（如：国务院、发改委、证监会等）",
      "name": "政策名称（如：新能源汽车产业发展规划等）"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出政策核心内容。）",
    "summary": "政策简介（要求：100字以内，快速介绍政策核心内容，让股市小白也能看懂。包含：1.政策的主要内容和关键目标；2.对市场的直接影响；3.客观准确的描述。建议：先说结论，再说原因）",
    "context": "政策解读（要求：300字以内，解释该政策为什么值得关注。包含：1.政策出台背景；2.当前发展阶段；3.未来推进方向；4.对市场的深层影响；5.具体数据支撑。建议：由浅入深，层层展开）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-3个月内有明显影响；中期：3-12个月内逐步显现；长期：1年以上的持续性影响）",
    "importance": "重要程度（取值范围：1-3。3分：高确定性、高影响、高关注度；2分：中等确定性、中等影响；1分：待观察、潜在影响）",
    "highlights": [  // 政策核心看点，1-3个
      {
        "tag": "政策看点（10字以内，提炼政策核心点，如：目标提升、补贴力度、准入放宽、监管加强等。用于快速理解该政策最值得关注的方面和未来推进重点）",
        "reason": "具体说明（30字以内，对看点进行解释，包括当前进展、后续观察重点等）"
      }
    ],
    "benefits": [  // 受益标的，0-3个
      {
        "tag": "受益对象（10字以内，填写在此政策下可能受益的行业、板块或个股）",
        "reason": "具体说明（30字以内，说明为何会受益，受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 受损标的，0-3个
      {
        "tag": "受损对象（10字以内，填写可能受到负面影响的行业、板块或个股）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]

# Initiation
请按以上任务要求，根据提供的信息进行分析，并按要求的json格式输出。

```

## **行业洞察**


```
# 任务要求
你需要根据提供的材料，整理{}行业的重要事件，并挖掘事件在未来短期、中期、长期，对于市场的具体影响。
最终输出一个包含多个事件的JSON对象，至少包含5个事件，并对每个事件按照输出要求整理事件的详细解读信息。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个单一的行业洞察对象）：
{
  "industry": { // 行业基本信息
    "name": "行业名称",
    "code": "行业代码",
    "hotness": "热度值（1-5，5表示最热）"
  },
  "events": [ // 行业内的关键事件，至少5个
    {
      "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
      "title": "事件名称（要求：50字以内，简洁明了，突出行业核心动态。）",
      "type": "事件类型（可选值：技术突破、行业趋势、竞争格局、产业链变化）",
      "content": "事件内容（要求：100字以内，快速介绍事件核心内容和影响逻辑，让股市小白也能看懂。）",
      "importance": "重要程度（取值范围：1-3。3分：高确定性、高影响、高关注度；2分：中等确定性、中等影响；1分：待观察、潜在影响）",
      "timeTag": "影响期限（短期：1-4周，中期：1-6个月，长期：3-12个月）",
      "analysis": "事件解读（要求：300字以内，解释该事件为什么值得关注。包含：1.事件发展背景；2.当前事件发展阶段；3.未来可能的发展方向；4.对市场影响的具体传导逻辑；5.具体数据支撑。建议：由浅入深，层层展开）",
      "highlights": [  // 事件核心看点，1-3个
        {
          "tag": "事件看点（10字以内，提炼事件核心看点，如：技术突破、需求爆发、政策支持、产能扩张等。用于快速理解该事件最值得关注的方面）",
          "reason": "具体说明（30字以内，对看点进行解释，包括当前进展、后续观察重点等）"
        }
      ],
      "benefits": [  // 受益标的，0-3个
        {
          "tag": "受益对象（10字以内，填写在此事件下可能受益的细分领域或龙头企业）",
          "reason": "具体说明（30字以内，说明为何会受益，受益逻辑和程度）"
        }
      ],
      "drawbacks": [  // 受损标的，0-3个
        {
          "tag": "受损对象（10字以内，填写可能受到负面影响的相关行业或企业）", 
          "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
        }
      ]
    }
  ]
}

# Initiation
请按以上任务要求，根据提供的信息分析{}行业的热门事件，并按要求的json格式输出。
```

## **热股动向**
```
# 任务要求
你需要根据提供的材料，筛选出近期市场关注度高、出现重要动态的热点个股事件。
针对每个筛选出的个股事件，你需要按照输出要求整理事件的详细信息，侧重分析事件对该个股的直接影响。
最终输出一个包含所有热点个股事件对象的JSON数组。
输出的事件列表需要按照以下规则排序：
1. 主要按日期排序，最新日期在前。
2. 对于同一天的事件，按照 importance 值降序排列。
总事件数量为5-10条。

# 信息
今天的日期是：{}
近期事件如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有事件对象的数组）：
[
  {
    "date": "事件日期（格式：YYYY/MM/DD，如2025/5/15）",
    "item": { //此项必填
      "marketid": "市场ID (17 代表上交所股票，33表示深交所股票)",
      "stockcode": "股票代码 (例如: '601127')",
      "stockname": "股票名称 (例如: '赛力斯')"
    },
    "title": "事件名称（要求：50字以内，简洁明了，突出个股核心动态。）",
    "type": "事件类型（可选值：业绩动态、重大事项、经营动态、投资者关系、市场表现）", // 对应Requirement.md中的细分事件
    "summary": "事件简介（要求：100字以内，快速介绍事件核心内容，让股市小白也能看懂。包含：1.事件的核心内容和关键数据；2.对个股的直接影响；3.客观准确的描述。）",
    "context": "事件解读（要求：300字以内，解释该事件对个股的影响。包含：1.事件背景；2.当前进展；3.对公司基本面或股价的潜在影响分析；4.相关数据或市场反应。建议：聚焦个股本身，分析影响逻辑）",
    "timeTag": "影响期限（短期/中期/长期。短期：1-4周；中期：1-6个月；长期：6个月以上，根据事件类型判断）",
    "importance": "重要程度（取值范围：1-3。3分：对股价或基本面有重大影响；2分：有较明显影响；1分：一般性动态）",
    "highlights": [  // 事件核心看点，1-3个
      {
        "tag": "事件看点（10字以内，提炼事件核心点，如：业绩超预期、重组获批、新品放量、股东增持、资金追捧等。用于快速理解该事件最值得关注的方面）",
        "reason": "具体说明（30字以内，对看点进行解释，包括关键数据、后续观察点等）"
      }
    ],
    "benefits": [  // 受益标的，0-3个 (通常只包含该个股本身，或强相关的少数标的)
      {
        "tag": "受益对象（10字以内，通常为该股票本身）",
        "reason": "具体说明（30字以内，说明受益逻辑和程度）"
      }
    ],
    "drawbacks": [  // 利空标的，0-3个
      {
        "tag": "受损对象（10字以内，填写可能受到负面影响的竞争对手或相关方）", 
        "reason": "具体说明（30字以内，说明为什么会受到影响，影响的方式和程度）"
      }
    ]
  }
]

# Initiation
请按以上任务要求，根据提供的信息分析热点个股动态，并按要求的json格式输出。
```

## **全球经济**
```
# 任务要求
你需要根据提供的全球重要经济指标数据，分析近期全球经济形势，并重点解读对中国资本市场可能产生的影响。
针对每个重要经济指标，你需要按照输出要求整理详细的分析信息。
最终输出一个包含所有经济指标分析的JSON数组。
输出的指标分析需要按照以下规则排序：
1. 主要按日期排序，最新数据在前
2. 同一天的数据，按照 importance 值降序排列
3. 同等重要性的数据，按照国家/地区顺序：中国 > 美国 > 欧元区
总分析数量为5-10条。

# 信息
今天的日期是：{}
近期经济指标数据如下：{}

# 输出要求
输出的json格式和内容要求如下（注意：最外层是一个包含所有分析对象的数组）：
[
  {
    "date": "数据发布日期（格式：YYYY/MM/DD，如2025/5/15）",
    "time": "数据发布时间（格式：HH:mm，如10:00）",
    "item": {
      "country": "国家/地区（如：中国、美国、欧元区）",
      "indicator": "指标名称（如：CPI同比、PMI、GDP等）",
      "actual": "实际",
      "forecast": "预期",
      "previous": "前值"
    },
    "title": "分析标题（要求：50字以内，突出数据偏离预期的程度和方向。例如：美国CPI超预期回升，通胀压力仍存）",
    "summary": "数据简析（要求：100字以内。包含：1.数据表现；2.与预期和前值的对比；3.背后反映的经济现象。用通俗易懂的语言解释，让小白也能看懂）",
    "context": "深度解读（要求：300字以内。包含：1.指标基本概念和重要性解释；2.本次数据变化原因分析；3.经济周期与政策研判；4.对全球经济的影响；5.通过汇率、贸易、资金流等渠道对中国经济和A股市场的传导机制。建议：由浅入深，层层展开）",
    "importance": "重要程度（1-3分。3分：核心经济指标且严重偏离预期；2分：重要指标或中等偏离；1分：一般指标或轻微偏离）",
    "deviation": "偏离程度（相对预期的偏离：超过预期、不及预期、符合预期）",
    "highlights": [  // 核心看点，2-3个
      {
        "tag": "看点标签（10字以内，如：通胀压力、就业改善、需求收缩等）",
        "reason": "具体说明（30字以内，说明该看点的关键表现和后续关注重点）"
      }
    ],
    "benefits": [  // 利好影响，2-3个
      {
        "tag": "受益对象（10字以内，如：板块、行业、大宗商品等）",
        "reason": "受益逻辑和影响期限（30字以内，说明在当前数据下为何受益，其影响是短期中期还是长期"
      }
    ],
    "risks": [  // 利空影响，2-3个
      {
        "tag": "风险对象（10字以内，如：板块、行业、大宗商品等）",
        "reason": "风险逻辑（30字以内，说明在当前数据下的不利影响，其影响是短期中期还是长期）"
      }
    ]
  }
]

# 分析要点
1. 指标解读
- 用通俗易懂的语言解释专业术语
- 说明指标对经济的指示作用
- 分析数据背后的经济现象

2. 影响传导
- 全球经济层面的影响
- 对中国经济的传导机制
- 对A股市场的影响路径

3. 投资机会
- 受益板块和机会
- 影响时间和力度
- 具体操作建议

4. 风险提示
- 重点风险领域
- 影响范围和程度
- 风险规避建议

# Initiation
请按以上任务要求，根据提供的经济指标数据进行分析，并按要求的json格式输出。
```
