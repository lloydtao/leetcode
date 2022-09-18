from __future__ import annotations
from typing import Dict, List, Optional, Set, Tuple


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        """Leetcode's definition for a binary tree node.

        Args:
            val (int, optional): Node value. Defaults to 0.
            left (Optional[TreeNode], optional): Node's left child. Defaults to None.
            right (Optional[TreeNode], optional): Node's right child. Defaults to None.
        """
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
        # Handle empty case (no more items to add)
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
