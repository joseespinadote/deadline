# coding=utf-8
#!/usr/bin/python

from datetime import datetime
import urllib2

strDeadlineDate = '2017,5,6'

def checkDeadline() :
	webRequest = urllib2.Request('http://just-the-time.appspot.com/?f=%Y,%M,%d')
	try:	
		return datetime.strptime(urllib2.urlopen('http://just-the-time.appspot.com/?f=%Y,%m,%d').read(), '%Y,%m,%d') < datetime.strptime(strDeadlineDate, '%Y,%m,%d')
	except Exception:
		return datetime.now() < datetime.strptime(strDeadlineDate, '%Y,%m,%d')
	return False