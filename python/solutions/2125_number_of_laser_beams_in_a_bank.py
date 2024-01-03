#!/usr/bin/env python3
"""
Anti-theft security devices are activated inside a bank. You are given a 0-indexed
binary string array `bank` representing the floor plan of the bank, which is an `m x n`
2D matrix. `bank[i] represents the `ith` row, consisting of `'0'`s and `'1'`s. '0'
means the cell is empty, while `1` means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:
- The two devices are located on two different rows: `r_1` and `r_2`, where `r_1 < r_2`.
- For each row `i` where `r_1 < i < r_2`, there are no security devices on the `ith`
row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """For each row with at least one device, look forwards until another row is
        found with at least one device. Increment the total laser count by the product
        of the number of devices on the previous row and the number of devices on the
        new row. Repeat this strategy, using the current row as the previous row.
        Return the total laser count once all rows have been exhausted.
        """
        # Initialise tracker for previous row. We can avoid special logic to handle the
        # first row with lasers by using the value 0, meaning that its product is 0.
        previous_row = 0
        # Initialise counter of lasers
        total_lasers = 0
        # Iterate over rows
        for row in bank:
            # Get number of devices on the row
            current_row = row.count("1")
            if current_row == 0:
                # If empty, skip row
                continue
            else:
                # If devices found, increment the laser count by the product
                total_lasers += previous_row * current_row
                # Set the rear row to the current row
                previous_row = current_row
        # Return the total laser count
        return total_lasers


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [["011001", "000000", "010100", "001000"]]
        expected = 8

        assert Solution().numberOfBeams(*case) == expected
