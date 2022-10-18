#!/usr/bin/env python3
"""
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def countAndSay(self, n: int) -> str:
        # Handle empty case
        if n == 0:
            return ""
        # Build up string using count() function
        output = "1"
        for i in range(1, n):
            output = self.count(output)
        return output

    def count(self, s):
        """Take a string of digits and count its digits."""
        # Initialise variables for loop
        output = ""
        previous = s[0]
        count = 1
        # Iterate over string, starting from second element as first is handled above
        for n in s[1:]:
            # Character is same as previous, so increment count and continue
            if n == previous:
                count += 1
                continue
            # Character is different to previous, so handle string and reset count
            else:
                output += str(count) + previous
                count = 1
            # Set previous to current for next iteration
            previous = n
        # End reached, so handle string for final output
        output += str(count) + previous
        return output


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [4]
        expected = "1211"

        assert Solution().countAndSay(*case) == expected

    def test_base(self):
        """Given test case from Leetcode, using just the base case."""
        case = [1]
        expected = "1"

        assert Solution().countAndSay(*case) == expected

    def test_count(self):
        """Given test case from Leetcode."""
        case = ["21"]
        expected = "1211"

        assert Solution().count(*case) == expected

    def test_count_single(self):
        """Given test case from Leetcode."""
        case = ["1"]
        expected = "11"

        assert Solution().count(*case) == expected
