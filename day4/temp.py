#第一个单元测试框架示例
#1.要想用unittest框架，首先要导包
#为什么selenium需要先安装或者解压？unitest不需要
#因为unittest比selenium更常用，几乎所有测试都要用unittest组织测试
#所有python把unittest集成在pythonSDK中了，不需要单独下载，只要安装python就有，unnitest是python内置的代码库
import unittest

class FirstUnitTest(unittest.TestCase):
    #3.重写父类的setUp和tearDown方法
    def setUp(self):
        #setUp()是在测试用例方法执行之前要做的操作
#         类似手工测试中的预置条件
        #setup和teardown方法在每个测试用例方法执行时，都会执行一次
        print(1)
    def tearDown(self):
        #tearDown()是在测试用例方法执行之后要做的操作
        #比如可能需要还原测试场景，清除脏数据
        print(2)
    def test_login(self):
        #这个方法用来编写测试步骤
        #框架规定：测试用例方法必须以test开头
        print(3)
    def switch_window(self):
        #这个方法不是test开头的，不能直接运行，只有被调用才能执行
        print(4)

    def test_zhuce(self):

        self.switch_window()


    @classmethod
    def setUpClass(cls):
        print(5)

    @classmethod
    def tearDownClass(cls):
        print(6)
