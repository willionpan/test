# coding: utf8

import datetime

with open('a.txt', 'w') as f:
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	f.write(now)