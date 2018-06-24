# 1.登录海盗商城
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://localhost")
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("username").send_keys("bernice")
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB).send_keys("lyx123").perform();
# driver.find_element_by_id("username").submit()
#文件名，类名，包名，变量名，所有的命名都应该以字母开头，可以有数字和下划线
#但是不能有空格和中文
from Day2.loginTest import Login
driver = webdriver.Chrome()
#每次创建浏览器时，implicitly_wait固定写一次，对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要检测页面的加载时间，检测什么时候页面加载完，什么时候执行后续的操作
driver.implicitly_wait(20)
#实例化对象会占用内存，pycharm会自动帮我们释放内存
#代码运行完，检测到Login()这个对象，不再被使用，系统会自动释放内存
#把dirver浏览器传入到登录方法中
#让登录方法和下面的点击账号
Login().loginWithDefaultUser(driver)
driver.find_element_by_link_text("账号设置").click()
#partial_link_text可以使用链接的一部分进行元素定位
# driver.find_element_by_partial_link_text("账号设置").click()
driver.find_element_by_link_text("个人资料").click()
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("甘家")
# driver.find_element_by_xpath("//input[@id='xb'][@value=2]").click()
#通过cssselector定位元素，只需要在唯一属性两个边加
#单斜杠表示绝对路径，一般都是从/html根节点开始定位元素
#相对路径一般通过元素的特殊属性查找元素
#绝对路径一般通过元素的位置，层级关系查找元素
#绝对路径写起来比较长，涉及到的节点比较多，当开发修改页面布局时，受到影响的可能性比较大
#相对路径，查询速度比较慢，因为可能需要遍历更多的节点
#工作中一般用绝对还是相对？工作中推荐用css_selector
#css_selector的查询速度比xpath快一点
#Css和xpath的可读性比较
#xpath在某些浏览器上支持的不太好，比如 IE8
#css_selector 所有前端开发都会用，易于沟通交流
#*星号表示任意节点
#[@]表示通过属性定位
# driver.find_element_by_css_selector('input[id="xb"][value="0"]').click()
# driver.find_element_by_css_selector('//*[@value="2"]').click()
driver.find_elements_by_id("xb")[1].click()
# driver.execute_script('$("#date").val("2000-01-01")')
# driver.execute_script('$("#date").removeAttr("readonly")')
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("2018-06-03")
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("11111111")
# driver.find_element_by_id("qq").submit()
driver.find_element_by_class_name("btn4").click()

driver.switch_to.alert.accept()