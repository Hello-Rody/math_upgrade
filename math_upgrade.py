#https://ideone.com/3TGr00
#これからの引用
import time
import math
def funclog(func):
	def wrapper(*args, **kwargs):
		print(f"{func.__name__} start", *args)
		start_time = time.perf_counter()
		return_val = func(*args, **kwargs)
		end_time = time.perf_counter()
		print(f"{func.__name__} end (time={end_time-start_time:.4f})")
		return return_val
	return wrapper

def list_primes(limit):
	primes = []
	is_prime = [True] * (limit + 1)
	is_prime[0] = False
	is_prime[1] = False
	for p in range(0, limit + 1):
		if is_prime[p]:
			primes.append(p)
			for i in range(p * p, limit + 1, p):
				is_prime[i] = False
	return primes

#@funclog
def P_n_2(n):
	"""n番目の素数を得られます
	下のP_n_1より、約80倍高速です"""
	limit = max(100, int(n * math.log2(n) * 1.2))
	while True:
		primes = list_primes(limit)
		if len(primes) > n:
			return primes[n - 1]
		limit *= 2
#ここまで

def gcd(a,b):
	"""aとbの最大公約数を求めます"""
	c = a
	d = b
	while a % b > 0:
		a,b = b, a % b
	return b

def lcm(a,b):
	"""aとbの最小公倍数を求めます"""
	c = a * b
	d = a
	while a % b != 0:
		a,b = b, a % b
	return c//b

def factorial(num):
	"""引数の階乗を求めます"""
	for i in range(num - 1):
		num *= i + 1
	return num

def summation(fac,k,n):
	"""任意の関数の総和を求めます
	関数の定義が必要です
	引数には関数、足し始めの整数、足し終わりの整数を順に入力してください"""
	sum = 0
	for i in range(k,n+1):
		sum += fac(i)
	return sum

def factor(n):
	"""nを素因数分解します"""
	a = []
	while n % 2 == 0:
		a.append(2)
		n //= 2
	f = 3
	while f * f <= n:
		if n % f == 0:
			a.append(f)
			n //= f
		else:
			f += 2
	if n != 1:
		a.append(n)
	return a

def P_n_1(n):
	"""n番目の素数を得られます
	より高速なP_n_2が上に定義されています"""
	primes = [2]
	a = b = 3
	while len(primes) < n:
		for i in primes:
			if a % i == 0:
				b = a / i
				break
		if b == a:
			primes.append(a)
		a  += 2
		b = a
	return primes[n - 1]

def F_n(n):
	"""フィボナッチ数列のn番目の数を得られます"""
	a, b = 0, 1
	fib_l=[]
	while n:
		n-=1
		fib_l.append(b)
		a, b = b, a+b
	return fib_l[-1]

def less_P(n):
	"""n以下の素数のリストを返します"""
	lesses = []
	for i in range(n):
		if  P_n_2(i+1) <= n:
			lesses.append(P_n_2(i+1))
	return lesses

def pi(n):
	"""n以下の素数の個数を返します(素数計算関数)"""
	return len(less_P(n))

def coprime(n):
	"""nと互いに素なn以下の自然数を返します"""
	num = []
	for i in range(1,n+1):
		if gcd(n,i) == 1:
			num.append(i)

	return num

def totient(n):
	"""n以下のnと互いに素な自然数の個数を返します(オイラーのφ関数)"""
	return len(coprime(n))

