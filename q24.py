#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

operator = str(input("enter the operator(+, -, *, /):"))
num1 = 4
num2 = 6

if operator == '+':

    sum = num1+num2
    print("addition:" , sum)

elif operator== '-':

    if num2>num1:
        sub = num2-num1
        print("subtraction:" , sub)

    else:
        sub = num1-num2
        print("subtraction:" , sub)


elif operator == '*':

    multip = num1*num2
    print("Multiplication:" , multip)


else:

    if num2 == 0:
        print("infinte value")

    else:
        div = num1/num2

        print("division:" , div)




