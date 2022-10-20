#!/usr/bin/env python3
"""
Roman numerals are represented by seven different symbols:

| Symbol    | Value     |
| --------- | --------- |
| I         | 1         |
| V         | 5         |
| X         | 10        |
| L         | 50        |
| C         | 100       |
| D         | 500       |
| M         | 1000      |

For example, 2 is written as II, and 12 is written as XII.

Only up to three of the same symbol are used in succession.
For example, 4 is written as IV instead of III, and 9 is written as IX.

Given an integer, convert it to a roman numeral.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def intToRoman(self, num: int) -> str:
        """Generate a string based on the number of thousands, hundreds, tens and ones.
        Use appropriate tokens for each value from 0 to 9.

        Args:
            num (int): Integer to convert to roman numeral.

        Returns:
            str: Roman numeral as string.
        """
        # Create numeral dictionary
        numerals = [
            ["", "M", "MM", "MMM"],
            [
                "",
                "C",
                "CC",
                "CCC",
                "CD",
                "D",
                "DC",
                "DCC",
                "DCCC",
                "CM",
            ],
            [
                "",
                "X",
                "XX",
                "XXX",
                "XL",
                "L",
                "LX",
                "LXX",
                "LXXX",
                "XC",
            ],
            [
                "",
                "I",
                "II",
                "III",
                "IV",
                "V",
                "VI",
                "VII",
                "VIII",
                "IX",
            ],
        ]
        # Generate numeral
        numeral = ""
        numeral += numerals[0][num // 1000]  # Thousands
        numeral += numerals[1][num % 1000 // 100]  # Hundreds
        numeral += numerals[2][num % 100 // 10]  # Tens
        numeral += numerals[3][num % 10]  # Ones
        return numeral


class Test:
    def test_complex(self):
        """Given test case from Leetcode."""
        case = [58]
        expected = "LVIII"

        assert Solution().intToRoman(*case) == expected

    def test_bigger(self):
        """Given test case from Leetcode with more complexity."""
        case = [1994]
        expected = "MCMXCIV"

        assert Solution().intToRoman(*case) == expected
