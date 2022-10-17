#!/usr/bin/env python3
"""
Given the head of a singly-linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
from typing import Dict, List, Optional, Set, Tuple

from utils.linked_list import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Initialise two pointers (slow, fast):
        - If fast pointer's next node is null, slow pointer is middle (odd case).
        - If fast pointer itself is null, slow pointer is middle (even case).
        - If neither case is true:
          - Move slow pointer forward by one.
          - Move fast pointer forward by two.
        """
        # Initialise slow and fast pointers
        p1 = head
        p2 = head
        while True:
            # If fast pointer is at, or has passed, the end, the slow pointer is on the middle
            if not p2:
                return p1
            if not p2.next:
                return p1
            # Move pointers along
            p1 = p1.next
            p2 = p2.next.next


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [ListNode.list_to_node([1, 2, 3, 4, 5])]
        expected = [3, 4, 5]

        middle = Solution().middleNode(*case)
        assert ListNode.node_to_list(middle) == expected

    def test_even(self):
        """Given test case from Leetcode, with an even number of elements."""
        case = [ListNode.list_to_node([1, 2, 3, 4, 5, 6])]
        expected = [4, 5, 6]

        middle = Solution().middleNode(*case)
        assert ListNode.node_to_list(middle) == expected
