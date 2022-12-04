def print_table(a):
    for i in range(0,11):
        print(a,'*',i,'=',a*i)
n=25
print_table(n)


def fname (age,name):
    print(age,name)
fname("shannu",12)



def fname(*a):
    print(a)
fname(1,2,3,4)



def name (**a):
    print(a)
fname("shannu","tinku")


def pyramid(a):
    for i in range(0,a):
        for j in range(1,a+1):
          print("*",end="")
    print("")
pyramid(5)
