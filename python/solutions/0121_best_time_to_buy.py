#!/usr/bin/env python3
"""
You are given an array `prices` where `prices[i]` is the price of a given stock on the
`ith` day. 

You want to maximise your profit by choosing a single day to buy one stock, and a
single, different day in the future to sell that stock.

Return the maximum profit that you can achieve from this transaction.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Pass through list, keeping track of lowest price seen so far.
        Use this lowest known price to calculate current day's profit.
        Keep track of highest known profit.

        Args:
            prices (List[int]): List of numbers representing each day's price.

        Returns:
            int: Maximum profit possible, or 0 if profit is unachievable.
        """
        profit = 0
        lowest_so_far = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i] - lowest_so_far)
            lowest_so_far = min(lowest_so_far, prices[i])
        return profit


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[7, 1, 5, 3, 6, 4]]
        expected = 5

        assert Solution().maxProfit(*case) == expected
