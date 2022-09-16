#!/usr/bin/env python3
"""
An image is represented by an `m x n` integer grid `image`, where `image[i][j]`
represents the pixel value of the image.

You are also given three integers: `sr`, `sc` and `color`. You should perform a flood
fill on the image, starting from the pixel `image[sr][sc]`.

To perform a flood fill, consdier the starting pixel and any pixels connected
4-directionally to the starting pixel of the same colour as the starting pixel, plus
any pixels connected 4-directionally to those pixels as well, and so on.

Replace the colour of all of the aforementioned pixels with `color`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """Fill neighbours with same colour, as well as their neighbours.

        Args:
            image (List[List[int]]): Grid of pixel values of the image
            sr (int): Starting pixel's row index
            sc (int): Starting pixel's column index
            color (int): Value (colour) to fill with

        Returns:
            List[List[int]]: Grid of pixel values of flood-filled image
        """
        # Store neighbour indices
        nis = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Initialise collections
        starter_color = image[sr][sc]
        queue = [(sr, sc)]
        visited = {}
        # Set up
        for pixel in queue:
            # Colour current pixel
            image[pixel[0]][pixel[1]] = color
            # Add same-coloured neighbours to queue
            for ni in nis:
                try:
                    # Get index of neighbour
                    nx = pixel[0] + ni[0]
                    ny = pixel[1] + ni[1]
                    # Handle index underflow
                    if nx < 0 or ny < 0:
                        continue
                    neighbour = (nx, ny)
                    # Neighbour has been visited
                    if neighbour in visited:
                        continue
                    # Set colour and add appropriate neighbour's neighbours to queue
                    if image[neighbour[0]][neighbour[1]] == starter_color:
                        queue.append(neighbour)
                        visited[neighbour] = True
                except IndexError:
                    # Handle index overflow
                    continue
        return image


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2]
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

        assert Solution().floodFill(*case) == expected

    def test_zero(self):
        """Given test case from Leetcode."""
        case = [[[0, 0, 0], [0, 0, 0]], 0, 0, 0]
        expected = [[0, 0, 0], [0, 0, 0]]

        assert Solution().floodFill(*case) == expected
