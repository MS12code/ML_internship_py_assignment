#Write a program that takes a string input from the user and writes it to a text file.

str1 = str(input("enter string:"))

with open('demmo.txt', 'w') as file:
   
    file.write(str1)


print("The input has been written to 'demmo.txt'.")

