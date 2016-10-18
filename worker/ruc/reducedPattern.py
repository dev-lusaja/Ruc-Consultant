# -*- coding: utf-8 -*-
import os
import time
import urllib2
import logging
import zipfile

class reducedPattern(object):

	def __init__(self, options):
		self.url = options['url']
		self.zip_path = options['zip_path']
		self.unzip_path = options['unzip_path']
		self.ext = options['ext']
		self.date = time.strftime("%Y%m%d")
		self.zip_file =os.path.join(self.zip_path, self.date + self.ext)
		self.unzip_file = os.path.join(self.unzip_path, self.date)


	def download(self):
		if self.fileNotExists(self.zip_file):
			response = urllib2.urlopen(self.url)
			zipcontent = response.read()
			with open(self.zip_file, 'w') as f:
				f.write(zipcontent)
			msg = "File Downloaded %s in %s" % (self.zip_file, self.zip_path)
			logging.warning(msg)
		else:
			msg = "The file %s exists in %s" % (self.zip_file, self.zip_path)
			logging.warning(msg)
		self.unzip()


	def fileNotExists(self, file):
		return not os.path.exists(file)


	def unzip(self):
		if self.fileNotExists(self.unzip_file):
			zip_ref = zipfile.ZipFile(self.zip_file, 'r')
			zip_ref.extractall(self.unzip_file)
			msg = "File Unziped %s in %s" % (self.unzip_file, self.unzip_path)
			zip_ref.close()
			logging.warning(msg)
		else:
			msg = "The unzip file %s exists in %s" % (self.unzip_file, self.unzip_path)
			logging.warning(msg)
		