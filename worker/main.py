# -*- coding: utf-8 -*-
import yaml
import logging
from ruc.reducedPattern import reducedPattern

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def Run():
	options = makeOptions()
	reduced_pattern = reducedPattern(options)
	download = reduced_pattern.download()

def makeOptions():
	file = open('config/config.yml', 'r')
	config = yaml.load(file)
	if (config is None):
		raise Exception('Config file not found or format error.')

	options = {}
	options['url'] = config['sunat']['url']
	options['zip_path'] = config['paths']['zip']
	options['unzip_path'] = config['paths']['unzip']
	options['ext'] = config['paths']['ext']
	return options

if __name__ == '__main__':
	try:
		Run()
	except Exception as e:
		msg = 'Error: %s' % (e)
		logging.error(msg)