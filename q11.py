#Write a python program that generates the first n numbers in the Fibonacci sequence.

n = int(input("enter n:"))

a = 0 
b = 1

for i in range(n):

    c = a+b
    a = b
    b = c

    print(c)