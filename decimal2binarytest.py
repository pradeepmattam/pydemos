input_number = int(input("enter a decimal number: "))
decimal_number = ''
number = input_number
while number > 0:
    remainder = number % 2
    decimal_number += str(remainder)
    number = number // 2

decimal_number = decimal_number[::-1]

print("binary equivalent : {}".format(decimal_number))
