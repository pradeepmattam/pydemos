
input_numbers = input("input comma separated numbers :")
input_numbers = list(map(int, input_numbers.split(',')))

sumeven = 0
sumodd = 0
for num in input_numbers:
    if num % 2 == 0:
        sumeven += num
    else:
        sumodd += num
print("for the given list of numbers {} \n \tsum of evens:{} and odds:{}".format(input_numbers, sumeven, sumodd))



