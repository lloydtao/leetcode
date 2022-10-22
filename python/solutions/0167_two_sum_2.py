#!/usr/bin/env python3
"""
Given a sorted list of integers `numbers`, find two numbers such that they add up to a
specific `target` number. Return the indices of the two numbers in an integer array of
length two (i.e. [i, j]).

Tests are generated such that there is exactly one solution. The same element must not
be used twice. 

The solution must use only constant extra space.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Two pointers: Set a start pointer and an end pointer. For these pointers,
        take their sum. If their sum is larger than the target, the end pointer needs
        to be shifted down, making their sum smaller. If their sum is smaller than the
        target, the start pointer can similarly be shifted up. Repeat this until their
        sum is the target, and you now have the two indexes.

        This has complexity of O(n). Compare this to a binary search in a loop, with
        complexity of O(n log n).
        """
        n = len(numbers)
        for i in range(n):
            # Set start and end pointers
            start = 0
            end = n - 1
            # Adjust start and end pointers until their sum equals the target
            while True:
                current_sum = numbers[start] + numbers[end]
                if current_sum == target:
                    return [start + 1, end + 1]  # Adjust for one-based indexing
                # Sum is smaller than target
                if current_sum < target:
                    start += 1
                # Sum is larger than target
                else:
                    end += -1

    def twoSum_brute(self, numbers: List[int], target: int) -> List[int]:
        """For each number, look ahead for its complement."""
        n = len(numbers)
        for i in range(n):
            # Calculate complement to look for
            complement = target - numbers[i]
            # Look ahead in the list for the complement
            for j in range(i + 1, n):
                if numbers[j] == complement:
                    return [i + 1, j + 1]  # Adjust for one-based indexing


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[2, 7, 11, 15], 9]
        expected = [1, 2]

        assert Solution().twoSum(*case) == expected

    def test_width(self):
        """Given test case from Leetcode."""
        case = [[2, 3, 4], 6]
        expected = [1, 3]

        assert Solution().twoSum(*case) == expected

    def test_final(self):
        """Given test case from Leetcode."""
        case = [[5, 25, 75], 100]
        expected = [2, 3]

        assert Solution().twoSum(*case) == expected

    def test_negative(self):
        """Given test case from Leetcode."""
        case = [[-1, 0], -1]
        expected = [1, 2]

        assert Solution().twoSum(*case) == expected
