#coding:utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,cookies=None):
		res = None
		if cookies !=None:	
			res = requests.post(url=url,data=data,cookies=cookies,verify=False)
		else:
			res = requests.post(url=url,data=data,verify=False)
		return res.json()

	def get_main(self,url,data=None,cookies=None):
		res = None
		if cookies !=None:	
			res = requests.get(url=url,data=data,cookies=cookies,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res.json()

	def put_main(self,url,data,cookies=None):
		res = None
		if cookies !=None:	
			res = requests.put(url=url,data=data,cookies=cookies,verify=False)
		else:
			res = requests.put(url=url,data=data,verify=False)
		return res.json()

	def delete_main(self,url,data,cookies=None):
		res = None
		if cookies !=None:	
			res = requests.delete(url=url,data=data,cookies=cookies,verify=False)
		else:
			res = requests.delete(url=url,data=data,verify=False)
		return res.json()

	def run_main(self,method,url,data=None,cookies=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,cookies)
		elif method == 'put':
			res = self.put_main(url,data,cookies)
		elif method == 'delete':
			res = self.delete_main(url,data,cookies)
		else:
			res = self.get_main(url,data,cookies)
		return json.dumps(res,ensure_ascii=False)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
