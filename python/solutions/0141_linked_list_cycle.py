#!/usr/bin/env python3
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Return True if there is a cycle in the linked list. Otherwise, return False.
"""
from typing import Dict, List, Optional, Set, Tuple

from utils.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Fast and slower pointers:
        - Start a fast pointer one place in front of the slow pointer.
        - Move the fast pointer forwards 2, and the slow pointer forwards 1.
        - If the fast pointer is ever on the same node as the slow pointer, there must
        be a cycle.
        - If the fast pointer reaches the end of the list, there is no cycle.

        This solution uses 2 pointers but has no need to store visited nodes, making it
        more space efficient than traversing with one pointer and storing this info.

        Args:
            head (Optional[ListNode]): Head of a linked list

        Returns:
            bool: True if cycle detected
        """
        # Handle empty case
        if not head:
            return False
        # Initialise fast and slow pointers
        tortoise = head
        hare = head.next
        # If fast pointer catches back up to slow, there is a cycle
        while tortoise:
            # Handle fast pointer is finished
            if not hare:
                return False
            # Handle fast pointer is final node
            if not hare.next:
                return False
            # Move pointers along
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise is hare:
                return True
        return False

    def hasCycleOnePointer(self, head: Optional[ListNode]) -> bool:
        """Traverse the linked list, store visited nodes, and see if a node runs back
        to a previously visited node.

        Args:
            head (Optional[ListNode]): Head of a linked list

        Returns:
            bool: True if cycle detected
        """
        visited = {}
        node = head
        cycle = False
        while True:
            if not node:
                # End of linked list
                return False
            if node in visited:
                # Cycle found
                return True
            visited[node] = None
            node = node.next


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [ListNode.list_to_node_cycle([3, 2, 0, -4], 1)]
        expected = True

        assert Solution().hasCycle(*case) == expected

    def test_full_loop(self):
        """Given test case from Leetcode, with a full loop."""
        case = [ListNode.list_to_node_cycle([1, 2], 0)]
        expected = True

        assert Solution().hasCycle(*case) == expected

    def test_no_loop(self):
        """Given test case from Leetcode, with a full loop."""
        case = [ListNode.list_to_node_cycle([1], -1)]
        expected = False

        assert Solution().hasCycle(*case) == expected
