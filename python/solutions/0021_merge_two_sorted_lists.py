#!/usr/bin/env python3
"""
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Initialise a pointer at the head of each linked list.
        Choose the smallest value between the pointers, and increment that respective
        pointer forwards.
        Use a pointer on the merged list to keep track of its tail.

        Args:
            list1 (Optional[ListNode]): Head of the first linked list
            list2 (Optional[ListNode]): Head of the second linked list

        Returns:
            Optional[ListNode]: Head of the merged linked list
        """
        merged = ListNode()
        # Initialise pointers
        p1 = list1
        p2 = list2
        pm = merged
        # Case where both lists have a node
        while p1 and p2:
            if p1.val < p2.val:
                # Add node to merged list, and move p1 along
                pm.next = ListNode(p1.val)
                pm = pm.next
                p1 = p1.next
            else:
                # Add node to merged list, and move p2 along
                pm.next = ListNode(p2.val)
                pm = pm.next
                p2 = p2.next
        # Case where one list has a node
        while p1 or p2:
            if p1:
                # Add node to merged list, and move p1 along
                pm.next = ListNode(p1.val)
                pm = pm.next
                p1 = p1.next
            else:
                # Add node to merged list, and move p2 along
                pm.next = ListNode(p2.val)
                pm = pm.next
                p2 = p2.next
        # Case where neither list has a node (i.e. fully merged)
        return merged.next


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [ListNode.list_to_node([1, 2, 4]), ListNode.list_to_node([1, 3, 4])]
        expected = [1, 1, 2, 3, 4, 4]

        merged = Solution().mergeTwoLists(*case)
        assert ListNode.node_to_list(merged) == expected
