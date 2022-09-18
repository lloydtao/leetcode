from __future__ import annotations
from typing import Dict, List, Optional, Set, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        """Definition for singly-linked list.

        Args:
            val (int, optional): Node value. Defaults to 0.
            next (Optional[ListNode], optional): Next node in list. Defaults to None.
        """
        self.val = val
        self.next = next

    def list_to_node(nums: List[int]) -> Optional[ListNode]:
        """Take a list of values, and return the head of a linked list representing it.

        Args:
            nums (List[int]): List of values.

        Returns:
            Optional[ListNode]: Head node of its corresponding linked list.
        """
        # Initialise linked list with a dummy node
        dummy = ListNode()
        current = dummy
        # Iterate through each value in list
        for n in nums:
            # Add new node for the value
            current.next = ListNode(val=n, next=None)
            # Move pointer along
            current = current.next
        # Discard dummy by returning node proceeding it
        return dummy.next

    def list_to_node_cycle(nums: List[int], pos: int) -> Optional[ListNode]:
        """Take a list of values, and return the head of a linked list representing it,
        where the tail links back to the node at a given position, creating a cycle.

        Args:
            nums (List[int]): List of values.
            pos (int): Position of the node to link the tail back to.

        Returns:
            Optional[ListNode]: Head node of its corresponding linked list.
        """
        head = ListNode.list_to_node(nums)
        # No cycle in the linked list
        if pos == -1:
            return head
        # Find the respective node
        current = head
        for i in range(0, pos):
            current = current.next
            # Handle case where pos is larger than list
            if not current:
                return head
        # Find the tail
        tail = current
        while tail.next:
            tail = tail.next
        # Link the tail
        tail.next = current
        return head

    def node_to_list(node: Optional[ListNode]) -> List[int]:
        """Take the head of a linked list, and return a list of values representing it.

        Args:
            head (Optional[ListNode]): Head node of a linked list.

        Returns:
            List[int]: List of values representing the linked list.
        """
        # Initialise a list
        nums = []
        while node:
            # Add value to list
            nums.append(node.val)
            # Go to next node
            node = node.next
        return nums
