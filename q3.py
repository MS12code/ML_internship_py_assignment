#3. Write a python program that calculates the factorial of a given number.

fact  = 1

num = int(input("enter num:"))

for i in range(1,num+1):

    fact = fact*i


print("factorial:" , fact)