#!/usr/bin/env python3
"""
Given two string arrays `word1` and `word2`, return True if the two arrays represent
the same string, and False otherwise.

A string is represented by an array if the array elements concatenated in order form
the string.
"""
from itertools import chain
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """Create generators to yield characters from each list of strings, which uses
        O(1) space. Iterate over the generators in unison in a single pass, comparing
        the respective characters.

        Args:
            word1 (List[str]): First string array representing a word
            word2 (List[str]): Second string array representing a word

        Returns:
            bool: If both arrays represent the same word (i.e. after concatenation)
        """
        # Initialise generators to yield characters from each list
        w1 = chain.from_iterable(word1)
        w2 = chain.from_iterable(word2)

        # Compare each pair of characters
        try:
            for c1, c2 in zip(w1, w2, strict=True):
                if c1 != c2:
                    return False
            return True
        # Case of inputs are of different lengths
        except ValueError:
            return False


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [["ab", "c"], ["a", "bc"]]
        expected = True

        assert Solution().arrayStringsAreEqual(*case) == expected

    def test_false(self):
        """Given falsey test case from Leetcode."""
        case = [["a", "cb"], ["ab", "c"]]
        expected = False

        assert Solution().arrayStringsAreEqual(*case) == expected

    def test_false(self):
        """Given falsey test case from Leetcode."""
        case = [["abc", "d", "defg"], ["abcddef"]]
        expected = False

        assert Solution().arrayStringsAreEqual(*case) == expected
