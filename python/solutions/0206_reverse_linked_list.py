#!/usr/bin/env python3
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.linked_list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse in-place."""
        new_head = None
        while head:
            # Store the next node in the linked list
            next = head.next
            # Set the head's next node
            head.next = new_head
            # Store the head as the new head
            new_head = head
            # Set the head to the stored node
            head = next
        return new_head


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [ListNode.list_to_node([1, 2])]
        expected = [2, 1]

        reverse = Solution().reverseList(*case)
        assert ListNode.node_to_list(reverse) == expected

    def test_empty(self):
        """Given empty test case from Leetcode."""
        case = [ListNode.list_to_node([])]
        expected = []

        reverse = Solution().reverseList(*case)
        assert ListNode.node_to_list(reverse) == expected
