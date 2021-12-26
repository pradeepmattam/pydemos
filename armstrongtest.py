def checkarmstrong(number):
    input_number = number
    total = 0
    length = len(str(number))
    while number > 0:
        digit = number - ((number // 10) * 10)
        total += digit**length
        number //= 10
    if total == input_number:
        return True
    else:
        return False

number = int(input(" enter the number to check :"))

print("the check if {} is an armstrong number returned {}". format(number, checkarmstrong(number)))

