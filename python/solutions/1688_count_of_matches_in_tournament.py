#!/usr/bin/env python3
"""
You are given an integer `n`, the number of teams in a tournament that has these rules:

- If the current number of teams is even, then each team gets paired with another team.
A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.

- If the current number of teams is odd, one team randomly advances in the tournament,
and the rest are paired. A total of `(n - 1) / 2) matches are played, and 
`(n - 1) / 2 + 1` teams advance to the next round.

Return the number of matches played in the tournament until a winner is decided.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numberOfMatches(self, n: int) -> int:
        """One match knocks out one player. In order to be left with 1 player, you must
        knock out n - 1 players, and therefore, have n - 1 matches.
        """
        return n - 1

    def numberOfMatches_brute(self, n: int) -> int:
        """Simulate the matches, and return the count at the end.

        For each round:
        - In the even case, n / 2 matches are played, and n / 2 teams advance.
        - In the odd case, (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 advance.
        """
        # Initialise counter and tracker
        matches = 0
        current_teams = n
        # Iterate until one team remains
        while current_teams > 1:
            # Odd case
            if current_teams % 2:
                matches += (current_teams - 1) / 2
                current_teams = ((current_teams - 1) / 2) + 1
            # Even case
            else:
                matches += current_teams / 2
                current_teams = current_teams / 2
        # Return final count
        return matches


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [7]
        expected = 6

        assert Solution().numberOfMatches(*case) == expected

    def test_larger(self):
        """Given test case from Leetcode with a larger argument."""
        case = [14]
        expected = 13

        assert Solution().numberOfMatches(*case) == expected
