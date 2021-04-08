#coding=utf-8
from suds.client import Client
class WebserviceTest:
	def __init__(self,url):
		self.client = Client(url)

	def get_methods_name(self):
		'''
		获取所有方法名称
		'''
		method_list = []
		for i in self.client.wsdl.services[0].ports[0].methods:
			method_list.append(i)
		return method_list

	#获取方法参数
	def get_method_parame(self,method_name):
		method = self.client.wsdl.services[0].ports[0].methods[method_name]
		input_parames = method.binding.input
		parames = input_parames.param_defs(method)[0]
		return parames[1].name,parames[1].type[0]
	
	def run_main(self):
		for method in self.get_methods_name():
			func = getattr(self.client.service,method)
			print func('122.122.122.2')


if __name__ == '__main__':
	url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
	web = WebserviceTest(url)
	#name = web.get_methods_name()[0]

	print web.run_main()