import csv
import os

class CsvFileManager4:
    def read(self, filename):
        list =[]
        base_path = os.path.dirname(__file__)
        print(base_path)
        path = base_path.replace('day5','data/' + filename)
        print(path)

        with open(path,'r') as file:
            data_table = csv.reader(file)

            for row in data_table:
                print(row)

                list.append(row)

        return list

if __name__ == '__main__':
    list = CsvFileManager4().read('test_data.csv')
    print(list[1][0])
