#!/usr/bin/env python3

import time
import re
import requests
from lxml import etree

osearch_templates = {
	'DuckDuckGo': 'https://duckduckgo.com/ac/?q={}&type=list',
	'Google': 'http://suggestqueries.google.com/complete/search?output=firefox&q={}',
	'Bing': 'http://api.bing.com/osjson.aspx?query={}',
	'Yahoo': 'https://search.yahoo.com/sugg/os?command={}&output=fxjson&fr=opensearch'
}

def opensearch_ihate(template, ethnicity):
	q = 'I hate ' + ethnicity
	json = requests.get(template.format(q)).json()
	suggestions = json[1]
	for suggestion in suggestions:
		rex = re.escape(q)
		if re.fullmatch(rex, suggestion, re.IGNORECASE):
			return True

	return False

def get_ethnicities():
	html = requests.get('https://en.wikipedia.org/wiki/List_of_contemporary_ethnic_groups').content
	html = etree.HTML(html)
	tbody = html.xpath('//div[@id="mw-content-text"]/table[1]')[0]
	ret = tbody.xpath('./tr[position() > 1]/td[1]/a/text()')
	return ret

def main():
	ethnicities = get_ethnicities()

	for ethnicity in ethnicities:
		ihate = []
		for name, template in osearch_templates.items():
			if opensearch_ihate(template, ethnicity):
				ihate.append(name)

		ihate = ' '.join(ihate)
		print('I hate {}: {}'.format(ethnicity, ihate))

	religions = [
		'Catholics',
		'Christians',
		'Atheists',
		'Jehovah\'s Witnesses',
		'Muslims',
		'Hindu',
		'Buddhists',
		'Lutherans',
		'Baptists',
		'Religion',
		'Sunnis',
		'Shiites'
	]

	for religion in religions:
		ihate = []
		for name, template in osearch_templates.items():
			if opensearch_ihate(template, religion):
				ihate.append(name)

		ihate = ' '.join(ihate)
		print('I hate {}: {}'.format(religion, ihate))

if __name__ == '__main__':
	main()
