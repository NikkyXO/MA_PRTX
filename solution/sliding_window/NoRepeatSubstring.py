#!/usr/bin/python3.8
"""
PROBLEM STATEMENT

Given a string, find the length of the 
longest substring which has no repeating characters.Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

"""


class Solution:
    def NoRepeatSubstring(self, string):
        d = {}
        start = 0
        end = 0
        max_len = 0
        str_len = len(string)

        while end < str_len:
            d[string[end]] = end
            if string[end] in d.values():
                start = end + 1
                del d[string[end]]
            end += 1
            max_len = len(d.keys())
        return max_len


if __name__ == '__main__':
    String = "aabccbb"
    res = Solution()
    print(res.NoRepeatSubstring(String))
