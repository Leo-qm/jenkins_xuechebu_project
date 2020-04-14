"""
首页页面
"""
import page
from base.base_page import BasePage


class IndexPage(BasePage):  # 1. 根据文件名创建类名(继承自基类)

    def click_mine(self):  # 2. 将元素的操作与属性组成封装方法名
        """点击我的方法"""
        # 3. 调用基类方法完成元素定位及操作
        self.click_func(self.find_element_func(page.mine))
