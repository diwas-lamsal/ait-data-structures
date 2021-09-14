# Diwas Lamsal - st122324
# 2021-August-18 Data Structures and Algorithms Week 5
# Question: Implementing Heapsort and Quicksort Using Python

# imports
import math


# ----------------------------------------------------------------------------------------------------- #
# --------------------------------------- IMPLEMENTING HEAPSORT --------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #

def parent(i):
    return math.floor((i - 1) / 2) # i - 1 because python index starts with 0


def left(i):
    return 2 * i + 1 # Doing + 1 because python index starts with 0 and left of 0 would otherwise be 2 * 0 = 0


def right(i):
    return (2 * i) + 2 # Doing + 2 because of the same reason as left


def max_heapify(A, i, heapsize):
    l = left(i)
    r = right(i)
    if l <= heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest, heapsize)


def build_max_heap(A):
    heapsize = len(A) - 1
    # In the for loop, using the index down to 0 does not work but -1 works
    # I also checked online for other implementations of heapsort and everyone went down to -1

    # Because 0 is the index of the first element, we are performing max-heapify up to this index.
    # the -1 implies run the loop until index >= 0 and stop after we have heapified all the parent elements
    for i in range(math.floor((len(A) - 1) / 2), -1, -1):
        max_heapify(A, i, heapsize)


def heapsort(A):
    heapsize = len(A) - 1
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heapsize -= 1
        max_heapify(A, 0, heapsize)


# ----------------------------------------------------------------------------------------------------- #
# --------------------------------------- IMPLEMENTING QUICKSORT -------------------------------------- #
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
    heaparr = A[:]
    quickarr = A[:]
    heapsort(heaparr)
    quicksort(quickarr, 0, len(A) - 1)
    print("Sorted array using heapsort:", heaparr)
    print("Sorted array using quicksort:", quickarr)
    print("------------------------------------------------------------")


test_sort([7, 4, 10, 8, 1, 9, 3, 16, 14, 2])
test_sort([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
test_sort([3, 2, 5, 10, 8, 7])
test_sort([9, 2, 5, 1, 10, 4, 14, 3, 6])

# ----------------------------------------------------------------------------------------------------- #
