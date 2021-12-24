def search(input_list, number):
    for i in input_list:
        if i == number:
            return True
    return False

input_list = [1,2,4,5,6,6,3,2,1,5,7,8]

number = 10

if search(input_list, number):
    print("{} is found in {}".format(number, input_list))
else:
    print("{} is not found in {}".format(number, input_list))
