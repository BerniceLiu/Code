from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
# 1.登录海盗商城的后台
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userverify").submit()
# 2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
# 3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
# 4.输入商品名称
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone")
# 5.选择商品分类（双击或者点击“选择当前分类”）
driver.find_element_by_link_text("手机、数码、通讯").click()
# 6.在下拉框中选择商品品牌
driver.find_element_by_link_text("手机配件").click()
# 7.根据以上7步，编写代码，找出第一个不能实现的地方
