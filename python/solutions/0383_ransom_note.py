#!/usr/bin/env python3
"""
Given two strings, `ransomNote` and `magazine`, return True if `ransomNote` can be
constructed by using the letters from `magazine` and False otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Build frequency of letters in magazine
        frequencies = {}
        for c in magazine:
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
        # Check if letters are available for ransom note
        for c in ransomNote:
            # Check if current letter is in magazine
            if c not in frequencies:
                return False
            else:
                # Check if current letter has been exhausted
                if frequencies[c]:
                    frequencies[c] -= 1
                else:
                    return False
        return True


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["aa", "aab"]
        expected = True

        assert Solution().canConstruct(*case) == expected

    def test_bad(self):
        """Given falsey test case from Leetcode."""
        case = ["aa", "ab"]
        expected = False

        assert Solution().canConstruct(*case) == expected

    def test_single_letter(self):
        """Given falsey test case from Leetcode."""
        case = ["a", "b"]
        expected = False

        assert Solution().canConstruct(*case) == expected
