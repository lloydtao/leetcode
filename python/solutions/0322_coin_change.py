#!/usr/bin/env python3
"""
You are given an integer array `coins` representing coins of different denominations,
and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount
of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Perform a breadth-first tree search, starting from zero, where each node has
        a child for each possible selection of next coin. If the target amount is
        found, return the current depth. If all nodes at the current depth are larger
        than the target amount, return -1.

        Time complexity: O((|V|+|E|)), or O(n * m), where m is the amount and n is the
        number of denominations of coins.

        Args:
            coins (List[int]): Denominations of coins
            amount (int): Target sum of coins

        Returns:
            int: Fewest number of coins required to make amount, or -1 if infeasible
        """
        queue = [{"amount": 0, "depth": 0}]
        visited = {}
        for node in queue:
            # Skip node if amount has been visited, since its tree will be identical
            if node["amount"] in visited:
                continue
            # Return depth as solution if node is target
            if node["amount"] == amount:
                return node["depth"]
            else:
                # Add all children nodes (one for each coin) to queue
                for coin in coins:
                    new_amount = node["amount"] + coin
                    new_depth = node["depth"] + 1
                    # Only add to queue if smaller than target
                    if new_amount <= amount:
                        queue.append({"amount": new_amount, "depth": new_depth})
                # Store node value so that its identical trees will not be searched
                visited[node["amount"]] = True
        # Queue has been exhausted, so change is infeasible
        return -1


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 2, 5], 11]
        expected = 3  # 11 = 5 + 5 + 1

        assert Solution().coinChange(*case) == expected

    def test_false(self):
        """Given falsey test case from Leetcode."""
        case = [[2], 3]
        expected = -1

        assert Solution().coinChange(*case) == expected

    def test_zero(self):
        """Given test case from Leetcode, where the target amount is zero."""
        case = [[1], 0]
        expected = 0

        assert Solution().coinChange(*case) == expected

    def test_greedy(self):
        """Custom test case where a greedy search fails."""
        case = [[20, 14, 13, 1], 27]
        expected = 2  # 27 = 14 + 13, and not 20 + (1 * 7)

        assert Solution().coinChange(*case) == expected
