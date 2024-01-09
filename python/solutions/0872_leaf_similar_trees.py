#!/usr/bin/env python3
"""
Consider all the leaves of a binary tree, from left to right order, the values of those
leaves form a leaf value sequence.

For example, in the given tree:
          3
      5       1
    6   2   9   8
       7 4

The leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return `True` if and only if the two given trees with head nodes `root1` and `root2`
are leaf-similar.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.binary_tree import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Perform a depth-first search on each tree, adding a node to its sequence if
        it has no children. Compare the sequences at the end."""

        def leafSequence(root: Optional[TreeNode]) -> List[int]:
            """Generate leaf sequence via depth-first search."""
            # Initialise sequence
            sequence = []
            # Initialise stack for node traversal
            stack = [root]
            # Perform depth-first search
            while len(stack) > 0:
                # Pop node from stack
                node = stack.pop()
                # Check if node is leaf
                if node.left is None and node.right is None:
                    # Add node's value to leaf sequence
                    sequence.append(node.val)
                # Add nodes to stack for traversal
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            # Return leaf sequence
            return sequence

        # Return equality of leaf sequences
        return leafSequence(root1) == leafSequence(root2)


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [
            TreeNode.list_to_node(
                [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            ),
            TreeNode.list_to_node(
                [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
            ),
        ]
        expected = True

        assert Solution().leafSimilar(*case) == expected

    def test_falsey(self):
        """Given falsey test case from Leetcode."""
        case = [
            TreeNode.list_to_node(
                [1, 2, 3],
            ),
            TreeNode.list_to_node(
                [1, 3, 2],
            ),
        ]
        expected = False

        assert Solution().leafSimilar(*case) == expected

    def test_falsey_similar(self):
        """Given falsey test case from Leetcode."""
        case = [
            TreeNode.list_to_node(
                [4, 2, 6, 1, 3, 5, 7],
            ),
            TreeNode.list_to_node(
                [4, 2, 6, None, 3, 5, 7],
            ),
        ]
        expected = False

        assert Solution().leafSimilar(*case) == expected
