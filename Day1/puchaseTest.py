#这个文件用来实现一个登录功能的自动化操作
#1.打开浏览器
from selenium import webdriver
#从谷歌公司的一个项目导入网络驱动，用来操作浏览器
driver = webdriver.Chrome()
driver.get("http://localhost")
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("bernice")
driver.find_element_by_name("password").send_keys("lyx123")
driver.find_element_by_class_name("login_btn").click()
driver.find_element_by_link_text("您好 bernice")

driver.get("http://localhost/index.php")
driver.find_element_by_xpath("//div[@class='module_pro']//img").click()

driver.find_element_by_name("cart_num").send_keys(3);


