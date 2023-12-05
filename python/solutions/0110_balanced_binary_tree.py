#!/usr/bin/env python3
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    "Binary tree in which left and right subtrees of every node differ in height by no
    more than 1."
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """In order to do this in one pass, we start from the bottom and work up:
        - If a node does not have children, it is balanced and of height 0.
        - If a node has children, we can compare the height of its children.
        - If the children are of similar heights, they are balanced. The height of the
          node can be stored as 1 + the highest child.
        - If the children are of differing heights, they are imbalanced. The root of
          the tree can now be considered imbalanced.

        We can achieve this with a helper function that returns if a given node is
        balanced and its height. This helper function will be called on the node's
        children, recursively, until it hits the base case of null (i.e. a leaf node's
        child).

        Args:
            root (Optional[TreeNode]): Root node of binary search tree

        Returns:
            bool: True if tree is balanced
        """

        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            """Perform a recursive depth-first search, storing the heights of subtrees
            from the bottom up. At each subtree, see whether its own subtrees are
            balanced. Balance is determined by if the height of each subtree differs by
            more than 1.

            Args:
                node (Optional[TreeNode]): Root of a subtree in the search tree

            Returns:
                Tuple[bool, int]: True if balanced, and height of subtree
            """
            # Base case: Balanced, and of height -1 (i.e. parent is a leaf node)
            if not node:
                return True, -1
            # General case: Search recursively on left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # Get heights of subtrees
            left_h = left[1]
            right_h = right[1]
            # Optimise by exiting early if imbalanced subtree found
            if not left[0] or not right[0]:
                return False, 1 + max(left_h, right_h)
            # Check if current subtree is balanced
            branches_balanced = left[0] and right[0]
            subtree_balanced = branches_balanced and abs(left_h - right_h) < 2
            # Return 'if balanced' and height of this subtree
            return subtree_balanced, 1 + max(left_h, right_h)

        # Return 'if balanced' of root
        return dfs(root)[0]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [TreeNode.list_to_node([3, 9, 20, None, None, 15, 7])]
        expected = True

        assert Solution().isBalanced(*case) == expected

    def test_single_child(self):
        """Given test case from Leetcode."""
        case = [TreeNode.list_to_node([1, 2, 3, 4, 5, 6, None, 8])]
        expected = True

        assert Solution().isBalanced(*case) == expected

    def test_root_is_child(self):
        """Given test case from Leetcode."""
        case = [TreeNode.list_to_node([1, None, 2, None, 3])]
        expected = False

        assert Solution().isBalanced(*case) == expected
