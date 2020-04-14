"""
PO文件基类
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):  # 封装代码过程中, 如果需要驱动对象, 直接编写此方法
        self.driver = driver

    def find_element_func(self, location, timeout=5, poll=.5):
        """
        元素定位方法
        :param location: 元素定位信息
        :param timeout: 超时时长
        :param poll: 定位方法执行间隔
        :return: 元素对象
        """
        # 1. 添加显式等待
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))
        # 2. 返回定位到的元素对象
        return element

    def input_func(self, element, text):
        """
        元素输入方法
        :param element: 元素对象
        :param text: 输入的内容
        :return: 无
        """
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def click_func(self, element):
        """
         元素点击方法
         :param element: 元素对象
         :return: 无
         """
        element.click()

    def get_toast_func(self, text):
        """获取toast信息方法"""
        # 处理传入进来的定位信息
        # xpath = '//*[contains(@text, "再次点击")]' # 文本值不能写死
        xpath = By.XPATH, '//*[contains(@text, "{}")]'.format(text)
        element = self.find_element_func(xpath)  # 调用当前类中的元素定位方法
        return element.text  # 返回目标元素的text属性值

        # element = WebDriverWait(driver, 3, .3). \
        #     until(lambda x: x.find_element_by_xpath('//*[contains(@text, "再次点击")]'))
