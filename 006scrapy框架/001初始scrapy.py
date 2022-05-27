
# scrapy框架  功能：1.高性能的持久化存储  2.异步的数据下载  3.高性能的数据解析  4.支持分布式

# scrapy的使用  安装：pip install scrapy

# 1.创建scrapy的工程：scrapy startproject  项目名称
# 2.切到---项目名称---文件夹   在spiders文件夹下创建爬虫文件
#   命令：scrapy  genspider  文件名称  www.xx.com
# 3.执行工程：scrapy crawl 文件名称


# 1.创建scrapy的工程：scrapy startproject  项目名称     生成的树结构
#                 firstTest
#                     ├── firstTest
#                     │   ├── __init__.py
#                     │   ├── items.py
#                     │   ├── middlewares.py
#                     │   ├── pipelines.py
#                     │   ├── settings.py
#                     │   └── spiders
#                     │       ├── __init__.py
#                     └── scrapy.cfg

# 2.切到---项目名称---文件夹   在spiders文件夹下创建爬虫文件
#   命令：scrapy  genspider  文件名称  www.xx.com     在项目名称文件夹下的项目名称问价加下的spiders下生成  文件名称.py
#   变成一下的树结构
#                 firstTest
#                     ├── firstTest
#                     │   ├── __init__.py
#                     │   ├── items.py
#                     │   ├── middlewares.py
#                     │   ├── pipelines.py
#                     │   ├── settings.py
#                     │   └── spiders
#                     │       ├── __init__.py
#                     │       └── first.py     执行完 2 的名令会生成新文件
#                     └── scrapy.cfg

# 3.执行工程：scrapy crawl 文件名称

# 1.项目firstTest是scrapy简单使用， 爬虫文件first.py 和settings.py 文件的说明及使用
# 2.项目testWeibo是scrapy简单使用， 爬取微博数据 并解析 并存储到本地指定的文件中
# 3.scrapy的s数据持久化存储：
#     一.基于终端指令：
#             命令：scrapy crawl 爬虫文件名称 -o  路径/文件名.类型
#             例子：在 scrapytestWeibo下面执行 crawl weibo -o ./data/weibo.csv      会在testWeibo下面创建文件及目录
#             类型：只能是这几种 ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
#             要求：只可以将 爬虫文件中parse方法 的返回值存储到本地文本文件中
#             优点：简介高效便捷
#             缺点：局限性比较强（只能存储在本地指定的文件后缀名中）
#     二.基于管道：
#             编码流程：
#               1.数据解析
#               2.在item类中定义相关的属性
#               3.将解析到的数据封装存储到item类型的对象中
#               4.将item类型的对象提交给管道进行数据持久化存储操作
#               5.在管道process_item中要将其接收到的item对象中存储的数据进行持久化存储操作
#               6.在配置文件settings.py中开启管道
#      三.将爬取的数据一份存储到本地xx.csv中，一份存储到数据库中
#              分析: 管道文件中一个管道类对应的是将数据存储到一个平台
#                   爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
#                   process_item中的  return item   表示将item传递给下一个即将被执行的管道类
#
#              方法：settings.py 的字典ITEM_PIPELINES 中添加一个 管道类配置 ，
#                   在pipelines.py中添加一个管道类类 把数据存到数据库
