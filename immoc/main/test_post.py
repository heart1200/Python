#coding:utf-8
import requests
import json
cookies = {
	"apsid":"M5M2Q3YzBkOGVjYzdkYzE3OTM4M2IwYzIwYjRkMWYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTI0OTE5MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADM0NTBiMTk0NjIwM2U3NGQ5Mzk4OTFjNzAyNjI1ZjhjZN8HWmTfB1o"
}
list_data = json.dumps([{"goods_id":"346","type":"1","type_id":"131","status":"1","price":"388.00","ios_price":"388.00","service_lifetime":0,"open_discount":"0","discount_start_time":"1503936000","discount_end_time":"1503936000","discount_price":"0.00","discount_type":"0","code_white_list":10001,"using_discount":"false","pay_price":"388.00","code":0},
	{"goods_id":"362","type":"1","type_id":"136","status":"1","price":"366.00","ios_price":"366.00","service_lifetime":90,"open_discount":"0","discount_start_time":"1505232000","discount_end_time":"1505232000","discount_price":"0.00","discount_type":"0","code_white_list":10001,"using_discount":"false","pay_price":"366.00","code":0}]
)
data = {
	"uid":"5249191"
	}
url = "https://m.imooc.com/api/user/ajaxusercheck?uid=5249191"
res = requests.delete(url=url,data=data,verify=False).text
print res
