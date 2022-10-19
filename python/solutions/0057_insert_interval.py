#!/usr/bin/env python3
"""
You are given an array of non-overlapping intervals `intervals`, where `intervals[i] =
[start i, end i]` represents the start and end of the ith interval, and `intervals` is
sorted in ascending order by `start i`.

You are also given an intervals `newInterval = [start, end]` that represents the start
and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in
ascending order by `start i`, and that `intervals` still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """There are three types of intervals in the list:
        - Intervals that wholly belong on the left.
        - Intervals that wholly belong on the right.
        - Intervals that overlap with the new interval.

        Our method is to collect 'left' intervals until an interval's end passes the
        start of the new interval. At this point, if the interval's start is greater
        than the end of the new interval, collect it as a 'right' interval. If not,
        there is an overlap, so merge the intervals. By repeating in this fashion,
        we account for the case where the new interval overlaps multiple intervals.

        This merge can be performed by editing the new interval in-place, and then
        appending it between the left and right interval collections at the end.

        Args:
            intervals (List[List[int]]): List of existing intervals
            newInterval (List[int]): New interval to merge in

        Returns:
            List[List[int]]: List of intervals including the inserted/merged interval
        """
        left = []
        right = []
        for interval in intervals:
            # Iterval's end is smaller than new interval's start
            if interval[1] < newInterval[0]:
                left.append(interval)
                continue
            # Iterval's start is greater than new interval's end
            if interval[0] > newInterval[1]:
                right.append(interval)
                continue
            # One of the above isn't true, so merge interval with new interval
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
            # Append collections and return
        return left + [newInterval] + right


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[[1, 3], [6, 9]], [2, 5]]
        expected = [[1, 5], [6, 9]]

        assert Solution().insert(*case) == expected

    def test_big_merge(self):
        """Given test case from Leetcode, with multiple intervals to be merged."""
        case = [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]]
        expected = [[1, 2], [3, 10], [12, 16]]

        assert Solution().insert(*case) == expected
