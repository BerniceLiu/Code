from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost");
driver.get("http://localhost/index.php?m=user&c=public&a=reg");
driver.find_element_by_name("username").send_keys("bernice1")
driver.find_element_by_name("password").send_keys("lyx123")
driver.find_element_by_name("userpassword2").send_keys("lyx123")
driver.find_element_by_name("mobile_phone").send_keys("13800138000")
driver.find_element_by_name("email").send_keys("11111111@qq.com")
driver.find_element_by_class_name("reg_btn").click();
