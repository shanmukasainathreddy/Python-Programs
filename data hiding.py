#Data Hiding
class Abc:
    def __init__(self):
        self.__a=1
    def disp(self):
        return self.__a
    def __disp2(self):
        return self.__a
obj1=Abc()
print(obj1.__disp())

# remove __disp2 for excution
