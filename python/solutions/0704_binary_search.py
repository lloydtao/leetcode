#!/usr/bin/env python3
"""
Given an array of integers `nums` which is sorted in ascending order, an an integer
`target`, write a function to search `target` in `nums`.

If `target` exists, return its index. Otherwise, return -1.
"""
from math import sqrt
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set search pointers (start and end)
        p1 = 0
        p2 = len(nums)
        # While pointers haven't touched
        while p1 < p2:
            # Find middle value based on current pointers
            pm = int(p1 + (p2 - p1) / 2)
            middle = nums[pm]
            # Compare to target
            if target == middle:
                return pm
            elif target > middle:
                # Shift lower pointer up
                p1 = pm + 1
            else:
                # Shift upper pointer down
                p2 = pm
        return -1


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[-1, 0, 3, 5, 9, 12], 9]
        expected = 4

        assert Solution().search(*case) == expected

    def test_erroneous(self):
        """Given test case from Leetcode."""
        case = [[-1, 0, 3, 5, 9, 12], 2]
        expected = -1

        assert Solution().search(*case) == expected

    def test_empty(self):
        """Given test case from Leetcode."""
        case = [[], 0]
        expected = -1

        assert Solution().search(*case) == expected
