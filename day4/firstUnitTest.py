#第一个单元测试框架示例
#1.要想用unittest框架，首先要导包
#为什么selenium需要先安装或者解压？unitest不需要
#因为unittest比selenium更常用，几乎所有测试都要用unittest组织测试
#所有python把unittest集成在pythonSDK中了，不需要单独下载，只要安装python就有，unnitest是python内置的代码库
import unittest

#2创建一个类，用来编写自动化测试用例
#这个自动化测试用例的类需要继承unitest框架中的TestCase类
#我们继承了TestCase这个类，就说明我们这个类是一个测试用例类
#python中类名最好和文件名不一样， 文件名首字母小写，类名首字母大写
#类名和文件不强制要求，只是一个python的习惯
#()表示继承，继承是指子类完全继承父类的所有方法和属性，并且有自己扩展的内容
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
        #在python中,类里面的每个方法都有一个默认参数叫self
        #self类似于java中this关键字，代表类本身
        #如果你想使用类的属性和方法，那么必须在前面加self关键字
        #根据光标所在的位置，决定执行什么测试用例
        #光标在哪个方法中，那么就会只运行哪个测试用例
        #光标在unittest.main（）这行就会执行所有的测试用例
        self.switch_window()

#也可以选择重写setUpClass和tearDownClass方法
  #一个类中，所有测试用例方法的执行顺序，是根据方法名的字母顺序决定的

    @classmethod
    def setUpClass(cls):
        print(5)
        #@classmethod在python中叫装饰器，在java中叫注解
    @classmethod
    def tearDownClass(cls):
        print(6)

    #写完之后，在unittest.main()
    # #if __name__ == '__main__':这是一个固定写法
    # #在程序运行时，通过这句话，可以自动判断当前文件不是程序的入口
    #     if __name__ == '__main__':
    #         unittest.main()

