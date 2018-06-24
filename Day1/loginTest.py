#这个文件用来实现一个登录功能的自动化操作
#1.打开浏览器
import time
from selenium import webdriver
#从谷歌公司的一个项目导入网络驱动，用来操作浏览器
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

#2.打开海盗商城网站
# driver.get("http://localhost")
#3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名和密码
driver.find_element_by_id("username").send_keys("bernice")
driver.find_element_by_name("password").send_keys("lyx123")
#5.点击登录按钮
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功
#现在实现一个自动化注册功能
#Alt+Enter导包快捷键，选Import this name,选最短的time
#time.sleep()这个方法提供了一个固定的时间等待
#这里的意义是点击登录按钮后，等5秒后，再检查用户名是否正常显示
#弊端是，因为网络延迟，不知道是每次等1秒合适还是5秒合适
#解决办法：使用智能等待，替换固定等待

#设置隐式等待：一旦找到页面元素，马上执行后面的语句
#如果超过20秒，仍然找不到页面元素，那么程序将会报超时错误
driver.implicitly_wait(20)

# driver.find_element_by_link_text("您好 bernice")
# time.sleep(5);
username_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text);
#我们可以通过if语句，判断页面显示的文本和预期的文本是否一致，来判断测试用例是否正常执行
if username_text == '您好 bernice':
    print("测试执行通过")
else:
    print("测试执行失败")

#因为selenium 主要做回归测试，所以测试脚本都是pass的，只有开发做了代码变更，我们的测试用例才有可能失败
#一般工作中不用if...else语句做判断，后面讨论详细原因
#7.点击进入商城购物
#xpath有一个缺点，定位元素的可读性比较差
# driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a")
driver.find_element_by_link_text("进入商城购物").click()
#8.在商城主页，输入搜索条件"iphone"
driver.find_element_by_name("keyword").send_keys("iphone")
#9.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#10.在搜索结果页面点击第一个单品的图片
driver.find_element_by_xpath("//div[@class='shop_01-imgbox']//img").click()
#窗口切换
driver.close() #关闭selenium正在工作的窗口
# driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_name("cart_num").clear()//clear Method is unavailable
# time.sleep(5)
driver.find_element_by_name("cart_num").send_keys(Keys.BACK_SPACE)
driver.find_element_by_name("cart_num").send_keys("3")
# #11.点击加入购物车
driver.find_element_by_id("joinCarButton").click()

driver.find_element_by_class_name("shopCar_T_span3").click()

price = driver.find_element_by_xpath("//span[@id='priceTotal']/span").text
print(price)
# expectPrice = 4988*3
#
# if price == expectPrice :
#     print("金额显示正确")
# else:
#     print("金额显示不正确")
# # driver.close();







