import time

def fibonacci(n):
    """
    Returns the value of the nth
    Fibonacci number.
    :param n: The nth fibonacci number.
    :return: int
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def theirfibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

start_time = time.clock()
print(theirfibonacci(997))
end_time = time.clock()
print("Google algo time =", (end_time - start_time))
