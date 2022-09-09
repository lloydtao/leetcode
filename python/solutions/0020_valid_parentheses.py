#!/usr/bin/env python3
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def isValid(self, s: str) -> bool:
        """Use a stack to parse the parentheses.
        For an open parenthesis, add to the stack.
        For a closed parenthesis, check if the top of the stack matches it.
        """
        # Initialise stack and store parenthesis pairs
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            # Stack is currently empty
            if len(stack) == 0:
                # Check if starting with a closer
                if c in pairs:
                    stack.append(c)
                    continue
                else:
                    return False
            # Check if character is an opener
            if c in pairs:
                stack.append(c)
                continue
            # Character is a closer, so make sure that it matches
            top = stack.pop()
            if pairs[top] == c:
                continue
            else:
                return False
        # Check if any of the stack remains
        if len(stack):
            return False
        return True


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = ["()[]{}"]
        expected = True

        assert Solution().isValid(*case) == expected

    def test_erroneous(self):
        """Given test case with stray opener."""
        case = ["["]
        expected = False

        assert Solution().isValid(*case) == expected

    def test_erroneous_closer(self):
        """Given test case with stray closer."""
        case = ["))"]
        expected = False

        assert Solution().isValid(*case) == expected
