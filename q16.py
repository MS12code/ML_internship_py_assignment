#. Write a program in python that counts the frequency of each character in a string.

str1= "aabbccc"

cnt_a = 0
cnt_b = 0
cnt_c = 0

for ch in str1:

    if ch == 'a':
        cnt_a+=1

    elif ch == 'b':
        cnt_b+=1

    else:
        cnt_c+=1

print("frequency of a:", cnt_a)
print("frequency of b:", cnt_b)
print("frequency of c:", cnt_c)