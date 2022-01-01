def nontail_sigma(x):
    if x == 1:
        return 1
    else:
        return x + nontail_sigma(x-1)


def tail_sigma(x, total):
    if x == 0:
        return total
    else:
        return tail_sigma(x-1, total+x)


print(nontail_sigma(10))
print(tail_sigma(10, 0))
