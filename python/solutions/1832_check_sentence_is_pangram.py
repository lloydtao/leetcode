#!/usr/bin/env python3
"""
[Problem description.]
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique = 0
        letters = {}
        for c in sentence:
            if c in letters:
                continue
            letters[c] = None
            unique += 1
        return unique == 26


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["thequickbrownfoxjumpsoverthelazydog"]
        expected = True

        assert Solution().checkIfPangram(*case) == expected

    def test_false(self):
        """Given falsey test case from Leetcode."""
        case = ["leetcode"]
        expected = False

        assert Solution().checkIfPangram(*case) == expected
