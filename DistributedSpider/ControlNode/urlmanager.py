#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__title__=''
__author__ = 'w'
__mtime__='9/16/18'
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