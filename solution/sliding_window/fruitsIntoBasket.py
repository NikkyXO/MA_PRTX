#!/usr/bin/python3.8

"""
Problem statement:

Given an array of characters where each character represents a fruit tree, you are given
two baskets and your goal is to put maximum number of fruits in each basket. The only 
restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you cant skip a tree. You will pick one 
fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third 
fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


class solution:
    def maxFruitCountOf2Types(self, tree) -> int:
        windowStart = 0
        windowEnd = 0
        min_idx = 0
        max_len = 0
        tree_len = len(tree)
        d = {}

        while windowEnd < tree_len:
            d[tree[windowEnd]] = windowEnd
            if len(d) > 2:
                min_idx = min(d.values())
                windowStart = min_idx + 1
                del d[tree[min_idx]]
            max_len = max(max_len, windowEnd - windowStart + 1)
            windowEnd += 1
        return max_len


if __name__ == '__main__':
    res = solution()

    tree = ['A', 'B', 'C', 'B', 'B', 'C']  # d {b:4 c:5  } max_len= 5
    print(res.maxFruitCountOf2Types(tree))
