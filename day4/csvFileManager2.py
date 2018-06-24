import csv

class CsvFileManager2:
    def read(self):
        path = r'D:\Bernice\S1\Day1\Code\data\test_data.csv'
        file = open(path,'r')
        #通过csv代码库，读取打开的csv文件，获取到文件中的数据集
        data_table = csv.reader(file)
        #for循环,item每一行， in 在数据集中 data_table表示数据集、
        #data_table中有几行，我们就会被执行几次
        for item in data_table:
            print(item)

        #如果想测试一下这个方法：
if __name__ == '__main__':
    csvr = CsvFileManager2()
    csvr.read()
            #如果在方法上面加上classmethod，表示这个方法可以直接 被调用
                # CsvFileManager2.read()