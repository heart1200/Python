import json

import requests

url_cate = 'http://coding.imooc.com/api/cate'
data_cate = {
    'timestamp': '1507034803124',
    'uid': '5249191',
    'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
    'secret': '078474b41dd37ddd5efeb04aa591ec12',
    'token': '7d6f14f21ec96d755de41e6c076758dd',
    'cid': '0',
    'errorCode': 1001
}


def test_requests_post(url, data):
    # post请求
    # res = requests.post(url=url, data=data).json()
    # return json.dumps(res)

    # get请求
    res = requests.get(url=url, data=data).json()
    return json.dumps(res, indent=2, sort_keys=True)


print(test_requests_post(url_cate, data_cate))
