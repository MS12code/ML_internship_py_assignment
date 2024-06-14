#Write a program that reads the content of a text file and prints it to the console.

with open('demmo.txt', 'r') as file:
  
    contents = file.read()

print(contents)