#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__title__=''
__author__ = 'w'
__mtime__='9/16/18'
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
