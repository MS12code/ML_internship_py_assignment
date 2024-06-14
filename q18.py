#Write a python program that checks if two strings are anagrams of each other.

str1 = "heart"
str2 = "earth"

if len(str1) == len(str2):

    for ch in str1:

        if ch in str2:

            print("Yes")
            break
        else:
            print("No")
            break