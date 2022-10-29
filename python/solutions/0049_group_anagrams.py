#!/usr/bin/env python3
"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """For each word, add it to an anagram group indexed by its sorted string.
        Return the list of anagram groups values at the end.

        Args:
            strs (List[str]): List of words to sort into anagram groups

        Returns:
            List[List[str]]: List of anagram groups
        """
        # Initialise store of anagram groups
        groups = {}
        for word in strs:
            # Get group key, which is the sorted anagram
            s = "".join(sorted(word))
            # Initialise group key if it does not exist
            if s not in groups:
                groups[s] = []
            # Add word to the anagram group
            groups[s].append(word)
        # Return a list of anagram group values
        return [x for x in groups.values()]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [["eat", "tea", "tan", "ate", "nat", "bat"]]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

        assert Solution().groupAnagrams(*case) == expected

    def test_blank(self):
        """Given empty test case from Leetcode."""
        case = [[""]]
        expected = [[""]]

        assert Solution().groupAnagrams(*case) == expected

    def test_single(self):
        """Given singleton test case from Leetcode."""
        case = [["a"]]
        expected = [["a"]]

        assert Solution().groupAnagrams(*case) == expected
