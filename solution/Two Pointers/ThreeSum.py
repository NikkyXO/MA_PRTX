#!/usr/bin/python3.8

"""
Have the function ThreeSum(arr) take the array of integers stored in an array and
determine if any three distinct members(excluding the first element) in the array can 
sum up to the first element in the array

for example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three sets of triplets
that sum to the number 8:[2, 1, 5], [4, 5, -1] and [10, -1, -1]
Your program should return true if 3 distinct elements sum to the first element
Otherwise your program should return the string false.
The input will always contain at least elements

Examples
input: [10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2]
        p1                                 p2
output: true
"""


def ThreeSum(arr):
    p1 = 1
    p2 = len(arr) - 1
    target = arr[0]
    sum_no = 0

    while p1 < p2:
        if arr[p1] > target:
            pass
