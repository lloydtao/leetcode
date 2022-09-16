#!/usr/bin/env python3
"""
Given the `root` of a binary tree, invert the tree, and return its root.
"""
from __future__ import annotations
from typing import Dict, List, Optional, Set, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def node_to_list(root: Optional[TreeNode]) -> List[int]:
        """Take a head of a binary tree, and return the list of values representing it.

        Args:
            root (Optional[TreeNode]): Root of a binary tree

        Returns:
            List[int]: Respective list of values
        """
        # Handle empty case
        if not root:
            return []
        # Initialise queue
        queue = [root]
        # Traverse tree to store values
        values = []
        for node in queue:
            # Store value
            values.append(node.val)
            # Add branches to queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return values

    def list_to_node(values: List[int]) -> Optional[TreeNode]:
        """Take a list of values, and return the head of a binary tree representing it.

        Args:
            values (List[int]): List of values

        Returns:
            Optional[TreeNode]: Head of respective binary tree
        """
        # No more items to add
        if not values:
            return None
        # Create node for current value
        it = iter(values)
        root = TreeNode(next(it))
        # Initialise a queue with this node
        queue = [root]
        # Iterate through queue by creating, adding and then queueing branch nodes
        for node in queue:
            # Get next value, for left branch
            val = next(it, None)
            if val:
                # Assign value to left branch
                node.left = TreeNode(val)
                # Add branch to queue for processing
                queue.append(node.left)
            # Get next value, for right branch
            val = next(it, None)
            if val:
                # Assign value to right branch
                node.right = TreeNode(val)
                # Add branch to queue for processing
                queue.append(node.right)
        return root


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
        """Given test case from Leetcode.

        Pending implementation of tree methods."""
        case = [TreeNode.list_to_node([4, 2, 7, 1, 3, 6, 9])]
        expected = [4, 7, 2, 9, 6, 3, 1]

        inverted = Solution().invertTree(*case)
        assert TreeNode.node_to_list(inverted) == expected
