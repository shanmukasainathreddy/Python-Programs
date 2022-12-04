#1
password="sharag"
for i in range(0,3):
    b=input("enter the password")      
    if b==password:
        print("you have sucessfully login")
        break
    else:
        print("you have been denied access")



#2
a=int(input())
b=int(input())
c=a+b
if c>100:
    print("that is a big number")
else:
    print("small")
exit()


#3
n=int(input("enter number:"))
org=n
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if (org==rev):
    print("the number is a palindrome!")
else:
    print("the number is not  a palindrome!")

    
#4
nterms=int(input("how many terms?"))
n1,n2 =0,1
count=0
if nterms<=0:
   print("please enter a positive integer")
elif nterms==1:
    print("Fibonacci  sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count +=1
            


