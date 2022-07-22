#!/usr/bin/python 3.8

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""
    for i in range(len(strs[0])):
        chars = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != chars:
                return strs[0][:i]
    return strs[0]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    res = longestCommonPrefix(strs)
    print(res)
