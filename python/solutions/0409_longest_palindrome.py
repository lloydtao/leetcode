#!/usr/bin/env python3
"""
Given a string `s` which consists of lowercase or uppercase letters, return the length
of the longest palindrome that can be built with those letters.

Letters are case sensitive. For example, "Aa" is not considered a palindrome here.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """Iterate over letters, counting the number of pairs.
        Also keep track of if a singleton is available, as we can put a single
        character in the middle when forming a palindrome.
        """
        pairs = 0
        singletons = 0
        count = {}
        for c in s:
            # Handle case of first instance of character
            if c not in count:
                count[c] = 1
                singletons += 1
                continue
            # Increase count of characters
            count[c] += 1
            # Check if pair formed, and set singleton and pair counts accordingly
            if count[c] % 2:
                singletons += 1
                continue
            pairs += 1
            singletons -= 1
        # If a singleton exists, add 1 to the max length
        pairs_length = 2 * pairs
        if singletons:
            return pairs_length + 1
        return pairs_length


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["abccccdd"]
        expected = 7

        assert Solution().longestPalindrome(*case) == expected

    def test_single(self):
        """Given test case from Leetcode using a single character."""
        case = ["a"]
        expected = 1

        assert Solution().longestPalindrome(*case) == expected
