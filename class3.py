class student:
    def __init__(s,name,age):
        s.name=name
        s.age=age
        s.section="k22EP"
    def show(s):
        print(s.name)
        print(s.age)
        print(s.section)
s1=student('shannu',2)
s1.show()
s2=student('mickey',4)
s2.section="DS-A"
s2.show()
s3=student('tinso',3)
s3.section="k22EPDS-A"
s3.show()
