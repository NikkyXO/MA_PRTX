#!/usr/bin/python3
"""Problem statement
    Given a string, find the length of the longest
    substring with no more than K distinct characters
"""

"""
from collections import defaultdict


class solution:
    def longestSubstringKdistinct(self, s: str, k: int) -> int:
        d = defaultdict(int)

        max_len = 0
        windowstart = 0
        str_len = len(s)

        for window_end, ch in enumerate(s):
            d[ch] += 1

            while len(d) > k:
                d[s[windowstart]] -= 1

                if d[s[windowstart]] == 0:
                    del d[s[windowstart]]

                windowstart += 1
            max_len = max(max_len, window_end - windowstart)
        return max_len


if __name__ == '__main__':
    s = "aabacbeabbed"
    k = 3
    res = solution()
    print(res.longestSubstringKdistinct(s, k))

"""


class solution:
    def longestSubstringKdistinct(self, s: str, k: int) -> int:
        windowend = 0
        windowstart = 0
        str_len = len(s)
        max_len = 0
        d = {}

        while windowend < str_len:
            d[s[windowend]] = windowend
            if len(d) > k:
                min_idx = min(d.values())
                windowstart = min_idx + 1
                del d[s[min_idx]]

            max_len = max(max_len, windowend - windowstart + 1)
            windowend += 1
        return max_len


if __name__ == '__main__':
    s = "aabacbeabbed"
    k = 3
    res = solution()
    print(res.longestSubstringKdistinct(s, k))
