import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("http://localhost")
#点击“登录”链接
#用javascript的方法找登录链接的代码：
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用Selenium的方法找登录链接的代码
#driver.find_element_by_link_text("登录")
#通常，用selenium的方法找元素比js更容易
#但是selenium找到登录链接和js找到的是同一个元素
#我们可不可以把selenium找到的这个元素代入到js方法里，代替原来的js定位
login_link=driver.find_element_by_link_text("登录")
#arguments参数的复数形式,[0]表示第一个参数，指的就是js后面的login_link
#所以下面这句代码，相当于把driver.find_element_by_link_text("登录")带入到js语句中
#变成了driver.find_element_by_link_text("登录").removeAttribute('target')
#arguments是参数数组，指的是js字符串后面的所有参数
#一般情况下我们只会用到argument[0],即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')", login_link)
login_link.click()
#登录
driver.find_element_by_id("username").send_keys("bernice")
ActionChains(driver).send_keys(Keys.TAB).send_keys("lyx123").send_keys(Keys.ENTER).perform()
#返回商城首页
driver.find_element_by_link_text("进入商城购物").click()
#搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#复制出来的css往往比较长，我们可以适当的缩写长度
#我们定位元素的目标节点是最后一个节点
#大于号>的前面是父节点，后面是子节点
#每个节点的第一个单词是标签名，比如a,div,body
#小数点后面表示class属性
#:nth-child(2),nth表示第n个， child表示子节点
#所以，:nth-child(2)表示当前标签是它的父节点的第二个子节点
product_link_xpath = driver.find_element_by_css_selector("div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a")
# product_link_xpath = driver.find_element_by_xpath("//div[@class='shop_01-imgbox']//a")
driver.execute_script("arguments[0].removeAttribute('target')",product_link_xpath)
product_link_xpath.click()
driver.find_element_by_id("joinCarButton").click()
#点击结算按钮
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
#点击添加新地址
driver.find_element_by_css_selector("#address-box > div").click()
#输入收货人等信息（选择地区）
driver.find_element_by_name("address[address_name]").send_keys("bernice")
driver.find_element_by_name("address[mobile]").send_keys("13800138000")
# select1 = Select(driver.find_element_by_id("add-new-area-select"))
# select.select_by_index()
# select.select_by_value("")

#下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样
#Selenium为这种特殊的元素，专门创建了一个类Select
#dropdown1的类型是一个普通的网页元素，下面这句代码的意思是
#把一个普通的网页元素，转换成一个下拉框的特殊网页元素
dropdown1 = driver.find_element_by_id("add-new-area-select")
print(type(dropdown1))
select1 = Select(dropdown1)

# for select in select1.all_selected_options:
# print(select.text)
print(type(select1))
select1.select_by_value("320000")
time.sleep(2)

#尝试一下，选择沈阳市
select1.select_by_visible_text("辽宁省")
select2 = Select(driver.find_elements_by_class_name("add-new-area-select")[1])
select2.select_by_value("210200")

select3 = Select(driver.find_elements_by_tag_name("select")[2])
select3.select_by_value("210281")

# select2 = Select(driver.find_element_by_xpath("//div[@class='add-new-area']//select[2]"))
# select2.select_by_value("210200")

driver.find_element_by_name("address[address]").send_keys("辽宁省大连市xxxx")
driver.find_element_by_name("address[zipcode]").send_keys("5111111")
# #点击保存收货人信息
driver.find_element_by_class_name("aui_state_highlight").click()










