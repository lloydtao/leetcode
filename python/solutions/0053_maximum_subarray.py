#!/usr/bin/env python3
"""
Given an integer array `nums`, find the contiguous subarray (containing at least one
number) which has the largest sum, and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Run through the list from left to right, keeping track of the current sum.
        If the sum becomes negative, reset it to zero, as the current subarray is
        useless to the sum."""
        # Get starting value (first element)
        max_sum = nums[0]
        current_sum = nums[0]
        # Handle case of single value
        if len(nums) == 1:
            return max_sum
        # Iterate from second element
        for n in nums[1:]:
            # Break negative subarray by reseting current sum to zero
            if current_sum < 0:
                current_sum = 0
            # Calculate current sum, and see if it's a maximum
            current_sum += n
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
        expected = 6  # From: [4, -1, 2, 1]

        assert Solution().maxSubArray(*case) == expected

    def test_single(self):
        """Given test case from Leetcode, using a single element."""
        case = [[1]]
        expected = 1  # From: [1]

        assert Solution().maxSubArray(*case) == expected
