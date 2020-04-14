"""
登录测试用例
"""
import allure
import pytest

from page.page_factory import PageFactory
from utlis import get_driver


class TestLogin(object):
    """登录测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = get_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 实例化统一入口类
        yield  # 结束工作
        self.driver.quit()

    def test_login(self):
        """登录测试方法"""
        # 成功登录
        # self.page_factory.index_page().click_mine()  # 点击我的
        # self.page_factory.mine_page().click_login()  # 点击登录/注册
        # self.page_factory.login_page().login_func('13157523435', 'lm123456')  # 登录
        # self.page_factory.login_page().click_confirm_btn() # 点击登录提示确定按钮
        # # 断言
        # username_text = self.page_factory.mine_page().get_username_text()
        # assert '3435' in username_text

        # 未注册
        self.page_factory.index_page().click_mine()  # 点击我的
        self.page_factory.mine_page().click_login()  # 点击登录/注册
        self.page_factory.login_page().login_func('13800001111', 'lm123456')  # 登录

        try:
            # 断言
            toast_msg = self.page_factory.login_page().get_login_toast('账号还未注册')
            assert '账号还未注册' in toast_msg

        except AssertionError as e:  # AssertionError: 为断言失败异常类型

            # 给 allure 报告添加截图(断言失败时进行截图操作)
            self.driver.get_screenshot_as_file('./screenshot/info.png')
            # rb: 以二进制方式读取
            with open('./screenshot/info.png', 'rb') as f:
                # allure.MASTER_HELPER.attach('文件名称', 文件内容, 文件类型)
                allure.MASTER_HELPER.attach('my_info', f.read(), allure.MASTER_HELPER.attach_type.PNG)

            raise e  # 当截图操作完成后, 应该还原测试用例的真实结果, 因此需要再主动抛出异常
