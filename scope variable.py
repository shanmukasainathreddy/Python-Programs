#scope variable
class Student:
    def __init__(self):
        self.a=1
    def disp(self):
        self.a+=1
        print(self.a)
        b=self.a+2
        print(b)
    def disp2(self):
        self.disp()
s1=Student()
print(s1.a)
s1.disp()
s1.disp2()
print(b)# will show an error 
