import unittest
from testcase.testcase import Test
from suit_test.HTMLTestRunner import HTMLTestRunner


class Suit(unittest.TestCase):
    def test_suit(self):
        # 创建测试套件
        suit = unittest.TestSuite()
        # 定义要是用的测试用例列表
        case_list = ['test_002', 'test_001', 'test_003']
        # 遍历测试用例列表
        for case in case_list:
            # 将测试用例添加到测试套件中
            suit.addTest(Test(case))
        # # 运行Runner执行测试，verbosity=2指定为每个测试用例生成报告，run中传入要执行的测试套件
        # unittest.TextTestRunner(verbosity=2).run(suit)

        # 生成HTML格式报告步骤
        with open('../report.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='第一个测试报告',
                description='设定测试报告描述',
                verbosity=2
            ).run(suit)


if __name__ == '__main__':
    unittest.main()
