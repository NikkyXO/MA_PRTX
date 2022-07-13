#!/usr/bin/python3.8

import math
"""

def maxSumSubarraySumKSize(arr, k):

    ans = -math.inf
    for i in range(len(arr) - k + 1):
        sum = 0
        for j in range(i, i + k):
            sum += arr[j]
        ans = max(ans, sum)
    return ans


if __name__ == '__main__':
    print(maxSumSubarraySumKSize([2, 6, -9, 7, -1, 5, 4], 3))
    print(maxSumSubarraySumKSize([5, 2, -4, 9, -8, 3, -1, 5], 5))
"""


def maxSumSubarraySumKSize(array=[], k=0):

    windowStart = 0
    windowSum = 0
    ans = -math.inf

    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        if windowEnd >= k - 1:
            ans = max(ans, windowSum)
            windowSum -= array[windowStart]
            windowStart += 1
    return ans


if __name__ == '__main__':
    print(maxSumSubarraySumKSize([2, 6, -9, 7, -1, 5, 4], 3))
    print(maxSumSubarraySumKSize([5, 2, -4, 9, -8, 3, -1, 5], 5))
    print(maxSumSubarraySumKSize([2, 1, 5, 1, 3, 2], k=3))
    print(maxSumSubarraySumKSize([2, 3, 4, 1, 5], k=2))
