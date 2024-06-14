#Write a python program that returns the minimum and maximum values in a list of numbers.

list1 = [1,2,3]

max = list1[0]
min = list1[0]

for num in list1:

    if max<num:

        max = num

    else:

        min = num

print("max val:" , max)
print("min val:" , min)
