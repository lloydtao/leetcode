#!/usr/bin/env python3
"""
There are a total of `numCourses` courses you have to take, labeled from 0 to
`numCourses - 1`.

You are given an array `prerequisites` where `prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai. For example, [0, 1]
indicates that in order to take course 0, you first have to take course 1.

Return `true` if you can finish all courses. Otherwise, return `false`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Create a lookup table of each course's prerequisites.
        Then, create a queue of courses that can be completed (O(n^2)):
        - Initialise the queue as the list of courses with no prerequisites.
        - For each course in the queue, knock it off of other courses' prerequisites.
            - If this leads to the other course having no prequisites left, queue it.
        - Once the queue is empty, check that all courses have no prerequisites left.
        If all course have no prerequisites left, return True. If not, return False.

        Args:
            numCourses (int): Total number of courses, from 0 to numCourses
            prerequisites (List[List[int]]): List of prerequisite pairs

        Returns:
            bool: If all courses can be completed when constrained by prerequisites
        """
        # Create a 'course prerequisite' lookup table
        cpr = {}
        for i in range(numCourses):
            cpr[i] = {}
        for p in prerequisites:
            cpr[p[0]][p[1]] = None
        # Create queue of courses with no prerequisites
        queue = [k for k, v in cpr.items() if v == {}]
        for node in queue:
            # Knock the current node off each node's prerequisites
            for k, v in cpr.items():
                if node in v:
                    v.pop(node)
                    if v == {}:
                        queue.append(k)
        # If all courses have lost their prerequisites, the courses are doable
        result = True
        for k, v in cpr.items():
            result = result and v == {}
        return result


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [2, [[1, 0]]]
        expected = True

        assert Solution().canFinish(*case) == expected

    def test_falsey(self):
        """Given falsey test case from Leetcode."""
        case = [2, [[1, 0], [0, 1]]]
        expected = False

        assert Solution().canFinish(*case) == expected
