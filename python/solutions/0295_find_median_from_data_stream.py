#!/usr/bin/env python3
"""
The median is the middle value in an ordered integer list.

If the size of the list is even, there is no middle value, and the median is the mean
of the two middle values.

Implement the MedianFinder class:
 - MedianFinder()
 - void addNum(int num)
 - double findMedian()
"""
import bisect
import heapq

from typing import Dict, List, Optional, Set, Tuple


class MedianFinder:
    """O(n) space, O(log n) insertion time, O(1) lookup time.
    Use a min heap for the largest values, and a max heap for the smallest. The top
    of the max heap (or the average of both tops) will represent the median, as long as
    the elements are equally divided between the two heaps.
    """

    def __init__(self):
        """Initialise a heap each for the smallest and largest values respectively."""
        self.smallest_heap = []
        self.largest_heap = []

    def addNum(self, num: int) -> None:
        """Insert value into largest values heap, then pop the minimum of the largest
        values. Put this minimum into the smallest values heap. This ensures that the
        heaps do not overlap (i.e. max_smallest <= min_largest).

        Args:
            num (int): Value to insert
        """
        # Insert into largest heap, and pop its minimum value
        min_largest = heapq.heappushpop(self.largest_heap, num * -1) * -1
        # Put the minimum value into the smallest heap
        heapq.heappush(self.smallest_heap, min_largest)
        # If the smallest heap becomes heavier, pop an element into the largest heap
        # This ensures that either the weights are equal, or the largest is 1 heavier
        if len(self.smallest_heap) > len(self.largest_heap):
            max_smallest = heapq.heappop(self.smallest_heap)
            heapq.heappush(self.largest_heap, max_smallest * -1)

    def findMedian(self) -> float:
        """For an odd number of elements, take the minimum (top) of the largest heap.
        For an even number of elements, take the average of the minimum (top) of the
        largest heap and the maximum (top) of the smallest heap. Note that we're always
        taking the top(s) of the heap(s), which has O(1) time complexity.

        Returns:
            float: Median value (if length is even, average of both midpoints)
        """
        if len(self.largest_heap) > len(self.smallest_heap):
            return self.largest_heap[0] * -1
        else:
            left = self.smallest_heap[0]
            right = self.largest_heap[0] * -1
            return (left + right) / 2


class MedianFinder_SortedList:
    """O(n) space, O(n) insertion time, O(1) lookup time.
    Keep a sorted list of values, using a binary search to efficiently insert new
    values. Locate the median at any time by taking the midpoint value (i.e. len / 2).
    """

    def __init__(self):
        """Initialise sorted list, and keep track of length for efficiency."""
        self.length = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        """Insert new value into sorted list via binary search.

        Args:
            num (int): Value to insert
        """
        bisect.insort(self.nums, num)
        self.length += 1

    def findMedian(self) -> float:
        """Get value at midpoint.

        Returns:
            float: Median value (if length is even, average of both midpoints)
        """
        if self.length % 2:
            return self.nums[self.length // 2]
        else:
            left = self.nums[self.length // 2 - 1]
            right = self.nums[self.length // 2]
            return (left + right) / 2


class Test:
    def test(self):
        """Given test case from Leetcode."""
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0

    def test_long(self):
        """A longer test case."""
        mf = MedianFinder()
        mf.addNum(5)
        mf.addNum(15)
        assert mf.findMedian() == 10.0
        mf.addNum(-2)
        mf.addNum(-30)
        assert mf.findMedian() == 1.5
        mf.addNum(1)
        mf.addNum(-1)
        assert mf.findMedian() == 0.0
