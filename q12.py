#Write a python program that calculates the sum of the digits of a given number.

num = int(input("enter num:"))

sum = 0

while(num!=0):

    dig = num%10
    sum = sum+dig
    num = num//10

print(sum)

