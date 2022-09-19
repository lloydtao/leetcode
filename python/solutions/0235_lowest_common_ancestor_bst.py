#!/usr/bin/env python3
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two
given nodes in the BST.

"The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node
in `T` that has both `p` and `q` as descendants. Nodes are descendants of themselves."
"""
from typing import Dict, List, Optional, Set, Tuple

from utils.binary_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """Find all parents of p. Find all parents of q.
        Compare lineage of parents and see for how long they are equal.

        Args:
            root (Optional[TreeNode]): Root of the binary search tree
            p (Optional[TreeNode]): A node in the BST
            q (Optional[TreeNode]): Another node in the BST

        Returns:
            Optional[TreeNode]: Lowest common ancestor of p and q
        """
        # Handle empty case
        if not root:
            return None
        # Store parents of nodes
        queue = [root]
        parents = {root: None}
        for node in queue:
            # Parents found, skip rest of search
            if p in parents and q in parents:
                break
            # Add node's branches to queue, and store their parents
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
        # Get lineage of p node
        child = p
        p_ancestors = [child]
        while child:
            parent = parents[child]
            p_ancestors.append(parent)
            child = parent
        # Get lineage of q node
        child = q
        q_ancestors = [child]
        while child:
            parent = parents[child]
            q_ancestors.append(parent)
            child = parent
        # Compare lineages
        lca = None
        while True:
            # Handle case where one list is exhausted (inequal depth)
            if len(p_ancestors) == 0 or len(q_ancestors) == 0:
                return lca
            # Check if ancestors are common
            p_lca = p_ancestors.pop()
            q_lca = q_ancestors.pop()
            if p_lca != q_lca:
                # Ancestor isn't common, so return the last ancestor
                return lca
            lca = p_lca


class Test:
    def test(self):
        """Given test case from Leetcode."""
        tree = TreeNode.list_to_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = tree.left
        q = tree.right

        case = [tree, p, q]
        expected = tree

        assert Solution().lowestCommonAncestor(*case) == expected

    def test_self_descendant(self):
        """Given test case from Leetcode, where the LCA is one of the input nodes."""
        tree = TreeNode.list_to_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = tree.left
        q = tree.left.right

        case = [tree, p, q]
        expected = tree.left

        assert Solution().lowestCommonAncestor(*case) == expected
