#!/usr/bin/env python3
"""
Given the `root` node of a binary search tree and two integers `low` and `high`, return
the sum of values of all nodes with a value in the inclusive range `[low, high]`.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.binary_tree import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Iterate over nodes, adding each node's value to an accumulator if it falls
        within the range.
        """
        # Initialise accumulator
        range_sum = 0
        # Initialise queue
        queue = [root]
        # Iterate over nodes in the queue, populating it with new nodes as discovered
        for node in queue:
            # Check range
            if node.val >= low and node.val <= high:
                # Add value to accumulator
                range_sum += node.val
            # Add child nodes to queue
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        # Return final range sum
        return range_sum


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [TreeNode.list_to_node([10, 5, 15, 3, 7, None, 18]), 7, 15]
        expected = 32

        assert Solution().rangeSumBST(*case) == expected

    def test_singletons(self):
        """Given test case with singleton children from Leetcode."""
        case = [TreeNode.list_to_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10]
        expected = 23

        assert Solution().rangeSumBST(*case) == expected
