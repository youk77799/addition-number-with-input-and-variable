num1 = input("Enter a Number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

# you would got a wrong answer just because
# when you use input function without conversion
# the variable always gonna collect the information in string

print("you would got a wrong answer just because when you use input function without conversion,")
print("the variable always gonna collect the information in string")
print("use \"int\" for converting a variable to integer(full number).")
print("use \"float\" for number converting a variable to float (ex.=5.6)")
num1 = input("Enter a Number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)
