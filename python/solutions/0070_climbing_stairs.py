#!/usr/bin/env python3
"""
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
import math

from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def climbStairs(self, n: int) -> int:
        # Get maximum double steps
        total = 0
        max_double_steps = n // 2
        # For each possible number of double steps, calculate total combinations
        for double_steps in range(0, max_double_steps + 1):
            # Adjust number of steps based on double steps taken
            steps = n - double_steps
            total += math.comb(steps, double_steps)
        return total


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [2]
        expected = 2

        assert Solution().climbStairs(*case) == expected

    def test_three(self):
        """Given test case from Leetcode with 3 distinct ways."""
        case = [3]
        expected = 3

        assert Solution().climbStairs(*case) == expected
