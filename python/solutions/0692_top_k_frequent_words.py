#!/usr/bin/env python3
"""
Given an array of strings `words` and an integer `k`, return the `k` most frequent
strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with
the same frequency, by their lexicographical order.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Get all word counts. Sort alphabetically and then by frequency, as this will
        achieve lexicographical order. Clip the list at the end."""
        # Get counts of words
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        # Sort words alphabetically (by key)
        sorted_word_counts = sorted(word_counts)
        # Sort words by frequency
        sorted_word_counts = sorted(
            sorted_word_counts, key=word_counts.get, reverse=True
        )
        # Return clipped list
        return sorted_word_counts[:k]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [
            ["i", "love", "leetcode", "i", "love", "coding"],
            2,
        ]
        expected = ["i", "love"]

        assert Solution().topKFrequent(*case) == expected

    def test_bigger(self):
        """Given test case from Leetcode, with more elements."""
        case = [
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4,
        ]
        expected = ["the", "is", "sunny", "day"]

        assert Solution().topKFrequent(*case) == expected
