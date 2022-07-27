#!/usr/bin/python3.8
"""
Problem Statement #

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

Logic [1, 2, 3, 4, 6] Target=6 Note=sorted
        p1       p1
"""


def twoSum(arr, target):
    p1 = 0
    p2 = len(arr) - 1
    sum = 0
    ret_arr = [0, 0]

    while p1 < p2 and sum != target:
        sum = arr[p1] + arr[p2]
        if sum > target:
            p2 -= 1
        if sum < target:
            p1 += 1
        if sum == target:
            ret_arr = p1, p2
    return ret_arr


def twoSum1(arr, target):

    nums_hash = {}
    for i, num in enumerate(arr):
        Match = target - num
        if Match in nums_hash:
            return [nums_hash[Match], i]
        nums_hash[num] = i


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    target = 6
    res = twoSum1(arr, target)
    print(res)
