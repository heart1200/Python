#coding=utf-8
import requests
import json
url = 'http://127.0.0.1:4444/wd/hub/session/'
data = json.dumps({
	"capabilities":{
		"browserName":"chrome"
		}
})
session = requests.post(url,data).json()['sessionId']

base_url = url+session
get_url = base_url+"/url"
get_url_data = json.dumps({
	"url":"http://www.baidu.com"
})
requests.post(get_url,get_url_data)