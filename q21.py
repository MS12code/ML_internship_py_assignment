#Write a python program that counts the occurrences of a specific element in a list.

list1 = [1,2,2,2,3]

ele = int(input("enter element you want to count:"))

cnt = 0

for num in list1:

    if num == ele:

        cnt+=1

print(cnt)

    