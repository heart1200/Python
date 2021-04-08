#coding=utf-8
import requests
import json
class WebDriver1:
	def __init__(self):
		self.driver = self.get_driver()
	def get_driver(self):
		url = 'http://127.0.0.1:4444/wd/hub/session/'
		data = json.dumps({
			"capabilities":{
				"browserName":"chrome"
				}
		})
		session = requests.post(url,data).json()['sessionId']
		driver = url+session
		return driver

	def get(self,url):
		get_url = self.driver+"/url"
		get_url_data = json.dumps({
			"url":url
			})
		requests.post(get_url,get_url_data)
	#id:kw
	def find_element_by_id(self,id):
		get_element = self.driver+"/element"
		get_element_data = json.dumps({
			"using":"id",
			"value":id
			})
		element = requests.post(get_element,get_element_data).json()
		return element['value']['ELEMENT']

	#输入
	def send_keys(self,element,value):
		get_url = self.driver+"/element/"+element+"/value"
		get_send_data = json.dumps({
			"value":[value]
			})
		requests.post(get_url,get_send_data)

if __name__ == '__main__':
	driver = WebDriver1()
	driver.get("http://www.baidu.com")
	element = driver.find_element_by_id("kw")
	driver.send_keys(element,"selenium")
