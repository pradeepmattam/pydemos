import math


def gcd(a, b):

	x = max(a, b)
	y = min(a, b)

	while y != 0:
		r = x % y
		x = y
		y = r

	return x


x = 324
y = 48

print(gcd(x, y))
