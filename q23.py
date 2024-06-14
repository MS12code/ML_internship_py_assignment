#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

char_temp = input("Celsius or Fahrenheit (C/F)? : ")
temp = float(input("Enter temperature: "))

if char_temp == 'C':
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif char_temp == 'F':
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius:" , celsius)
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

