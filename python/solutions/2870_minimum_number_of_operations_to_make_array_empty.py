#!/usr/bin/env python3
"""
You are given a 0-indexed array `nums` consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:
- Choose two elements with equal values and delete them from thearray.
- Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or `-1` if it
is not possible.

Example:

Input: nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
Output: 4
Explanation: Remove a pair of 2s to get [3, 3, 2, 4, 2, 4]. Remove another pair of 2s to
get [3, 3, 4, 4]. Remove a pair of 3s to get [4, 4]. Remove a pair of 4s to get [].
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """Create a frequency map of each value. Then, calculate how many operations are
        required to clear a particular value. The optimal strategy is to clear as many
        triples as possible until the remainder requires removing a double in order to
        to be completely cleared, or rather, removing as little doubles as possible so
        that the remainder is a multiple of 3."""

        def minOperationsForFrequency(num: int) -> int:
            operations = 0
            # Case where input is 1, which is not reducable
            if num == 1:
                return -1
            # Case where input is 2 larger than a multiple of 3
            if num % 3 == 2:
                num -= 2
                operations += 1
            # Case where input is 1 larger than a multiple of 3
            elif num % 3 == 1:
                num -= 4
                operations += 2
            # Remove multiples of 3
            return operations + num // 3

        # Initialise counter
        total_operations = 0
        # Get frequency map of values
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        # Iterate through frequencies, calculating minimum operations for each frequency
        for _, frequency in frequencies.items():
            # Get operations needed
            operations = minOperationsForFrequency(frequency)
            #
            if operations == -1:
                return -1
            total_operations += operations
        # Return total minimum operations
        return total_operations


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[2, 3, 3, 2, 2, 4, 2, 3, 4]]
        expected = 4

        assert Solution().minOperations(*case) == expected

    def test_impossible(self):
        """Given impossible test case from Leetcode."""
        case = [[2, 1, 2, 2, 3, 3]]
        expected = -1

        assert Solution().minOperations(*case) == expected
