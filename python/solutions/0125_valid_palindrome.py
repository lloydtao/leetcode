#!/usr/bin/env python3
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters, and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `True` if palindrome, or `False` otherwise.
"""
from math import ceil
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Read string simultaneously from beginning and end.
        Make sure that characters match.

        Args:
            s (str): Input string

        Returns:
            bool: String is palindromic
        """
        # Strip all non-alphanumeric characters
        s = "".join([c.upper() for c in s if c.isalnum()])
        print(s)
        # Iterate through string each way simultaneously
        check_range = ceil(len(s) / 2)
        for i in range(check_range):
            c1 = s[i]  # 0, 1, 2, 3...
            c2 = s[-i - 1]  # -1, -2, -3, -4...
            # Compare characters
            if c1 == c2:
                continue
            # Characters do not match
            return False
        return True


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["A man, a plan, a canal: Panama"]
        expected = True

        assert Solution().isPalindrome(*case) == expected
