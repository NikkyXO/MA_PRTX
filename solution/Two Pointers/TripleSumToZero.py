#!/usr/bin/python3.8

"""
Problem Statement #

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
         i
            p1=i+1           p2=n-1
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""


def TripletSumToZero(arr):
    n = len(arr) - 1
    arr.sort()
    new_arr = [[0] * 3 for i in range(n//2)]

    for i in range(0, n):
        start = i + 1
        end = n
        x = arr[i]
        while start <= end:
            if (x + arr[start] + arr[end] == 0):

                new_arr[i] = [x, arr[start], arr[end]]
                end -= 1
                start += 1
            elif (x + arr[start] + arr[end] < 0):
                start += 1
            else:
                end -= 1
    return new_arr


if __name__ == '__main__':
    arr = [-3, 0, 1, 2, -1, 1, -2]
    res = TripletSumToZero(arr)
    print(res)
"""Time Complexity 0(n*2)"""
