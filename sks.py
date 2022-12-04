#Importing the random module
import random

# Defining the function of the password generator
def pass_gen(n,first_char):
    password=""
    password=first_char
    for i in range(1,len0):
        b=random.randint(0,3)
        if b==0:
            ind=random.randint(0,len(lower)-1)
            password+=lower[ind]
        if b==1:
            ind=random.randint(0,len(upper)-1)
            password+=upper[ind]
        if b==2:
            ind=random.randint(0,len(digits)-1)
            password+=digits[ind]
        else:
            ind=random.randint(0,len(spchars)-1)
            password+=spchars[ind]
    for j in password:
        if j in lower:
            pass
        elif j in upper:
            pass
        elif j in digits:
            pass
        elif j in spchars:
            pass
        else:
            pass_gen(len0,first_char)
    print()
    print("------------------------------------")
    print("Your Password is->",password[:len0],)
    print("------------------------------------")
    
''' Main program of the password generator '''

#Initiating a string of all lowercase alphabets.
lower="abcdefghijklmnopqrstuvwxyz"

#Initiating a string with uppercase alphabets.
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Initiating a string with all the digits i.e. 0-9
digits="0123456789"

#Initiating a string with all the special characters.
spchars="~!@#$%^&*()_-+=-/{}[]\|,.;:"

#Welcome message for the user
print()
print("*=======================*")
print("|| Password Generator  ||")
print("||*********************||")
print("||    Made by:         ||")
print("||      Md Faizan      ||")
print("||      Rohit Kumar    ||")
print("||      Sainath Reddy  ||")
print("*=======================*")
print()

#About the password generator

while True:
    about0=input("Enter \"about\" to know about Password Generator! ")
    if about0.lower()=="about":
        print("-> This password generator has been made by Md Faizan, Rohit Kumar and Sainath Reddy for the end-term project of INT-108")
        print("-> It generates a password consisting of special characters, upper and lower case alphabets and numbers.")
        print("-> It takes the length of the password as input from the user and generate a strong password.")
        print()
        break
    else:
        print("Sorry invalid input! Please enter valid input :) ")
        print()
        pass

#Starting the password generator on user command

while True:
    start=input("Enter \"start\" to start creating your password! ")
    print()
    if start.lower()=="start":  
        print("*NOTE* Minimum length of password should be 12!")
        print()
        #Taking length of password as input from the user
        len0=int(input("Enter length of password! "))
        if len0>11:
            #Calling thge password generator function
            print()
            first_char=input("Enter character to start your password with: ")
            pass_gen(len0,first_char)
            print()
            print("Thank You for using :)")
            break
        else:
            print("Entered password length is less than the minimum length!")
            print()
    else:
        print("Sorry invalid input! Please enter valid input :) ")
        print()
        pass
print()
c=input("Enter any character to exit!")
