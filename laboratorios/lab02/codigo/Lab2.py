# Laboratorio 2
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.


print("Presentado por:\n\tJuan Pablo Vidal C.\n\tAlejandro Murillo G.")

import time
import random
import copy
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)

# Random array generation
randomArrays = []
for x in range(2, 6):
    randomArrays.append([random.randint(0, 2500) for i in range(5 ** x)])


# --- Array Sum -----------------------------------------

arraySum_ExecutionTime = []

def arraySum(array):
    """
    Prints the sum of every element in the array.

    :param array: The array whose elements will be added.
    :return: Void
    """
    start_time = time.clock()
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    end_time = time.clock()
    arraySum_ExecutionTime.append((len(array), (end_time - start_time)))
    return sum

print("\n\n-- Array Sum --")
for array in randomArrays:
    print("Array sum =", arraySum(array))

print(arraySum_ExecutionTime)


# --- Array Maximum -------------------------------------

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

# --- Insertion Sort ------------------------------------

insertionSort_ExecutionTime = []

def insertionSort(array):
    """
    Sorts an array using the insertion
    sort algorithm.

    :param array: The Array to be sorted.
    :return: The sorted array.
    """
    start_time = time.clock()
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp
            j -= 1
    end_time = time.clock()
    insertionSort_ExecutionTime.append((len(array), (end_time - start_time)))

    return array

print("\n\n-- Insertion Sort --")
for array in randomArrays:
    a = copy.deepcopy(array)   #Avoids changing the original array which will be used later with other sorting algorithm
    print("Insertion Sort", array, "=", insertionSort(a))

print(insertionSort_ExecutionTime)

# --- Merge Sort ----------------------------------------
#Title: Merge Sort
#Author: Michael H. Goldwasser, David Letscher
#Date: 2008
#Code version: 1.0
#Availability: Object-Oriented Programming in Python. Chapter 14.4

mergeSort_ExecutionTime = []

def mergeSort(array):
    """
    Uses the Merge Sort Algorithm
    to sort an array.

    :param array:
    :return: The sorted array.
    """

    def _merge(data, start, mid, stop, tempData):
        i = start
        while i < stop:
            tempData[i] = data[i]
            i += 1

        mergedMark = start
        leftMark = start
        rightMark = mid

        while mergedMark < stop:
            if leftMark < mid and (rightMark == stop or tempData[leftMark] < tempData[rightMark]):
                data[mergedMark] = tempData[leftMark]
                leftMark += 1
            else:
                data[mergedMark] = tempData[rightMark]
                rightMark += 1
            mergedMark += 1

        return data

    def _recursiveMS(data, start, stop, tempData):
        if start < stop - 1:
            mid = (start + stop) // 2
            _recursiveMS(data, start, mid, tempData)
            _recursiveMS(data, mid, stop, tempData)
            return _merge(data, start, mid, stop, tempData)

    return _recursiveMS(array, 0, len(array), [None] * len(array))

print("\n\n-- Merge Sort --")
for array in randomArrays:
    start_time = time.clock()
    print("Merge Sort", array, "=", mergeSort(array))
    end_time = time.clock()
    mergeSort_ExecutionTime.append((len(array), (end_time - start_time)))

print(mergeSort_ExecutionTime)

# --- Graphs --------------------------------------------------------------
algorithms = {"Array Sum" : arraySum_ExecutionTime, "Array Maximum" : arrayMax_ExecutionTime, "Insertion Sort" : insertionSort_ExecutionTime, "Merge Sort" : mergeSort_ExecutionTime}

for algo in algorithms.keys():
    algorithms[algo] = sorted(algorithms[algo])
    algoTime = [item[0] for item in algorithms[algo]]
    algoSpace = [item[1] for item in algorithms[algo]]
    plt.plot(algoTime, algoSpace, "ro-")
    plt.xscale('log')
    plt.xlabel("Data Input (Space)")
    plt.ylabel("Time (ms)")
    plt.title(algo)
    plt.savefig(algo + "_Plot.pdf")
    plt.show()
