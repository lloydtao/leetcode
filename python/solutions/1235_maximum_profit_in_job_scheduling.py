#!/usr/bin/env python3
"""
We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to
`endTime[i]`, obtaining a profit of `profit[i]`.

Given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can
take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time `X`, you will be able to start another job that
starts at time `X`.

[Unsure of solution, need to revisit.]
"""
import bisect
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Calculate the maximum profit that can be obtained by scheduling jobs without
        overlapping time ranges. Sort the jobs based on their end times, and then
        iterate through them to find the maximum profit.
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]]
        expected = 120

        assert Solution().jobScheduling(*case) == expected
