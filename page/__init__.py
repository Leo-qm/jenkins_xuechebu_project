"""
元素统一文件
"""
from selenium.webdriver.common.by import By

# 首页页面
mine = By.XPATH, '//*[contains(@text, "我的")]'  # 我的

# 我的页面
login = By.XPATH, '//*[contains(@text, "登录")]'  # 登录/注册
username = By.ID, 'com.bjcsxq.chat.carfriend:id/mine_username_tv'  # 用户昵称

# 登录页面
user = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'  # 账号
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
confirm_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/btn_neg'  # 弹窗确认按钮
