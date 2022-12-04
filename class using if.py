class student:
    def __init__(s,name,age):
        s.name=name
        s.age=age
        s.section=section
    def show(s):
        print(s.name)
        print(s.age)
        print(s.section)
l=[]
no=int(input("Total number of students"))
for i in range(no):
    name=input("enter name")
    age=input("enter age")
    section=input("enter section")
    l.append(student(name,age,section))
    l[i].show()
