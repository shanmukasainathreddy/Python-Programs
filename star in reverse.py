row=int(input("enter no of rows"))
for i in range(0,row):
    for j in range(row,i,-1):
        print("*",end="")
    print("")
