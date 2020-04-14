"""
统一入口类
"""
from page.index_page import IndexPage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):  # 1. 根据文件名写类名
    def __init__(self, driver):
        self.driver = driver

    def index_page(self):  # 2. 根据页面文件名写方法名
        """首页页面"""
        return IndexPage(self.driver)  # 3. 在方法内直接返回页面对象的实例化操作

    def mine_page(self):
        """我的页面"""
        return MinePage(self.driver)

    def login_page(self):
        """登录页面"""
        return LoginPage(self.driver)
