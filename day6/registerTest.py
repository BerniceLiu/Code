import unittest

import time

import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By

from day4.csvFileManager import data_table
from day5.csvFileManager4 import CsvFileManager4
from day5.myTestCase import MyTestCase
from day6.DBconnection import DBConnection

@ddt.ddt
class RegisterTest(MyTestCase):
    data_table = CsvFileManager4().read("test_data.csv")
    @ddt.data(*data_table)
    def test_register(self,row):
        sql = 'select * from hd_user order by id desc;'
        #数据库验证，测试的正常情况
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")  # 这两种方法，没有任何区别，但是后面的这种方法扩展性更好，便于框架封装
        driver.find_element(By.NAME, "username").send_keys(row[0])
        driver.find_element(By.NAME, "password").send_keys(row[1])
        driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
        driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
        driver.find_element(By.NAME, "email").send_keys(row[4])
        driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(2)
        new_record = DBConnection().execute_sql_command(sql)
        self.assertEqual(row[0],new_record[1])

if __name__ == '__main__':
    unittest.main()