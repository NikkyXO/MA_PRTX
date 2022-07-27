#!/usr/bin/python3.8
"""
Problem Statement #

Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3] [   ]
        p1            p2
                       p
Output: [0, 1, 4, 4, 9]

Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""


def SortedArraysSquares(arr):
    new_list = [0, 0, 0, 0, 0]
    highestSquareIdx = len(arr) - 1
    end = len(arr) - 1
    start = 0
    leftSquare = 0
    rightSquare = 0

    while (start <= end):
        leftSquare = arr[start] * arr[start]
        rightSquare = arr[end] * arr[end]
        if leftSquare > rightSquare and highestSquareIdx >= 0:
            new_list[highestSquareIdx] = leftSquare
            highestSquareIdx -= 1
            start += 1
        else:
            rightSquare > leftSquare and highestSquareIdx >= 0
            new_list[highestSquareIdx] = rightSquare
            highestSquareIdx -= 1
            end -= 1
    return new_list


if __name__ == "__main__":
    arr = [-2, -1, 0, 2, 3]
    answer = SortedArraysSquares(arr)
    print(answer)

""" TIME COMPLEXITY = 0(N)
"""
