input_list = list(i*10 for i in range(1,11))
print(input_list)
passed_list = list(i for i in input_list if i > 20)
print(passed_list)
special_list = list('1st class' if i >= 60 else 'just passed' for i in passed_list)

print(special_list)
