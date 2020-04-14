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

    def login_func(self, name, password):
        """登录方法"""
        self.input_user(name)  # 输入用户名
        self.input_pwd(password)  # 输入密码
        self.click_login_btn()  # 点击登录按钮
        self.click_confirm_btn()  # 点击确认按钮
