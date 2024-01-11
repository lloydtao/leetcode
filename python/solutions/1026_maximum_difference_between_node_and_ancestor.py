#!/usr/bin/env python3
"""
Given the `root` of a binary tree, find the maximum value `v` for which there exist
different nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any
child of `a` is an ancestor of `b`.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.binary_tree import TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """Subproblem: For each node, find the difference between it and its largest
        ancestor, and the difference between it and its smallest ancestor, and take the
        largest difference as the node's maximum difference. We can then take the
        largest difference across all nodes as our answer.

        Strategy: Work down the tree, calculating each child node's known largest and
        smallest by comparing the current node's value to the current node's
        known largest and smallest ancestors. Track the largest known difference.
        """
        # Initialise tracker
        result = 0
        # Initialise queue for breadth-first search
        queue = [root]
        # Initialise store of largest/smallest ancestors
        ancestors = {
            root: (root.val, root.val),
        }
        for node in queue:
            # Set smallest and largest ancestors for children
            smallest = min(node.val, ancestors[node][0])
            largest = max(node.val, ancestors[node][1])
            # Calculate largest known difference
            result = max(result, largest - smallest)
            # Add ancestors to store for children
            if node.left:
                ancestors[node.left] = {}
                ancestors[node.left][0] = smallest
                ancestors[node.left][1] = largest
                queue.append(node.left)
            if node.right:
                ancestors[node.right] = {}
                ancestors[node.right][0] = smallest
                ancestors[node.right][1] = largest
                queue.append(node.right)
        return result


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [
            TreeNode.list_to_node(
                [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13],
            )
        ]
        expected = 7

        assert Solution().maxAncestorDiff(*case) == expected
