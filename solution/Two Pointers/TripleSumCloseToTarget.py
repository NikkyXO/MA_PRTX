#!/usr/bin/python3.8
"""
Problem Statement #

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:

Input: [-3, -1, 1, 2]
        i
          p1        p2
, target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""

import sys


def TripletSumCloseToTarget(arr, target):

    arr.sort()
    n = len(arr) - 1
    val = 0
    closest_sum = sys.maxsize
    val_dif = 0

    for i in range(n):
        x = arr[i]
        start = i + 1
        end = n

        while start < end:
            val = x + arr[start] + arr[end]
            if val > target:
                end -= 1
            if val < target:
                start += 1
            val_dif = target - val
            if abs(target - closest_sum) > abs(val_dif):
                closest_sum = val
    return closest_sum


if __name__ == '__main__':
    arr = [-2, 0, 1, 2]
    target = 2
    res = TripletSumCloseToTarget(arr, target)
    print(res)


"""Time COMPLEXITY : 0(n*2)"""
