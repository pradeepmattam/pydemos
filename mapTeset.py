products = [('shirt', 10.00),
          ('shot', 5.00),
          ('belt', 1.00),
            ('cap', 25.00)]

map_func = lambda data: (data[0],data[1]*2)

inflation = list(map(map_func,products))
print(inflation)

filter_func = lambda data: int(data[1] % 5) == 0

no_change = list(filter(filter_func, map(map_func,products)))

print(no_change)

total_sum = lambda x, data: (x[0]+' & '+data[0], x[1]+data[1])
import functools
total_bill = functools.reduce(total_sum, no_change)
print(total_bill)

def factorial(num):
    multiply = lambda x,y: x*y
    numbers = list(i for i in range(1,num+1))
    return functools.reduce(multiply,numbers)

print(factorial(3))
print(factorial(5))
print(factorial(10))
