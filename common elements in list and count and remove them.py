#1
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
res = len((listA) & listB);
print(res)

print(listA.difference(listB)) 

#2
def findMinAndMax(nums):
    max = min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
        elif nums[i] < min:
            min = nums[i]
    print('The minimum element in the list is', min)
    print('The maximum element in the list is', max)
if __name__ == '__main__':
    nums = list(input())
    findMinAndMax(nums)

#3
def calsum(l):
    return sum([int(i) for i in l if type(i)== int or i.isdigit()])
list1 = [12,  2, '41',  10, '8', 6, 4,  7, '10']
list2 = [100,  200, '400',  101, '2018', 64, 74,  27, '7810']
print (calsum(list1))
print (calsum(list2))

#OR

list1=['1','2','h','4']
addition=0
import string
for i in list1:
    if i.isdigit():
        addition=addition+int(i)
print(addition)

