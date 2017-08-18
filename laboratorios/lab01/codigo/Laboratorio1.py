import time
# --- Fibonacci ----------------------------------------------------
class Fibonacci:

    _knownAnswers = {}

    def largeFibonacci(self, n):
        """
        Returns the value of the nth
        Fibonacci number.
        :param n: The nth fibonacci number.
        :return: int
        """
        if n > 499:
            self._knownAnswers[499] = self._fibonacci(499)

        if n not in self._knownAnswers:
            self._knownAnswers[n] = self._fibonacci(n)

        return self._knownAnswers[n]

    def _fibonacci(self, n):
        if n <= 1:
            return n
        return self.largeFibonacci(n - 1) + self.largeFibonacci(n - 2)


df = Fibonacci()
start_time = time.clock()
print(df.largeFibonacci(997))
end_time = time.clock()
print("My algo time =", (end_time - start_time))


