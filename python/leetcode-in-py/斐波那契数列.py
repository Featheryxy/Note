# 1,1,2,3,5,8,13...

def Fibonacci_Induction(n):
	ret = []
	for i in range(n):
		if i == 0 or i == 1:
			ret.append(1)
		else:
			ret.append(ret[i-1] + ret[i-2])
		
	return ret


def Fibonacci_Recursion_tool(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return Fibonacci_Recursion_tool(n-1) + Fibonacci_Recursion_tool(n-2)
	
	
def Fibonacci_Recursion(n):
	ret = []
	for i in range(1, n+1):
		ret.append(Fibonacci_Recursion_tool(i))
	return ret


def Fibonacci_loop(n):
	ret = []
	a, b = 0, 1
	while n:
		ret.append(b)
		a, b = b, a+b
		n -= 1
	return ret
	

from functools import wraps

def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap
	
@memo
def fib(i):
	if i<=2:
		return 1
	return fib(i-1)+fib(i-2)
	
	
	
	
print(Fibonacci_Induction(10))
print(Fibonacci_Recursion(10))
print(Fibonacci_loop(10))
print(fib(100))
	
	
	

