#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
response = requests.get('https://www.imooc.com/').content
html_text = BeautifulSoup(response,"html.parser")
#print html_text.findAll(attrs={"class":"shizhan-intro-box"})
#main > div:nth-child(3) > div > div > div:nth-child(1) > a > div.course-card-content > h3
courses = html_text.select('#main > div:nth-of-type(3) > div > div > div > a > div.course-card-content > h3')
nums = html_text.select('#main > div:nth-of-type(3) > div > div > div > a > div.course-card-content > div > div.course-card-info > span:nth-of-type(3)')
moneys = html_text.select('#main > div:nth-of-type(3) > div > div > div > a > div.course-card-content > div > div.course-card-price')
for course,num,money in zip(courses,nums,moneys):
	data = {
	'course_name:':course.get_text(),
	'number:':num.get_text(),
	'money:':money.get_text()
	}
	print data
test = ["this is test ,please {} ask me you name".format(str(i)) for i in range(1,5)]
print test
#get_text()获取文字
#get('src')获取某个标签的属性信息
#stripped_string  获取父标签下的所有子标签文本信息
#定位信息div.property_title>a[target="_blank"]
#定位title信息 soup.title.text
#for course in html_text.select('.shizhan-intro-box'):
#	print course.select(".shizan-name")[0]
#	break
