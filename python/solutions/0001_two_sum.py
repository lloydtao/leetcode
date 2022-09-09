#!/usr/bin/env python3
"""
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """For each number, check if a previous number is its complement.
        If not, add it to the list of known complements."""
        # Initialise store of integers
        complements = {}
        for i in range(len(nums)):
            # Check if a previous number is its complement
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            # Add the current number as a known complement
            complements[nums[i]] = i


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[2, 7, 11, 15], 9]
        expected = [0, 1]

        assert Solution().twoSum(*case) == expected
