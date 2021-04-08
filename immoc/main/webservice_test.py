#coding=utf-8
import time
from suds.client import Client
url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
client = Client(url)
def get_methods_name():
	method_list = []
	for i in client.wsdl.services[0].ports[0].methods:
		method_list.append(i)
	return method_list
#print ()
#print client.service   getCountryCityByIp()
for i in get_methods_name():
	print i
	time.sleep(5)
	func = getattr(client.service,i)
	print func('112.212.121.2')