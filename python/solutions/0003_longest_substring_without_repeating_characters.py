#!/usr/bin/env python3
"""
Given a string `s`, find the length of the longest substring without repeating
characters.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Iterate over the list, keeping track of: the last time a character was seen,
        the start of the substring, and the max length seen so far.

        The current length becomes the max length if the current length is larger than
        the max length, based on the distance from the start pointer to the current
        character.

        The start pointer is set to 1 index after the previous instance of a character
        if a character is seen an additonal time. For example, in the string "abcba",
        seeing the second b at index 3 will set the start pointer to after the first b
        at index 1.
        """
        # Case of single character string
        if len(s) == 1:
            return 1
        # Iterate over string
        last_seen = {}
        start = 0
        max_length = 0
        for i in range(len(s)):
            # Compute values
            c = s[i]
            current_length = (i - start) + 1
            # First occurrence: add to dictionary, adjust max length, continue
            if c not in last_seen:
                max_length = max(max_length, current_length)
                last_seen[c] = i
                continue
            # First occurrence in substring: adjust max length
            if last_seen[c] < start:
                max_length = max(max_length, current_length)
                last_seen[c] = i
                continue
            # Second occurrence in substring: reset start pointer, capture max length
            start = last_seen[c] + 1
            max_length = max(max_length, current_length - 1)  # -1 (c not in substring)
            last_seen[c] = i
        return max_length


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["a"]
        expected = 1

        assert Solution().lengthOfLongestSubstring(*case) == expected

    def test_singletons(self):
        """Given test case from Leetcode, with just two singleton characters."""
        case = ["au"]
        expected = 2

        assert Solution().lengthOfLongestSubstring(*case) == expected

    def test_repeated(self):
        """Given test case from Leetcode, where substring includes used characters."""
        case = ["tmmzuxt"]
        expected = 5

        assert Solution().lengthOfLongestSubstring(*case) == expected

    def test_all_repeated(self):
        """Given test case from Leetcode, where all characters are repeated."""
        case = ["bbbbb"]
        expected = 1

        assert Solution().lengthOfLongestSubstring(*case) == expected
