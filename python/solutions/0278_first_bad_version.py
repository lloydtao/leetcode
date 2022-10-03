#!/usr/bin/env python3
"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad
version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

Implement a function to find the first bad version. You should minimize the number of
calls to the API.
"""
from typing import Dict, List, Optional, Set, Tuple


def isBadVersion(version: int) -> bool:
    """Given API bool isBadVersion(version) which returns whether version is bad.

    Args:
        version (int): Version number to check.

    Returns:
        bool: Version is bad.
    """
    # First bad version hard-coded as 4
    if version >= 4:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Perform a standard binary search.
        Return the low pointer at the end, as it will stop moving once it becomes the
        first bad version."""
        # Binary search
        p_low = 1
        p_high = n
        p_mid = None
        while p_low < p_high:
            p_mid = p_low + (p_high - p_low) // 2
            if isBadVersion(p_mid):
                p_high = p_mid
            else:
                p_low = p_mid + 1
        return p_low


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [5]
        expected = 4

        assert Solution().firstBadVersion(*case) == expected

    def test_last(self):
        """Given test case from Leetcode, where first bad version is latest version."""
        case = [4]
        expected = 4

        assert Solution().firstBadVersion(*case) == expected
