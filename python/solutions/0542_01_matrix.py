#!/usr/bin/env python3
"""
Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each
cell.

The distance between two adjacent cells is 1.
"""
import math

from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Calculate the minimum distance from any 0 at each cell by working top-left
        to bottom-right. The distance is either 0 (if the cell is 0), or the minimum of
        the top and left neighbours.

        Infinity is used as the base case distance (i.e. edge nodes and any neighbours
        this cascades upon).

        We then repeat this from bottom-right to top-left, looking at bottom and right
        neighbours to get minimum distances.

        We do this second pass as it restricts us to pre-computed values (i.e. we're
        not looking at bottom and right neighbours in the first pass as they haven't
        been computed yet).

        Args:
            mat (List[List[int]]): Input matrix of booleans

        Returns:
            List[List[int]]: Output matrix of distances from 0
        """
        # Get height and width of matrix
        m = len(mat)
        n = len(mat[0])

        # Run through matrix, get distances based on top and left neighbour
        for j in range(m):
            for i in range(n):
                # Cell is zero, so distance is zero
                if mat[j][i] == 0:
                    continue
                # Cell is not zero, so get distance from nearest zero using neighbours
                if j == 0:
                    top = math.inf  # Edge node, set distance to infinity
                else:
                    top = mat[j - 1][i]  # Distance of top neighbour
                if i == 0:
                    left = math.inf  # Edge node
                else:
                    left = mat[j][i - 1]  # Distance of left neighbour
                mat[j][i] = min(top + 1, left + 1)

        # Run through matrix backwards, get distances based on bottom and right
        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                # Cell is zero, so distance is zero
                if mat[j][i] == 0:
                    continue
                # Cell is not zero, so get distance from nearest zero using neighbours
                if j + 1 >= m:
                    bottom = math.inf  # Edge node
                else:
                    bottom = mat[j + 1][i]  # Distance of bottom neighbour
                if i + 1 >= n:
                    right = math.inf  # Edge node
                else:
                    right = mat[j][i + 1]  # Distance of right neighbour
                mat[j][i] = min(mat[j][i], bottom + 1, right + 1)
        return mat


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

        assert Solution().updateMatrix(*case) == expected

    def test_two(self):
        """Given test case from Leetcode, with a distance of 2."""
        case = [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

        assert Solution().updateMatrix(*case) == expected

    def test_big(self):
        """Given big test case from Leetcode."""
        case = [
            [
                [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
            ]
        ]
        expected = [
            [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
            [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
            [3, 2, 2, 1, 0, 1, 0, 0, 1, 1],
        ]

        assert Solution().updateMatrix(*case) == expected
