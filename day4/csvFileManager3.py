import csv
#每个测试用例对应着不同的csv文件
class CsvFileManager3:
    def read(self):
        path = r'D:\Bernice\S1\Day1\Code\data\test_data.csv'
        file = open(path,'r')
        #通过csv代码库，读取打开的csv文件，获取到文件中的数据集
        try:
            data_table = csv.reader(file)
            #for循环,item每一行， in 在数据集中 data_table表示数据集、
            #data_table中有几行，我们就会被执行几次
            for item in data_table:
                  print(item)
        finally: #finally最终，不论过程是否报错，都会执行以下代码
            file.close()
            print("file.close() method is executed")
        #如果想测试一下这个方法：


if __name__ == '__main__':
    csvr = CsvFileManager3()
    csvr.read()
        #如果在方法上面加上classmethod，表示这个方法可以直接 被调用
        # CsvFileManager2.read()