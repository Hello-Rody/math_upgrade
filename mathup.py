def factorial(num):
	for i in range(num - 1):
		num *= i + 1
	return num

def summation(fac,k,n):
	sum = 0
	for i in range(k,n+1):
		sum += fac(i)
	return sum
