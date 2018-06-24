#1、打开主页
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost")
# driver.get("http://localhost/index.php?m=user&c=public&a=login")
# driver.find_element_by_id("username").send_keys("bernice")
# driver.find_element_by_id("password").send_keys("lyx123")
#2、点击登录按钮
# driver.find_element_by_class_name("login_btn").click()
driver.find_element_by_link_text("登录").click()
#3、在搜索框中输入Iphone
driver.find_element_by_name("keyword").send_keys("iphone")
#如果我们想在新的标签页上操作页面元素，怎么办？
#需要进行窗口切换
#driver.switch_to.window(第二个窗口的名字)
#seleium提供了浏览器中所有窗口名字的集合
#handle是句柄的意思，把句柄理解为名字就可以了
#driver.window_handes可以理解为是一个数组
#[1]表示数组的第二个元素
#所以，第二个窗口的名字既是 driver.window_handles[1]
#所以，窗口切换的语句就是:
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name("keyword").send_keys("iphone")
#这就是窗口切换的方法
#[1]表示第二个元素,[-1]表示最后一个元素
#在python中元组和列表可以正着从0开始数
#可以负着从-1开始数，倒数第一个-1，倒数第二个-2
















