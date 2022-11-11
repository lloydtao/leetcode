#!/usr/bin/env python3
"""
Given an integer array `nums`, sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once.

Return k after placing the final result in the first k slots of nums.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Initialise two pointers: the result pointer, and the array pointer:
        - The array pointer is used to traverse each element in the input list.
        - The result pointer is used to keep track of where we're writing to the list.
        Method:
        - Move the array pointer along, and:
          - If the next element is different, write it to the result pointer and move the
        result pointer along.
          - If the next element is the same, do nothing.
        - Return the result pointer at the end, which will equal the position of the
        k-th element (i.e. k is the final result pointer).

        Args:
            nums (List[int]): Input list of numbers to be edited in-place

        Returns:
            int: The k-th unique element
        """
        # Keep track of previous letter
        previous = None
        # Initialise our two pointers
        result_pointer = 0
        for array_pointer in range(len(nums)):
            # Compare current letter to previous
            current = nums[array_pointer]
            if current != previous:
                # Edit list in-place and move pointer
                nums[result_pointer] = current
                result_pointer += 1
            # Store previous number
            previous = current
        return result_pointer


class Test:
    def test(self):
        """Generic test case."""
        case = [[1, 2, 2, 3, 4, 4, 5]]
        expected = 5

        assert Solution().removeDuplicates(*case) == expected

    def test_singleton(self):
        """Generic test case."""
        case = [[1]]
        expected = 1

        assert Solution().removeDuplicates(*case) == expected

    def test_two(self):
        """Generic test case."""
        case = [[1, 2]]
        expected = 2

        assert Solution().removeDuplicates(*case) == expected

    def test_equal(self):
        """Generic test case."""
        case = [[1, 1, 1]]
        expected = 1

        assert Solution().removeDuplicates(*case) == expected

    def test_long(self):
        """Generic test case."""
        case = [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
        expected = 5

        assert Solution().removeDuplicates(*case) == expected
