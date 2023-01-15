# 標準モジュールmathの拡張的な

#### より細かい操作を行えます
## 使い方
### gcd(m,n)
> mとnの最大公約数を返します

	result = math_upgrade.gcd(20,45)
	print(result)

> 実行結果

```> 5⏎```
### lcm(m,n)
> mとnの最小公倍数を返します

	result = math_upgrade.gcd(20,45)
	print(result)

> 実行結果

```> 180⏎```
### factorial(n)
> nの階乗を返します

	result = math_upgrade.factorial(10)
	print(result)

> 実行結果

```> 3628800⏎```

### summation(function,m,n)
> 任意の関数の総和( Σ[k=m~n]function(k) )を返します
> 
> 事前に関数を定義する必要があります
> 
> 第一引数には関数、第二には足し始めの整数、第三には足し終わりの整数を代入してください

	def function(x):
		return 3 * x - 2
	result = math_upgrade.summation(function,1,10)
	print(result)
> 実行結果

```> 145⏎```

### factor(n)
> nの素因数のリストを返します

	result = math_upgrade.factor(365)
	print(result)

> 実行結果

```> [5, 73]⏎```

### P_n_1(n), P_n_2(n)
> n番目の素数を返します
> P_n_1(n)とP_n_2(n)について、返り値は同じですが処理速度はP_n_2のほうが200倍ほど高速です

	result1 =math_upgrade.P_n_1(125)
	result2 = math_upgrade.P_n_2(413)
	print(result1, result2)
> 実行結果

```> 691 2843⏎```


### less_P(n)
> n以下の素数のリストを返します

	result = math_upgrade.less_P(100)
	print(result)

> 実行結果

```> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]⏎```


### pi(n)
> n以下の数の個数を返します(素数計算関数)

	result = math_upgrade.pi(811)
	print(result)

> 実行結果

```> 141⏎```


### F_n(n)
> n番目のフィボナッチ数を返します

	result = math_upgrade.F_n(21)
	print(result)

> 実行結果

```> 10946⏎```


### coprime(n)
> n以下のnと互いに素な自然数のリストを返します

	result = math_upgrade.comprime(50)
	print(result)

> 実行結果

```> [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49]⏎```

### totient(n)
> n以下のnと互いに素な自然数の個数を返します(オイラーのφ関数)

	result = math_upgrade.torient(100)
	print(result)
> 実行結果

```> 40⏎```
