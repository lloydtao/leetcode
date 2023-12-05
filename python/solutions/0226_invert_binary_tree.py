#!/usr/bin/env python3
"""
Given the `root` of a binary tree, invert the tree, and return its root.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.binary_tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """For a given node, switch its branches around. Queue its branches to have the
        same done.

        Args:
            root (Optional[TreeNode]): Head of a binary tree

        Returns:
            Optional[TreeNode]: Head of the inverted binary tree
        """
        # Initialise queue
        queue = [root]
        for node in queue:
            if node:
                # Switch left and right branches around
                node.left, node.right = node.right, node.left
                # Add branches to queue in respective order
                queue.append(node.left)
                queue.append(node.right)
        return root


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [TreeNode.list_to_node([4, 2, 7, 1, 3, 6, 9])]
        expected = [4, 7, 2, 9, 6, 3, 1]

        inverted = Solution().invertTree(*case)
        assert TreeNode.node_to_list(inverted) == expected
