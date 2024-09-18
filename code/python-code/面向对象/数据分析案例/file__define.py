"""
和文件相关的类定义

"""
from data_define import Recode
import json

class FileReader:
    def read_data(self)->list[Recode]:
        """读到的每一行数据转换成Recode类"""
        pass


class TextFileReader(FileReader):
    def __init__(self,path):    #path:文件路径
        self.path=path          #定义成员变量，记录文件路径

    #复写父类的方法，读取数据
    def read_data(self) ->list[Recode]:
        f=open(self.path,"r",encoding="UTF-8")
        recode_list:list[Recode]=[]
        for line in f.readlines():
            line=line.strip()
            line=line.split(",")
            recode=Recode(line[0],line[1],int(line[2]),line[3])
            recode_list.append(recode)
        f.close()
        return recode_list

class JsonFileReader(FileReader):
    def __init__(self,path):    #path:文件路径
        self.path=path          #定义成员变量，记录文件路径

    #复写父类的方法，读取数据
    def read_data(self) ->list[Recode]:
        f=open(self.path,"r",encoding="UTF-8")
        recode_list: list[Recode] = []
        for line in f.readlines():
            date_dict=json.loads(line)
            recode=Recode(date_dict["date"],date_dict["order_id"],int(date_dict["money"]),date_dict["province"])
            recode_list.append(recode)
        f.close()
        return recode_list




if __name__ == '__main__':
    textreder=TextFileReader("E:/python/python资料/第13章资料/2011年1月销售数据.txt")
    jsonreder=JsonFileReader("E:/python/python资料/第13章资料/2011年2月销售数据JSON.txt")
    ls1=textreder.read_data()
    ls2=jsonreder.read_data()
    for i in ls1:
        print(i)





