#Inheritence
class Parent:
    def __init__(self):
        self.a=1
    def disp(self):
        self.a+=1
        print(self.a)
class Child(Parent):
    def dispchild(self):
        print("Iam child class")
c1=Child()
c1.disp()
c1.dispchild()
p1=Parent( )
