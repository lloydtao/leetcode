#!/usr/bin/env python3
"""
Given two binary strings `a` and `b`, return their sum as a binary string.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        result = ""
        # Keep iterating while characters are left to read
        while a or b:
            # Get values for addition
            if a:
                a_current = int(a[-1])
            else:
                a_current = 0
            if b:
                b_current = int(b[-1])
            else:
                b_current = 0
            # Handle case where carrying the 1 from last addition
            if carry:
                if a_current and b_current:
                    result = "1" + result
                elif a_current or b_current:
                    result = "0" + result
                else:
                    result = "1" + result
                    carry = False
            # Handle case of regular addition
            else:
                if a_current and b_current:
                    result = "0" + result
                    carry = True
                elif a_current or b_current:
                    result = "1" + result
                else:
                    result = "0" + result
            # Pop ends of strings off
            a = a[:-1]
            b = b[:-1]
        # Append a final 1 to the front if still carrying the 1
        if carry:
            result = "1" + result
        return result


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["11", "1"]
        expected = "100"

        assert Solution().addBinary(*case) == expected

    def test_longer(self):
        """Given test case from Leetcode."""
        case = ["1010", "1011"]
        expected = "10101"

        assert Solution().addBinary(*case) == expected
