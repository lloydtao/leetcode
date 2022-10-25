#!/usr/bin/env python3
"""
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Take each number and check if its complement has been seen before. If not,
        add it to the list of known complements along with its index.

        Args:
            nums (List[int]): Input array of integers
            target (int): Target integer

        Returns:
            List[int]: Indices of the two integers that sum to target
        """
        # Initialise hash map to store known integers
        complements = {}
        # Iterate through the list
        for i in range(len(nums)):
            # Check if the current number's complement has been seen before
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            # Add the current number to the list of known complements
            complements[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Take each pair of numbers and see if they add up to the target.

        Args:
            nums (List[int]): Input array of integers
            target (int): Target integer

        Returns:
            List[int]: Indices of the two integers that sum to target
        """
        # Get length of input array
        n = len(nums)
        # Iterate over all pairs (i,j)
        for i in range(n):
            for j in range(i + 1, n):
                # Check if this pair equals the target
                if nums[i] + nums[j] == target:
                    return [i, j]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[2, 7, 11, 15], 9]
        expected = [0, 1]

        assert Solution().twoSum(*case) == expected
