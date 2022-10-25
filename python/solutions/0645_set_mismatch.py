#!/usr/bin/env python3
"""
You have a set of integers `s` containing the numbers 1 through `n`.

Due to some error, one of the numbers in `s` was duplicated to another number in the
set, resulting in the repetition of one numbers and the loss of another number.

You are given an array `nums` represeting the set of integers after this error.

Find the number that occurs twice and the number that is missing.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Perform cycle detection to find the duplicate number. We can achieve this in
        O(n) time complexity and O(1) space complexity through Floyd's hare and
        tortoise algorithm. The missing value can then be inferred from the duplicate
        value and the expected sum of the list.

        For example, if 4 replaces 1, then the total sum will be (4 - 1) = 3 larger
        than the expected sum. Knowing that 4 is the duplicate, and as the sum is 3
        larger than expected, the value that it replaced must be (4 - 3) = 1.

        Args:
            nums (List[int]): Array of integers after the duplication error

        Returns:
            List[int]: The duplicated value followed by the missing value
        """
        # Get duplicate value through Floyd's hare and tortoise
        total = sum(nums)
        duplicate = None
        for n in nums:
            index = abs(n)
            # Check if value revisited
            if nums[index - 1] < 0:
                duplicate = index  # Value revisited, store as duplicate
                break
            # Make negative to flag as visited
            nums[index - 1] *= -1
        # Find missing value by taking duplicate and subtracting the difference of sums
        n = len(nums)
        expected = n * (n + 1) // 2
        missing = duplicate - (total - expected)  # ∵ difference = duplicate - missing
        # Return the values
        return [duplicate, missing]

    def findErrorNums_sets(self, nums: List[int]) -> List[int]:
        """Compare the sum of the list with the sum of its set to find the duplicate
        value. The missing value can then be inferred from the duplicate value and
        the expected sum of the list.

        For example, if 4 replaces 1, then the total sum will be (4 - 1) = 3 larger
        than the expected sum. Knowing that 4 is the duplicate, and as the sum is 3
        larger than expected, the value that it replaced must be (4 - 3) = 1.

        Args:
            nums (List[int]): Array of integers after the duplication error

        Returns:
            List[int]: The duplicated value followed by the missing value
        """
        # Get duplicate value by comparing sum with set sum
        total = sum(nums)
        duplicate = total - sum(set(nums))
        # Find missing value by taking duplicate and subtracting the difference of sums
        n = len(nums)
        expected = n * (n + 1) // 2
        missing = duplicate - (total - expected)  # ∵ difference = duplicate - missing
        # Return the values
        return [duplicate, missing]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 2, 2, 4]]
        expected = [2, 3]

        assert Solution().findErrorNums(*case) == expected

    def test_ones(self):
        """Given test case from Leetcode, with two 1s."""
        case = [[1, 1]]
        expected = [1, 2]

        assert Solution().findErrorNums(*case) == expected

    def test_twos(self):
        """Given test case from Leetcode, with two 2s."""
        case = [[2, 2]]
        expected = [2, 1]

        assert Solution().findErrorNums(*case) == expected

    def test_unsorted(self):
        """Given test case from Leetcode, with an unsorted array."""
        case = [[3, 2, 4, 3, 6, 5]]
        expected = [3, 1]

        assert Solution().findErrorNums(*case) == expected
