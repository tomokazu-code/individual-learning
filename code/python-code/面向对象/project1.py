
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.age,self.name

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age<=other.age



stu1=Student("zzx",20)
stu2=Student("asdf",43)

print(stu2<=stu1)