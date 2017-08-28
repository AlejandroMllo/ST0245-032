# Laboratorio 1: Recursion
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

print("Presentado por:\n\tJuan Pablo Vidal C.\n\tAlejandro Murillo G.")

import time
import random
import matplotlib.pyplot as plt


# Random array generation
randomArrays = []
for x in range(1, 11):
    randomArrays.append([random.randint(0, 2500) for i in range(x * random.randint(10, 20))])
    
# --- ArraySum ----------------------------------------------------
def arraySum(array, n):
    """
    Returns the sum of the elements
    in the array.
    :param array:
    :param n: Last element's index
    :return: int
    """
    if (n == 0):
        return array[n]
    sum = array[n] + arraySum(array, n - 1)
    return sum


arraySum_ExecutionTime = []

print("\n\n-- Array sum --")
for array in randomArrays:
    start_time = time.clock()
    sum = arraySum(array, len(array) - 1)
    end_time = time.clock()
    arraySum_ExecutionTime.append((len(array), (end_time - start_time)))
    print("Array sum =", sum)

print(arraySum_ExecutionTime)

# -- Graph Array Sum

time_ArraySum = [item[0] for item in arraySum_ExecutionTime]
space_ArraySum = [item[1] for item in arraySum_ExecutionTime]

plt.plot(time_ArraySum, space_ArraySum, "bo")
plt.xlabel("Data Input (Space)")
plt.ylabel("Time (ms)")
plt.title("Array Sum")
plt.savefig("ArraySum_Plot.pdf")
plt.show()


# --- ArrayMax ----------------------------------------------------
def arrayMax(array, n):
    """
    Returns the maximum element in
    the array.

    :param array:
    :param n: Last element's index
    :return: int
    """
    max = array[n]
    if n != 0:
        temp = arrayMax(array, n - 1)
        if temp > max:
            max = temp
    return max


arrayMax_ExecutionTime = []

print("\n\n-- Array Max --")
for array in randomArrays:
    start_time = time.clock()
    max = arrayMax(array, len(array) - 1)
    end_time = time.clock()
    arrayMax_ExecutionTime.append((len(array), (end_time - start_time)))
    print("Array max =", max)

print(arrayMax_ExecutionTime)

# -- Graph Array Max

time_ArrayMax = [item[0] for item in arrayMax_ExecutionTime]
space_ArrayMax = [item[1] for item in arrayMax_ExecutionTime]

plt.plot(time_ArrayMax, space_ArrayMax, "bo")
plt.xlabel("Data Input (Space)")
plt.ylabel("Time (ms)")
plt.title("Array Max")
plt.savefig("ArrayMax_Plot.pdf")
plt.show()

# --- GroupSum -----------------------------------------------------
def groupSum(start, nums, target):
    """
    Returns whether or not you can reach
    target with the elements on the
    array.

    n = len(nums)

    :param start: The starting index in the array.
    :param nums: The array of numbers.
    :param target: Target sum.
    :return: boolean
    """
    if start >= len(nums):
        return target == 0
    return groupSum(start + 1, nums, target) or groupSum(start + 1, nums, target - nums[start])

groupSum_ExecutionTime = []

print("\n\n-- Group Sum --")
for array in randomArrays:
    start_time = time.clock()
    r = random.randint(5000, 15000)
    result = groupSum(0, array, r)
    end_time = time.clock()
    groupSum_ExecutionTime.append((len(array), (end_time - start_time)))
    print("Group sum =", result)

print(groupSum_ExecutionTime)

# -- Graph Group Sum

time_GroupSum = [item[0] for item in groupSum_ExecutionTime]
space_GroupSum = [item[1] for item in groupSum_ExecutionTime]

plt.plot(time_GroupSum, space_GroupSum, "bo")
plt.xlabel("Data Input (Space)")
plt.ylabel("Time (ms)")
plt.title("Group Sum")
plt.savefig("GroupSum_Plot.pdf")
plt.show()

# --- Fibonacci ----------------------------------------------------
class Fibonacci:
    """
    ADT to make the Fibonacci 
    computation faster.
    """

    _knownAnswers = {}

    def largeFibonacci(self, n):
        """
        Returns the value of the nth
        Fibonacci number.
        :param n: The nth fibonacci number.
        :return: int
        """
        if n > 499:
            for i in range(3, n // 150):
                self._knownAnswers[i * 150] = self._fibonacci(i * 150)

        if n not in self._knownAnswers:
            self._knownAnswers[n] = self._fibonacci(n)

        return self._knownAnswers[n]

    def _fibonacci(self, n):
        if n <= 1:
            return n
        return self.largeFibonacci(n - 1) + self.largeFibonacci(n - 2)

fibonacci_ExecutionTime = []

fibo = Fibonacci()
print("\n\n-- Fibonacci--")
for array in randomArrays:
    start_time = time.clock()
    answer = fibo.largeFibonacci(len(array))
    end_time = time.clock()
    fibonacci_ExecutionTime.append((len(array), (end_time - start_time)))
    print("Fibonacci =", answer)

print(fibonacci_ExecutionTime)

# -- Graph Fibonacci

time_Fibo = [item[0] for item in fibonacci_ExecutionTime]
space_Fibo = [item[1] for item in fibonacci_ExecutionTime]

plt.plot(time_Fibo, space_Fibo, "bo")
plt.xlabel("Data Input (Space)")
plt.ylabel("Time (ms)")
plt.title("Fibonacci")
plt.savefig("Fibonacci_Plot.pdf")
plt.show()
