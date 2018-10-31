#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__title__=''
__author__ = 'w'
__mtime__='9/16/18'
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

