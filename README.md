## 网络爬虫
### 概述
1. 简述：网络爬虫是(网页蜘蛛、网络机器人)按照一定规则，自动抓取万维网信息的程序或者脚本。
2. 分类：通用爬虫、聚焦爬虫("面向特定主题需求"可以自己筛选有用信息)、增量式爬虫、深层网络爬虫(比如暗网、对提升搜索引擎的覆盖率很重要)。
3. 应用：
    1. 搜索引擎，但是目前的搜索引擎大多提供关键字搜索，难以支持语义查询(人工智能)
    2. 聚焦爬虫，它是可定制的、面向语义需求、内容准确的，但是覆盖范围小
    3. 增量式爬虫：无需重新爬取，只爬取更新数据，因此难点在于去重（例如爬取招聘信息）
    4. 深层网络爬虫：简单的说就是搜索引擎覆盖不到的链接，比如某些论坛的信息只能登陆之后才能抓取(模拟登陆可以解决但是要防反爬机制)
    5. 文件搜索
4. 常见网站：百度、磁力搜、盘搜搜、盘找找
5. 爬虫结构：[[1]](https://www.processon.com/view/link/5bd9c5d2e4b00cdc18c410c5)
### 基础
### 必会知识
- IO编程
- 进程、线程、协程
- 网络编程（TCP、UDP）
- Web前端（会点就行）
- 抓包
- 数据库
### 常用的工具
#### HTTP请求工具
- urllib2/urllib(p2)
- urllib(p3)
- requests(p23)
- httplib/urllib(一般不用，比较复杂)
> 一般学会构造请求头、发送get\post请求、识别响应码、处理cookie、设置代理、重定向和历史消息就OK
#### HTML解析工具
- Firebug(火狐，Chrome也有)
- re正则表达式(字符转义、常用元字符、可匹配重复的限定符、字符集合、分支条件、分组、反义、向后引用、贪婪与非贪婪)
- BeautifulSoup(超好用)
- lxml（Xpath）
#### 数据存储
- json（经常用）
- csv（以，分割字段序列，以某种换行符分割记录）
- urlretrive（多媒体文件抽取）
- MongoDB
- Redis（缓存、去重）
- SQLite
### 爬虫初窥
#### 基础爬虫
- 运行流程：[[2]](https://www.processon.com/view/link/5bd9c5d2e4b00cdc18c410c5)
#### 简单的分布式爬虫
- 运行流程：[[3]](https://www.processon.com/view/link/5bd9c5d2e4b00cdc18c410c5)

#### 动态爬虫
- 例1(http://movie.mtime.com/219640/)解析Ajax网站

分析特征：
http://movie.mtime.com/219640/票房链接
```
http://service.library.mtime.com/
Movie.api?
Ajax_CallBack=true&
Ajax_CallBackType=Mtime.Library.Services&
Ajax_CallBackMethod=GetMovieOverviewRating&
Ajax_CrossDomain=1&
Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F219640%2F&
=201811108674522&
Ajax_CallBackArgument0=219640
```
http://movie.mtime.com/225752/
```
http://service.library.mtime.com/
Movie.api?
Ajax_CallBack=true&
Ajax_CallBackType=Mtime.Library.Services&
Ajax_CallBackMethod=GetMovieOverviewRating&
Ajax_CrossDomain=1&
Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F225752%2F&
t=2018111014317274&
Ajax_CallBackArgument0=225752
```
json 数据
```
var result_2018111014317274 = {
    "value": {
        "isRelease": true,
        "movieRating": {
            "MovieId": 225752,
            "RatingFinal": 7.8,
            "RDirectorFinal": 7.6,
            "ROtherFinal": 7.3,
            "RPictureFinal": 7.5,
            "RShowFinal": 0,
            "RStoryFinal": 7.7,
            "RTotalFinal": 0,
            "Usercount": 2775,
            "AttitudeCount": 1422,
            "UserId": 0,
            "EnterTime": 0,
            "JustTotal": 0,
            "RatingCount": 0,
            "TitleCn": "",
            "TitleEn": "",
            "Year": "",
            "IP": 0
        },
        "movieTitle": "无双",
        "tweetId": 0,
        "userLastComment": "",
        "userLastCommentUrl": "",
        "releaseType": 1,
        "boxOffice": {
            "Rank": 2,
            "TotalBoxOffice": "12.24",
            "TotalBoxOfficeUnit": "亿",
            "TodayBoxOffice": "238.5",
            "TodayBoxOfficeUnit": "万",
            "ShowDays": 33,
            "EndDate": "2018-11-01 00:10",
            "FirstDayBoxOffice": "5472.56",
            "FirstDayBoxOfficeUnit": "万"
        }
    },
    "error": null
};
var movieOverviewRatingResult = result_2018111014317274;

```
- 例二 PhantomeJS(无头浏览器)+Selenium
1. 屏幕捕获（get_screen.js）：https://www.cnblogs.com/5315hejialei/p/6938538.html
2. 网络监控（net_monitor.js）：https://www.cnblogs.com/5315hejialei/p/6938538.html
3. 页面自动化。
4. 破解滑动验证码
5. 动态爬取去哪网http://hotel.qunar.com/策略
### web终端协议分析
#### 网页登陆的POST分析

1. 隐藏表单分析（知乎）
2. 加密数据分析（百度云）
#### 验证码问题
1. IP代理（应对淘宝）
- VPN（实时更换IP，速度快，不稳定）
- IP代理池（稳定，价格高）
- ADSL宽带拨号（断开重连ip会自动变化，效率不高）
2. Cookie登陆（前几年QQ盗号常用）
3. 传统验证码识别（手动输入，tensorflow+OpenCV字体识别）
4. 人工打码（自动识别+人工识别 比如qq超人）
5. 滑动验证码（1使用浏览器模拟鼠标拖动操作2计算图片偏移量3模拟人类拖动鼠标的轨迹）

### 终端协议分析
#### PC客户端抓包分析（各种抓包工具）
#### APP抓包分析（模拟器+Wireshark）
### 突破反爬机制
#### 基于验证码的反爬虫
- 传统验证码、逻辑验证码（1+1=？）、滑动验证码以及更复杂的验证码（例如google），这些都可以用上面突破验证码的方式解决
#### 基于Headers的反爬虫
- UserAgent池
- 禁用Cookie
#### 基于用户行为的反爬虫
- 设置下载延时自动限速
- 代理IP池
- Tor代理
- 分布式下载器Crawlera（要充钱的）
- Google cache 或者 Baidu cache（快照）
### 框架Scrapy、PySpider(支持国产)

## 分布式爬虫爬取百度词条500条数据(无框架版)
### 爬虫结构分析
- 本次爬虫采取主从模式，有一台主机作为控制点，负责管理所有运行网络爬虫的主机，爬虫只需要从控制节点那里接收任务，并把新生的任务提交给控制节点就可以了，在这个过程中不必与其他爬虫进行通信，这种方式简单而且易于管理。但是缺陷在于控制节点就是整个系统的瓶颈，很容易导致系统性能下降。
### 爬虫结构设计
```
DistributedSpider/
├── ControlNode
│   ├── baike_2018_09_17_07_12_1537193564.html
│   ├── dataoutput.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── new_url
│   ├── nodemanager.py
│   ├── old_url
│   └── urlmanager.py
├── __init__.py
├── __init__.pyc
└── SpiderNode
    ├── htmldownloader.py
    ├── htmlparser.py
    ├── __init__.py
    └── spiderwork.py

2 directories, 14 files

```
### 爬虫结构设计说明
- **控制节点**：该节点主要分为URL管理器(urlmanager.py)、数据存储器(dataoutput.py)、控制调度器(nodemanager.py)。
1. URL管理器：我们需要对URL进行去重操作，这里采用set的方法，但是这种方法的缺点是如果直接存储大量的URL链接，尤其是url比较长的时候，很容易内存溢出。所以我们将爬取过(old_url)的url进行MD5处理。字符串经过MD5处理之后，信息摘要长度是128位，可以减少内存消耗。在python中的MD5算法生成的是32位的字符串，由于我们爬取的url较少，MD5的冲突不大，所以只取中间16位即可。然后通过save-process和load-process方法分别保存进度和存储到本地
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__author__ = 'w'
"""
import cPickle
import hashlib
class UrlManager(object):
	def __init__(self):
		self.new_urls = self.loadprogress('new_urls')#未爬取的ＵＲＬ集合
		self.old_urls = self.loadprogress('old_urls')#已爬取的ＵＲＬ集合

	def has_new_url(self):
		'''
		判断是否有未爬取的ＵＲＬ
		:return:
		'''
		return self.new_url_size()!=0

	def new_url_size(self):
		'''
		获取未爬取ＵＲＬ集合的大小
		:return:
		'''
		return len(self.new_urls)

	def get_new_url(self):
		'''
		获取一个未爬取的ｕｒｌ
		:return:
		'''
		new_url = self.new_urls.pop()
		m = hashlib.md5()
		m.update(new_url)
		self.old_urls.add(m.hexdigest()[8:-8])
		return new_url

	def add_new_url(self , url):
		'''
		将新的URL添加到待爬取集合周
		:param url:
		:return:
		'''
		if url is None:
			return
		m = hashlib.md5()
		m.update(url)
		if m.hexdigest()[8:-8] not in self.old_urls and url not in self.new_urls:
			self.new_urls.add(url)

	def add_new_urls(self , urls):
		'''
		将新的URL添加到URL集合中
		:param urls:
		:return:
		'''
		if urls is None or len(urls)==0:
			return
		for url in urls:
			self.add_new_url(url)

	def old_url_size(self):
		'''
	    :param self:
	    :return:
	    '''
		return len(self.old_urls)

	def loadprogress(self , path):
		'''
		从本地加载数据
		:param path:
		:return:
		'''
		if path == None:
			print '无效路径%s'%path
			return
		try:
			with open(path , 'rb') as f:
				temp = cPickle.load(f)
				return temp
		except Exception:
			print '[1]无进度文件,创建%s'% path
		return set()
	def saveprogress(self , path , data):
		'''
		保存进度
		:param path:
		:return:
		'''
		with open(path , 'wb') as f:
			cPickle.dump(data , f)
```
2. 数据存储器：只是简单的将爬取的数据存储到本地的一个HTML文档中
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""

__author__ = 'w'

"""
import codecs
import time

class DataOutPut(object):
	def __init__(self):
		'''
		创建一个数据列表
		'''
		self.filepath = 'baike_%s.html'%(time.strftime('%Y_%m_%d_%H_%M_%s' , time.localtime()))
		self.output_head(self.filepath)
		self.datas = []
	def output_head(self , path):
		'''
		讲HTML的头写进去
		:param path:
		:return:
		'''
		fout = codecs.open(path, 'w', encoding='utf8')
		fout.write("<html><head><meta charset='utf-8'></head><body><table>")
		fout.close()

	def store_data(self , data):
		'''
		用于存储数据
		:param data:
		:return:
		'''
		if data is None:
			return
		self.datas.append(data)
		if len(self.datas)>10:
			self.output_html(self.filepath)
	def output_html(self , path):
		if self.datas is None or path is None:
			return
		fout = codecs.open(path , 'a' , encoding='utf8')
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' % data['title'])
			fout.write('</tr>')
			fout.write('<tr>')
			fout.write('<td>%s</td>'%data['url'])
			fout.write('</tr>')
			fout.write('<tr>')
			fout.write('<td>%s</td>' % data['summary'])
			fout.write('</tr>')
			self.datas.remove(data)

	def output_end(self , path):
		'''
		写文件尾
		:param path:
		:return:
		'''
		with open(path ,'a') as fout:
			fout.write('</table></body></html>')
			fout.close()
```
3. 控制调度器：主要是产生并启动URL管理进程、数据提取进程、数据存储进程，同时维护以下4个队列：url-q(url管理进程将url传递给爬虫节点的通道)、result-q(是爬虫节点将数据返回给数据提取进程的通道)、conn-q(数据提取进程将新的url提交给URL管理进程)、store-q(数据提取进程将数据提交给数据存储进程)
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""

__author__ = 'w'

"""
import urllib2

from DistributedSpider.ControlNode.urlmanager import UrlManager
from DistributedSpider.ControlNode.dataoutput import DataOutPut
from multiprocessing.managers import BaseManager
from multiprocessing import Process , Queue
import time
class NodeManager(object):

	def start_Manager(self , url_q , result_q):
		'''
		创建一个分布式管理器
		:param url_q: url队列
		:param result_q: 结果队列
		:return:
		'''
		#注册 暴露两个队列
		BaseManager.register('get_task_queue', callable=lambda: url_q)
		BaseManager.register('get_result_queue', callable=lambda: result_q)
		manager = BaseManager(address=('' , 8001) , authkey='baike')
		return manager
	def url_manager_proc(self , url_q , conn_q , root_url):
		'''
		url管理进程会将conn_q中取出的url先去重,再交给url管理器处理
		:param url_q:
		:param conn_q:
		:param root_q:
		:return:
		'''
		url_manager = UrlManager()
		url_manager.add_new_url(root_url)
		print root_url
		while True:
			while url_manager.has_new_url():
				new_url = url_manager.get_new_url()
				url_q.put(new_url)
				print 'new_url=',new_url
				print 'old_url=',url_manager.old_url_size()
				if url_manager.old_url_size()>500:
					url_q.put('end')#发出停止抓取的信号
					print '控制节点发出停止的通知'
					url_manager.saveprogress('new_url' ,url_manager.new_urls)
					url_manager.saveprogress('old_url' , url_manager.old_urls)
					return
				try:
					if conn_q.empty():
						urls = conn_q.get()
						print 'conn_q.get()' , urls
						url_manager.add_new_urls(urls)
				except BaseException as e:
					time.sleep(0.1)#延时休息
	def result_solve_proc(self , result_q ,conn_q , store_q ):
		'''
		结果分析进程
		:param result_q:
		:param conn_q:
		:param store_q:
		:return:
		'''
		while True:
			try:
				if not result_q.empty():
					content = result_q.get()
					if content['new_urls']=='end':
						print '结果分析进程收到通知结束'
						store_q.put('end')
						return
					print ';)======>连接',content['new_urls']
					# for url in content['new_urls']:
					# 	conn_q.put(url)
					conn_q.put(content['new_urls'])
					store_q.put(content['data'])

				else:
					time.sleep(0.1)

			except BaseException as e:
				time.sleep(0.1)
	def store_proc(self , store_q):
		'''
		结果存储进程
		:param store_q:
		:return:
		'''
		output = DataOutPut()
		while True:
			if not store_q.empty():
				data = store_q.get()
				if data == 'end':
					print '存储进程收到通知然后结束'
					output.output_end(output.filepath)
					return
				output.store_data(data)
			else:
				time.sleep(0.1)


if __name__=='__main__':
	#创建四个队列
	url_q = Queue()
	result_q = Queue()
	store_q = Queue()
	conn_q = Queue()
	#创建分布式管理器
	node = NodeManager()
	manager = node.start_Manager(url_q , result_q)
	url_manager_proc = Process(target=node.url_manager_proc , args=(url_q , conn_q , 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin'))
	result_solve_proc = Process(target=node.result_solve_proc , args=(result_q , conn_q , store_q))
	store_proc = Process(target=node.store_proc , args=(store_q,))
	#启动
	url_manager_proc.start()
	result_solve_proc.start()
	store_proc.start()
	manager.get_server().serve_forever()


```
- **爬虫节点**：爬虫节点主要包含HTML下载器(htmldownloader.py)、HTML解析器(htmlparser.py)、爬虫调度器(spiderwork.py)。执行流程：爬虫调度器从控制节点中的url-q队列读取url >>--->> 爬虫调度器调用HTML下载器、解析器获取网页内容和新的url >>--->> 爬虫调度器将新的内容和url传入result-q队列返回给控制节点
1. HTML下载器：只是简单的下载功能，注意伪装和反爬
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""

__author__ = 'w'

"""
import requests

class HtmlDownLoader(object):

	def download(self , url):
		'''
		下载HTML
		:param url:
		:return:
		'''
		if url is None:
			return None
		user_Agent = 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/62.0'
		headers = {'user-Agent':user_Agent ,}
		r = requests.get(url , headers=headers)
		if r.status_code == 200:
			r.encoding='utf-8'
			return r.text
		return None

```
2. html解析器：
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""

__author__ = 'w'

"""
import re
import urlparse
from bs4 import BeautifulSoup
import chardet
class HtmlParser(object):
	def parser(self , page_url , page_cont):
		'''
		解析网页内容获取URL和网页内容
		:param page_url:
		:param page_cont:
		:return:
		'''
		if page_cont is None or page_url is None:
			print 'page_html',page_cont,'page_url' , page_url
			return
		soup = BeautifulSoup(page_cont , 'lxml' )
		new_urls = self._get_new_urls(soup , page_url)
		new_page_data  = self._get_new_page_data(soup , page_url)
		return new_urls , new_page_data

	def _get_new_urls(self , soup , page_url):
		'''
		获取当前网页中的词条url
		:param soup:
		:param page_url:
		:return:
		'''
		new_urls = set()
		links = soup.find_all(name='a' , attrs={'href': re.compile(r'^/item/.+')})
		for link in links:
			url = link.attrs['href']
			http = urlparse.urlparse(page_url).scheme
			hostname  = urlparse.urlparse(page_url).hostname
			hosturl = '%s://%s'%(http , hostname)
			new_url = urlparse.urljoin(hosturl , url)
			if new_url not in ['https://baike.baidu.com/item/%E5%92%8F%E6%98%A5?force=1','https://baike.baidu.com/item/%E8%83%A1%E4%B8%96%E6%9D%B0','https://baike.baidu.com/item/Various%20Artists','https://baike.baidu.com/item/%E5%91%A8%E5%85%AD%E5%A4%9C%E7%8E%B0%E5%9C%BA','https://baike.baidu.com/item/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9?force=1','https://baike.baidu.com/item/Troy' , 'https://baike.baidu.com/item/%E7%A6%BB%E5%A9%9A%E5%8D%8F%E8%AE%AE?force=1','https://baike.baidu.com/item/%E7%A7%80%E5%85%B0%C2%B7%E9%82%93%E6%B3%A2%E5%84%BF?force=1' ,'https://baike.baidu.com/item/%E5%A4%A7%E8%A5%BF%E6%B4%8B%E7%9C%81']:
				new_urls.add(new_url)
		return new_urls

	def _get_new_page_data(self , soup , page_url):
		'''
		获取有效数据
		:param soup:
		:param page_url:
		:return:
		'''
		data = {}
		data['url'] = page_url
		title = soup.select("dd[class='lemmaWgt-lemmaTitle-title'] > h1")[0].get_text()
		print title
		data['title'] = title
		summary = soup.select("div[class='lemma-summary']")[0].get_text()
		# if encod=='utf-8' or encod =='UTF-8':
		# 	summary = summary.decode('utf-8' , 'ignore').encode('utf-8')
		# else:
		# 	summary = summary.decode('gb2312' , 'ignore').encode('utf-8')
		data['summary'] = summary
		print summary
		return data

```
3. 爬虫调度器：主要是创建分布式进程
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__author__ = 'w'

"""
from DistributedSpider.SpiderNode.htmldownloader import HtmlDownLoader
from DistributedSpider.SpiderNode.htmlparser import HtmlParser
from multiprocessing.managers import BaseManager
import time
import chardet
class SpiderWork(object):
	def __init__(self):
		'''
		实现分布式进程中的连接工作
		'''
		#①
		BaseManager.register('get_task_queue')
		BaseManager.register('get_result_queue')
		server_address = '127.0.0.1'
		print '连接到%s...........'%server_address
		self.m = BaseManager(address=(server_address , 8001) , authkey='baike')
		self.m.connect()

		self.task = self.m.get_task_queue()
		self.result = self.m.get_result_queue()

		self.downloader = HtmlDownLoader()
		self.parser = HtmlParser()

	def crawl(self):
		while True:
			try:
				if not self.task.empty():
					url = self.task.get()
					if url == 'end':
						print '控制节点通知爬虫节点停止工作'
						self.result.put({'new_urls':'end' , 'data' : 'end'})
						return
					print '爬虫节点正在爬取%s'% url.encode('utf8')
					content = self.downloader.download(url)
					print '爬虫节点正在解析....'
					new_urls , data = self.parser.parser(url , content)
					print new_urls
					print data['title']
					print data['summary']
					print data
					self.result.put({'new_urls':new_urls , 'data':data})
				else:
					print 'waitting....'
					time.sleep(0.1)
			except EOFError:
				print '连接工作节点失败'
				return
			except Exception as e:
				print e
				print 'crawl fail'

if __name__=='__main__':
	spider = SpiderWork()
	spider.crawl()
```
### 总结

爬虫构造思路比较简单，再次基础上可以完善反爬机制，添加数据库，完善去重机制
