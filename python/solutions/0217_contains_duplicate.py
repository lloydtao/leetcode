#!/usr/bin/env python3
"""
Given an integer array `nums`, return True if any value appears at least twice in the
array, and return False if every element is distinct.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Run through the list of integers, and keep track of which values have been
        seen before. If a value has been seen before, return True. If the end of the
        list is reached without returning, return False.

        Args:
            nums (List[int]): List of values.

        Returns:
            bool: List contains a duplicate value.
        """
        # Initialise collection of seen values
        visited = {}
        # Iterate through values
        for n in nums:
            # Value has been seen before
            if n in visited:
                return True
            # Value has not been seen before
            visited[n] = None
        return False


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
        expected = True

        assert Solution().containsDuplicate(*case) == expected

    def test_false(self):
        """Given falsey test case from Leetcode."""
        case = [[1, 2, 3, 4]]
        expected = False

        assert Solution().containsDuplicate(*case) == expected
