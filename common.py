listA=[]
n=int(input("Enter number of elements in the list:"))
for i in range(0,n):
     print("Enter element no",i)
    elm=int(input())
    listA.append(elm)
print("The entered list is :",listA)
      
listB=[]
n=int(input("Enter number of elements in the list:"))
for i in range(0,n):
    print("Enter element no",i)
    elm=int(input())
    listB.append(elm)
print("The entered list is :",listB)
      
def common_member(listA,listB):
    result=[i for i in listA if i in listB]
    return result
print("The common element in the two lists are: ")
print(common_member(listA,listB))
