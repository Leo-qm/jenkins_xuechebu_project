"""
我的页面
"""
import page
from base.base_page import BasePage


class MinePage(BasePage):
    def click_login(self):
        """点击登录方法"""
        self.click_func(self.find_element_func(page.login))

    def get_username_text(self):
        """获取用户昵称信息"""
        return self.find_element_func(page.username).text
