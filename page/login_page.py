"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    def input_user(self, name):
        """输入用户名方法"""
        self.input_func(self.find_element_func(page.user), name)

    def input_pwd(self, password):
        """输入密码方法"""
        self.input_func(self.find_element_func(page.pwd), password)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.click_func(self.find_element_func(page.login_btn))

    def click_confirm_btn(self):
        """点击弹窗确认按钮方法"""
        self.click_func(self.find_element_func(page.confirm_btn))

    # 注意: 如果想要在测试用例中少调用方法, 也可以考虑在封装完元素之后,
    # 单独封装一个方法来组装所有元素, 形成一个测试方法
    def login_func(self, name, password):
        """登录方法"""
        self.input_user(name)  # 输入用户名
        self.input_pwd(password)  # 输入密码
        self.click_login_btn()  # 点击登录按钮
        # self.click_confirm_btn()  # 点击确认按钮

    def get_login_toast(self, text):
        """获取登录页面toast信息方法"""
        # 调用基类获取 toast方法时, 需要添加返回值, 否则当前方法被调用时, 调用处获取不到元素的文本信息
        return self.get_toast_func(text)
