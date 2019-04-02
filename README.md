# scrapy-mongo-zhihu_user
使用scrapy+mongodb完成对知乎用户详细信息提取
我需要安装什么库函数？
-pymongo和本地mongodb数据库
-scrapy
-twisted

gihub上传图片格式
// ![图片说明1](https://github.com/liuhuakun/BrushShots/blob/master/1.PNG)

怎么开启mongodb?
首先启动Mongod服务器，然后再建立连接服务。

工作流程分析
`以初始的URL初始化Request，并设置回调函数，当该request下载完毕并返回时，将生成response，并作为参数传给回调函数. spider中初始的requesst是通过start_requests()来获取的。start_requests()获取 start_urls中的URL，并以parse以回调函数生成Request 
`在回调函数内分析返回的网页内容，可以返回Item对象，或者Dict，或者Request，以及是一个包含三者的可迭代的容器，返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数
`在回调函数内，可以通过lxml，bs4，xpath,css等方法获取我们想要的内容生成item
`最后将item传递给Pipeline处理


start_url:
这里我们找的账号地址是：https://www.zhihu.com/people/excited-vczh/answers
我们抓取的大V账号的主要信息是：
![知乎样例](https://github.com/ivat4u/scrapy-mongo-zhihu_user/image/997599-20170721023220693-1484269289.png)

利用网页模拟获取关注和粉丝信息
![关注信息](https://github.com/ivat4u/scrapy-mongo-zhihu_user/image/997599-20170721023434521-2059770281.png)

爬虫逻辑（其中strat用户有重复爬取一次粉丝和关注，代码中本人已经修改）
![爬虫逻辑框架](https://github.com/ivat4u/scrapy-mongo-zhihu_user/image/997599-20170724113838477-494118700.png)
