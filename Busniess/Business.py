from Commonlib.Commonlib import Commonshare


class Login(Commonshare):
    def login_yhd(self, user, pwd):
        self.open_url('http://mer.shuamachina.com/login')
        # 输入账号
        self.input_data('css', 'input.form-control:nth-child(3)', user)
        # 输入密码
        self.input_data('css', 'input.form-control:nth-child(4)', pwd)
        # 点击登陆
        self.click('id', 'btnSubmit')


if __name__ == '__main__':
    login = Login()
    login.login_yhd('3800042', '06040057')
