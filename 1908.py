Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input("))
def number(n):
    if n%3==0:
        print("FIZZ")
    if n%5==0:
        print("BUZZ")
    if n%3==0 and n%5==0:
        print("FIZZBUZZ")
    else:
        print("NO")