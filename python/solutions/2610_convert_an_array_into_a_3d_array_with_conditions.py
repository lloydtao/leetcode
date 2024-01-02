#!/usr/bin/env python3
"""
You are given an integer array `nums`. You need to create a 2D array from `nums`
satisfying the following conditions:

- The 2D array should contain only the elements of the array `nums`
- Each row in the 2D array contains distinct integers
- The number of rows in the 2D array should be minimal

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """Iterate over the list of numbers, keeping track of how many times a value has
        been seen within a map. Add the number to the row respective of how many times
        the value has been seen (e.g., seeing value for 2nd time = add to 2nd row),
        making sure to initialise a new row within the output array if necessary.
        """
        # Initialise output array and frequency map
        output = []
        frequency = {}
        # Iterate over input numbers
        for num in nums:
            # Record frequency of current number
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
            # Initialise new row if necessary
            if frequency[num] > len(output):
                output.append([])
            # Append current number to appropriate row
            output[frequency[num] - 1].append(num)
        # Return output array
        return output


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 3, 4, 1, 2, 3, 1]]
        expected = [[1, 3, 4, 2], [1, 3], [1]]

        assert Solution().findMatrix(*case) == expected

    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 2, 3, 4]]
        expected = [[1, 2, 3, 4]]

        assert Solution().findMatrix(*case) == expected
