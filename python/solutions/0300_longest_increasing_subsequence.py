#!/usr/bin/env python3
"""
Given an integer array `nums`, return the length of the longest 'strictly increasing'
subsequence.

[Unsure of solution, need to revisit.]
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

    def lengthOfLIS_brute_force(self, nums: List[int]) -> int:
        """Start with [] as the only existing subsequence. Iterate over the input array,
        creating a new subsequence for each existing subsequence whose tail is smaller
        than the current input. Return the length of the longest subsequence.
        """
        subsequences: List[List[int]] = [
            [],
        ]
        longest_subsequence: int = 1
        # Iterate over input array
        for num in nums:
            # Check tail of each existing subsequence
            for subsequence in subsequences:
                if subsequence == [] or subsequence[-1] < num:
                    # Create new subsequence
                    new_subsequence = subsequence.copy()
                    new_subsequence.append(num)
                    # Add new subsequence to existing subsequences
                    subsequences.append(new_subsequence)
                    # Update length of longest subsequence
                    longest_subsequence = max(longest_subsequence, len(new_subsequence))
        # Return length of longest subsequence
        return longest_subsequence


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[10, 9, 2, 5, 3, 7, 101, 18]]
        expected = 4

        assert Solution().lengthOfLIS(*case) == expected

    def test_similar_values(self):
        """Given similar test case from Leetcode."""
        case = [[0, 1, 0, 3, 2, 3]]
        expected = 4

        assert Solution().lengthOfLIS(*case) == expected

    def test_repeated_values(self):
        """Given repeating case from Leetcode."""
        case = [[7, 7, 7, 7, 7, 7, 7]]
        expected = 1

        assert Solution().lengthOfLIS(*case) == expected
