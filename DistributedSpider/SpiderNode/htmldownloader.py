#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__title__=''
__author__ = 'w'
__mtime__='9/16/18'
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
