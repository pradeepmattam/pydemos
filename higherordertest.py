import math


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func, text):
    return func(text)


print(hello(loud, "hI tHeRe"))
print(hello(quiet, "hI tHeRe"))


def divide(x):
    def divisor(y):
        return y/x
    return divisor


print(math.floor(divide(3)(10)))
