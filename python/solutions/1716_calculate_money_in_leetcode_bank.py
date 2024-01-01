#!/usr/bin/env python3
"""
Hercy puts money in the bank every day.

- He puts $1 in on Monday.
- Every day from Tuesday through Sunday, he puts in $1 more than the day before.
- Every Monday, he puts in $1 more than the previous monday.

Given `n` days, return the total money at the end of the `n`th day.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def totalMoney(self, n: int) -> int:
        """Use an arithmetic expression for full weeks and then the remaining partial.

        For reference, weeks accumulate money as such:
        - Week n: ((1 + n) + (2 + n) + ... + (7 + n))

        For a full week, we can calculate:
        - Week n: (1 + 2 + 3 + 4 + 5 + 6 + 7) + 7n

        Or:
        - Week n: 28 + 7n

        The sum of an arithmetic series in the form (a + dn) is:
        - Sn = (n / 2)(2a + (n - 1)d)

        Therefore, the full weeks can be calculated as:
        - (n / 2)(2 * 28 + (n - 1) * 7)

        Time complexity:  O(1), due to performing one calculation for the full weeks,
                          and up to six calculations for the partial week.
        Space complexity: O(1), due to no storage other than an accumulator.
        """
        # Initialise counter
        total_money = 0
        # Optimise full weeks
        full_weeks = n // 7
        total_money += int((full_weeks / 2) * (2 * 28 + (full_weeks - 1) * 7))
        # Iterate through partial week's days
        for day in range(full_weeks * 7, n):
            # Get date values to calculate deposit
            weekday = (day % 7) + 1
            week = day // 7
            # Calculate and add to total money
            total_money += weekday + week
        # Return counter
        return total_money

    def totalMoney_brute_weekly(self, n: int) -> int:
        """Accumulate money by counting full weeks and then the remaining partial.

        For reference, weeks accumulate money as such:
        - Week n: ((1 + n) + (2 + n) + ... + (7 + n))

        For a full week, we can calculate:
        - Week n: (1 + 2 + 3 + 4 + 5 + 6 + 7) + 7n

        For the partial week:
        - Week n: ((1 + n) + (2 + n) + ...)

        Time complexity:  O(n), due to performing one calculation per 7 days in n.
        Space complexity: O(1), due to no storage other than an accumulator.
        """
        # Initialise counter
        total_money = 0
        # Optimise full weeks
        full_weeks = n // 7
        for week in range(full_weeks):
            total_money += (1 + 2 + 3 + 4 + 5 + 6 + 7) + 7 * week
        # Iterate through partial week's days
        for day in range(full_weeks * 7, n):
            # Get date values to calculate deposit
            weekday = (day % 7) + 1
            week = day // 7
            # Calculate and add to total money
            total_money += weekday + week
        # Return counter
        return total_money

    def totalMoney_brute_daily(self, n: int) -> int:
        """Accumulate money by tracking it one day at a time.

        For reference, weeks accumulate money as such:
        -    Day:  0   1   2   3   4   5   6
        - Week 0: (1 + 2 + 3 + 4 + 5 + 6 + 7)
        - Week 1: (2 + 3 + 4 + 5 + 6 + 7 + 8)
        - Week 2: (3 + 4 + 5 + 6 + 7 + 8 + 9)

        Or, in general:
        - Week n: ((1 + n) + (2 + n) + ... + (7 + n))

        Time complexity:  O(n), due to performing one calculation per day in n.
        Space complexity: O(1), due to no storage other than an accumulator.
        """
        # Initialise counter
        total_money = 0
        # Iterate through days
        for day in range(n):
            # Get date values to calculate deposit
            weekday = (day % 7) + 1
            week = day // 7
            # Calculate and add to total money
            total_money += weekday + week
        # Return counter
        return total_money


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [4]
        expected = 10

        assert Solution().totalMoney(*case) == expected

    def test_larger(self):
        """Given, larger test case from Leetcode."""
        case = [10]
        expected = 37

        assert Solution().totalMoney(*case) == expected

    def test_largest(self):
        """Given, even larger test case from Leetcode."""
        case = [20]
        expected = 96

        assert Solution().totalMoney(*case) == expected
