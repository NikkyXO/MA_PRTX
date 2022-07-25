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
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefx = strs[0]
    pf_len = len(prefx)

    for s in strs[1:]:
        while prefx != s[0:pf_len]:
            prefx = prefx[0:(pf_len - 1)]
            pf_len -= 1

            if pf_len == 0:
                return ""

    return prefx


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    res = longestCommonPrefix(strs)
    print(res)
