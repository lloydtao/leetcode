#!/usr/bin/env python3
"""
Given two string `s` and `t`, return True if `t` is an anagram of `s`, or False otherwise.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        # Build count of letters in `s`
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        # Compare to letters in `t`
        for c in t:
            if c in freq:
                # Letter exists once more in s, delete it from count
                if freq[c] == 1:
                    freq.pop(c)
                # Letter exists multiple more times in s, decrement its count
                elif freq[c] > 1:
                    freq[c] -= 1
            # Letter no longer exists in count, return False
            else:
                return False
        # If count is empty, return True
        return not freq


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["anagram", "nagaram"]
        expected = True

        assert Solution().isAnagram(*case) == expected
