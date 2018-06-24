#1.要想读取csv文件，首先要导入csv代码库
#这个csv也不用下载，是Python内置的代码库
#如果要读取excel需要下载相应的代码库：xlrd
#怎么下载：1、通过命令下载：在dos窗口中输入pip install -U xlrd
#之前发的selenium离线包 也可以通过命令行在线安装：
#pin install -U selenium 或者 pin3 install selenium
#-U是升级到最新版的意思
#pin是python语言最常用的项目管理工具，和java中的maven类似
#如果你又安装python2,同时安装python3,那么，可能需要把pin改成pin3
#2.点击File-Settings-project下面的interpreter
import csv

#指定要读取的文件的路径
# path = 'D:\\Bernice\\S1\\Day1\\Code\\data\\test_data.csv'
# path2 = 'D:/Bernice/S1/Day1/Code/data/test_data.csv'

path = r'D:\Bernice\S1\Day1\Code\data\test_data.csv'

#因为字符串中包含反斜线\t等，怎么办
#1.每个反斜线前面加一个反斜线
#2.把每个反余线都改成正斜线
#相比，第二种方法更好一点，因为java,python都是跨平台语言
#在字符串中两个反斜线会自动根据转义字符的规则转成一个反斜线
#在windows操作系统中，用反斜线\表示目录结构
#但是在linux操作系统中，只有正斜线/才能表示目录
#如果用双反斜线，那么代码就失去了跨平台的能力，因为linux用不了\
#如果用正斜线，代码可以同时在linux和windows中执行
#2.3.在字符串外面加上一个字母r,认为中间所有的代码都不存在转义字符
#print(path)
#3.打开路径所对应的文件
file = open(path,'r') #默认为R
#4.读取文件的内容，通过什么来读取呢
#reader()方法是专门用来读取文件的
data_table = csv.reader(file)
#5.打印data_table中每一行数据，怎么办？循环for_each语句
#for是循环的关键字，item代表每一行，每循环一次，就代表，item就代表最新的一行数据
#data_table表示整个文件中的所有数据
for item in data_table:
    print(item)

#我们是不是这样，就成功从excel中读取出来所有数据了
#很多的测试用例可能都需要从excel中读取数据，所以我们应该对这些代码做一个
# 简单的封装，建一个文件叫csvFileManager2,把以上代码封装到一个方法中，并
# 且再建一个文件来读取封装方法




