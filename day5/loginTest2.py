import unittest

import time
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day5.page_object.loginPage import LoginPage
from day5.page_object.memberCenterPage import MemberCenterPage


class LoginTest2(MyTestCase):
    def test_login(self):
        # driver = self.driver
        # driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # driver.find_element(By.NAME,"username").send_keys("bernice")
        # driver.find_element(By.NAME,"password").send_keys("lyx123")
        # old_title = driver.title
        # driver.find_element(By.NAME,"password").submit()
        # time.sleep(5)
        # #通过判断导航栏中是否存在用户名，从而判断 登录是否成功
        # welcomTxt = driver.find_element(By.PARTIAL_LINK_TEXT,"您好").text
        #
        # self.assertEqual(welcomTxt,"您好 bernice")

        #现在这个测试用例，把元素定位这样的技术问题和手工测试用例的业务逻辑混合在一个文件中,不利于后期维护
        #我们应该分层处理，有的文件只处理业务逻辑，有的文件只负责元素定位
        #我们这是一个测试用例类，应该只包含测试用例的业务逻辑，把元素定位单独放在其他文件中
        #所以我们的测试用例应该写成这样：

        #1.打开注册页面：
        #要想调用login_page类中封装好的open(),
        #首先必须实例化LoginPage的对象
        login_page = LoginPage(self.driver)

        login_page.open()
        #2.输入用户名：
        login_page.input_username()
        #3.输入密码
        login_page.input_password()
        #4.点击登录按钮
        login_page.click_login_button()

        #5.在会员中心页面，验证用户名是否显示正确

        self.name = "bernice"
        member_center_page = MemberCenterPage(self.driver)
        self.assertEqual(member_center_page.get_welcome_link_Text(),"您好 %s" %self.name)

        #应该把代码写成和手工测试用例一样的感觉
        #这样别人一看你的代码就知道你测试用例设计的业务逻辑对不对

if __name__ == "__main__":
    unittest.main