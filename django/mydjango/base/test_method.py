import json
import unittest

from django.mydjango.base.request_test import RunMain

url_cate = 'http://coding.imooc.com/api/cate'
url_test = 'https://www.baidu.com/home/xman/data/tipspluslist?indextype=manht&_req_seqid=0x8b814a890008fe7' \
           '6&asyn=1&t=1617421662161&sid=33839_33638_33747_33344_31660_33782_33675_33392_26350 '
data_cate = {
    'timestamp': '1507034803124',
    'uid': '5249191',
    'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
    'secret': '078474b41dd37ddd5efeb04aa591ec12',
    'token': '7d6f14f21ec96d755de41e6c076758dd',
    'cid': '0',
    'errorCode': 1001
}


class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("cls setUp is running")

    @classmethod
    def tearDownClass(cls):
        print("cls tearDown is running")

    def setUp(self):
        self.run = RunMain()
        print("setUP is running")

    def tearDown(self):
        print("tearDown is running")

    def test_01(self):
        res = json.loads(self.run.run_main(url_test, 'get'))
        self.assertEqual(res['errNo'], '403', '测试失败')

    def test_02(self):
        res = json.loads(self.run.run_main(url_cate, 'post', data_cate))
        self.assertEqual(res['errorCode'], 1007, '测试失败')


if __name__ == '__main__':
    unittest.main
