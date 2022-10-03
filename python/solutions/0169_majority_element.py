#!/usr/bin/env python3
"""
Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n / 2` times.
You may assume that the majority element always exists in the array.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        threshold = len(nums) / 2
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
            if count[nums[i]] > threshold:
                return nums[i]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[3, 2, 3]]
        expected = 3

        assert Solution().majorityElement(*case) == expected

    def test_long(self):
        """Given test case from Leetcode."""
        case = [[2, 2, 1, 1, 1, 2, 2]]
        expected = 2

        assert Solution().majorityElement(*case) == expected

    def test_single(self):
        """Given test case from Leetcode."""
        case = [[1]]
        expected = 1

        assert Solution().majorityElement(*case) == expected
