"""
和文件相关的类的定义
"""
import json
from abc import ABC, abstractmethod
from data_define import Record
# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader(ABC):
    @abstractmethod
    def read_data(self) -> list[Record]:
        # 读取文件的数据，读到的每一条数据都转换成Record对象，并将它们存储到一个列表中，返回该列表
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    # 实现父类的抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip() # 去掉每行末尾的换行符
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/BaiduNetdiskDownload/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/BaiduNetdiskDownload/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)