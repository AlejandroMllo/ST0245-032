# Taller 5
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

fibonacci_ExecutionTime = []

print("\n\n-- Fibonacci--")
for array in randomArrays:
    start_time = time.clock()
    fibo = fibonacci(len(array) // 3)
    end_time = time.clock()
    fibonacci_ExecutionTime.append((len(array) // 3, (end_time - start_time)))
    print("Fibonacci =", fibo)

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