from selenium import webdriver
from Day2.loginTest import Login

#只要import了loginTest这个文件，文件中类外面的代码就会被执行
#只有加上if __name__=="__main__":才能避免类外面的代码被其他文件调用时自动执行
#所以if __name__== '__main__':的意思就是：
#__name__指的是当前文件
#__main__指的是程序入口
#如果当前文件是程序的入口，那么才执行下面的语句
driver = webdriver.Chrome()
driver.implicitly_wait(20)
Login().loginWithDefaultUser(driver)