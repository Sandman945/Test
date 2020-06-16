# coding=utf-8
import unittest
from Busniess.Business import Login


class Test(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print('over')

    # 正确登录的测试用例
    def test_001(self):
        login = Login()
        login.login_yhd('3800042', '06040057')
        data = login.get_text('css', '#side-menu > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)')
        self.assertEqual('基本信息', data)

    # 没有输账号密码直接点击登录的测试用例
    def test_002(self):
        login = Login()
        login.login_yhd('', '')
        data = login.get_text('xpath', ".//*[@id='username-error']")
        self.assertEqual('请输入您的用户名', data)

    # 随意输入账号，不输入密码的测试用例
    def test_003(self):
        login = Login()
        login.login_yhd('hgvjchgc', '')
        data = login.get_text('xpath', ".//*[@id='password-error']")
        self.assertEqual('请输入的密码', data)

    # # 用于演示出bug的测试用例
    # def test_004(self):
    #     login = Login()
    #     login.login_yhd('hgvjchgc', '')
    #     data = login.get_text('id', 'error_tips')
    #     # 我们故意写错预期结果，让这个断言抛出
    #     self.assertEqual('请输入密码itcast', data)


# if __name__ == '__main__':
#     unittest.main()
#     # # 创建测试套件
#     # suit = unittest.TestSuite()
#     # # 定义要是用的测试用例列表
#     # case_list = ['test_002', 'test_003']
#     # # 遍历测试用例列表
#     # for case in case_list:
#     #     # 将测试用例添加到测试套件中
#     #     suit.addTest(Test(case))
#     # # 运行Runner执行测试，verbosity=2指定为每个测试用例生成报告，run中传入要执行的测试套件
#     # unittest.TextTestRunner(verbosity=2).run(suit)
