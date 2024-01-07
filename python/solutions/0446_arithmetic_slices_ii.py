#!/usr/bin/env python3
"""
Given an integer array `nums`, return the number of all the arithmetic subsequences of
`nums`.

A sequence of numbers is called arithmetic if it consists of at least three elements and
if the difference between any two consecutive elements is the same.

- For example, `[1, 3, 5, 7, 9]`, `[7, 7, 7, 7]`, and `[3, -1, -5, -9]`, are all
arithmetic sequences.

- For example, `[1, 1, 2, 5, 7]` is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements
(or, no elements) of the array.

- For example, `[2, 5, 10]` is a subsequence of `[1, 2, 1, 2, 4, 1, 5, 10]`.

[Unsure of solution, need to revisit.]
"""
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Dynamic Programming approach:
        - Initialize a 2D array dp to store the number of arithmetic subsequences ending
        at index i with difference diff.
        - Iterate through the array and for each pair of elements, calculate the
        difference.
        - Use defaultdict to efficiently track the count of subsequences with the same
        difference.
        - Increment the count of subsequences ending at the current index based on the
        count of subsequences ending at the previous index with the same difference.
        - Sum up all the counts to get the total number of arithmetic subsequences.
        """
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]
                dp[i][diff] += cnt + 1
                ans += cnt
        return ans


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[2, 4, 6, 8, 10]]
        expected = 7

        assert Solution().numberOfArithmeticSlices(*case) == expected
