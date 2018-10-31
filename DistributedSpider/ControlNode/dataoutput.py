#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
__title__=''
__author__ = 'w'
__mtime__='9/16/18'
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