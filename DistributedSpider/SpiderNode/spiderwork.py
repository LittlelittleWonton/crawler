#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__title__=''
__author__ = 'w'
__mtime__='9/17/18'
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