import json

import requests


class RunMain:
    def __init__(self, url, method, data=None):
        self.res = self.run_main(self, url, method, data)

    def test_requests_post(self, url, data):
        res = requests.post(url=url, data=data)
        if res is not None:
            return json.dumps(res.json(), indent=2, sort_keys=True)
        else:
            return None

    def test_requests_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    # get请求，不一定需要data，所以默认为空
    def run_main(self, url, method='GET', data=None):
        method_lower = method.lower()
        if method_lower == 'post':
            return self.test_requests_post(url, data)
        if method_lower == 'get':
            return self.test_requests_get(url, data)
        else:
            return 'method is wrong'


if __name__ == '__main__':
    url_cate = 'http://coding.imooc.com/api/cate'
    url_test = 'https://www.baidu.com/sugrec?prod=pc_his&from=pc_web&json=1&sid=\
    33812_33751_33344_31254_33781_33760_33676_33714_26350_22159_33794&hisdata=&_t=1617328420907&csor=0 '
    data_cate = {
        'timestamp': '1507034803124',
        'uid': '5249191',
        'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
        'secret': '078474b41dd37ddd5efeb04aa591ec12',
        'token': '7d6f14f21ec96d755de41e6c076758dd',
        'cid': '0',
        'errorCode': 1001
    }
    run = RunMain(url_test, 'get')
    # print(run.res)

# print(run_main(url_test, 'get'))
# print(run_main(url_cate, 'POST', data_cate))
# print("This is post \n" + test_requests_post(url_cate, data_cate) + '\n')
# print("This is get \n" + test_requests_get(url_cate, data_cate) + '\n')
