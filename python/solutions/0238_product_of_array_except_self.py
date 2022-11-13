#!/usr/bin/env python3
"""
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal
to the product of all elements of `nums` except `nums[i]`.

The algorithm should run in O(n) time, and without using the division operation.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Initialise an array to keep track of products. Make one pass forwards over
        the input array multiplying each respective product by the input values behind
        it. Make one pass backwards, multiplying each product by the input values ahead
        of it. Keep this multiplication O(n) by accumlating the product behind/ahead of
        the current num (prefix/suffix), rather than multiplying it all out every time.

        For example, take the input array [a, b, c, d]:
        - Forwards pass operations: [1, a, ab, abc]
        - Backwards pass operations [bcd, cd, d, 1]
        - Multiply these together:  [bcd, acd, abd, abc]

        Args:
            nums (List[int]): Input list of numbers

        Returns:
            List[int]: List of products
        """
        # Initialise accumulators
        prefix = 1
        suffix = 1
        products = [1 for _ in nums]
        # Do forwards and backwards operations simultaneously (i.e. one pass)
        for i in range(len(nums)):
            # Forwards operations:  -> [1, a, ab, abc, ...]
            products[i] *= prefix
            prefix *= nums[i]
            # Backwards operations: [..., bcd, cd, d, 1] <-
            products[~i] *= suffix
            suffix *= nums[~i]
        return products

    def productExceptSelf_brute(self, nums: List[int]) -> List[int]:
        """Loop over the array and, for each number, generate its non-inclusive product
        by multiplying all other elements together. Return these results at the end.

        Args:
            nums (List[int]): Input list of numbers

        Returns:
            List[int]: List of products
        """
        # Initialise array to store results
        res = []
        for i in range(len(nums)):
            # Get the product of every other number in the array
            acc = 1
            for j in range(len(nums)):
                # Skip multiplication for same number
                if i == j:
                    continue
                acc *= nums[j]
            # Add product to results
            res.append(acc)
        return res


class Test:
    def test(self):
        """[Test description.]"""
        case = [[1, 2, 3, 4]]
        expected = [24, 12, 8, 6]

        assert Solution().productExceptSelf(*case) == expected

    def test_zero(self):
        """[Test description.]"""
        case = [[-1, 1, 0, -3, 3]]
        expected = [0, 0, 9, 0, 0]

        assert Solution().productExceptSelf(*case) == expected
