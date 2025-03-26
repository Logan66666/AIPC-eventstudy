# DataAPI接入文档

## 一、说明
当前DataAPI定义了5种类型的接口接入：

1. 取一个股票列表的某些指标的数据；业务场景类似表头等；
2. 取某些股票一段时间区间范围内某些指标的数据；业务场景类似折线图，柱状图等；
3. 用于给前端获取对应的代码表，比如同花顺指数成分股，prompt2data 选股代码表；
4. 证券关联关系，比如多地上市的代码关联，指数跟踪ETF等；
5. 股票标签，比如涨停标签，龙头标签等；
接入DataAPI务必登记走Tangram的需求登记，并在请求头部加上相关的业务来源，包括 Source-Id, Platform 信息，如果是内部访问，则通过内部域名，如果是C端流量，则还需要额外带上用户登录的Cookie信息

## 二、使用DataAPI的优势
统一协议，一次性接入与理解成本，可以不断持续扩充支持指标数据范围；
搭配端侧组件化，丝滑搭建一个新页面；

## 三、如何使用DataAPI
3-1、查看DataAPI的协议与协议了解

### 【DataAPI】表格式指标取数：比如取全A股的收盘价，涨幅，净利润 等数据
【DataAPI】表格式指标取数
一、api 适用场景
用于客户端或 web 端表格类型的数据取数，适合多个代码获取多个特定时间（如最新时间）指标的数据。
例如：
场景一：获取沪深 A 股下股东户数、股东户同比变动、人均流通股、公告日期的最新数据。
场景二：获取用户自选股下的涨幅、热度等数据。
二、api 的边界说明
数据不具备强实时性，存在一定延迟(10秒)。
数据提供形式为 https，不支持推送业务场景。
三、请求协议
头部字段说明
名称	说明	示例
Source-Id	来源业务 id	shareholders
Cookie	用户的 cookie	需根据实际情况填写
Platform	来源平台	PC/APP 等
接口字段说明
初级入门
以下是请求“同花顺的主动买入小单金额”的示例：

{
    "indexes": [
        {
            "index_id": "fy00001894"
        }
    ],
    "code_selectors": {
        "include": [
            {
                "type": "stock_code",
                "values": [
                    "33:300033"
                ]
            }
        ]
    }
}

所有参数细节说明
indexes: 指标信息说明，每个指标的信息描述包括：
    index_id: 指标id,来源于tangram平台上的指标id
    timestamp: 时间信息，一般为秒级的时间戳，如果为天的话，以当地交易所的时间为准（A股是东八区零点时间戳，港股是12点时间戳，美股是美东时间中午12点时间戳），如果为小时，以小时整点的时间戳为准，依此类推，特殊表示：当传0的时候表示最新，用于取偏移量的话，0表示最新，-1表示往前偏移1，-2表示往前偏移2，不能小于-1000（按照当前偏移不能太小）
   time_type: 数据周期，为分钟，天还是周、月、季等等，具体传参可以通过Tangram上查询指标对应的周期
    req_uniq_id: 非必传，请求方用于区分指标的唯一id，服务端不处理，原样返回，该id用于请求方自行区分请求的指标
    attribute：指标的附加属性，根据具体的指标决定是否需要传相应的信息，非必需，如果指标没有attribute的不需要填，详细信息可以看： 指标的额外属性，可以看下文补充部分
 
code_selectors: 代码筛选器
    include ： code_selector数组，得到的代码进行合并
    exclude： code_selector数组,里面的代码合并后，作为排除的代码列表
    intersection: code_selector数组，里面的代码交集
    最后筛选出来的代码为。{include} + {intersection} - {exclude}
code_selector: 代码筛选器，主要是用于确定证券代码列表，详情可看DataAPI的CodeSelector文档，可以看下文补充部分
   type: 支持stock_code,market_code,block_code,tag 等模式，其中
    values: 根据type传递不同的数组，如果是stock_code，传递的是类 33:300033 {market}:{code} 的模式，block_code为板块服务，tag表示业务开发过程中生成的代码列表，比如热榜列表等
 
page_info: 分页详情，不需要分页的时候可以不传
    page_begin：0 数据起始下标，从0开始
    page_size: 10 分页大小
    code_begin: 0 代码下标，该字段非必传，主要用于返回额外的排序代码列表
    code_page_size: 20 分页大小，该字段非必传，当需要返回额外代码表的时候可以传。
sort： 排序信息，为了之后的扩展，以数组的形式返回， 不需要排序的时候可以不传，默认会按照第一个指标进行排序
    idx: 0 指定排序的字段，代表的是index_info的列表的下标
    type: desc/asc 升序或者降序规则  ,建议大小写不区分
 
follow: 该字段非必传，主要用于对齐时间戳使用
    idx： 非必传，对应的index_info的下标，表示取对应index_info的值的时间戳，当作缺省的时间戳，该时间戳给其他没有传时间戳的指标当缺省值
    timestamp： 非必传，相比较于idx，该字段用于直接指定时间戳的方式，给其他没有时间戳的指标当缺省值
 
filters： 过滤字段（暂未支持）


请求样例：

{
    "code_selectors": {
        "include": [
            {
                "type": "stock_code",
                "values": [
                    "33:300033"
                ]
            }
        ]
    },
    "indexes": [
        {
            "index_id": "security_name",
            "timestamp": 0,
            "time_type": "SNAPSHOT"
        },
        {
            "index_id": "F10-shareholders_total_num",
            "timestamp": 0,
            "time_type": "SNAPSHOT"
        }
    ],
    "page_info": {
        "page_begin": 0,
        "page_size": 20
    },
    "sort": [
        {
            "idx": 0,
            "type": "dsc"
        }
    ]
}

四、返回协议
返回字段说明
indexes: 数组，包含指标的元信息
    value_type: 数据类型，BIG_DECIMAL，INT，STRING等，具体以Tangram平台为准
    index_id: 指标id,来源于tangram平台上的指标id
    timestamp: 时间信息，一般为秒级的时间戳，表示最新的时候，也返回下对应的时间戳（比如用户传参的时候，传的是最新的0，返回的时候，返回具体的数据的时间戳）
    time_type: 数据周期，为分钟，天还是周、月、季等等，查看Tangram对应的指标的支持周期
    attribute：可以看DataAPI的指标attribute的文档，在本文后面
data: 对象数组
    code: 证券对象，market + ":" + code ,比如 33:300033
    values: 值数组对象
     idx: 下标，对应参数meta_data中下标
        value: 为Object 形式，具体类型根据 value_type 来；
total: 代码总数
 
part_order_code_list: 为一个list，返回额外的代码表，如果没有传code_begin相关的参数，不会返回该字段

返回样例
{
    "data": {
        "indexes": [
            {
                "value_type": "STRING",
                "index_id": "security_name",
                "timestamp": "0",
                "time_type": "SNAPSHOT",
                "attribute": {}
            },
            {
                "value_type": "BIG_DECIMAL",
                "index_id": "F10-shareholders_total_num",
                "timestamp": "0",
                "time_type": null,
                "attribute": {}
            }
        ],
        "data": [
            {
                "code": "33:300033",
                "values": [
                    {
                        "idx": 0,
                        "value": "同花顺"
                    },
                    {
                        "idx": 1,
                        "value": 60125
                    }
                ]
            }
        ],
        "total": 1
    },
    "status_code": 0,
    "status_msg": "success"
}

五、yapi 地址
https://yapi.myhexin.com/yapi/service/314766/interface/api/587532

六、code_selector
类型	说明	示例
stock_code	已经是代码维度，成分股即为自己。	33:300033成分股就是33:300033，{"type":"stock_code","values":["33:300033"]}
block_code	板块后台针对板块的唯一标识，由一个十六进制的字符串标识，例如: C199。	C199，可看板块 2.0 服务的文档:【#】已支持板块说明，{"type":"block_code","values":["E"]}
market_code	行情市场	{"type":"market_code","values": ["33"]} 代表33市场下的股票
hq_block_code	区分 block_code，一般指带有行情数据的板块对应的行情代码。	48:884507，https://dq.10jqka.com.cn/fuyao/sjht_concept_block/block/v1/list_block_code 请求样例：{"type":"hq_block_code","values": ["48:885431"]}
tag	一些业务方自己定义的板块。	比如:spec_index表示估值掘金精选指数列表，所有的tag可在tangram上查看到，表示 tag为lhb的从1706112000 到 1706112000 的代码总和：{"type":"tag", "values":["lhb"], "end":"1706112000", "start":"1706112000"} ,如果是动态参数，比如某个板块下的某些业务标签，可以使用动态传参的模式，形式为：动态tag，类似：split_{你的业务名，不带下划线，避免影响分割}_48:885431
prompt_code	根据 prompt2data 得到的代码表。	{"type":"prompt_code","values":["671b1fb3f72e0839cbe7b454"]}，该请求的id和Source-Id需要申请，不然不可访问
self_block_code	板块后台针对板块的唯一标识，由一个十六进制的字符串标识，例如: C199。	传递该type不会转化为对应的成分股，而是直接就是该板块的数据，比如总市值是C199的总市值。该type不能与上面的type在同一个请求存在，标的不一样，上面的都为行情代码，而该type为板块服务的ID暂未在DataAPI中生效，占位。
custom_type 处理	特殊的tag标签，不解析由各个业务。	比如:查一种关联关系的所有数据，这个时候不传code，那么请求参数为:{"type": "custom_type", "values":["ALL"]}

七、指标的attribute
指标 attribute 属性为指标的附加信息说明。

名称	说明	样例
win_size	区间的偏移量，一般用于类似区间涨幅。例如五日涨幅指标的表示：{ "index_id": "inr- price_change_ratio_pct-sum", "time_type":"day_1", "attribute":{ "win_size":5 }}	
related_index_code	表示指标关联的指数代码，比如贡献度指标中，关联的指数代码，表示在该指数下的贡献度数据。如 881101 的指数的成分股的贡献度：{ "index_id":"contribute_point", 'timestamp": 0, "time_type":"snapshot", "attribute":{ "related_index_code":"48: 881101" }	
win_start_timestamp	来表示区间计算起始时间，比如 win_start_timestamp 传 20240101 时间，周期是日线，表示年初至今的涨幅。例如某段时间内的区间涨幅统计："index_id': 'inr-turnover_ratio_pct-sum", "attribute":{ "win_start_timestamp": 1730217600 }, 'timestamp": 1731600000, "time_type":"DAY_1"。其他说明：win_start_timestamp 传 -1 表示从上市日开始	
currency	表示货币属性，不传的话则为证券代码所上市的交易所的货币，传了之后，返回值为对应的货币（根据汇率计算），当前支持：人民币 CNY、美元 USD、港币 HKD、新加坡元 SGD、日元 JPY、加元 CAD、澳元 AUD、英镑 GBP、欧元 EUR。如以港币形式显示综合总市值："index_id": "composite_total_market_value", 'timestamp": 0, 'time_type":"snapshot", "attribute":{ "currency":"HKD" }	
data_auth	标识实时行情和延迟行情，real 标识实时行情，delay 表示延迟行情。如实时行情涨幅："index_id": "inr-turnover_ratio_pct-sum", "attribute": { "data_auth": "real", "timestamp": 0, "time_type": "DAY_1" }

### 【DataAPI】折柱式指标取数：取一段时间区间的指标的数据 比如取 上证指数近一年的涨幅 这类场景；
【DataAPI】折柱式指标取数
一、api 适用场景
时间轴与时间周期固定，支持不同指标取不同的数据项，多用于画折线图和柱状图
例如：
场景一：股票的价格与大盘的分时走势涨幅叠加；
场景二：全A指数的涨停表现数据与上证指数的涨幅情况对比;
二、api 的边界说明
不支持大批量的代码和指标的获取
三、请求协议
头部字段说明
名称	说明	示例
Source-Id	来源业务 id	shareholders
Cookie	用户的 cookie	需根据实际情况填写
Platform	来源平台	PC/APP 等

接口字段说明
所有参数细节说明
time_range: 时间表示
    time_type: 数据周期，为分钟，天还是周、月、季等等，数据周期，为分钟，天还是周、月、季等等，查看Tangram对应的指标的支持周期
    start: "秒级时间戳,如果数据周期是天、月或者年等这种的，请以当天的时间（按照具体的类型来，A股是东八区零点，港股是12点，美股是美东时间中午12点）"
    end: "秒级时间戳,如果数据周期是天、月或者年等这种的，请以当天的时间戳（按照具体的类型来，A股是东八区零点，港股是12点，美股是美东时间中午12点）"
    offset: 0, 偏移量， 当大于0的时候，以end字段为准往未来偏移N个周期数据，当小于0的时候，以end字段为准往历史偏移N个数据,如果传了start 和end 和offset，则以 start和end参数为准，offset无效。 注意，offset 为-1 表示最近2条数据。


indexes: 数组，数组内的元素包含 一个 指标数组【index_info】与一个代码表【codes】

index_info： 指标信息数组
    index_id 指标的id
    attribute：指标的附加属性，根据具体的指标决定是否需要传相应的信息，非必需，根据具体的指标定义来，可以看DataAPI的指标attribute的文档，本文后面补充部分。
    codes: 代码表，数组的元素为：传递的是类似 33:300033 {market}:{code} 的模式
 


请求样例： 取300033 的5日涨幅、日开盘价 和  300034 的 日最低价 和 3日涨幅  ，在 20240109 到20240111 之间的数据

{
    "indexes": [
        {
            "codes": ["33:300033"],
            "index_info": [
                {
                    "index_id": "inr-price_change_ratio-sum",
                    "attribute": {
                        "win_size": "5"
                    }
                },
                {
                    "index_id": "basehq00000080"
                }
            ]
        },
        {
            "codes": ["33:300034"],
            "index_info": [
                {
                    "index_id": "basehq00000082"
                },
                {
                    "index_id": "inr-price_change_ratio-sum",
                    "attribute": {
                        "win_size": "3"
                    }
                }
            ]
        }
    ],
    "time_range": {
        "time_type": "DAY_1",
        "start": "1704729600",
        "end": "1704902400"
    }
}

四、返回协议
返回字段说明
time_range: 返回时间戳数组，表示该指标在用户请求的start 和 end时间区间内的数据时间 
indexes: 数组，包含指标的元信息
    value_type: 数据类型，BIG_DECIMAL，INT，STRING等，具体以Tangram平台为准
    index_id: 指标id,来源于tangram平台上的指标id    
    attribute：指标的附加属性，根据具体的指标决定是否需要传相应的信息，非必需，根据具体的指标定义来，可以看DataAPI的指标attribute的文档，补充在最后
data:
    code: 代码，格式为{market:code}，比如 33:300033
    values: 值数组对象
        idx: 下标，对应参数meta_data中下标
        value: 数据数组，跟time_range中的时间戳列表中一一对应

返回样例
{
    "status_code": 0,
    "status_msg": "success",
    "data": {
        "time_range": [
            "1704729600",
            "1704816000",
            "1704902400"
        ],
        "indexes": [
            {
                "value_type": "BIG_DECIMAL",
                "index_id": "inr-price_change_ratio-sum",
                "attribute": {
                    "win_size": "5"
                }
            },
            {
                "value_type": "BIG_DECIMAL",
                "index_id": "basehq00000080",
                "attribute": {}
            },
            {
                "value_type": "BIG_DECIMAL",
                "index_id": "basehq00000082",
                "attribute": {}
            },
            {
                "value_type": "BIG_DECIMAL",
                "index_id": "inr-price_change_ratio-sum",
                "attribute": {
                    "win_size": "3"
                }
            }
        ],
        "data": [
            {
                "code": "33:300033",
                "values": [
                    {
                        "idx": 0,
                        "values": [
                            2.0,
                            4.0,
                            5.0
                        ]
                    },
                    {
                        "idx": 1,
                        "values": [
                            120.0,
                            120.1,
                            130.1
                        ]
                    }
                ]
            },
            {
                "code": "33:300034",
                "values": [
                    {
                        "idx": 2,
                        "values": [
                            34.0,
                            44.0,
                            55.0
                        ]
                    },
                    {
                        "idx": 3,
                        "values": [
                            1.0,
                            -2.0,
                            3.0
                        ]
                    }
                ]
            }
        ]
    }
}

五、其他补充
关于Trend 周期的参数说明： 分时取数协议规范： {"time_type":"TREND","start":0,"end":0} 表示取最近的一个交易日的整天的分时数据 {"time_type":"TREND","end":0,"offset":-240} 备注： 分时目前不支持跨天取，超过的offset如果跨天则以当天的为准 {"time_type":"TREND","end":0,"offset":0} 取最新的分时的一条数据 

{"time_type":"TREND","start":{秒级时间戳},"end":{秒级时间戳}} 返回秒级时间戳对应的那一天的分时数据，按照交易所来，以end为准 以上协议只是个规范，并不是所有的指标都支持这种方式的传参

六、yapi 地址
https://yapi.myhexin.com/yapi/service/314766/interface/api/585697

七、指标的attribute
指标 attribute 属性为指标的附加信息说明。

名称	说明	样例
win_size	区间的偏移量，一般用于类似区间涨幅。例如五日涨幅指标的表示：{ "index_id": "inr- price_change_ratio_pct-sum", "time_type":"day_1", "attribute":{ "win_size":5 }}	
related_index_code	表示指标关联的指数代码，比如贡献度指标中，关联的指数代码，表示在该指数下的贡献度数据。如 881101 的指数的成分股的贡献度：{ "index_id":"contribute_point", 'timestamp": 0, "time_type":"snapshot", "attribute":{ "related_index_code":"48: 881101" }	
win_start_timestamp	来表示区间计算起始时间，比如 win_start_timestamp 传 20240101 时间，周期是日线，表示年初至今的涨幅。例如某段时间内的区间涨幅统计："index_id': 'inr-turnover_ratio_pct-sum", "attribute":{ "win_start_timestamp": 1730217600 }, 'timestamp": 1731600000, "time_type":"DAY_1"。其他说明：win_start_timestamp 传 -1 表示从上市日开始	
currency	表示货币属性，不传的话则为证券代码所上市的交易所的货币，传了之后，返回值为对应的货币（根据汇率计算），当前支持：人民币 CNY、美元 USD、港币 HKD、新加坡元 SGD、日元 JPY、加元 CAD、澳元 AUD、英镑 GBP、欧元 EUR。如以港币形式显示综合总市值："index_id": "composite_total_market_value", 'timestamp": 0, 'time_type":"snapshot", "attribute":{ "currency":"HKD" }	
data_auth	标识实时行情和延迟行情，real 标识实时行情，delay 表示延迟行情。如实时行情涨幅："index_id": "inr-turnover_ratio_pct-sum", "attribute": { "data_auth": "real", "timestamp": 0, "time_type": "DAY_1" }

### 【DataAPI】获取（板块成分股、业务标签、prompt2data选股）代码表接口 比如获取同花顺板块成分股、prompt2data选股成分股
一、api 适用场景
面向C端使用的，可以直接通过行情代码获取到对应的成分股，其中包括： 行业、概念、指数， 使用示例：通过行情代码比如 48:884057的方式获取相应的成分股 关于行业、概念、指数的概念可看Tangram对应的研发指南
二、api 的边界说明
1、支持同花顺指数、行业、同花顺概念，同花顺指数等。
2、支持板块服务2.0的板块ID对应成分股获取；
3、支持业务代码表接入获取；
4、支持prompt2data代码表获取；

三、请求协议
头部字段说明
名称	说明	示例
Source-Id	来源业务 id	shareholders
Cookie	用户的 cookie	需根据实际情况填写
Platform	来源平台	PC/APP等

接口字段说明
所有参数细节说明
代码筛选器
    include ： code_selector数组，得到的代码进行合并
    exclude： code_selector数组,里面的代码合并后，作为排除的代码列表
    intersection: code_selector数组，里面的代码交集
    最后筛选出来的代码为。{include} + {intersection} - {exclude}
code_selector: 代码筛选器，主要是用于确定证券代码列表
    type: 支持stock_code,market_code,block_code,tag 等模式，其中
    values: 根据type传递不同的数组，如果是stock_code，传递的是类 33:300033 {market}:{code} 的模式，block_code为板块服务，tag表示业务开发过程中生成的代码列表，比如热榜列表等
 


请求样例：

筛选规则为：
include： 48:884222的成分股 加上48:884217的成分股 + 33市场的成分股得到集合A
intersection： 48:884228 的成分股 和 48:884039 成分股  和 17市场的成分股  取交集 得到 集合B
exclude： 48:884507的成分股 和 22 和 21 的成分股取并集（这里跟include集合的算法一样） 得到集合C

最终的结果代码集合是： 集合A的成分股 加上 集合B的成分股 减去 集合C的成分股
{
    "include": [
        {
            "type": "hq_block_code",
            "values": [
                "48:884222",
                "48:884217"
            ]
        },
        {
            "type": "market_code",
            "values": [
                "33"
            ]
        }
    ],
    "intersection": [
        {
            "type": "hq_block_code",
            "values": [
                "48:884228",
                "48:884039"
            ]
        },
        {
            "type": "market_code",
            "values": [
                "17"
            ]
        }
    ],
    "exclude": [
        {
            "type": "hq_block_code",
            "values": [
                "48:884507"
            ]
        },
        {
            "type": "market_code",
            "values": [
                "22",
                "21"
            ]
        }
    ]
}

四、返回协议
返回字段说明
codes: 返回的代码表

返回样例
{
    "status_code": 0,
    "status_msg": "success",
    "data": {
        "codes": [
            "33:300033",
            "33:300034"
        ]
    }
}

五、yapi 地址
https://yapi.myhexin.com/yapi/service/314766/interface/api/618772

六、其他补充
DataAPI-代码表中的CodeSelector 说明 | 类型 | 说明 | 示例 | | --- | --- | --- | | stockcode | 已经是代码维度，成分股即为自己。 | 33:300033成分股就是33:300033，{"type":"stock_code","values":["33:300033"]} | | block_code | 板块后台针对板块的唯一标识，由一个十六进制的字符串标识，例如: C199。 | C199，可看板块 2.0 服务的文档:【#】已支持板块说明，{"type":"block_code","values":["E"]} | | market_code | 行情市场 | {"type":"market_code","values": ["33"]} 代表33市场下的股票 | | hq_block_code | 区分 block_code，一般指带有行情数据的板块对应的行情代码。 | 48:884507，https://dq.10jqka.com.cn/fuyao/sjht_concept_block/block/v1/list_block_code 请求样例：{"type":"hq_block_code","values": ["48:885431"]} | | tag | 一些业务方自己定义的板块。 | 比如:spec_index表示估值掘金精选指数列表，所有的tag可在tangram上查看到，表示 tag为lhb的从1706112000 到 1706112000 的代码总和：{"type":"tag", "values":["lhb"], "end":"1706112000", "start":"1706112000"} ,如果是动态参数，比如某个板块下的某些业务标签，可以使用动态传参的模式，形式为：动态tag，类似：split{你的业务名，不带下划线，避免影响分割}_48:885431 | | prompt_code | 根据 prompt2data 得到的代码表。 | {"type":"prompt_code","values":["671b1fb3f72e0839cbe7b454"]}，该请求的id和Source-Id需要申请，不然不可访问 | | self_block_code | 板块后台针对板块的唯一标识，由一个十六进制的字符串标识，例如: C199。 | 传递该type不会转化为对应的成分股，而是直接就是该板块的数据，比如总市值是C199的总市值。该type不能与上面的type在同一个请求存在，标的不一样，上面的都为行情代码，而该type为板块服务的ID暂未在DataAPI中生效，占位。 | | custom_type 处理 | 特殊的tag标签，不解析由各个业务。 | 比如:查一种关联关系的所有数据，这个时候不传code，那么请求参数为:{"type": "custom_type", "values":["ALL"]} |


### 【DataAPI】证券关联关系 比如获取指数关联ETF相关数据等（暂无）

### 【DataAPI】证券实体标签服务 证券实体标签服务（暂无）

3-2、如何查看DataAPI支持指标
需要用户进入tangram平台查询确认，提供指标对应的dataapi-id。查看是否支持DataAPI

举例：一个常规的表格式接口的拼接规则：

{
    "indexes": [
        {
            "index_id": "security_name",
            "attribute": {
                "win_size": "20"
            },
            "timestamp": 0,
            "time_type": "DAY_1"
        }
    ],
    "code_selectors": {
        "include": [
            {
                "type": "stock_code",
                "values": [
                    "33:300033",
                    "33:000506"
                ]
            }
        ]
    },
    "page_info": {
        "page_begin": 0,
        "page_size": 100
    },
    "sort": [
        {
            "idx": 0,
            "type": "DESC"
        }
    ]
}

示例： 收盘价中， index_id 为 close_price , time_type 支持的为 DAY_1 ， WEEK_1 等

查看DataAPI的相关参数

3-3、如何登记需求
Tangram平台需求登记

3-4、 DataAPI的Header头：
platform:hevo
Source-Id:PC