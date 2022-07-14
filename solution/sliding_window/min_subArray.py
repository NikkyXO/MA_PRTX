#!/usr/bin/python3.8
"""
Problem Statement

Given an array of positive numbers and a positive number 'S', 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to 'S'. Return 0, if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or
equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or
equal to '7' is [8].

Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to
'8' are [3, 4, 1] or [1, 1, 6].

"""
import math

"""
def MinSubArray(array, k):
    if k in array:
        return 1

    min_len = float('inf')
    windowStart = 0
    sub_sum = array[windowStart]
    #sub_sum = array[(windowStart := 0)]

    array_len = len(array)
    windowEnd = 1
    while windowEnd < array_len:
        while sub_sum < k:
            sub_sum += array[windowEnd]
            windowEnd += 1
        while sub_sum > k:
            sub_sum -= array[windowStart]
            windowStart += 1
        if sub_sum == k:
            print(array[windowStart:windowEnd], windowEnd - windowStart)
            min_len = min(min_len, windowEnd - windowStart)
            sub_sum -= array[windowStart]
            windowStart += 1
    return min_len if min_len <= array_len else -1


"""


def FindMinSubArray(array, k):
    if array is None or k == 0:
        return None
    windowStart = 0
    window_sum = 0
    array_len = len(array)
    min_len = math.inf

    for windowend in range(array_len):
        window_sum += array[windowend]
        while window_sum >= k:
            # print(window_sum)
            min_len = min(min_len, windowend - windowStart)
            window_sum -= array[windowStart]
            windowStart += 1
    return min_len if min_len < array_len else -1


if __name__ == '__main__':
    res = FindMinSubArray([2, 1, 5, 2, 3, 2], 7)
    print(res)
