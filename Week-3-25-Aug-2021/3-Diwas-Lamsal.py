# Diwas Lamsal - st122324
# 2021-August-18 Data Structures and Algorithms Week 3
# Question: Maximum Subarray Problem Using Python

# import matplotlib and numpy
import math
import numpy as np
import timeit
import math
import random
import matplotlib.pyplot as plt


# -------------------------------------- Initialize Variables -------------------------------------- #

def find_max_crossing_subarray(A, low, mid, high):
    max_left = -math.inf
    left_sum = -math.inf
    sum_subarray = 0
    for i in reversed(range(mid + 1)):
        sum_subarray = sum_subarray + A[i]
        if sum_subarray > left_sum:
            left_sum = sum_subarray
            max_left = i
    right_sum = -math.inf
    max_right = -math.inf
    sum_subarray = 0
    for j in range(mid + 1, high + 1):
        sum_subarray = sum_subarray + A[j]
        if sum_subarray > right_sum:
            right_sum = sum_subarray
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = math.floor((low + high) / 2)
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


# Test (Same arrays as classroom)

def test_function(A_test):
    print("--------------------------------------------------")
    print("Input: ", A_test)
    (start, end, sum) = find_maximum_subarray(A_test, 0, len(A_test) - 1)
    print(f"Maximum subarray: Start: {start}, End: {end}, Sum: {sum}")
    print("--------------------------------------------------")


test_function(np.array([5, -6, 2, -10, 13, 1]))
test_function(np.array([-5, 1, 2, 9, -5, 8]))
test_function(np.array([-2, -3, 4, -1, -2, 1, 5, 3, -3, 2]))
test_function(np.array([2, -1, 4, -5, 4, 3]))

# Find the time taken by algorithm and plot compared to nlogn

from random import sample
from timeit import timeit

# The range of n will be between 10 and 1000 with a growth rate of 10 per iteration
num_samples = range(10, 1000, 10)

# The constant value c shows somewhat of a match between nlogn and the algorithm when c = 1/200000
# This is probably true for my PC due to hardware and might be a different value for a different one
c = 1/200000

# https://stackoverflow.com/questions/41883548/python-for-algorithm-execution-visualization
timevals = []
y_nlogn = []
for n in num_samples:
    my_list = sample(range(n), n)
    y_nlogn.append(c * n * np.log(n))
    # https://docs.python.org/3/library/timeit.html
    # https://www.geeksforgeeks.org/timeit-python-examples/
    time = timeit('find_maximum_subarray(my_list, 0, len(my_list) - 1)', number=1, globals=globals())
    timevals.append(time)
plt.plot(num_samples, y_nlogn, label='nlogn')
plt.plot(num_samples, timevals, label="Code Runtime")
plt.legend()
plt.show()