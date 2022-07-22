#!/usr/bin/python3

"""
Longest Substring with Same Letters after Replacement
Problem Statement
Given a string with lowercase letters only, if you are 
allowed to replace no more than k letters with any letter,
find the length of the longest substring 
having the same letters after replacement

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' 
to have a longest repeating substring "bbbbb".

Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' 
to have a longest repeating substring "bbbb".

Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' 
to have the longest repeating substring "ccc"
"""


class solution:
    """FIRST METHOD"""

    def maxSubS_SameLettres(self, s: str, k: int) -> int:
        ch_count = {}
        max_len = 0
        w_len = 0
        w_start = 0

        for w_end in range(len(s)):
            ch_count[s[w_end]] = 1 + ch_count.get(s[w_end], 0)

            while (w_end - w_start + 1) - max(ch_count.values()) > k:
                ch_count[s[w_start]] -= 1
                w_start += 1
            max_len = max(max_len, w_end - w_start + 1)
        return max_len

    def Char_Replacement(self, s: str, k: int) -> int:
        ch_count = {}
        max_len = 0
        max_f = 0
        w_start = 0

        for w_end in range(len(s)):
            ch_count[s[w_end]] = 1 + ch_count.get(s[w_end], 0)

            max_f = max(max_f, ch_count[s[w_end]])
            while (w_end - w_start + 1) - max_f > k:
                ch_count[s[w_start]] -= 1
                w_start += 1
            max_len = max(max_len, w_end - w_start + 1)
        return max_len


res = solution()
tst = solution()
tl = res.maxSubS_SameLettres("aabccbb", 2)
ts = tst.Char_Replacement("aabccbb", 2)

print(tl)
print(ts)
#w_len - max(ch_count.values()) > k
# w_len = w_end - w_start + 1
