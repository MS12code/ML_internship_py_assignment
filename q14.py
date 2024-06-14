#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.


lines = []

while True:
    user_input = input("Enter a line (or press Enter to finish): ")
    if user_input == "":
        break
    lines.append(user_input)


print("\nYou entered:")
for line in lines:
    print(line)
