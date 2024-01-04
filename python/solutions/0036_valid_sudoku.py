#!/usr/bin/env python3
"""
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits 1-9 without
repetition.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Iterate over rows, checking for duplicate values excluding blanks. Iterate
        over columns by taking the `ith` element of each row for i columns, checking for
        duplicate values excluding blanks. Iterate over sub-boxes by starting at every
        third columns of every third row, extracting the respective 3 x 3 grid, and then
        checking for duplicate values excluding blanks.
        """

        # Helper function to check for duplicates
        def hasDuplicate(cs: List[str]) -> bool:
            """Return True if a duplicate value is detected. Otherwise, return False as
            all values are unique. Ignores '.', which represents a blank value.
            """
            frequencies = {}
            for c in cs:
                # Ignore blank cells
                if c == ".":
                    continue
                # Increment frequency tracker
                if c in frequencies:
                    frequencies[c] += 1
                else:
                    frequencies[c] = 1
            # Check frequencies
            for _, frequency in frequencies.items():
                if frequency > 1:
                    return True
            return False

        # Validate rows
        for i in range(0, 9):
            # Get row
            row = board[i]
            # Check for duplicates
            if hasDuplicate(row):
                return False
        # Validate columns
        for i in range(0, 9):
            # Get column
            column = [row[i] for row in board]
            # Check for duplicates
            if hasDuplicate(column):
                return False
        # Validate sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Get sub-box
                sub_box = [
                    board[i][j],
                    board[i][j + 1],
                    board[i][j + 2],
                    board[i + 1][j],
                    board[i + 1][j + 1],
                    board[i + 1][j + 2],
                    board[i + 2][j],
                    board[i + 2][j + 1],
                    board[i + 2][j + 2],
                ]
                # Check for duplicates
                if hasDuplicate(sub_box):
                    return False
        return True


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ]
        expected = True

        assert Solution().isValidSudoku(*case) == expected

    def test_falsey(self):
        """Given falsey test case from Leetcode."""
        case = [
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ]
        expected = False

        assert Solution().isValidSudoku(*case) == expected
