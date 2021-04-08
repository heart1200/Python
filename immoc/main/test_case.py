#coding:utf-8
import sys
sys.path.append('E:/www/ImoocInterface')
import unittest
from base.demo import RunMain
import json
import HTMLTestRunner
class TestMethod(unittest.TestCase):
   def setUp(self):
       self.userid=None
       self.run=RunMain()

   def test_02(self):
       url = 'http://coding.imooc.com/api/cate'
       data={
           'timestamp': '1507006626132',
           'uid': '5249191',
           'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
           'secret': '078474b41dd37ddd5efeb04aa591ec12',
           'token': '0b4c502ba647664be04dfedb32ad4f3d',
           'cid': '0'
       }
       res=self.run.run_main(url,'POST',data)
       #print res
       self.assertEqual(res['errorCode'],1000,"测试失败")
       print '这是第一个case'
   #@unittest.skip('test_02')
   def test_01(self):
       url = 'http://coding.imooc.com/api/cate'
       data = {
           'timestamp': '1507006626132',
           'uid': '5249192',
           'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
           'secret': '078474b41dd37ddd5efeb04aa591ec12',
           'token': '0b4c502ba647664be04dfedb32ad4f3d',
           'cid': '0'
       }
       res=self.run.run_main(url,'POST',data)
       self.assertEqual(res['errorCode'], 1000, "测试失败")
       print '这是第二个case'

if __name__=='__main__':
   #suite=unittest.TestSuite()
   #suite.addTest(TestMethod('test_02'))
   #suite.addTest(TestMethod('test_01'))
   #unittest.TextTestRunner().run(suite)
   filepath='../report/htmlreport1.html'
   fp=file(filepath,'wb')
   suite = unittest.TestSuite()
   suite.addTest(TestMethod('test_02'))
   suite.addTest(TestMethod('test_01'))
   runer=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
   runer.run(suite)