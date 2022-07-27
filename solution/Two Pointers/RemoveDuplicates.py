#!/usr/bin/python3.8

"""
PROBLEM STATEMENT

Given an array of SORTED numbers, remove all duplicates from it...
YOU SHOULD NOT USE ANY EXTRA SPACE, after removing the duplicates in-place return the
new length of the array

Examples
input : [2, 3, 3, 3, 6, 9, 9]
            l
            p
output : 4

input : [2, 2, 2, 11]
output : 2
"""


def remove_duplicates(arr):
    l = 1

    for p in range(1, len(arr)):
        if arr[p] != arr[l]:
            arr[l] = arr[p]
            l += 1
    return l


if __name__ == '__main__':
    res = remove_duplicates([2, 3, 3, 3, 6, 9, 9])
    print(res)
