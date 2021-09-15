# Diwas Lamsal - st122324
# 2021 - September - 15 -- Data Structures and Algorithms Week 6
# Question: Implementing Bucket Sort and Radix Sort

# imports
import numpy as np
import timeit
import math
import random
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------- #
# -------------------------------------- IMPLEMENTING BUCKET SORT ------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #

# Insertion sort from week 1
def insertion_sort(slist):
    for x in range(1, len(slist)):  # Starting from 1 because the first element has nothing to compare itself to
        key = slist[x]
        y = x - 1
        while y > -1 and slist[y] > key:  # Iteratively take the key to the left if it is smaller
            slist[y + 1] = slist[y]
            y -= 1
        slist[y + 1] = key


def do_bucket_sort(buckarr):
    greatest = 0
    for i in range(len(buckarr)):
        if buckarr[i] > 1:
            length = len(str(buckarr[i]))
            greatest = length if length > greatest else greatest
    divisor = 10 ** greatest
    for i in range(len(buckarr)):
        buckarr[i] = (buckarr[i] / divisor)
    bucket_sort(buckarr)
    if greatest == 0:
        return
    for i in range(len(buckarr)):
        buckarr[i] = round(buckarr[i] * divisor) if math.isclose(buckarr[i] * divisor, round(buckarr[i] * divisor))\
            else buckarr[i] * divisor


def bucket_sort(A):
    B = []
    n = len(A)
    for i in range(10):  # Making 0-9 empty lists
        B.append([])

    for i in range(n):
        B[math.floor(10 * A[i])].append(A[i])

    for i in range(len(B)):
        insertion_sort(B[i])

    idx = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            A[idx] = B[i][j]
            idx += 1


# ----------------------------------------------------------------------------------------------------- #
# -------------------------------------- IMPLEMENTING RADIX SORT -------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #

# Normal Counting Sort
def counting_sort(A, B, k):
    C = [0] * (k + 1)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        # Have to do -1 because the indexing for B is starting from 1 otherwise
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1


def do_counting_sort(A):
    B = [0] * len(A)
    greatest = max(A)
    counting_sort(A, B, greatest)
    return B


def counting_radix_sort(A, d):
    # B for storing the sorted array
    B = [0] * len(A)
    C = [0] * (10) # 10 and not maximum of A like normal counting sort

    # Unlike normal counting sort, divide the number by the divisor and get the digit
    divisor = 10 ** d
    for j in range(len(A)):
        digit = (int(A[j]/divisor)) % 10
        C[digit] = C[digit] + 1
    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        digit = (int(A[j]/divisor)) % 10
        B[C[digit] - 1] = A[j]
        C[digit] = C[digit] - 1
    # We have to return A for the next sorting step
    for i in range(len(A)):
        A[i] = B[i]
    return A


# Radix Sort
# Took slight references from https://www.geeksforgeeks.org/radix-sort/
# Such as using 10 instead of k like in normal counting sort
def radix_sort(A, d):
    for i in range(d):
        counting_radix_sort(A, i)
    return A


def do_radix_sort(A):
    d = 0
    for i in range(len(A)):
        if A[i] > 1:
            length = len(str(A[i]))
            d = length if length > d else d
    return radix_sort(A, d)


# ----------------------------------------------------------------------------------------------------- #
# -------------------------------------- QUICKSORT FOR COMPARISON ------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


# ----------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #

def test_sort(A):
    print("------------------------------------------------------------")
    print("Original array:", A)

    buckarr = A[:]
    do_bucket_sort(buckarr)
    quickarr = A[:]
    quicksort(quickarr, 0, len(A) - 1)
    radarr = A[:]
    radarr = do_radix_sort(radarr)

    print("Sorted array using bucket sort:", buckarr)
    print("Sorted array using quicksort:", quickarr)
    print("Sorted array using radix sort:", radarr)
    print("------------------------------------------------------------")

# Uncomment if need to test all the sorts
# test_sort([7, 4, 10, 8, 1, 9, 3, 16, 14, 2])
# test_sort([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
# test_sort([3, 2, 5, 10, 8, 7])
# test_sort([9, 2, 50, 10, 10, 40, 14, 30, 6])
# test_sort([768, 231, .321, .456, 2.220, 214, 123])

# ------------------------------------------------------------------------------------------------------- #
# --------------------------------PLOTTING THE CODE TIME VS COMPLEXITY----------------------------------- #
# ------------------------------------------------------------------------------------------------------- #

# Taken from Week 3

from random import sample
from timeit import timeit

num_samples = range(10, 1000, 10)

t_bucketsort_integer = []
t_bucketsort_decimal = []
t_radixsort = []
t_quicksort = []
y_nlogn = []

# c to be changed according to device and sometimes resources
c = 1/5000000

for n in num_samples:
    my_list = sample(range(n), n)

    # Compare bucketsort converting to decimal and without
    buckarr_integer = my_list[:]
    buckarr_decimal = [0] * len(buckarr_integer)

    # Already convert bucket to floating point
    greatest = 0
    for i in range(len(buckarr_integer)):
        if buckarr_integer[i] > 1:
            length = len(str(buckarr_integer[i]))
            greatest = length if length > greatest else greatest
    divisor = 10 ** greatest
    for i in range(len(buckarr_decimal)):
        buckarr_decimal[i] = (buckarr_integer[i] / divisor)

    radarr = my_list[:]
    d = 0
    for i in range(len(radarr)):
        if radarr[i] > 1:
            length = len(str(radarr[i]))
            d = length if length > d else d

    quickarr = my_list[:]

    y_nlogn.append(c * n * np.log(n))

    time_bucketsort_integer = timeit('do_bucket_sort(buckarr_integer)', number=1, globals=globals())
    time_bucketsort_decimal = timeit('bucket_sort(buckarr_decimal)', number=1, globals=globals())
    time_radixsort = timeit('radix_sort(radarr, d)', number=1, globals=globals())
    time_quicksort = timeit('quicksort(quickarr, 0, len(quickarr) - 1)', number=1, globals=globals())

    t_bucketsort_integer.append(time_bucketsort_integer)
    t_bucketsort_decimal.append(time_bucketsort_decimal)
    t_radixsort.append(time_radixsort)
    t_quicksort.append(time_quicksort)


plt.plot(num_samples, y_nlogn, label=f'c * n (log n), c = {c}')

plt.plot(num_samples, t_bucketsort_integer, label="Bucket Sort Runtime With Conversion to Float (+3n)")
plt.plot(num_samples, t_bucketsort_decimal, label="Bucket Sort Runtime Without Conversion (Already float)")
plt.plot(num_samples, t_radixsort, label="Radix Sort Runtime")
plt.plot(num_samples, t_quicksort, label="Quicksort Runtime")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------------------------------- #
