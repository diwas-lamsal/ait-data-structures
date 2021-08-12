# Diwas Lamsal - st122324
# 2021-August-10 Data Structures and Algorithms Week 1
# Question: Using python, please implement:
# - Insertion Sort
# - Merge Sort

import math


# -------------------------------------- Insertion Sort -------------------------------------- #


def insertion_sort(slist):
    """
    Sorts the given list in ascending order using insertion sort
    Parameters:
        slist - the list to be sorted
    """
    for x in range(1, len(slist)):  # Starting from 1 because the first element has nothing to compare itself to
        key = slist[x]
        y = x - 1
        while y > -1 and slist[y] > key:  # iteratively 
            slist[y + 1] = slist[y]
            y -= 1
        slist[y + 1] = key


# Testing the insertion sort function

sample_list = [5, 2, 1, 7, 4, 9, 11, 45, 3, 27, 33, 4]
print(f"List before using insertion sort: {sample_list}")
insertion_sort(sample_list)
print(f"List sorted using insertion sort: {sample_list}")


# -------------------------------------- Merge Sort -------------------------------------- #

def merge(slist, start, middle, end):
    """
    Merges the given list
    Parameters:
        slist - the list to be sorted
        start - the starting index
        middle - the middle index (element to be the splitting point)
        end - the ending index
    """
    n = middle - start + 1
    m = end - middle
    left = [None] * (n + 1)
    right = [None] * (m + 1)

    for i in range(0, n):
        left[i] = slist[start + i]
    for j in range(0, m):
        right[j] = slist[middle + 1 + j]

    left[n] = math.inf
    right[m] = math.inf
    i = 0
    j = 0

    for k in range(start, end + 1):
        # print(f"k:{k}, n:{n}, m:{m}, i:{i}, j:{j}, start: {start}, end: {end}, \n left: {left}, right: {right}, "
        #       f"slist:{slist}")
        if left[i] <= right[j]:
            slist[k] = left[i]
            i += 1
        else:
            slist[k] = right[j]
            j += 1

    # Alternate solution:
    # This was referenced from https://www.programiz.com/dsa/merge-sort
    # I was trying this solution while I had errors trying to implement the pseudocode. I fixed the errors later.
    # k = start
    # while i < n and j < m:  # sort all the elements in left and right array while merging them
    #     if left[i] <= right[j]:
    #         slist[k] = left[i]
    #         i += 1
    #     else:
    #         slist[k] = right[j]
    #         j += 1
    #     k += 1
    #
    # # If any elements remain in the longer array, copy the elements
    # while i < n:
    #     slist[k] = left[i]
    #     i += 1
    #     k += 1
    # while j < m:
    #     slist[k] = right[j]
    #     j += 1
    #     k += 1


def merge_sort(slist, start, end):
    """
    Sorts the given list given list in ascending order using merge sort
    Parameters:
        slist - the list to be sorted
        start - the starting index
        end - the ending index
    """
    if start < end:
        middle = (start + end) // 2
        merge_sort(slist, start, middle)
        merge_sort(slist, middle + 1, end)
        merge(slist, start, middle, end)


# Testing the merge sort function

sample_list = [9, 2, 3, 11, 4, 8, 20, 7, 15]
print(f"List before using merge sort: {sample_list}")
merge_sort(sample_list, 0, len(sample_list) - 1)
print(f"List sorted using merge sort: {sample_list}")


# -------------------------------------- Testing Algorithms -------------------------------------- #


num_elements = int(input("Enter the number of elements to be sorted in the list: "))
user_list = [0] * num_elements
for i in range(0, num_elements):
    user_list[i] = int(input(f"Enter element {i+1}: "))
print(f"List before sorting: {user_list}")
insertion_sort(user_list)
print(f"List sorted using insertion sort: {user_list}")
merge_sort(user_list, 0, len(user_list) - 1)
print(f"List sorted using merge sort: {user_list}")
