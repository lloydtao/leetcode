#!/usr/bin/env python3
"""
You are given an integer array `matches`, where `matches[i] = [winner_i, loser_i]`
indicates that the player `winner_i` defeated the player `loser_i` in a match.

Return a list `answer` of size 2, where:
- `answer[0]` is a list of all players that have not lost any matches.
- `answer[1]` is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Initialise sets for 1. winners, 2. lost-once and 3. lost-many.
        Then, for each match:
        - Add the winner to the set of winners (if not already in a set).
        - Check if the loser is already in a set:
          - Pop them down a set if already in a set.
          - Put them in lost-oncers if not in a set.
        Finally, convert the first two sets to ordered lists and return appropriately.
        """
        # Initialise empty sets
        won_all = {}
        lost_one = {}
        lost_many = {}
        # Iterate through matches
        for match in matches:
            # Get winner and loser
            winner = match[0]
            loser = match[1]
            # Handle winner logic
            if winner not in lost_one and winner not in lost_many:
                won_all[winner] = True
            # Handle loser logic
            if loser in lost_many:
                pass
            elif loser in lost_one:
                lost_one.pop(loser)
                lost_many[loser] = True
            elif loser in won_all:
                won_all.pop(loser)
                lost_one[loser] = True
            else:
                lost_one[loser] = True
        # Get output lists
        return [sorted(list(won_all.keys())), sorted(list(lost_one.keys()))]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [
            [
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ]
        ]
        expected = [[1, 2, 10], [4, 5, 7, 8]]

        assert Solution().findWinners(*case) == expected

    def test_only_winners(self):
        """Given test case from Leetcode, where all losers lose many times."""
        case = [[[2, 3], [1, 3], [5, 4], [6, 4]]]
        expected = [[1, 2, 5, 6], []]

        assert Solution().findWinners(*case) == expected
