fibo = {} # initialize to implement memoization
def fibonacci(num):
    global fibo
    if(fibo.get(num) == None):
        if(num == 0):
            fibo[num] = 0
        elif num == 1 or num == 2:
            fibo[num] = 1
        else:
            fibo[num] = fibonacci(num-1) + fibonacci(num-2)
    else:
        print('returning {} from dictionary'.format(num))
    return fibo[num]

number = int(input('enter the number for the fib sequence :'))
fibo_list = []
for num in range(0, number):
    fibo_list.append(fibonacci(num))
print("fibonacci series for first {} numbers: {} \n\tresult length: {} ".format(number, fibo_list, len(fibo_list)))


