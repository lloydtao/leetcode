#!/usr/bin/env python3
"""
Given an array of `points`, where `points[i] = [x i, y i]` represents a point on the X-Y
plane, and an integer `k`, return the `k` closest points to the origin (0,0).

The distance between two points on the X-Y plane is the Euclidean distance.

You may return the answer in any answer. The answer is guaranteed to be unique.
"""
from heapq import heappush, heappushpop
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Max heap: Maintain a heap (priority queue) of points by distance, popping
        the largest if a new value is added.

        Complexity: O(n log k), as the push/pop is O(log k) and performed for n points.

        Args:
            points (List[List[int]]): List of points
            k (int): Number of closest points to return

        Returns:
            List[List[int]]: List of k closest points
        """

        # Distance function (skip sqrt as if a^2 > b^2 then a > b)
        distance = lambda p: p[0] ** 2 + p[1] ** 2
        # Iterate over points
        heap = []
        for i, point in enumerate(points):
            # Get distance
            dist = distance(point)
            # Add to heap, using negative distance to keep smallest values at top
            if len(heap) < k:
                heappush(heap, (-dist, i))  # Heap is not at limit (k), so only push
            else:
                heappushpop(heap, (-dist, i))  # Heap is at limit, so push and pop
        # Return top k closest points
        return [points[i] for (_, i) in heap]

    def kClosest_sort(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Sort: Get distance of all points and take the top k closest points.

        Args:
            points (List[List[int]]): List of points
            k (int): Number of closest points to return

        Returns:
            List[List[int]]: List of k closest points
        """
        # Get distance for each point (skip sqrt as if a^2 > b^2 then a > b)
        distance = lambda p: p[0] ** 2 + p[1] ** 2
        # Sort points using distance function as custom key function
        sorted_points = sorted(points, key=distance)
        # Return top k closest points
        return sorted_points[:k]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[[1, 3], [-2, 2]], 1]
        expected = [[-2, 2]]

        assert Solution().kClosest(*case).sort() == expected.sort()
        assert Solution().kClosest_sort(*case).sort() == expected.sort()

    def test_multiple(self):
        """Given test case from Leetcode, with k > 1."""
        case = [[[3, 3], [5, -1], [-2, 4]], 2]
        expected = [[3, 3], [-2, 4]]

        assert Solution().kClosest(*case).sort() == expected.sort()
        assert Solution().kClosest_sort(*case).sort() == expected.sort()

    def test_duplicate(self):
        """Given test case from Leetcode, with a duplicate point."""
        case = [[[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]], 4]
        expected = [[1, 1], [2, 2], [2, 2], [2, -2]]

        assert Solution().kClosest(*case).sort() == expected.sort()
        assert Solution().kClosest_sort(*case).sort() == expected.sort()
