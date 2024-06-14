#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

str1= "GeeksforGeeks"

prefix = str(input("enter prefix:"))

suffix = str(input("enter suffix:"))

if str1.startswith(prefix)==True:

    print("Yes, it starts with the given prefix ")

else:
    print("It does not start with the given prefix")


if str1.endswith(suffix) == True:

     print("Yes, it end with the given suffix ")

else:

    print("It does not end with the given suffix")


